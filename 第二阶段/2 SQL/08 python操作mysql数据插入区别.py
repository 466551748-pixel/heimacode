"""
 pymysql在执行数据插入或者其他产生数据更改的sql语句时，默认是需要提交更改的
 也就是说，需要通过代码 ‘确认’ 这种更改行为 （手动确认）
 通过 链接对象.commit() 确认此行为

 或者在Connection内设置自动提交  autocommit = True
"""

# 演示使用pymysql库进行数据插入的操作

import os

from pymysql import Connection
# 构建数据库的连接
conn=Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = os.environ["MYSQL_PASSWORD"],
    autocommit = True
)
# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('world')
# 执行sql
cursor.execute('insert into student values(10001,"周杰伦",31,"男");')
# 通过commit确认
# conn.commit()
# 关闭链接
conn.close()
