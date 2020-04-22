import wx
class MyFrame(wx.Frame):
  def __init__(self,parent,title):
    super(MyFrame,self).__init__(parent,title=title,size=(320,200))
    self.InitUI()
  def InitUI(self):
    panel = wx.Panel(self)
    self.cb_music = wx.CheckBox(panel,label='音乐',pos=(10,10))  #复选框.
    self.cb_movie = wx.CheckBox(panel,label='电影',pos=(10,40))  #复选框.
    self.cb_artist = wx.CheckBox(panel,label='艺术',pos=(10,70)) #复选框.
    #创建选项列表，并添加到单选按钮中.
    ageList = ['儿童','青年','中年','老年']
    self.rb_age = wx.RadioBox(panel,label='年龄',pos=(80,10),
    choices=ageList,majorDimension=1,style=wx.RA_SPECIFY_ROWS)
    self.btn_add = wx.Button(parent=panel,label='确 定',pos=(110,100))
    self.Bind(wx.EVT_BUTTON,self.On_btn_ok,self.btn_add)
    self.Center()
    self.Show(True)
  #按钮事件.
  def On_btn_ok(self,event):
    str = "您的年龄段: " + self.rb_age.GetStringSelection() + "\n您的爱好："
    if self.cb_music.GetValue(): str = str + self.cb_music.GetLabel()
    if self.cb_movie.GetValue(): str = str + self.cb_movie.GetLabel()
    if self.cb_artist.GetValue(): str = str + self.cb_artist.GetLabel()
    wx.MessageBox(str)     	#在消息框中显示.
if __name__ == '__main__':
  app = wx.App()
  MyFrame(None,'复选框和单选按钮使用')
  app.MainLoop()
