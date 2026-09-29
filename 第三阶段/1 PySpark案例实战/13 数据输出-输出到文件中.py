"""
 saveAsTextFile算子：
 功能：将RDD数据写入文本文件中，支持本地写出，hdfs等文本系统
"""
from pyspark import SparkContext, SparkConf
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\46655\Desktop\黑马python_副本\.venv\Scripts\python.exe"
os.environ["HADOOP_HOME"] = r"C:\Users\46655\Desktop\黑马python_副本\hadoop-3.0.0"  # 解决Windows下winutils.exe问题

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism", "1") # 设置为一个分区（全局）

sc = SparkContext(conf=conf)

# 准备三个RDD
rdd1 = sc.parallelize([1,2,3,4,5],numSlices=1)  # numSlices = 1 也是设置分区为1
rdd2 = sc.parallelize([("hello",3),("world",2),("hi",7)])
rdd3 = sc.parallelize([[1,2,3],[7,8,9],[4,5,6]])

# 输出到文件中
rdd1.saveAsTextFile(r"C:\Users\46655\Desktop\黑马python_副本\output1")
rdd2.saveAsTextFile(r"C:\Users\46655\Desktop\黑马python_副本\output2")
rdd3.saveAsTextFile(r"C:\Users\46655\Desktop\黑马python_副本\output3")
sc.stop()