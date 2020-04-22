# 定义商品类
class goods:
    def __init__(self, name):
        self.__name = name

    #     数量
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    # 进价
    @property
    def bid(self):
        return self.__bid

    @bid.setter
    def bid(self, bid):
        self.__bid = bid

    # 售价
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property  # 设置属性为只读.
    def name(self):
        return self.__name


list_goods = []
name = []
good1 = goods("冰糖葫芦")
good1.count = 5
good1.bid = 3
good1.price = 5


list_goods.append(good1)

for i in list_goods:
    name.append(i.name)

print("****************超市系统******************")
print("1、显示所有商品")
print("2、添加新的商品（包括商品名称、数量和进货价格）")
print("3、修改商品")
print("4、删除商品")
print("5、卖出商品，包括商品名称、数量和售出价格")
print("6、卖出商品，包括每种销售商品名称、数量、进货总价、销售总价等")
print("-1、退出")

while 1:
    n = int(input("请输入你的选择："))
    if n == 1:
        for i in list_goods:
            print("商品名称：%s，数量：%d，售出单价：%.2f元" % (i.name, i.count, i.price))
    elif n == 2:
        name = str(input("请输入添加商品的名称："))
        count = int(input("请输入添加商品的数量："))
        bid = int(input("请输入添加商品的进价："))
        price = int(input("请输入添加商品的售价："))
        good = goods(name)
        good.count = count
        good.bid = bid
        good.price = price
        list_goods.append(good)
        for i in list_goods:
            print("商品名称：%s，数量：%d，售出单价：%.2f元" % (i.name, i.count, i.price))
        print("商品添加成功！")
    elif n == 3:
        choice = str(input("请输入您要修改的商品名称："))
        if choice in name:
            for i in list_goods:
                count = int(input("请输入修改商品的数量："))
                bid = int(input("请输入修改商品的进价："))
                price = int(input("请输入修改商品的售价："))
                i.count = count
                i.bid = bid
                i.price = price
                print("修改成功！")
        else:
            print("超市中没有该商品")
    elif n == 4:
        choice = str(input("请输入您要删除的商品名称："))
        if choice in name:
            list_goods.remove(i)
            print("删除成功！")
        else:
            print("超市中没有该商品")

    elif n == 5:
        choice = str(input("请输入您要买的商品名称："))
        if choice in name:
            num = int(input("请输入您要买的数量："))
            for i in list_goods:
                if i.name == choice:
                    if num <= i.count:
                        i.count -= num
                        totalPrice = num * i.price
                        print("%s的数量还剩余：%d，售出价格为%.2f" % (i.name, i.count, totalPrice))
                    else:
                        print("商品剩余数量不足")
        else:
            print("超市中没有该商品")
    elif n == 6:
        choice = str(input("请输入您要买的商品名称："))
        if choice in name:
            num = int(input("请输入您要买的数量："))
            for i in list_goods:
                if i.name == choice:
                    if num <= i.count:
                        total_in = i.bid * i.price
                        i.count -= num
                        totalPrice = num * i.price
                        print("%s的数量还剩余：%d，售出总价为%.2f，购进总价为：%.2f"
                              % (i.name, i.count, totalPrice, total_in))
                    else:
                        print("商品剩余数量不足")
        else:
            print("超市中没有该商品")
    else:
        exit()
