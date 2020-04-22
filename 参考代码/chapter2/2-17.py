str = "时间是一切财富中最宝贵的财富"
print("子字符串位置：", str.find("财富"))             # 从字符串左边开始查找.
print("子字符串位置：", str.find("财富", 6))          # 从左边索引号为6的字符开始查找.
print("子字符串位置：", str.rfind("财富"))            # 从字符串右边开始查找.
print("子字符串位置：", str.rfind("财富", 4, 10))      # 从右边索引号4-10的字符开始查找.
print("子字符串位置：", str.rfind("成功"))            # 从字符串左边开始查找.
print(str.startswith("时间"))
print(str.endswith("财富"))



