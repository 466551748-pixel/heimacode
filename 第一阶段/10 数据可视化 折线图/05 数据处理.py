"""
 演示可视化需求
"""
import json

from matplotlib.pyplot import title
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts

f_us = open("/Users/zhuangyan/Desktop/黑马数据可视化/美国.txt","r",encoding="utf-8")
f_jp = open("/Users/zhuangyan/Desktop/黑马数据可视化/日本.txt","r",encoding="utf-8")
f_in = open("/Users/zhuangyan/Desktop/黑马数据可视化/印度.txt","r",encoding="utf-8")

us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 去掉不符合json规范的开头和结尾
us_data = us_data.strip("jsonp_1629344292311_69436(")
jp_data = jp_data.strip("jsonp_1629350871167_29498(")
in_data = in_data.strip("jsonp_1629350745930_63180(")
us_data = us_data.strip(");")
jp_data = jp_data.strip(");")
in_data = in_data.strip(");")

# json装python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取日期数据，用于x轴，取2020年，到314下标结束
us_x_data = us_trend_data["updateDate"][0:314]

# 获取确诊人数，用于y轴
us_y_data = us_trend_data["list"][0]["data"][0:314]
jp_y_data = jp_trend_data["list"][0]["data"][0:314]
in_y_data = in_trend_data["list"][0]["data"][0:314]


line_chart = Line()
line_chart.add_xaxis(us_x_data)
line_chart.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False)) # 轴上数据不显示
line_chart.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line_chart.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
line_chart.set_global_opts(
    title_opts=TitleOpts(title="2022年三国确诊新冠",pos_left="center"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)

line_chart.render()

f_us.close()
f_jp.close()
f_in.close()