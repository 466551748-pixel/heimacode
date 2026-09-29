"""
 数据输出：输出为python对象或者文件

 collect算子：
 功能：将RDD各个分区内的数据，统一收集到Driver中，形成一个List对象
 语法：rdd.collect()  返回值是list

 reduce算子：
 功能：对RDD数据集按照你传入的逻辑进行聚合
 语法：rdd.reduce(func)
 # func: (T,T)->T
 # 2个传入参数，1个返回值，返回值和传入参数类型要一致
 注意：reduceByKey是按照key分组，这个不用
"""

from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

# collect算子
rdd_list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子
num = rdd.reduce(lambda x,y:x+y)
print(num)

# take算子：取出RDD的前n个元素，组成list返回
take_list = rdd.take(3)
print(take_list)

# count：统计RDD内有多少条数据，返回为数字
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")
sc.stop()
