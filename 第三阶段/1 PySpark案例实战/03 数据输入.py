"""
 学习目标：
 1.理解RDD对象
 2.掌握PySpark数据输入的2种方法（数据容器和文件路径）

 RDD：弹性分布式数据集（resilient distributed datasets）
 PySpark支持多种数据的输入，在输入完成后，都会得到一个RDD类的对象
 PySpark针对数据的处理，都是以RDD对象作为载体，即：
 1.数据存储在RDD内
 2.各类数据的计算方法，都是RDD的成员方法
 3.RDD的数据计算方法，返回值依旧是RDD对象

 PySpark支持通过SparkContext对象的parallelize成员方法，将：
 list,tuple,str,set,dict
 转换为RDD对象
 注意：
 1.字符串会被拆分出一个个字符存入RDD对象
 2.字典仅有key会被存入RDD对象

 也支持通过SparkContext入口对象，来读取文件，来构建出RDD对象
 sc.textFile("文件路径")

"""

# 演示数据输入
from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# # 通过parallelize方法将python对象加载到spark内，称为RDD对象
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1,2,3,4,5})
# rdd5 = sc.parallelize({"key1":"value1","key2":"value2"})
#
# # 如果要查看RDD里面有什么内容，需要collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 用textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd = sc.textFile(r"C:\Users\46655\Desktop\黑马python_副本\hello.txt")
print(rdd.collect())

sc.stop()