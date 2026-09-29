# 函数功能：接收传入文件的路径，，打印文件的全部内容，若文件不存在则捕捉异常，输出提示信息，通过finally关闭文件
def print_file_info(file_name):
    open_file = None     # 防止关闭文件的时候出现问题，若打不开，何来的关闭文件，所以若没成功打开文件，最后关闭文件会爆错，设置一个变量控制是否需要关闭文件，若没打开不需要关闭文件
    try:
        open_file = open(file_name,'r',encoding='utf-8')
    except Exception as e:
        print(f"文件异常为{e}")
    else:
        print(open_file.read())
    finally:
        if open_file is not None:
            open_file.close()

# 接收文件路径以及传入数据，将数据追加写入文件中
def append_file_info(file_name,data):
    open_file = open(file_name,'a',encoding='utf-8')
    open_file.write(data)
    open_file.close()