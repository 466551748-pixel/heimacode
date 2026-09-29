# 函数功能：接收传入字符串，将字符串反转返回
def str_reverse(s):
    result = s[::-1]
    print(result)
    return result

# 按照下标x和y，对字符串进行切片
def substr(s,x,y):
    print(s[x:y])
    return s[x:y]