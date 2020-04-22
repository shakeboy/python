#定义书籍类Book.
class Book:
  #构造方法.
  def __init__(self,Name,Price,State):
    self.Name = Name                			#书籍名称.
    self.Price = Price                  		#书籍价格.
    self.State = State                  		#书籍状态.
  def __str__(self):
    State = '已借出'
    if self.State == 1:
      State = '未借出'
    return '名称:《%s》, 单价: %.2f元,  状态: %s' % (self.Name,self.Price,State)

#定义书籍管理类bookManager.
class BookManager:
  #书籍列表books，每个元素是一个书籍对象.
  books = []
  #构造方法.
  def init(self):
    self.books.append(Book('茶花女',32.6,0))
    self.books.append(Book('傲慢与偏见',41.8,1))
    self.books.append(Book('罗密欧与朱丽叶',29.5,1))
  #菜单.
  def Menu(self):
    self.init()
    print('\"书籍出租管理系统\"菜单:')
    print('1.显示书籍')
    print('2.增加书籍')
    print('3.借出书籍')
    print('4.归还书籍')
    print('5.统计书籍')
    print('-1.退出系统')
    while (True):
      menu_item = int(input('******请输入菜单编号: '))
      if menu_item == 1:
        self.show_all_books()
      elif menu_item == 2:
        self.add_books()
      elif menu_item == 3:
        self.lend_books()
      elif menu_item == 4:
        self.return_books()
      elif menu_item == 5:
        self.count_books()
      elif menu_item == -1:
        print('谢谢使用!')
        break
      else:
        print("请输入-1，1~5范围的菜单项编号！")
  #1. 查询并显示所有书籍.
  def show_all_books(self):
    for book in self.books:
      print(str(book))
  #2. 添加书籍.
  def add_books(self):
    book_name = input('请输入添加书籍名称: ')
    ret = self.check_books(book_name)
    if ret != None:
      print('书籍已经存在！')
    else:
      book_price = float(input('请输入书籍价格: '))
      new_book = Book(book_name,book_price,1)
      self.books.append(new_book)
      print('添加书籍成功！')
  #3. 借出书籍.
  def lend_books(self):
    book_name = input('请输入借出书籍的名称: ')
    ret = self.check_books(book_name)
    if ret != None:
      if ret.State == 0:
        print('您要借的书籍已经借出去了')
      else:
        ret.State = 0
        print('借书成功!')
    else:
      print('您要借的书籍不存在！')
  #4. 归还书籍.
  def return_books(self):
    book_name = input('请输入归还书籍名称: ')
    ret = self.check_books(book_name)
    if ret == None:
      print('您要归还的书籍不存在！')
    else:
      if ret.State == 1:
        print('您要归还的书籍未借出！')
      else:
        lend_days = int(input('请输入借书天数: '))
        fee = round(ret.Price * lend_days * 0.1,2)       	#保留2位小数.
        print('借出 %d 天，应付租书费%.2f元. ' % (lend_days,fee))
        while True:
          pay = float(input('请输入支付金额: '))
          if pay < fee:
            print('您所输入的金额不够！')
          else:
            break
        if pay >= fee:
          print('找零: %.2f元.' % (pay - fee))
        ret.State = 1
        print('还书成功！')
  #5. 统计书籍状况.
  def count_books(self):
    lend_count = 0
    not_lend_count = 0
    for item in self.books:
      if item.State == 0:
        lend_count = lend_count + 1
      else:
        not_lend_count = not_lend_count + 1
    print("已借出书籍: %d 册."%lend_count)
    print("未借出书籍: %d 册." %not_lend_count)
    print("总书籍: %d 册." %len(self.books))
  #检查书籍是否存在.
  def check_books(self,Name):
    for book in self.books:
      if book.Name == Name:
        return book
    else:
      return None

if __name__  ==  "__main__":
  #创建BookManager类的实例.
  manager = BookManager()
  #调用Menu()方法.
  manager.Menu()
