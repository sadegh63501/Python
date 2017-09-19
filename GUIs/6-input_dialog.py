import wx


def onButton(event):
    print("Button pressed.")


app = wx.App()

frame = wx.Frame()

# Create text input
dlg = wx.TextEntryDialog(frame, 'Enter some text', 'Text Entry')
# dlg.SetValue("Default")
if dlg.ShowModal() == wx.ID_OK:
    print('You entered: %s\n' % dlg.GetValue())
dlg.Destroy()
