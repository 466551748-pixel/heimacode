"""
 flatMap算子：
 功能：对RDD执行map操作，然后进行解除嵌套的操作
 和map算子区别只有加了个解除嵌套的功能

 解除嵌套：
 # 嵌套的list
 list = [[1,2,3],[4,5,6]]
 # 如果解除了嵌套
 list = [1,2,3,4,5,6]
"""
from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["zhuangyan 123","zhuangyue 456","xuqing 789"])

# 需求：将RDD数据里面的单词，一个个提取出来
rdd1 = rdd.map(lambda x:x.split(" "))
print(rdd1.collect())

# 使用flatMap方法，加入解除嵌套
rdd2 = rdd.flatMap(lambda x:x.split(" "))
print(rdd2.collect())
sc.stop()



