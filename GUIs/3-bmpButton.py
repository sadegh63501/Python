import wx

def onButton(event):
    print("Button Pressed.")

app = wx.App()

frame = wx.Frame(None, -1, 'Image Button',size=(300,400), pos=(180,50))

panel = wx.Panel(frame,wx.ID_ANY)

#bmp = wx.Bitmap("539558.gif")
bmp = wx.Bitmap("539558.gif", wx.BITMAP_TYPE_ANY)

button = wx.BitmapButton(panel, -1, bitmap=bmp, size=(bmp.GetWidth()+15,bmp.GetHeight()+15))

button.Bind(wx.EVT_BUTTON,onButton)
button.SetPosition((50,50))

frame.Show()
#frame.Centre()
app.MainLoop()
