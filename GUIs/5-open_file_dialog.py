import wx
import serial



def onButton(event):
    print("Button pressed.")


app = wx.App()

frame = wx.Frame(None, -1, 'win.py',pos=(0,0),size=(200,50))

# Create open file dialog
openFileDialog = wx.FileDialog(frame, "Open Files", "", "",
                               "Python files (*.py)|*.py",
                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)


openFileDialog.ShowModal()
print(openFileDialog.GetPath())
openFileDialog.Destroy()


