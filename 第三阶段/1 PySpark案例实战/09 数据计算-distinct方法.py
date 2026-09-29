"""
 distinct算子
 语法：rdd.distinct() 无需传参
 功能：对RDD数据进行去重，返回新的RDD
"""

from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1,1,3,3,4,4,7,8,8])
# 去重
rdd1 = rdd.distinct()
# 输出
print(rdd1.collect())
sc.stop()