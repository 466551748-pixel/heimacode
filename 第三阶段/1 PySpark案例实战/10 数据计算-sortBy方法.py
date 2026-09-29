"""
 sortBy算子：
 功能：对RDD数据进行排序，基于自己指定的排序依据
 语法：rdd.sortBy(func,ascending=True,numPartitions=1)
 # func: (T) -> U 告知按照rdd中的哪个数据进行排序，比如 lambda x:x[0] 表示按照rdd的第一列进行排序
 # ascending: True表示升序 False表示降序
 # numPartitions: 用多少分区排序，全局排序需要设置分区数为1
"""
from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.textFile(r"C:\Users\46655\Desktop\黑马python_副本\hello.txt")
# 取出所有单词
word_rdd1 = rdd.flatMap(lambda x:x.split(" "))

# 将所以单词都转换为二元元组
rdd3 = word_rdd1.map(lambda word:(word,1))

# 分组求和
rdd4 = rdd3.reduceByKey(lambda x,y:x+y)
print("求和结果：")
print(rdd4.collect())

# 对结果进行排序
result_rdd = rdd4.sortBy(lambda x:x[1],ascending=True,numPartitions=1)
print("排序结果：")
print(result_rdd.collect())
sc.stop()