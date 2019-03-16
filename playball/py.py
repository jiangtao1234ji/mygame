import wx

class SubclassDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '游戏时间到！', pos = (512,340))
        okButton = wx.Button(self, wx.ID_OK, "重新开始",size = (50,50))
        okButton.SetDefault()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dialog = SubclassDialog()
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print ("OK")
    dialog.Destroy()
