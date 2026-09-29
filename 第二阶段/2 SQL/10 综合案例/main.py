"""
 1.设计一个类，可以完成数据的封装
 2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
 3.读取文件，生产数据对象
 4.进行数据需求的逻辑计算（计算每一天的销售额）
 5.通过pyecharts进行绘图
"""

import os

from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pymysql import Connection
text_file_reader = TextFileReader(r"C:\Users\46655\Desktop\黑马python_副本\2011年1月销售数据.txt")
json_file_reader = JsonFileReader(r"C:\Users\46655\Desktop\黑马python_副本\2011年2月销售数据JSON.txt")

jan_data:list[Record]= text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()
# 将俩个月的数据合并成一个list存储
all_data:list[Record] = jan_data + feb_data
print(all_data)

# 构建mysql链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    passwd=os.environ["MYSQL_PASSWORD"],
    autocommit=True,
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_sql')
# 组织sql语句
for record in all_data:
    sql = (f"insert into orders(order_date,order_id,money,province) "
           f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')")
    cursor.execute(sql)
