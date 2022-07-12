from pwd import getpwuid
import wx

class buildgui(wx.Frame):
    def __init__(self, *args, **kw):
        super(buildgui, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileQuit = fileMenu.Append(wx.ID_EXIT, 'Quit\tCtrl+Q')
        menubar.Append(fileMenu, 'File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)
        self.SetTitle("Hacknet Extension Constructor")

    def OnQuit(self, e):
        self.Close()

        
def main():
    app = wx.App()
    ex = buildgui(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()


        