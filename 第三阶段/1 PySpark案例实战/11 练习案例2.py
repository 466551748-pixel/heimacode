import json

from pyspark import SparkContext, SparkConf
from unicodedata import category

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.textFile(r"C:\Users\46655\Desktop\黑马python_副本\orders.txt")

# 需求1：城市销售额的排名
# 变成一个个json字符串
json_str_rdd = rdd.flatMap(lambda x:x.split("|"))
# json字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
# (城市,销售额)
city_with_money_rdd = dict_rdd.map(lambda x:(x["areaName"],int(x["money"])))
# 按城市分组按销售额聚合
city_result_rdd= city_with_money_rdd.reduceByKey(lambda x,y:x+y)
# 按销售额聚合结果进行排序
result = city_result_rdd.sortBy(lambda x:x[1],ascending=False)
print("需求1的结果是：",result.collect())

# 需求2：全部城市有哪些商品类别在售卖
category_rdd = dict_rdd.map(lambda x:(x["category"]))
# 去重
result2 = category_rdd.distinct()
print("需求2的结果是：",result2.collect())

# 需求3：北京市有哪些商品类别在售卖
areaName_with_category_rdd = dict_rdd.map(lambda x:[x["areaName"],x["category"]])
# 过滤D
beijing_category_add = areaName_with_category_rdd.filter(lambda x:x[0]=="北京")
# 去重
result3 = beijing_category_add.map(lambda x:x[1]).distinct()
print("需求3的结果是",result3.collect())
sc.stop()
