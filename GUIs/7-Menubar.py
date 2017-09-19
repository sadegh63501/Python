import wx

app = wx.App()

frame = wx.Frame(None, -1, 'Menubar')

# Setting up the menu.
filemenu = wx.Menu()
filemenu.Append(wx.ID_OPEN, "&Open", "Open")
filemenu.Append(wx.ID_SAVE, "&Save", "Save")
filemenu.AppendSeparator()
filemenu.Append(wx.ID_ABOUT, "&About", "About")
filemenu.AppendSeparator()
filemenu.Append(wx.ID_EXIT, "E&xit", "Close")

# Creating the menubar.
menuBar = wx.MenuBar()
menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
frame.CreateStatusBar()  # A Statusbar in the bottom of the window
frame.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
frame.Show()

app.MainLoop()
