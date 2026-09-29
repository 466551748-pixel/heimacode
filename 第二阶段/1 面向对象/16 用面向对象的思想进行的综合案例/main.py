"""
 1.设计一个类，可以完成数据的封装
 2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
 3.读取文件，生产数据对象
 4.进行数据需求的逻辑计算（计算每一天的销售额）
 5.通过pyecharts进行绘图
"""

from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
text_file_reader = TextFileReader(r"C:\Users\46655\Desktop\黑马python_副本\2011年1月销售数据.txt")
json_file_reader = JsonFileReader(r"C:\Users\46655\Desktop\黑马python_副本\2011年2月销售数据JSON.txt")

jan_data:list[Record]= text_file_reader.read_data()

feb_data:list[Record] = json_file_reader.read_data()
# 将俩个月的数据合并成一个list存储
all_data:list[Record] = jan_data + feb_data

# 进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
print(data_dict)

# 可视化图表开发
bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis(
    "销售额",
    list(data_dict.values()),
    itemstyle_opts=ItemStyleOpts(                  # 渐变色
        color=JsCode("""                                     
            new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {offset: 0, color: '#83bff6'},
                {offset: 0.5, color: '#188df0'},
                {offset: 1, color: '#188df0'}
            ])
        """)
    )
)
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额"),
)

bar.render("每日销售额柱状图.html")