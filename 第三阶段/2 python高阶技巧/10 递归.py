
















"""
 递归：方法（函数）自己调用自己的一种特殊编程写法
 最典型的递归场景：找出一个文件夹中全部的文件
"""
import os

def test_os():
    # 演示os模块3个基础方法
    print(os.listdir(r"E:\python_code\text"))          # 把当前路径文件夹内容列出来
    print(os.path.isdir(r"E:\python_code\text\a"))     # 判断路径是否为一个文件夹
    print(os.path.exists(r"E:\python_code\text"))      # 判断路径是否存在
def get_files_recursion_from_dir(path):
    """
    通过递归的方式获得文件夹内全部的文件列表
    :param path: 被判断的文件夹
    :return: list,包含全部的文件，如果目录不存在或者无文件，返回空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path+rf"\{f}"
            if os.path.isdir(new_path):
                # 进入到这里，表面这个目录是文件夹
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)


    else:
        print(f"指定的目录{path}，不存在")
        return []
    return file_list

if __name__ == '__main__':
    print(get_files_recursion_from_dir(r"E:\python_code\新建文件夹"))
