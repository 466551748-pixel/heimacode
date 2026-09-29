"""
思考：无论在while循环还是for循环，都是重复性的执行特定操作
     在这个重复的过程中，会出现一些情况让我们不得不：
     一.(continue)暂时跳过某次循环，直接进行下一次循环 (通常搭配if使用)
        for i in range(1,100)
            语句1
            continue
            语句2
        在循环内遇到continue，语句2不会执行
     二.(break)提前结束所在的循环，不再继续
       for i in range(1,100)
            语句1
            break
            语句2
       只会输出一个语句1
     都是影响所在循环，影响不了上层循环
"""
# continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")
