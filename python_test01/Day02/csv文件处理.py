"""
使用Python标准库中的csv模块，该模块的writer函数会返回一个csvwriter对象，通过该对象的writerow或writerows方法就可以将数据写入到CSV文件中
一般数据处理中会使用pandas
pandas中封装了名为read_csv和to_csv的函数用来读写CSV文件
read_csv：将数据变成DataFrame对象。DataFrame就是pandas库中最重要的类型，它封装了一系列用于数据处理的方法（清洗、转换、聚合等）
to_csv：将DataFrame对象中的数据写入CSV文件，完成数据的持久化。
read_csv函数和to_csv函数远远比原生的csvreader和csvwriter强大。
"""
import csv
import random


def csv_create():
    """
    在使用 csv.writer 写入 CSV 文件时，如果文件是以 'w' 模式打开的，
    并且没有指定 newline='' 参数，csv.writer 会在每行之间自动添加一个额外的空行。
    这是因为在某些操作系统（如 Windows）中，换行符的处理方式会导致这种情况。
    :return: None 直接写入文件
    """
    with open('../../data/raw/scores.csv','w',encoding='utf-8',newline='') as f:
        """
        dialect：默认excel模式
        delimiter : 分隔符
        quoting：采用双引号包围
        """
        writer = csv.writer(f,delimiter='|', quoting=csv.QUOTE_ALL)
        writer.writerow(['姓名', '语文', '数学', '英语'])
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        for name in names:
            scores = [random.randrange(51,100) for _ in range(3)]
            scores.insert(0,name)
            writer.writerow(scores)

def csv_read():
    with open('../../data/raw/scores.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter='|')
        for row in reader:
            print(reader.line_num, end='\t')
            # print(row)
            for elem in row:
                print(elem, end='\t')
            print()

if __name__ == '__main__':
    csv_create()