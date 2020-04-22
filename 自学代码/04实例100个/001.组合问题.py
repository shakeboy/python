# 参考链接
# 1.https://blog.csdn.net/kongsuhongbaby/article/details/84330094?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2
# 2.https://blog.csdn.net/destiny_python/article/details/77461518?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4
import itertools
"""
总结：主要实例分析了itertools库里combinations函数与permutations函数的区别 
combinations：不考虑顺序的排列组合
permutations：考虑顺序的排列组合
"""
print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.permutations([1, 2, 3, 4], 2)))
print(dir(itertools))