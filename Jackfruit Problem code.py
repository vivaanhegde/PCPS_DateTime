import wx
from datetime import datetime

app = wx.App()

frame = wx.Frame(None, title="Date & Time", size=(300, 200))
frame.SetBackgroundColour("Black")
panel = wx.Panel(frame)

# ----- Headings -----

date_heading = wx.StaticText(panel, label="DATE:", pos=(30, 40))
date_heading.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
date_heading.SetForegroundColour(wx.Colour(0, 130, 139))


time_heading = wx.StaticText(panel, label="TIME:", pos=(30, 90))
time_heading.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
time_heading.SetForegroundColour( wx.Colour(0, 130, 139))


light_blue = wx.Colour(173, 216, 230)   # Light Blue

# ----- Date & Time Values -----
date_text = wx.StaticText(panel, label="", pos=(100, 40))
date_text.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
date_text.SetForegroundColour(light_blue)


time_text = wx.StaticText(panel, label="", pos=(100, 90))
time_text.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
time_text.SetForegroundColour(light_blue)

# ----- Update Function -----
def update_time(event):
    now = datetime.now()
    date_text.SetLabel(now.strftime("%d/%m/%Y"))
    time_text.SetLabel(now.strftime("%H:%M:%S"))


# ----- Timer -----
timer = wx.Timer(frame)
frame.Bind(wx.EVT_TIMER, update_time, timer)
timer.Start(1000)

update_time(None)

frame.Show()
app.MainLoop()