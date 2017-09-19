import wx,os

class MainWindows(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        filemenu = wx.Menu()

        menuOpen =filemenu.Append(wx.ID_OPEN, "&Open", "Open")
        menuSave =filemenu.Append(wx.ID_SAVE, "&Save", "Save")
        filemenu.AppendSeparator()
        menuAbout =filemenu.Append(wx.ID_ABOUT, "&About", "About")
        filemenu.AppendSeparator()
        menuExit =filemenu.Append(wx.ID_EXIT, "E&xit", "Close")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit , menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen , menuOpen)

        self.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        openFileDialog = wx.FileDialog(self, "Open Files", "", "",
                                       "Python files (*.py)|*.py",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if  openFileDialog.ShowModal()== wx.ID_OK:
            self.filename = openFileDialog.GetFilename()
            self.dirname = openFileDialog.GetDirectory()
            print(self.filename)
            print(self.dirname)
            self.path   = openFileDialog.GetPath()
            print(self.path)
            f = open(os.path.join(self.dirname, self.filename), 'r')
            f.close()
        openFileDialog.Destroy()

app = wx.App()
frame = MainWindows(None,'Sample')
app.MainLoop()
