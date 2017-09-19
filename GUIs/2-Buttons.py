import wx
def onButton(event):
    print("Button Pressed.")

app = wx.App()
frame = wx.Frame(None, -1,title="Hello World", size=(450,200), pos=(50,50))
#frame = wx.Frame(None, -1,title="Hello World")
#frame.SetSize(0,0,500,150)

panel = wx.Panel(frame,-1)
#panel = wx.Panel(frame, wx.ID_ANY)

rp = wx.RealPoint(170, 50)
p = wx.Point(int(round(rp.x)), int(round(rp.y)))

button = wx.Button(panel,-1,'Test',pos=p)
button.Bind(wx.EVT_BUTTON,onButton)

frame.Show()
#frame.Centre()
app.MainLoop()
            
