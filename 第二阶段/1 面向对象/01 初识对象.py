"""
 理解使用对象完成数据组织的思路

 生活中数据组织：
 若让学生们自己填写自己的信息，会写的很乱 -> 改为登记表，打印出来让学生统一填写
 这样就会很统一规整方便

 使用变量数据太乱了，如果程序也和生活中一样
 1.可以设计表格
 2.可以将设计的表格打印出来
 3.可以将打印好的表格供人填写
 那么数据的组织就非常方便了

 答：可以
 1.设计表格称为 --> 设计类
 class Student:
    name = None    # 记录学生姓名
 2.打印表格称为 --> 创建对象
 # 基于类创建对象
 stu_1 = Student()
 stu_2 = Student()
 3.填写表格称为 --> 对象属性赋值
 stu_1.name = "周杰伦"
 stu_2.name = "林俊杰"
"""
# 设计一个类
class Student:
    name = None          # 记录学生姓名
    gender = None        # 记录学生性别
    nationality = None   # 记录学生国籍
    native_place = None  # 记录学生籍贯
    age = None           # 记录学生年龄

# 创建一个对象 （打印一张登记表）
stu_1 = Student()

# 对象属性进行赋值 （填写表单）
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = "31"

# 获取对象中记录的内容
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
