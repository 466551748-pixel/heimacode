# 这个要求过程怪怪的，也没说要存进数据容器

class Student:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
student_dict = {}
i = 1
for i in range(10):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名")
    age = input("请输入学生年龄")
    address = "地址：" + input("请输入学生地址")
    stu_1 = Student(name,age,address)
    student_dict[name] = {age,address}
    print(student_dict)


