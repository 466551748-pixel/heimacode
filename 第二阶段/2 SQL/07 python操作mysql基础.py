import os

from pymysql import Connection
# 构建数据库的连接
conn=Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = os.environ["MYSQL_PASSWORD"],
)
# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('world')
# 执行sql
# cursor.execute("create table test_pymysql(id int);")

# 查询
cursor.execute('select * from student;')
# 获取查询结果
results = cursor.fetchall()
print(results)
for r in results:
    print(r)

# 关闭连接

cursor.close()

