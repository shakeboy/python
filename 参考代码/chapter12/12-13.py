import wx
class MyFrame(wx.Frame):
  def __init__(self,parent):
    wx.Frame.__init__(self,parent,size=(500,200),style=wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX)
    panel = wx.Panel(self,-1)                         #创建面板.
    box_h = wx.BoxSizer(wx.HORIZONTAL)              #创建水平boxsizer.
    txt_filePath = wx.TextCtrl(panel,-1)            #创建文本框.
    btn_open = wx.Button(panel,-1,label='打开')    #创建按钮.
    #将txt_filePath和btn_open添加到box_h中.
    box_h.Add(txt_filePath,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
    box_h.Add(btn_open,proportion=0,flag=wx.ALL,border=5)
    #创建编辑框.
    et_exit = wx.TextCtrl(panel,style=wx.TE_MULTILINE | wx.TE_RICH2)
    box_v = wx.BoxSizer(wx.VERTICAL)     #创建垂直boxsizer.
    box_v.Add(box_h,proportion=0,flag=wx.EXPAND) #将box_h添加到box_v中.
    #将et_exit添加到box_v中.
    box_v.Add(et_exit,proportion=1,flag=wx.EXPAND,border=5)
    panel.SetSizer(box_v)                  #设置panel布局.
if __name__ == '__main__':
  app = wx.App()
  frame = MyFrame(None)
  frame.SetTitle("BoxSizer使用示例")
  frame.Show()
  app.MainLoop()
