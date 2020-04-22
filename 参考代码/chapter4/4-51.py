import sys

print('*' * 40)
print('--------------游戏角色管理--------------')
print('1:查询角色')
print('2:添加角色')
print('3:修改角色')
print('4:删除角色')
print('5:显示所有角色')
print('-1:退出程序')
print('*' * 40)

# 角色列表.
roleList = [{"姓名": "刘备","单位": "蜀国","职务": "董事长兼总经理","武力": 6}]
while True:
  SN = int(input('===请输入操作序号: '))  # 输入操作序号.
  if SN in [1,2,3,4,5,-1]:
    if SN == 1:  # 查询角色.
      姓名 = input("请输入要查找角色的姓名: ")
      searchFlag = False  # 查找标志.
      for role in roleList:
        if 姓名 == role['姓名']:
          print("姓名: %s, 单位: %s, 职务: %s, 武力: %3.1f." % (role['姓名'],role['单位'],role['职务'],role['武力']))
          searchFlag = True  # 表示找到了
          break
      # 判断是否找到.
      if searchFlag == False:
        print('对不起。没有您要查找的角色!')
    elif SN == 2:  # 添加新角色
      姓名 = input('请输入姓名: ')
      searchFlag = False
      for role in roleList:
        if 姓名 == role['姓名']:
          print("您所输入的角色已存在！")
          searchFlag = True  # 表示找到了
          break
      if searchFlag == False:
        单位 = input('请输入单位: ')
        职务 = input('请输入职务: ')
        武力 = float(input('请输入武力: '))
        newRole = {}
        newRole["姓名"] = 姓名
        newRole["单位"] = 单位
        newRole["职务"] = 职务
        newRole["武力"] = 武力
        roleList.append(newRole)
    elif SN == 3:  # 修改角色.
      姓名 = input('请输入要修改角色的姓名: ')
      modifyFlag = False
      for role in roleList:
        if role['姓名'] == 姓名:
          role['单位'] = input('请输入新的单位: ')
          role['职务'] = input('请输入新的职务: ')
          role['武力'] = float(input('请输入新的武力: '))
          modifyFlag = True
          break
      if modifyFlag:
        print("修改角色成功！")
      else:
        print('您要修改的角色不存在！')
    elif SN == 4:  # 删除角色.
      姓名 = input("请输入要删除角色的姓名: ")
      delFlag = False
      for role in roleList:
        if role['姓名'] == 姓名:
          delFlag = True
          roleList.remove(role)
          break
      if delFlag:
        print("删除角色成功！")
      else:
        print("您要删除的角色不存在!")
    elif SN == 5:  # 显示所有角色.
      for role in roleList:
        print("姓名: %s, 单位: %s, 职务: %s, 武力: %3.1f." %(role['姓名'],role['单位'],role['职务'],role['武力']))
    else:  # 退出程序.
      print('退出程序!')
      sys.exit(0)
  else:
    print("输入错误!请重新输入'-1,1-5'之间的操作序号！")
