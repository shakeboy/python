# 世界十大经典美食.
delicacyList1 = {"中国冰糖葫芦", "墨西哥卷饼", "英国炸鱼", "美国热狗", "土耳其烤肉", "新加坡炒粿"}
delicacyList2 = { "新加坡炒粿", "日本章鱼烧", "韩国炸鸡", "越南虾饼", "曼谷香脆煎饼"}
print("并集操作:", delicacyList1 | delicacyList2)
print("交集操作:", delicacyList1 & delicacyList2)
print("差集操作:", delicacyList1 - delicacyList2)
print("子集操作:", delicacyList1 < delicacyList2)
print("'墨西哥巧克力'是世界十大经典美食吗?", "墨西哥巧克力" in delicacyList1 | delicacyList2)
