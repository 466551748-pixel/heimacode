import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取文件
f = open("/Users/zhuangyan/Desktop/黑马数据可视化/疫情.txt","r",encoding="utf-8")
m = f.read()
# 关闭文件
f.close()
# json转python
data_dict = json.loads(m)
# 从字典取到各个省数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份的确诊人数，并各省的数据都封装到列表内
data_list = []    # 绘图需要的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]
    if province_name in ["北京","上海","天津","重庆"]:
        province_name = province_name + "市"
    elif province_name in ["香港","澳门"]:
        province_name = province_name + "特别行政区"
    elif province_name in ["内蒙古","西藏"]:
        province_name = province_name + "自治区"
    elif province_name == "广西":
        province_name = province_name + "壮族自治区"
    elif province_name == "新疆":
        province_name = province_name + "维吾尔自治区"
    elif province_name == "宁夏":
        province_name = province_name + "回族自治区"
    else:
        province_name = province_name + "省"
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数",data_list,"china")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"lable":"1-99人","color":"red"},
            {"min":100,"max":999,"lable":"100-999人","color":"blue"},
            {"min":1000,"max":4999,"lable":"1000-4999人","color":"yellow"},
            {"min":5000,"max":9999,"lable":"5000-9999人","color":"#AEEEEE"},
            {"min":10000,"max":99999,"lable":"10000-99999人","color":"FFFAF0"},
            {"min":100000,"lable":"100000+人","color":"FFEFD5"},
        ])
)
# 打印地图
map.render()