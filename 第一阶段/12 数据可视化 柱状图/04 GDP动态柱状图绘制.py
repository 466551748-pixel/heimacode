# 读取文件
from scipy.constants import year
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
f = open("/Users/zhuangyan/Desktop/黑马数据可视化/1960-2019全球GDP数据.csv","r",encoding="gb2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一行
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 如何判断字典里有没有指定的key呢？
    try:
        data_dict[year].append([country,gdp])
    except:
        data_dict[year] = []
        data_dict[year].append([country,gdp])

timeline = Timeline(init_opts=InitOpts(theme="light"))
# 时间排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda x: x[1])
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country in year_data:
        x_data.append(country[0])
        y_data.append(country[1]/100000000)
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("gdp(亿)",y_data,label_opts=LabelOpts(position="right"),color_by="data",
                  itemstyle_opts=ItemStyleOpts(color="red",border_color="black"))
    bar.set_global_opts(
        title_opts=TitleOpts(title="每年gdp前8国家"),
        legend_opts=LegendOpts(pos_top="5%",pos_left="center"),
    )
    bar.reversal_axis()
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,        # 自动播放时间间隔，单位毫秒
    is_timeline_show=True,     # 是否在自动播放的时候显示时间线
    is_auto_play=True,         # 是否自动播放
    is_loop_play=True,         # 是否循环自动播放
)
timeline.render()