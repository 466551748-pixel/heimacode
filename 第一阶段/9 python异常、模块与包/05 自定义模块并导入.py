"""
 python中已经帮我们实现了很多的模块，不过我们有时候也需要一些个性化的模块，这里可以通过自定义模块实现，也就是自己制作一个模块
 做法：自己新建一个python文件，在其他的python文件import它，模块名称就是文件的名字(同目录或者设置搜索路径找到)
"""

# 导入自定义模块使用
# import my_module1
# my_module1.test(1,2)
# from my_module1 import test
# test(1,2)

# 导入不同模块的同名功能，后调用的会覆盖前面调用的
# from my_module1 import test
# from my_module2 import test
# test(2,3)      #会调用my_module2中的test功能函数，覆盖掉my_module1中的test

# __main__变量
from my_module1 import test
test(1,2)       # 若在模块文件里有执行函数，在这个文件里调用模块，会执行模块文件里的内容，出现俩个3
# 若不想出现俩个三，在模块文件里加if条件判断： if __name__ == '__main__'

# __all__变量：注意是列表对象
# 如果一个模块文件里有'__all__'变量，当使用from xxx import *导入时，只能导入这个列表的元素，*代表所有，是来自这个all
# *能导入什么来自这个all控制，若是不用*，直接指定的话，也是可以导入的，也就是说all只控制*
from my_module3 import *
test_A(1,2)
# test_B(2,3) my_module3中的all变量里没有test_B()，所以这里用不了，被all变量控制了