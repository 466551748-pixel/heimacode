"""
 演示非单例模式的效果
"""
class strTools:
    pass

s1 = strTools()
s2 = strTools()
# 内存地址，独立对象
print(s1)
print(s2)