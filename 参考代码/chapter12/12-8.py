import wx
class MyFrame(wx.Frame):
  def __init__(self,*args,**kw):
    super(MyFrame,self).__init__(*args,**kw)
    self.panel = wx.Panel(self)
    self.InitUI()
  def InitUI(self):
    #创建菜单栏和菜单.
    menuBar = wx.MenuBar()
    self.popupMenu = wx.Menu()
    #创建菜单项，添加到菜单.
    self.popupCopy = self.popupMenu.Append(wx.ID_COPY,'复制')
    self.popupCut = self.popupMenu.Append(wx.ID_CUT,'剪切')
    self.popupPaste = self.popupMenu.Append(wx.ID_PASTE,'粘贴')
    #绑定右键弹出菜单事件.
    self.Bind(wx.EVT_CONTEXT_MENU,self.OnRClick)
    #绑定菜单项事件.
    self.Bind(wx.EVT_MENU,self.OnpopupCopy,self.popupCopy)
    self.Bind(wx.EVT_MENU,self.OnpopupCut,self.popupCut)
    self.Bind(wx.EVT_MENU,self.OnpopupPaste,self.popupPaste)
    #将菜单栏添加到窗体.
    self.SetMenuBar(menuBar)
    #设置窗体.
    self.SetSize((400,150))
    self.SetTitle("弹出式菜单使用示例")
    self.Center()
    self.Show()
  #右键弹出菜单事件处理方法.
  def OnRClick(self,event):
    pos = event.GetPosition()
    pos = self.panel.ScreenToClient(pos)
    self.panel.PopupMenu(self.popupMenu,pos)
  #菜单项事件处理方法.
  def OnpopupCopy(self,event):wx.MessageBox("您选择了复制(Copy)菜单项！")
  def OnpopupCut(self,event):wx.MessageBox("您选择了剪切(Cut)菜单项！")
  def OnpopupPaste(self,event):wx.MessageBox("您选择了粘贴(Paste)菜单项！")
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None)
  app.MainLoop()
