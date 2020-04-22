import wx
class IsPrimeFrame(wx.Frame):
  def __init__(self,superion):
    wx.Frame.__init__(self,parent=superion,title='fontDialog使用示例',size=
      (240,220))
    panel = wx.Panel(self)
    self.txt_font = wx.TextCtrl(parent=panel,value="wx.fontDialog使用！",pos=(20,50),size=(200,30),style=wx.TE_READONLY)               #创建文本框.
    #创建按钮，添加到面板中.
    self.btn_font = wx.Button(parent=panel,label='改变字体',pos=(70,130))
    self.Bind(wx.EVT_BUTTON,self.On_btn_font,self.btn_font)  #绑定事件.
  #按钮事件处理方法.
  def On_btn_font(self,event):
    dlg = wx.FontDialog(self,wx.FontData())
    if dlg.ShowModal() == wx.ID_OK:
      font = dlg.GetFontData().GetChosenFont()
      self.txt_font.SetFont(font)
      dlg.Destroy()
if __name__ == '__main__':
  app = wx.App()
  IsPrimeFrame(None).Show()
  app.MainLoop()
