import wx
class MyFrame(wx.Frame):
  def __init__(self,superion):
    wx.Frame.__init__(self,parent=superion,title='2个数求和',size=(300,220))
    panel = wx.Panel(self)         #创建面板.
    #创建标签.
    wx.StaticText(parent=panel,label='请输入操作数1:',pos=(30,10))
    wx.StaticText(parent=panel,label='请输入操作数2:',pos=(30,50))
    wx.StaticText(parent=panel,label='结  果：',pos=(30,90))
    #创建文本框.
    self.txt_op1 = wx.TextCtrl(parent=panel,pos=(120,10))
    self.txt_op2 = wx.TextCtrl(parent=panel,pos=(120,50))
    self.txt_res = wx.TextCtrl(parent=panel,pos=(120,90),style=wx.TE_READONLY)
    #创建按钮并绑定事件.
    self.btn_Add = wx.Button(parent=panel,label='求 和',pos=(70,130))
    self.Bind(wx.EVT_BUTTON,self.On_btn_Add,self.btn_Add)
    self.btn_Quit = wx.Button(parent=panel,label='退 出',pos=(150,130))
    self.Bind(wx.EVT_BUTTON,self.On_btn_Quit,self.btn_Quit)
  #”求和”按钮事件处理方法.
  def On_btn_Add(self,event):
    op1 = int(self.txt_op1.GetValue())   	#返回文本框的内容.
    op2 = int(self.txt_op2.GetValue())   	#返回文本框的内容.
    sum = op1 + op2   	#求和.
    self.txt_res.SetValue(str(sum))	#将求和结果显示在文本框中.
  #”退出”按钮事件处理方法.
  def On_btn_Quit(self,event):
    wx.Exit()                                           #退出程序.
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None).Show()
  app.MainLoop()
