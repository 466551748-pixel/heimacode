"""
 学习目标：
 1.完成综合案例开发
 2.掌握\符号完成代码的跨行编写

 搜索引擎日志分析：
 读取文件转换为RDD，并且完成：
 1.打印输出：热门搜索时间段（小时精度）top3
 2.打印输出：热门搜索词top3
 3.打印输出：统计黑马程序员关键字在那个时间段被搜索最多
 4.将数据转换为json格式，写出为文件
"""
import json

from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("test")
sc = SparkContext(conf=conf)
rdd = sc.textFile(r"C:\Users\46655\Desktop\黑马python_副本\search_log.txt")

# 需求1：热门搜索时间段
# 取时间
rdd1 = rdd.map(lambda x:x.split("\t")).\
    map(lambda x:x[0][0:2]).\
    map(lambda x:(int(x),1))
result1 = rdd1.reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(result1)
print(f"所以热门搜索时间段top3分别是{result1[0][0]}点,{result1[1][0]}点,{result1[2][0]}点")

# 需求2：热门搜索词top3
# 取搜索词
rdd1 = rdd.map(lambda x:x.split("\t")).\
    map(lambda x:x[2]).\
    map(lambda x:(x,1))
result2 = rdd1.reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(result2)
print(f"所以热门搜索词top3分别是{result2[0][0]},{result2[1][0]},{result2[2][0]}")

# 需求3：统计黑马程序员关键字在那个时间段被搜索最多
rdd1 = rdd.map(lambda x:x.split("\t")).\
    filter(lambda x:x[2] == "黑马程序员").map(lambda x:(x[0][0:2],1))
result3 = rdd1.reduceByKey(lambda x,y:x+y). sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(result3)
print(f"最多的时段分别是{result3[0][0]},{result3[1][0]},{result3[2][0]}")

# 需求4：转换为json格式写出到文件
rdd.map(lambda x:x.split("\t")).\
    map(lambda x:json.dumps({"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]})).\
    coalesce(1).\
    saveAsTextFile(r"C:\Users\46655\Desktop\黑马python_副本\output_json.txt")


sc.stop()

