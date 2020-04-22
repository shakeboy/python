import wx,os
class MyFrame(wx.Frame):
  def __init__(self,superion):
    wx.Frame.__init__(self,parent=superion,title='fileDialog使用示例',
      size=(300,180))
    panel = wx.Panel(self)
    wx.StaticText(parent=panel,label="当前文件:",pos=(20,50),size=(60,30))
    self.txt_file = wx.TextCtrl(parent=panel,pos = (80,50),size=(180,30))
    self.btn_file = wx.Button(parent=panel,label='选择文件',pos=(100,110))
    self.Bind(wx.EVT_BUTTON,self.On_btn_file,self.btn_file)
  #按钮事件.
  def On_btn_file(self,event):
    #dlg = wx.FileDialog(self)
    wildcard = "Python 07teacher_source(*.py) | *.py |All files(*. *) | *.* "
    dlg = wx.FileDialog(self, "选择一个文件",wildcard,style=wx.FD_OPEN)
    if dlg.ShowModal() == wx.ID_OK:
      fileName = dlg.GetFilename()
      self.txt_file.SetValue(fileName)
      #print("hello")
    dlg.Destroy()
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None).Show()
  app.MainLoop()
