# 中国十大宜居城市.
cityList = ["珠海", "威海", "信阳", "惠州", "厦门", "金华", "柳州", "曲靖", "九江", "绵阳"]
del cityList[8]                                 # 删除列表第9个元素.
print("del语句删除元素后:", cityList)
cityList.pop()                                 # 删除列表末尾元素.
cityList.pop(6)                                # 删除列表第7个元素.
cityList.remove("厦门")                        # 删除列表元素值为"厦门"的元素.
print("list.remove('厦门')删除元素后:", cityList)
cityList[4:]=[]
print("切片删除:", cityList)
cityList.clear()                                # 清空列表.
print("使用list.clear()清空列表后:", cityList)

