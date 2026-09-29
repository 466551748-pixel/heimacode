from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])



"""
 pyecharts模块中有很多配置选项，常用俩个类别选项
 1.全局配置选项：针对整个图像进行配置，如标题，图例
    通过set_global_opts方法进行配置
 2.系列配置选项：针对具体的轴数据进行配置，如y轴
 
"""
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="",pos_bottom="20%"),
    legend_opts=LegendOpts(is_show=True,pos_top="20%",pos_right="20%"),
    toolbox_opts=ToolboxOpts(is_show=True,pos_top="20%"),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过render方法将图像生成
line.render()
