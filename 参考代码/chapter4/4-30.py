#中国古代部分杰出人物.
chinese_figure_dict = {"张衡":"地质学家","张仲景":"医学家","祖冲之":"数学家"}
chinese_figure_dict_copy1 = chinese_figure_dict.copy() #字典浅复制.
chinese_figure_dict_copy2 = chinese_figure_dict          #字典深复制.
chinese_figure_dict["沈括"] = "科学家"
print(chinese_figure_dict)
print(chinese_figure_dict_copy1)
print(chinese_figure_dict_copy2)
del chinese_figure_dict                                       #删除字典.
print(chinese_figure_dict)
