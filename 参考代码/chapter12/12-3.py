import wx
#创建窗体类，继承wx.Frame.
class MyFrame(wx.Frame):
  #定义构造方法.
  def __init__(self,parent):
    #调用父类构造方法，设置窗体参数.
    wx.Frame.__init__(self,parent,id=-1,title="芙蓉楼送辛渐",size=(250,160))
    panel = wx.Panel(self)       #创建面板.
    #创建标签，在标签中写入内容，添加到panel中.
    wx.StaticText(parent=panel,label="寒雨连江夜入吴",pos=(70,20))
    wx.StaticText(parent=panel,label="平明送客楚山孤",pos=(70,40))
    wx.StaticText(parent=panel,label="洛阳亲友如相问",pos=(70,60))
    wx.StaticText(parent=panel,label="一片冰心在玉壶",pos=(70,80))
    self.Center()                  #设置窗体运行初始位置为桌面中间.
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None).Show(True)
  app.MainLoop()
