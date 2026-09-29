"""
 基础柱状图的开发
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts, LegendOpts, TitleOpts, InitOpts
from pyecharts.globals import ThemeType
# 使用Bar构建基础柱状图
bar = Bar(init_opts=InitOpts(theme="red"))

# 添加x轴和y轴的数据
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(
    position="right"

))

# 反转x和y轴
bar.reversal_axis()
bar.set_global_opts(
    legend_opts=LegendOpts(pos_top="5%", pos_left="center"),  # ← 关键在这里

)
# 绘制
bar.render()