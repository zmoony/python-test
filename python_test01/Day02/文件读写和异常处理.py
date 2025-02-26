
def file_read_with():
    """
    with 自动关闭资源
    只有符合上下文管理器协议（有__enter__和__exit__魔术方法）的对象才能使用这种语法
    :return:
    """
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    with open(file_path,'r') as file:
        print(file.read())

def file_read():
    """
    如果文件较大，file.read() 会占用较多内存，因为它是一次性将整个文件内容加载到内存中。
如果只需要逐行读取或处理大文件，建议使用 file.readline() 或 for line in file 的方式来逐行读取。

    异常处理关键字：try、except、else、finally和raise
    :return:
    """
    file = None
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    try:
        file = open(file_path,'r')
        print(file.read())
    except FileNotFoundError :
        print('无法打开指定文件')
    except LookupError:
        print('找不到指定的编码格式')
    except UnicodeDecodeError:
        print('文件编码格式错误')
    except Exception as e:
        # raise InputError('只能计算非负整数的阶乘')
        raise e
    finally:
        if file:
            file.close()

def file_readline():
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    file = open(file_path,'r')
    lines = file.readlines()
    for line in lines:
        print(line,end='')
    file.close()

def file_read_forin():
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    file = open(file_path,'r')
    for line in file:
        print(line,end='')
    file.close()

def read_the_binary():
    """
    操作模式是'rb'，如果要进行写操作，操作模式是'wb'
    read方法的返回值以及write方法的参数是bytes-like对象（字节串）
    如：图片复制
    :return:
    """
    src_pic = 'C:\\Users\\yuez\\Desktop\\测试1.png'
    desc_pic = 'C:\\Users\\yuez\\Desktop\\测试-auto.png'
    try:
        with open(src_pic,'rb') as src:
            with open(desc_pic,'wb') as desc:
                desc.write(src.read())
    except Exception as e:
        print(e)
    print('复制完成')

def file_write_replace():
    """
    以写入模式打开文件。如果文件已经存在，会清空文件内容，即覆盖之前的内容；如果文件不存在，则会创建一个新文件。
    :return:
    """
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    file = open(file_path,'w')
    file.write('hello world')
    file.close()

def file_write_append():
    """
    以追加模式打开文件。如果文件已经存在，会从文件末尾开始追加内容；如果文件不存在，则会创建一个新文件。
    :return:
    """
    file_path = 'C:\\Users\\yuez\\Desktop\\接入模板\\keyperson.txt'
    file = open(file_path,'a')
    file.write('\n362421199009063250\n362421199009063250\n362421199009063250')
    file.close()

if __name__ == '__main__':
    # file_read()
    # file_write_append()
    # file_read()
    # file_readline()
    # file_read_forin()
    read_the_binary()