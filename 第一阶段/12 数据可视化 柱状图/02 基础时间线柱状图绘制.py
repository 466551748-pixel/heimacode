"""
 Timeline()  时间线
 柱状图描述的是分类数据，回答的是每一个分类：有多少？ 的问题
 柱状图很难动态的描述一个趋势性的数据，所以pyecharts为我们提供了一种解决方案-->时间线

 如果说一个Bar()对象是一张图表的话，时间线就是创建一个一维的x轴，轴上每一个点就是一个图表对象
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts ,LegendOpts,TitleOpts

# bar1
bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,30,10],label_opts=LabelOpts(
    position="right"
))
bar1.reversal_axis()
bar1.set_global_opts(
    legend_opts=LegendOpts(pos_top="5%", pos_left="center"),  # ← 关键在这里
)

# bar2
bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,50,40],label_opts=LabelOpts(
    position="right"
))
bar2.reversal_axis()
bar2.set_global_opts(
    legend_opts=LegendOpts(pos_top="5%", pos_left="center"),  # ← 关键在这里
)

# bar3
bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[70,60,50],label_opts=LabelOpts(
    position="right"
))
bar3.reversal_axis()
bar3.set_global_opts(
    legend_opts=LegendOpts(pos_top="5%", pos_left="center"),  # ← 关键在这里
)

# 设置时间线加入图表
timeline = Timeline({"theme":ThemeType.DARK})  # 设置主题
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

# 设置自动播放
timeline.add_schema(
    play_interval=1000,        # 自动播放时间间隔，单位毫秒
    is_timeline_show=True,     # 是否在自动播放的时候显示时间线
    is_auto_play=True,         # 是否自动播放
    is_loop_play=True,         # 是否循环自动播放
)

timeline.render()