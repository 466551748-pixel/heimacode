"""
 reduceByKey算子：
 rdd.reduceByKey(func)
 # func: (V,V) -> V  传入俩个返回一个，且类型一样
 功能：针对KV型RDD，自动按照key分组，然后依据所提供的聚合逻辑（传入函数），完成组内数据（value）的聚合操作
 KV型RDD：二元元组 代表元组里的数据只有俩个  ("庄严",317)  第一个元素叫key，第二个元素叫value
 注意：reduceByKey中接收的函数，只负责聚合，不理会分组
 注意：按key自动分组
 如果有[1,2,3,4,5] 且 lambda a,b:a+b
 运算过程是;1+2=3->3+3=6->6+4=10->10+5=15      也就是累加器
"""
from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([("男",99),("男",88),("女",77),("女",66)])
# 求男生女生俩个组的成绩之和
rdd1 = rdd.reduceByKey(lambda a,b:a+b)
print(rdd1.collect())
sc.stop()