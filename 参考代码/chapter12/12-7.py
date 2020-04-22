import wx
class MyFrame(wx.Frame):
  def __init__(self,*args,**kw):
    super(MyFrame,self).__init__(*args,**kw)
    self.InitUI()
  def InitUI(self):
    #创建菜单栏.
    self.menuBar = wx.MenuBar()
    #创建菜单，添加到菜单栏.
    self.menu_file = wx.Menu()
    self.menu_edit = wx.Menu()
    self.menu_about = wx.Menu()
    self.menuBar.Append(self.menu_file,"文件")
    self.menuBar.Append(self.menu_edit,"编辑")
    self.menuBar.Append(self.menu_about,"关于")
    #创建菜单项，添加到指定菜单.
    self.Menuitem_new = self.menu_file.Append(wx.ID_NEW,"新建\tCtrl+N")
    self.Menuitem_open = self.menu_file.Append(wx.ID_OPEN,"打开\tCtrl+O")
    self.Menuitem_save = self.menu_file.Append(wx.ID_SAVE,"保存\tCtrl+S")
    self.Menuitem_exit = self.menu_file.Append(wx.ID_EXIT,"退出\tCtrl+E")
    #将菜单栏添加到窗体.
    self.SetMenuBar(self.menuBar)
    #绑定事件.
    self.Bind(wx.EVT_MENU,self.OnNew,self.Menuitem_new)
    self.Bind(wx.EVT_MENU,self.OnOpen,self.Menuitem_open)
    self.Bind(wx.EVT_MENU,self.OnSave,self.Menuitem_save)
    self.Bind(wx.EVT_MENU,self.OnQuit,self.Menuitem_exit)
    #设置窗体.
    self.SetSize((400,200))
    self.SetTitle("菜单使用示例")
    self.Center()
    self.Show()
  #菜单项事件处理方法.
  def OnNew(self,e):wx.MessageBox("您选择了新建(New)菜单！")
  def OnOpen(self,e):wx.MessageBox("您选择了打开(Open)菜单！")
  def OnSave(self,e):wx.MessageBox("您选择了保存(Save)菜单！")
  def OnQuit(self,e):self.Close()                     #退出程序.
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None)
  app.MainLoop()
