import wx
class MyFrame(wx.Frame):
  def __init__(self,parent,title):
    super(MyFrame,self).__init__(parent,title=title,size=(250,200))
    self.InitUI()
    self.Centre()
    self.Show()
  def InitUI(self):
    panel = wx.Panel(self)
    gridSizer = wx.GridSizer(4,2,10,10)     #4*2网格.
    sTxt_name = wx.StaticText(panel,label="请输入您的姓名:",style=wx.ALIGN_LEFT)
    sTxt_sex = wx.StaticText(panel,label="请输入您的性别:",style=wx.ALIGN_LEFT)
    sTxt_age = wx.StaticText(panel,label="请输入您的年龄:",style=wx.ALIGN_LEFT)
    txt_name = wx.TextCtrl(panel)
    txt_sex = wx.TextCtrl(panel)
    txt_age = wx.TextCtrl(panel)
    btn_ok = wx.Button(parent=panel,label="确定")
    btn_exit = wx.Button(parent=panel,label="退出")
    gridSizer.Add(sTxt_name,1,wx.EXPAND)    #位置:第1行第1列.
    gridSizer.Add(txt_name,1,wx.EXPAND)     #位置:第1行第2列.
    gridSizer.Add(sTxt_sex,1,wx.EXPAND)     #位置:第2行第1列.
    gridSizer.Add(txt_sex,1,wx.EXPAND)      #位置:第2行第2列.
    gridSizer.Add(sTxt_age,1,wx.EXPAND)     #位置:第3行第1列.
    gridSizer.Add(txt_age,1,wx.EXPAND)      #位置:第3行第2列.
    gridSizer.Add(btn_ok,1,wx.EXPAND)       #位置:第4行第1列.
    gridSizer.Add(btn_exit,1,wx.EXPAND)     #位置:第4行第2列.
    panel.SetSizer(gridSizer)
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None,title='GridSizer使用示例')
  app.MainLoop()
