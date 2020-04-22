world_tournament_set = {"世界杯排球赛","世界乒乓球锦标赛","世界篮球锦标赛",
 		"世界足球锦标赛"}                              		#世界球类大赛.
print("世界大赛:",world_tournament_set)
world_tournament_set.remove("世界足球锦标赛")             	#删除指定集合元素.
print("set.remove()删除元素后:",world_tournament_set)
world_tournament_set.discard("世界杯排球赛")               	#删除指定集合元素.
print("set.discard()删除元素后:",world_tournament_set)
world_tournament_set.pop()         						#随机删除集合元素.
print("set.pop()删除元素后:",world_tournament_set)
world_tournament_set.clear()        					#清空集合元素.
print("set.clear()清空元素后:",world_tournament_set)
