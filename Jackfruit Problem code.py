import wx
from datetime import datetime

class AgeApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Age Calculator", size=(300, 200))
        panel = wx.Panel(self)
        
        # Label
        wx.StaticText(panel, label="Enter Year of Birth:", pos=(50, 30))

        # Input box
        self.year_input = wx.TextCtrl(panel, pos=(50, 55), size=(200, -1))

        # Button
        btn = wx.Button(panel, label="Calculate Age", pos=(80, 90))
        btn.Bind(wx.EVT_BUTTON, self.calculate_age)

        # Result
        self.result = wx.StaticText(panel, label="", pos=(80, 130))

        self.Show()

    def calculate_age(self, event):
        try:
            year = int(self.year_input.GetValue())
            cur_date_year = datetime.now().year
            age = cur_date_year - year
            self.result.SetLabel(f"Your age is {age}")
        except:
            self.result.SetLabel("Enter valid year!")

app = wx.App()
AgeApp()
app.MainLoop()
