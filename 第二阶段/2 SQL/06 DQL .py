"""
 1.基础数据查询
 语法：
 select 字段列或者* from 表 [where 条件判断];

 2.group by 分组聚合查询
 语法：
 select 字段列或者聚合函数 from 表 [where 条件判断] group by 列;
 聚合函数：sum()求和 avg()求平均值 min()求最小值 max()求最大值 count(列或者*)求数量
 注意:字段列只能出现group by写了的

 3.对查询结果进行排序分页
 语法：
 select 字段列或者聚合函数 from 表 [where 条件判断] group by 列 order by 列 [asc或desc] limit n[,m]
 asc升序，desc降序
 n:取n条
 n,m：从不包括n，向后取m条
"""