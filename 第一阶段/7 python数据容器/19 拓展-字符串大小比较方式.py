"""
 字符串的比较：字符串是按位比较，也就是一位位进行对比，只要有一位大，那么整体就大
"""

# abd 比较 abc
print(f"abd大于abc，结果是：{"abd" > 'abc'}")

# ad 比较 abc ：只要有一位大，整个都大
print(f"ad大于abc，结果是：{'ad' > 'abc'}")

# ab 比较 abc ：相同长度越长越大
print(f"abc大于ab，结果是：{'abc' > 'ab'}")

## key1 比较 key2
print(f"key2大于key1，结果是：{'key2' > 'key1'}")

