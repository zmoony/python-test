"""
pip install PyPDF2
PyPDF2没有办法从 PDF 文档中提取图像、图表或其他媒体，但它可以提取文本，并将其返回为 Python 字符串。
第三方工具：
pip install pdfminer.six
pdf2text.py test.pdf
创建pdf:
pip install reportlab
"""
import PyPDF2


def pdf_read():
    import PyPDF2

    reader = PyPDF2.PdfReader('D:\文档\wiscom\数据中台\江北\视图库\视图库存储推送数据协议说明.pdf')
    for page in reader.pages:
        print(page.extract_text())

def overlay_rotations():
    """
    上面的代码中通过创建PdfFileReader对象的方式来读取 PDF 文档，该对象的getPage方法可以获得PDF文档的指定页并得到一个PageObject对象，
    通过PageObject对象的rotateClockwise和rotateCounterClockwise方法可以实现页面的顺时针和逆时针方向旋转，
    通过PageObject对象的addBlankPage方法可以添加一个新的空白页，代码如下所示
    :return:
    """
    reader = PyPDF2.PdfReader('XGBoost.pdf')
    writer = PyPDF2.PdfWriter()

    for no, page in enumerate(reader.pages):
        if no % 2 == 0:
            new_page = page.rotate(-90)
        else:
            new_page = page.rotate(90)
        writer.add_page(new_page)

    with open('temp.pdf', 'wb') as file_obj:
        writer.write(file_obj)

def encrypt_pdf_files():
    """
    加密PDF文件
    :return:
    """
    reader = PyPDF2.PdfReader('XGBoost.pdf')
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt('foobared')

    with open('temp.pdf', 'wb') as file_obj:
        writer.write(file_obj)

def watermark():
    """
    添加水印
    上面提到的PageObject对象还有一个名为mergePage的方法，可以两个 PDF 页面进行叠加，通过这个操作，我们很容易实现给PDF文件添加水印的功能。例如要给上面的“XGBoost.pdf”文件添加一个水印，
    我们可以先准备好一个提供水印页面的 PDF 文件，然后将包含水印的PageObject读取出来，然后再循环遍历“XGBoost.pdf”文件的每个页，
    获取到PageObject对象，然后通过mergePage方法实现水印页和原始页的合并
    :return:
    """
    reader1 = PyPDF2.PdfReader('XGBoost.pdf')
    reader2 = PyPDF2.PdfReader('watermark.pdf')
    writer = PyPDF2.PdfWriter()
    watermark_page = reader2.pages[0]

    for page in reader1.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open('temp.pdf', 'wb') as file_obj:
        writer.write(file_obj)


def merge_pdf_files():
    """
    合并PDF文件
    :return:
    """
    reader1 = PyPDF2.PdfReader('XGBoost.pdf')
    reader2 = PyPDF2.PdfReader('watermark.pdf')
    writer = PyPDF2.PdfWriter()
    for page in reader1.pages:
        writer.add_page(page)
        writer.add_page(reader2.pages[0])
    writer.write('temp.pdf')
    watermark()
    encrypt_pdf_files()
    overlay_rotations()

def pdf_create():
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    pdf_canvas = canvas.Canvas('resources/demo.pdf', pagesize=A4)
    width, height = A4

    # 绘图
    image = canvas.ImageReader('resources/guido.jpg')
    pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

    # 显示当前页
    pdf_canvas.showPage()

    # 注册字体文件
    pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
    pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/青呱石头体.ttf'))

    # 写字
    pdf_canvas.setFont('Font2', 40)
    pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
    pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
    pdf_canvas.setFont('Font1', 40)
    pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
    pdf_canvas.rotate(18)
    pdf_canvas.drawString(250, 250, 'hello, world!')

    # 保存
    pdf_canvas.save()

if __name__ == '__main__':
    pdf_read()
