"""
 列表的sort方法：
 前面我们学习过sorted函数，可以数据容器进行排序
 在后面的数据处理中，我们需要对列表进行排序，并制定排序规则，sorted就无法完成了
 补充学习列表的sort方法
 使用方式：
 列表.sort(key=选择排序依据的函数,reverse=True或者False)
 1.key:要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据（按照元素的哪一部分排序）
 2.reverse：True表示降序，False表示升序
"""
# 演示sort
# 可用匿名函数或者def一个函数
my_list = [["a",33],["b",55],["c",11]]

my_list.sort(key=lambda x:x[1],reverse=True)  # 每个元素都传到匿名函数按下标1排序
print(my_list)
