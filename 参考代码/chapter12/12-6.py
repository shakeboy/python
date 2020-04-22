import wx
class MyFrame(wx.Frame):
  def __init__(self):
    super().__init__(parent=None,title="ListBox使用",size=(250,170))
    self.InitUI()
  def InitUI(self):
    self.Center()   	#设置窗体居中.
    panel = wx.Panel(parent=self)
    wx.StaticText(panel,label='请选择你从事的行业：',pos=(10,10))
    #创建列表框、添加选项和绑定事件.
    list = ['教育培训','航空航天',"石油化工","交通运输","医药卫生","旅游休闲"]
    self.listbox = wx.ListBox(panel,-1,choices=list,style=wx.LB_SINGLE,pos=(140,10))
    self.Bind(wx.EVT_LISTBOX,self.on_listbox,self.listbox)   #绑定事件.
    self.Show()
  #列表事件处理方法.
  def on_listbox(self,event):
    wx.MessageBox(self.listbox.GetStringSelection())
if __name__ == '__main__':
  app=wx.App()
  MyFrame().Show()
  app.MainLoop()
