import wx
class MyFrame(wx.Frame):
  def __init__(self,parent,title):
    super(MyFrame,self).__init__(parent,title=title)
    self.InitUI()
  def InitUI(self):
    #创建并设置工具栏.
    tb = wx.ToolBar(self,-1)
    self.ToolBar = tb
    tb.AddRadioTool(101,'',wx.Bitmap("png/New.png"))           #方法一.
    Open = tb.AddRadioTool(102,'',wx.Bitmap("png/Open.png")) #方法二.
    Save = tb.AddRadioTool(103,'',wx.Bitmap("png/Save.png"))
    tb.Bind(wx.EVT_TOOL,self.OnClick)
    tb.Realize()
    #创建并设置文本区.
    self.text = wx.TextCtrl(self,-1,style=wx.EXPAND | wx.TE_MULTILINE)
    self.text.Bind(wx.EVT_MOTION,self.OnTextMotion)
    #创建并设置状态栏.
    self.statusbar = self.CreateStatusBar()
    self.statusbar.SetFieldsCount(2)
    self.statusbar.SetStatusWidths([-1,-2])
    #窗体设置.
    self.SetSize((500,240))
    self.Centre()
    self.Show(True)
  def OnClick(self,event):
    if str(event.GetId()) == "101": self.text.AppendText("您选择了新建(New)" + "\n")
    if str(event.GetId()) == "102": self.text.AppendText("您选择了打开(Open)" + "\n")
    if str(event.GetId()) == "103": self.text.AppendText("您选择了保存(Save)" + "\n")
  def OnTextMotion(self,event):
    #设置状态栏内容
    self.statusbar.SetStatusText("鼠标位置：" + str(event.GetPosition()),0)
    self.statusbar.SetStatusText(("文本框状态:" + str(self.text.IsEmpty())),1)
    event.Skip()
if __name__ == '__main__':
  ex = wx.App()
  MyFrame(None,"工具栏和状态使用示例")
  ex.MainLoop()
