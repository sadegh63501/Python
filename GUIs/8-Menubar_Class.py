import wx

class MainWindows(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        filemenu = wx.Menu()
        filemenu.Append(wx.ID_OPEN, "&Open", "Open")
        filemenu.Append(wx.ID_SAVE, "&Save", "Save")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_ABOUT, "&About", "About")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", "Close")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar

        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show()


app = wx.App()
frame = MainWindows(None,'Sample')
app.MainLoop()
