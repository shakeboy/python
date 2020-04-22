grade_id=[1,2,3,4,5]
grade_list=[90,75,80,54,97]
grade=dict(zip(grade_id,grade_list))
# {"01":80,"02":85,"03":70,"04":84,"05":97}
grade[6]=83
print("添加后的成绩为：",grade)
grade[6]=87
print("修改后的成绩为：",grade[6])
grade.pop(6)
print("删除学号为06的成绩：",grade)
print("访问学号为03的成绩：",grade[3])
print("最高分为：",max(grade_list))
print("最低分为：",min(grade_list))
len=len(grade_list)
sum=sum(grade_list)
average=sum/len
print("平均分为：",average)