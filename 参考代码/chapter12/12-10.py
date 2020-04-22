import wx
class MyFrame(wx.Frame):
  def __init__(self,superion):
    wx.Frame.__init__(self,parent=superion,title='TextEntryDialog使用示例',
      size=(260,200))
    panel = wx.Panel(self)
    wx.StaticText(parent=panel,label="您的姓名:",pos=(15,55),size=(60,30))
    self.txt_name = wx.TextCtrl(parent=panel,pos=(75,50),size=(160,30),
      style=wx.TE_READONLY)
    self.btn_name = wx.Button(parent = panel,label = '请输入姓名',pos=(85,110))
    self.Bind(wx.EVT_BUTTON,self.On_btn_name,self.btn_name)
  #按钮事件.
  def On_btn_name(self,event):
    dlg = wx.TextEntryDialog(self,'请输入您的姓名：','文本输入对话框')
    if dlg.ShowModal() == wx.ID_OK:
      self.txt_name.SetValue(dlg.GetValue())
    dlg.Destroy()
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None).Show()
  app.MainLoop()
