import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f  = open("/Users/zhuangyan/Desktop/黑马数据可视化/疫情.txt","r",encoding="utf-8")

m_data = f.read()
f.close()

data_dict = json.loads(m_data)
data = []
province_data_list = data_dict["areaTree"][0]["children"][7]["children"]
for province_data in province_data_list:
    province_name = province_data["name"] + "市"
    if province_name == "境外输入":
        continue
    if province_name == "地区待确认市":
        province_name = "云浮市"

    province_confirm = province_data["total"]["confirm"]
    data.append((province_name, province_confirm))

map = Map()
map.add("各区确诊人数",data,"广东")
map.set_global_opts(
    title_opts = TitleOpts(title="广东省疫情图"),
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":0,"max":99,"label":"1-99人","color":"yellow"},
            {"min":100,"max":999,"label":"1-99人","color":"blue"},
            {"min":1000,"max":9999,"label":"1-99人","color":"red"},

        ]
    )
)
map.render()
