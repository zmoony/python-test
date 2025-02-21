import os

import win32com.client as win32
from docx import Document
import pandas as pd
import re
from docxtpl import DocxTemplate

"""
读取doc文件，提取关键词，写入excel中
"""
def docx_to_excel(file_path,excel_path):
    text = read_docx(file_path)
    keywords = extract_keywords(text)
    write_excel(keywords, excel_path)
    delete_file(file_path)

# 读取doc文件
def read_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# 提取关键词
def extract_keywords(text):
    """
    { 'project_name' : "采购项目名称" }
    { 'name' : "名称" }
    { 'num' : "数量" }
    { 'num_count' : "数量" }
    { 'num_unit' : "数量单位" }
    { 'time' : "交货时间" }
    { 'technical_requirements' : "技术要求" }
    { 'warranty_years' : "质保期" }
    { 'acceptance_plan' : "验收计划" }
    { 'capitalBudget' : "资金预算" }
    { 'howTheContractIsPriced' : "合同定价方式" }
    { 'suggestedProcurementMethods' : "建议采购方式" }
    { 'placeOfDelivery' : "交货地点" }
    { 'fundsAndPayments' : "资金与货款" }
    :param text:
    :return:
    """
    keywords = []

    pattern = r'采购项目名称\s*：\s*(.*)'
    matches = re.findall(pattern, text)
    for match in matches:
        keywords.append(['采购项目名称','project_name',match.strip()])

    pattern = r'\s*（三）名称、数量、规格（可另附表）\s*\n\s*1.名称：\s*(.*)\s*\n\s*2.数量：\s*(.*)(\w+)'
    matches = re.findall(pattern, text)
    for match in matches:
        name = match[0].strip().replace('。', '')
        quantity = match[1].strip()
        unit = match[2].strip()
        keywords.append(['名称', 'name', name])
        keywords.append(['数量', 'num', quantity+unit])
        keywords.append(['数量值', 'num_count', quantity])
        keywords.append(['数量单位', 'num_unit', unit])

    pattern = r'2.交货时间.*?☑(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['交货时间', 'time', match.strip()])

    pattern = r'（五）技术要求(.*?)（填写说明'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['技术要求', 'technical_requirements', match.strip()])

    pattern = r'（一）质保期\s*\n(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['质保期', 'warranty_years', match.strip().replace('。', '')])

    pattern = r'（二）验收方案\s*\n(.*?)\n四、资金与货款'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['验收计划', 'acceptance_plan', match.strip()])

    pattern = r'（四）资金预算.*?☑(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['资金预算', 'capitalBudget', match.strip()])

    pattern = r'（五）合同定价方式.*?☑(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['合同定价方式', 'howTheContractIsPriced', match.strip()])

    pattern = r'（六）建议采购方式.*?☑(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['建议采购方式', 'suggestedProcurementMethods', match.strip()])

    pattern = r'3.交货地点：\s*：\s*(.*)'
    matches = re.findall(pattern, text)
    for match in matches:
        keywords.append(['交货地点', 'placeOfDelivery', match.strip()])

    pattern = r'四、资金与货款.*?☑(.*?)\n'
    matches = re.findall(pattern, text, re.DOTALL)
    for match in matches:
        keywords.append(['资金与货款', 'fundsAndPayments', match.strip()])

    return keywords

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# 写入excel
def write_excel(variables, excel_path):
    # 如果excel文件存在先删除
    if os.path.exists(excel_path):
        os.remove(excel_path)
    df = pd.DataFrame(variables, columns=['名称','变量名称','值'])
    df.to_excel(excel_path, index=False, engine='openpyxl')
    pass

# 读取excel,找到模板变量
def read_excel(excel_path):
    result = {}
    df = pd.read_excel(excel_path)
    for index, row in df.iterrows():
        label = row['变量名称']
        value = row['值']
        result[label] = value
    return result

# 将doc文件转换为docx文件
def convert_doc_to_docx(doc_path, docx_path):
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(docx_path, FileFormat=16)
    doc.Close()
    word.Quit()

# 文件是否存在
def file_exists(file_path):
    return os.path.exists(file_path)

def template_to_doc(context, template_path, doc_path):
    """
    根据模板生成文档。

    使用 `python-docx-template` 库从给定的模板文件和上下文数据生成文档。

    参数:
    - context: 包含模板变量和它们的值的字典。
    { 'project_name' : "采购项目名称" }
    { 'name' : "名称" }
    { 'num' : "数量" }
    { 'num.count' : "数量" }
    { 'num.unit' : "数量单位" }
    { 'time' : "交货时间" }
    { 'technical_requirements' : "技术要求" }
    { 'warranty_years' : "质保期" }
    { 'acceptance_plan' : "验收计划" }

    - template_path: 模板文件的路径。
    - doc_path: 生成的文档的保存路径。

    返回:
    无。但是会在指定路径生成一个基于模板和上下文数据的文档。
    """
    try:
        print(context)
        doc = DocxTemplate(template_path)
        doc.render(context)
        doc.save(doc_path)
    except Exception as e:
        print(f"产生最终文件发生错误：{e}")


def main():
    print('********开始转换excel********')
    localDir = os.getcwd()
    # 需要转换的doc地址
    file_path = localDir + '\无人机干扰拦截设备小额采购需求书0109.doc'
    # file_path =  '无人机干扰拦截设备小额采购需求书0109.doc'
    # 转换后的docx地址
    docx_path = localDir +'\格式转换-采购需求转换.docx'
    # 输出的excel的地址
    excel_path =  localDir +'\采购需求转换.xlsx'
    # doc的模板地址
    template_path = localDir +'\模板-采购文件-无人机干扰拦截设备.docx'
    # 最终生成的文件地址
    final_doc_path = localDir +'\最终文件.docx'
    if not file_exists(file_path):
        print('文件不存在')
        return
    if not file_exists(docx_path):
        convert_doc_to_docx(file_path, docx_path)
    docx_to_excel(docx_path,excel_path)
    print('********结束转换excel********')
    print('********开始转换根据模板生成doc********')
    context = read_excel(excel_path)
    template_to_doc(context, template_path, final_doc_path)
    print('********结束转换根据模板生成doc********')

if __name__ == '__main__':
   main()

