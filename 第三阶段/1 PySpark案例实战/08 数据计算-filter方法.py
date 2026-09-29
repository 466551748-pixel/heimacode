"""
 filter算子:
 语法：rdd.filter(func)
 功能：过滤掉想要的数据进行保留
 # func：(T) -> U ：传入一个参数（随意类型），返回值必须True或者False
 True则保留

"""
from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\anaconda3\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

# 对RDD对象进行过滤 True则保留,False丢弃 
rdd1 = rdd.filter(lambda x: x % 2 == 0)

print(rdd1.collect())
sc.stop()




