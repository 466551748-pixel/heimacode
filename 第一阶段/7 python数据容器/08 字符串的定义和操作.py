"""
 尽管字符串看起来并不像：列表、元组那样，一看就是存放了很多数据的容器
 但是不可否认的是，字符串同样也是数据容器的一员
 字符串是字符的容器，一个字符串可以存放任意数量的字符
    如，字符串"zhuangyan",每一个字符算是一个元素
 一.字符串的下标：
    和列表、元组一样，字符串也可以通过下标进行访问
 二.字符串不可修改：
    同元组一样，字符串是一个无法修改的数据容器
    如果必须修改，得到的是一个新的字符串
 三.字符串的替换：
    1.语法：字符串.replace(字符串1,字符串2)
    2.功能：将字符串内的全部的字符串1，替换成字符串2
    3.注意：不是修改字符串本身，而是得到了一个新的字符串（返回值）
 四.字符串的分割
    1.语法：字符串.split(分割符字符串)
    2.功能：按照指定的分割符字符串，将字符串划分为多个字符串，并存入列表对象中
    3.注意：字符串本身不变，而是得到了一个新的列表对象
           分割符是按照原本字符串里的分割符填写的
           若"a,b,c" 则填","
           若"a b c" 则填"空格"
 五.字符串的规整操作（去除指定字符）
    1.语法1：字符串.strip("去除前后指定的字符")
    2.语法2:字符串.strip()：不传参数，去除前后空格，还有换行符
 总结：
    1.只可以存储字符串
    2.长度任意（取决于内存大小）
    3.支持下标索引
    4.允许重复字符串存在
    5.不可以修改，支持替换，但是变成新的字符串
    6.支持for循环
"""
# 1通过下标索引取值
my_str = "itheima and itcast"
print(f"取下标为1的元素：{my_str[1]}")
print(f"取下标为-1的元素：{my_str[-1]}")
# 2index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，起始下标是:{value}")
# 3replace方法
my_str = my_str.replace("it","程序")
print(f"替换后的字符串为：{my_str}")
# 4split方法
my_str = "hello python itheima and itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到:{my_str_list}，类型是：{type(my_str_list)}")
# 5strip方法
my_str = "  hello python itheima and itcast  "
new_str = my_str.strip() # 不传参数，去除首尾空格，还有换行符
print(f"字符串{my_str}被strip后，结果是:{new_str}")

my_str = "12hello python itheima and itcast12"
new_str = my_str.strip("12")
print(f"字符串{my_str}被strip后，结果是:{new_str}")
# 6统计count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是:{count}")
# 统计字符串的长度len
my_str = "itheima and itcast"
length = len(my_str)
print(f"字符串{my_str}的长度是：{length}")
