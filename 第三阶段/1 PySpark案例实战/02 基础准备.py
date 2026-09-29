"""
 构建pyspark执行环境入口对象：
 想要使用PySpark库完成数据处理，首先需要构建一个执行环境入口对象
 PySpark的执行环境入口对象是：类SparkContext的类对象

 PySpark的编程主要分为如下三大模型：
 1.数据输入：通过SparkContext类对象的成员方法，完成数据的读取操作，读取后得到RDD类对象
 2.数据处理计算：通过RDD类对象的成员方法，完成各种数据计算的需求
 3.数据输出：将处理完成后的RDD对象，调用各种成员方法完成写出文件、转为list等操作

"""
from pyspark import SparkContext,SparkConf

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")    # 设置运行模式：本机（单机）
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印pyspark的运行版本
print(sc.version)
# 停止SparkContext对象的运行（停止PySpark程序），关闭和spark的链接
sc.stop()
