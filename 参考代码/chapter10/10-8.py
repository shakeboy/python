#定义银行类.
class Bank:
  money = 0
  def Account(self,save,cost):
    if save < 0 or cost > 0 or (save + cost + self.money) < 0:
      raise BankException(save,cost,self.money)
    self.money = self.money + save + cost
    print("业务(%d, %d)办理后用户帐号资金为 %d."%(save,cost,self.money))
  def getMoney(self):
    return self.money

#定义异常处理类.
class BankException(BaseException):
  message = ""
  def __init__(self,save,cost,money):
    self.message = "入帐资金" + str(save) + "是负数, 或支出" + str(cost) + "是正数,  或业务办理后帐号资金" + str(save + cost + money) + "小于零，不符合系统要求."
  def getMessage(self):
    return self.message

if __name__ == '__main__':
  bank = Bank()
  try:
    bank.Account(300,-200)
    bank.Account(200,-100)
    bank.Account(200,-600)
  except BankException as e:
    print(e.getMessage())
  print("用户帐号资金为: %d."%bank.getMoney())
