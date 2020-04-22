import wx
#创建窗体类，继承wx.Frame.
class MyFrame(wx.Frame):
  #定义构造方法.
  def __init__(self):
    #调用父类构造方法,设置窗体参数.
    wx.Frame.__init__(self,None,-1,"事件处理示例",size=(300,150))
    panel = wx.Panel(self,-1)                  #创建面板.
    panel.Bind(wx.EVT_MOTION, self.OnMove)  #绑定事件.
    #创建标签.
    self.sTxt_pos = wx.StaticText(panel,-1, "",pos=(70,30),size=(160,40))
    #创建字体并设置为标签self.sTxt_pos的字体.
    font = wx.Font(20,wx.DECORATIVE,wx.NORMAL,wx.BOLD)
    self.sTxt_pos.SetFont(font)
  #鼠标移动事件处理方法.
  def OnMove(self,event):
    pos = event.GetPosition()                              #返回鼠标坐标位置.
    self.sTxt_pos.SetLabel("%s : %s" % (pos.x,pos.y)) #显示鼠标坐标位置.
if __name__ == '__main__':
  app = wx.App(False)
  MyFrame().Show(True)             #创建窗体对象，显示窗体.
  app.MainLoop()
