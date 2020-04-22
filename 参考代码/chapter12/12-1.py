import wx
#创建App对象.
app = wx.App()
#创建并设置Frame窗体.
frame = wx.Frame(None,title="第1个wxPython程序",size=(300,150))
#创建面板，添加到窗体frame中.
panel = wx.Panel(frame)
#创建、设置标签，添加到面板panel中.
sTxt_info = wx.StaticText(panel,label="欢迎来到Python世界！",pos=(60,40))
#显示窗体.
frame.Show(True)
#启动app.MainLoop()方法，进入循环.
app.MainLoop()
