"""
 pyspark的数据计算，依赖于RDD对象内置丰富的成员方法（算子）

 map算子：本质上是RDD类的成员方法，但叫算子
 功能：map算子，是将RDD的数据一条条处理（处理的逻辑基于map算子中接受的处理函数），返回新的RDD
"""

# 演示RDD的map成员方法的使用
from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

def func(data):
    return data*18

# 通过map方法将全部数据都乘以18
rdd1 = rdd.map(func)
# (T) -> U  : T表示传入参数的鉴定，表示这里接受一个传入参数，U代表返回值，代表有一个返回值  --> 总结：传入一个值返回一个值
# (T) -> T  : 这也是代表传入一个值返回一个值，但是加了一个要求，传入什么类型返回就得是什么类型，同为T

# 第二种写法，利用匿名函数
rdd2 = rdd.map(lambda x:x*18)

# 链式调用,可以继续.增加需要的计算  可以无限制的点map
rdd3 = rdd.map(lambda x:x*18).map(lambda x: x+5)
print(rdd3.collect())

