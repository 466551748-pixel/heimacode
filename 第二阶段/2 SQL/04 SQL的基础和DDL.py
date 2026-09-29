"""
 SQL全称：Structured Query Language，结构化查询语言，用于 访问和处理数据库的标准的计算机语言
 已经称为数据库领域统一的数据操作标准语言，简单来说，就是操作数据库的专用工具

 由于数据库管理系统（数据库软件）功能非常多，不仅仅是存储数据，还包括：数据的管理，表的管理，库的管理，账户管理，权限管理等等
 所以操作数据库的SQL语言，也基于功能，也可以划分为4类：
 1.数据定义：DDL (Data Definition Language)
    库的创建删除、表的创建删除等
 2.数据操纵：DML（Data Manipulation Language）
    新增数据、删除数据、修改数据等
 3.数据控制：DCL（Data Control Language）
    新增用户、删除用户、密码修改、权限管理等
 4.数据查询：DQL（Data Query Language）
    基于需求查询和计算数据

 SQL的语法特征
 1.大小写不敏感 ：不区分大小写的，语句大写小写都行
 2.可以单行或多行书写，最后以;结束
 3.支持注释：
    单行注释：-- 注释内容 （--后面一定要有一个空格）
    单行注释：# 注释内容  （#后面可以不加空格，规范加上）
    多行注释：/* 注释内容 */

 一.DDL - 库管理
 1.查看数据库
 SHOW DATABASES;
 2.使用数据库
 USE 数据库名称;
 3.创建数据库
 CREATE DATABASE 数据库名称 [CHARSET UTF8]       # 中括号里面代表可选的东西，真实写，不写中括号
 4.删除数据库
 DROP DATABASE 数据库名称;
 5.查看当前使用的数据库
 SELECT DATABASE();

 二.DDL - 表管理
 1.查看有哪些表 ：需要先选择数据库
 SHOW TABLES;
 2.删除表
 DROP TABLE 表名称;
 DROP TABLE IF EXISTS 表名称;
 3.创建表
 create table 表名称(
    列名称 列类型,
    列名称 列类型,
 )
 列类型：int float varchar(长度：最大255)：字符串  date：日期类型  timestamp：时间戳类型
"""