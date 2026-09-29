"""
 完成使用PySpark进行单词计数的案例
"""
from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.textFile(r"C:\Users\46655\Desktop\黑马python_副本\hello.txt")
# 取出所有单词
word_rdd1 = rdd.flatMap(lambda x:x.split(" "))

# 将所以单词都转换为二元元组
rdd2 = word_rdd1.flatMap(lambda word:(word,1))
print(rdd2.collect())
print("不能用flatMap，因为会自动解嵌套，而我们要的二元元组是要嵌套的，只能用map")
rdd3 = word_rdd1.map(lambda word:(word,1))
print(rdd3.collect())

# 分组求和
result_rdd = rdd3.reduceByKey(lambda x,y:x+y)
print(result_rdd.collect())
sc.stop()
