import wx

app = wx.App()

wx.MessageBox('Pythonspot wxWidgets demo', 'Info', wx.OK | wx.ICON_INFORMATION)

# simple dialog
wx.MessageBox('A dialog', 'Title', wx.OK)

# warning dialog
wx.MessageBox('Operation could not be completed', 'Warning', wx.OK | wx.ICON_WARNING)

# error dialog
wx.MessageBox('Operation could not be completed', 'Error', wx.OK | wx.ICON_ERROR)

wx.MessageBox('Operation could not be completed', 'Error', wx.YES_NO | wx.ICON_ERROR)

dlg = wx.MessageDialog(None, "Do you want to update?", 'Updater', wx.YES_NO | wx.ICON_QUESTION)
result = dlg.ShowModal()

if result == wx.ID_YES:
    print("Yes pressed")
else:
    print("No pressed")
