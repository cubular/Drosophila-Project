#Boa:Frame:fly_gui

import wx
from wxPython.wx import wxClientDC
from os import getcwd
import Image, ImageWin, ImageDraw

def create(parent, flags, slide):
    return fly_gui(parent, flags, slide)

[wxID_FLY_GUI, wxID_FLY_GUIANESTH, wxID_FLY_GUICAMERA_PANEL, 
 wxID_FLY_GUICAMVIEW, wxID_FLY_GUIENGINE1, wxID_FLY_GUIENGINE2, 
 wxID_FLY_GUIENGINE3, wxID_FLY_GUIENGINE4, wxID_FLY_GUIFINDFLIES, 
 wxID_FLY_GUIMMODEVIEW, wxID_FLY_GUIMMODE_PANEL, wxID_FLY_GUIPANEL1, 
 wxID_FLY_GUIPANEL2, wxID_FLY_GUIPERCENT_O2, wxID_FLY_GUIRESET, 
 wxID_FLY_GUISLIDEVIEW, 
] = [wx.NewId() for _init_ctrls in range(16)]

class fly_gui(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FLY_GUI, name='fly_gui', parent=prnt,
              pos=wx.Point(127, 65), size=wx.Size(1116, 856),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Fly Automation Control Panel')
        self.SetClientSize(wx.Size(1108, 822))

        self.camera_panel = wx.Panel(id=wxID_FLY_GUICAMERA_PANEL,
              name='camera_panel', parent=self, pos=wx.Point(424, 0),
              size=wx.Size(696, 608), style=wx.TAB_TRAVERSAL)

        self.camview = wx.Window(id=wxID_FLY_GUICAMVIEW, name='camview',
              parent=self.camera_panel, pos=wx.Point(32, 56), size=wx.Size(640,
              480), style=0)
        self.camview.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.camview.SetToolTipString('Microscope view')
        self.camview.SetWindowVariant(wx.WINDOW_VARIANT_MINI)
        self.camview.Bind(wx.EVT_LEFT_DOWN, self.OnCamviewLeftDown)

        self.mmode_panel = wx.Panel(id=wxID_FLY_GUIMMODE_PANEL,
              name='mmode_panel', parent=self, pos=wx.Point(424, 608),
              size=wx.Size(688, 216), style=wx.TAB_TRAVERSAL)

        self.panel1 = wx.Panel(id=wxID_FLY_GUIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 264), size=wx.Size(424, 576),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FLY_GUIPANEL2, name='panel2',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(424, 264),
              style=wx.TAB_TRAVERSAL)

        self.mmodeview = wx.Window(id=wxID_FLY_GUIMMODEVIEW, name='mmodeview',
              parent=self.mmode_panel, pos=wx.Point(80, 24), size=wx.Size(265,
              160), style=0)

        self.slideview = wx.Window(id=wxID_FLY_GUISLIDEVIEW, name='slideview',
              parent=self.panel1, pos=wx.Point(56, 40), size=wx.Size(272, 50),
              style=0)

        self.percent_O2 = wx.StaticText(id=wxID_FLY_GUIPERCENT_O2, label='0.0',
              name='percent_O2', parent=self.mmode_panel, pos=wx.Point(556, 56),
              size=wx.Size(32, 29), style=0)

        self.engine1 = wx.Window(id=wxID_FLY_GUIENGINE1, name='engine1',
              parent=self.panel1, pos=wx.Point(24, 128), size=wx.Size(160, 120),
              style=0)

        self.engine2 = wx.Window(id=wxID_FLY_GUIENGINE2, name='engine2',
              parent=self.panel1, pos=wx.Point(88, 280), size=wx.Size(80, 120),
              style=0)

        self.engine3 = wx.Window(id=wxID_FLY_GUIENGINE3, name='engine3',
              parent=self.panel1, pos=wx.Point(24, 424), size=wx.Size(160, 120),
              style=0)

        self.engine4 = wx.Window(id=wxID_FLY_GUIENGINE4, name='engine4',
              parent=self.panel1, pos=wx.Point(208, 424), size=wx.Size(160,
              120), style=0)

        self.findFlies = wx.Button(id=wxID_FLY_GUIFINDFLIES, label='Measure',
              name='findFlies', parent=self.panel2, pos=wx.Point(8, 112),
              size=wx.Size(75, 23), style=0)
        self.findFlies.SetToolTipString('Click to find and measure flies')
        self.findFlies.Bind(wx.EVT_BUTTON, self.OnFindFliesButton,
              id=wxID_FLY_GUIFINDFLIES)

        self.reset = wx.Button(id=wxID_FLY_GUIRESET, label='Reset',
              name='reset', parent=self.panel2, pos=wx.Point(8, 176),
              size=wx.Size(75, 23), style=0)
        self.reset.SetToolTipString('Reset slide position to (0,0,0)')
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton, id=wxID_FLY_GUIRESET)

        self.anesth = wx.Button(id=wxID_FLY_GUIANESTH, label='Anesthetize',
              name='anesth', parent=self.panel2, pos=wx.Point(8, 64),
              size=wx.Size(75, 23), style=0)
        self.anesth.Bind(wx.EVT_BUTTON, self.OnAnesthButton,
              id=wxID_FLY_GUIANESTH)

    def __init__(self, parent, flags, slide):
        self._init_ctrls(parent)
        
        self.flags  = flags
        self.slide  = slide

        self.CamViewDib = ImageWin.Dib("L", (640,480))
        self.camviewDC = wxClientDC(self.camview)
        self.MModeViewDib = ImageWin.Dib("L", (256,160))
        self.mmodeviewDC = wxClientDC(self.mmodeview)
        self.slideviewDib = ImageWin.Dib("L", (272,50))
        self.slideviewDC = wxClientDC(self.slideview)
        
        self.engine1ViewDib = ImageWin.Dib("L", (160,120))
        self.engine1DC = wxClientDC(self.engine1)
        self.engine2ViewDib = ImageWin.Dib("L", (80,120))
        self.engine2DC = wxClientDC(self.engine2)
        self.engine3ViewDib = ImageWin.Dib("L", (160,120))
        self.engine3DC = wxClientDC(self.engine3)
        self.engine4ViewDib = ImageWin.Dib("L", (160,120))
        self.engine4DC = wxClientDC(self.engine4)
        
##        self.graph1ViewDib = ImageWin.Dib("L", (160,120))
##        self.graph1DC = wxClientDC(self.graph1)

    def OnCamviewLeftDown(self, event):
        " Moves stage to center on the pixel that was clicked"
        displace_x,displace_y = event.GetPosition()
        displace_x = (displace_x - 320)*self.slide.scales['XPIX2MICR']
        displace_y = (displace_y - 240)*self.slide.scales['YPIX2MICR']
        self.slide.refresh()
        self.slide.displace([displace_x,displace_y,0])

    def displayCam(self,frame,draw_mask):
        frameDraw = ImageDraw.Draw(frame)             
        frameDraw.point(draw_mask,fill=128)  #draws MMode line on frame
        self.CamViewDib.paste(frame)
        self.CamViewDib.expose(self.camviewDC.GetHDC())

    def displayEngine1(self, im):
        self.engine1ViewDib.paste(im.resize((160,120)))
        self.engine1ViewDib.expose(self.engine1DC.GetHDC())

    def displayEngine2(self, im):
        self.engine2ViewDib.paste(im.resize((80,120)))
        self.engine2ViewDib.expose(self.engine2DC.GetHDC())

    def displayEngine3(self, im):
        self.engine3ViewDib.paste(im.resize((160,120)))
        self.engine3ViewDib.expose(self.engine3DC.GetHDC())

    def displayEngine4(self, im):
        self.engine4ViewDib.paste(im.resize((160,120)))
        self.engine4ViewDib.expose(self.engine4DC.GetHDC())
        
    def displaySlide(self,im):
        self.slideviewDib.paste(im.resize((272,50)))
        self.slideviewDib.expose(self.slideviewDC.GetHDC())
        
    def OnFindFliesButton(self, event):
        self.flags.toggle('FIND FLIES')

    def OnResetButton(self, event):
        self.slide.reset()

    def displayO2(self, O2):
        O2 = O2*100
        O2_str = '%2.2f'%O2       # Displays instantaneous and ave. HRs in top left corner
        self.percent_O2.SetLabel(O2_str)

    def OnAnesthButton(self, event):
        self.flags.set('ANESTH')
