from pyecharts.charts import Bar
from pyecharts.options import InitOpts














f = open(r
"C:\Users\46655\Desktop\黑马python_副本\2011年1月销售数据.txt","r",encoding="utf-8")


lines = f.readlines()
print(lines)
print(len(lines))
i = 0
list_date = []
list_data = []
for i in range(0,31):
    list_data.append(0)
for i in range(0,len(lines)):
    list_1 = lines[i].split(",")
    if list_1[0] not in list_date:
        list_date.append(list_1[0])
    if list_1[0] in list_date:
        list_data[list_date.index(list_1[0])] += int(list_1[2])

# for i in range(0,len(lines)):
#     list_2 = lines[i].split(",")
#     if list_2[0] in list_date:

print(list_data)
print(list_date)

bar = Bar()
bar.add_xaxis(list_date)
bar.add_yaxis("总销售额",list_data)

bar.render()


