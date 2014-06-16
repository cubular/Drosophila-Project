#-----------------------------------------------------------------------------
# Name:        Frame1.py
# Purpose:     
#
# Author:      <your name>
#
# Created:     2006/10/09
# RCS-ID:      $Id: Frame1.py $
# Copyright:   (c) 2004
# Licence:     <your licence>
# New field:   Whatever
#-----------------------------------------------------------------------------
#Boa:Frame:Frame1

import wx
from os import getcwd
import Image, ImageWin, ImageDraw


def create(parent, flags, slide):
    return Frame1(parent, flags, slide)

[wxID_FRAME1, wxID_FRAME1ACCUM_LABEL, wxID_FRAME1ADD, wxID_FRAME1ANESTH, 
 wxID_FRAME1AUTO, wxID_FRAME1AUTO_LABEL, wxID_FRAME1CAMERA_PANEL, 
 wxID_FRAME1CAMVIEW, wxID_FRAME1CAM_VIEW_LABEL, wxID_FRAME1CURR_FLY_LABEL, 
 wxID_FRAME1DEPOSIT, wxID_FRAME1DOWN_COARSE, wxID_FRAME1DURATION_LABEL, 
 wxID_FRAME1ENGINE1, wxID_FRAME1ENGINE2, wxID_FRAME1ENGINE3, 
 wxID_FRAME1ENGINE4, wxID_FRAME1ENGINE_VIEW_LABEL, wxID_FRAME1FINDFLIES, 
 wxID_FRAME1FOCUS_IN_COARSE, wxID_FRAME1FOCUS_IN_FINE, 
 wxID_FRAME1FOCUS_OUT_COARSE, wxID_FRAME1FOCUS_OUT_FINE, wxID_FRAME1GAS, 
 wxID_FRAME1GRAPH1, wxID_FRAME1HEART_RATE, wxID_FRAME1LEFT_COARSE, 
 wxID_FRAME1LOADSLIDE, wxID_FRAME1MANUAL_LABEL, wxID_FRAME1MEASURE_FLY, 
 wxID_FRAME1MMODEVIEW, wxID_FRAME1MMODE_DIR_LABEL, 
 wxID_FRAME1MMODE_DIR_LABEL2, wxID_FRAME1MMODE_PANEL, 
 wxID_FRAME1MMODE_VIEW_LABEL, wxID_FRAME1MOVE_DOWN, wxID_FRAME1MOVE_LEFT, 
 wxID_FRAME1MOVE_RIGHT, wxID_FRAME1MOVE_UP, wxID_FRAME1MOVIE, wxID_FRAME1NEW, 
 wxID_FRAME1O2_LABEL, wxID_FRAME1OUTLINE_LABEL, wxID_FRAME1PANEL1, 
 wxID_FRAME1PANEL2, wxID_FRAME1PERCENT_O2, wxID_FRAME1PINPOINT_LABEL, 
 wxID_FRAME1RESET, wxID_FRAME1RIGHT_COARSE, wxID_FRAME1SKIP, 
 wxID_FRAME1SLIDEVIEW, wxID_FRAME1SLIDE_LABEL, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICLINE2, wxID_FRAME1STATICLINE3, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STOP, wxID_FRAME1TEMPLATE_LABEL, 
 wxID_FRAME1TIME_LABEL, wxID_FRAME1TRACE_LABEL, wxID_FRAME1UP_COARSE, 
 wxID_FRAME1WARNING_O2, wxID_FRAME1ZERO_LABEL, 
] = [wx.NewId() for _init_ctrls in range(64)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(154, 112), size=wx.Size(1116, 856),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(1108, 822))

        self.camera_panel = wx.Panel(id=wxID_FRAME1CAMERA_PANEL,
              name='camera_panel', parent=self, pos=wx.Point(424, 0),
              size=wx.Size(696, 608), style=0)
        self.camera_panel.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.camview = wx.Window(id=wxID_FRAME1CAMVIEW, name='camview',
              parent=self.camera_panel, pos=wx.Point(32, 56), size=wx.Size(640,
              480), style=0)
        self.camview.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.camview.Bind(wx.EVT_LEFT_DOWN, self.OnCamviewLeftDown)

        self.mmode_panel = wx.Panel(id=wxID_FRAME1MMODE_PANEL,
              name='mmode_panel', parent=self, pos=wx.Point(424, 608),
              size=wx.Size(688, 216), style=0)

        self.mmodeview = wx.Window(id=wxID_FRAME1MMODEVIEW, name='mmodeview',
              parent=self.mmode_panel, pos=wx.Point(80, 24), size=wx.Size(256,
              160), style=0)
        self.mmodeview.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.mmode_dir_label = wx.StaticText(id=wxID_FRAME1MMODE_DIR_LABEL,
              label='up/left', name='mmode_dir_label', parent=self.mmode_panel,
              pos=wx.Point(32, 8), size=wx.Size(40, 13), style=0)

        self.mmode_dir_label2 = wx.StaticText(id=wxID_FRAME1MMODE_DIR_LABEL2,
              label='down/right', name='mmode_dir_label2',
              parent=self.mmode_panel, pos=wx.Point(16, 184), size=wx.Size(51,
              13), style=0)

        self.time_label = wx.StaticText(id=wxID_FRAME1TIME_LABEL, label='time',
              name='time_label', parent=self.mmode_panel, pos=wx.Point(200,
              184), size=wx.Size(19, 13), style=0)

        self.zero_label = wx.StaticText(id=wxID_FRAME1ZERO_LABEL, label='0',
              name='zero_label', parent=self.mmode_panel, pos=wx.Point(80, 184),
              size=wx.Size(6, 13), style=0)

        self.duration_label = wx.StaticText(id=wxID_FRAME1DURATION_LABEL,
              label='2 s', name='duration_label', parent=self.mmode_panel,
              pos=wx.Point(336, 184), size=wx.Size(14, 13), style=0)

        self.mmode_view_label = wx.StaticText(id=wxID_FRAME1MMODE_VIEW_LABEL,
              label='M-mode', name='mmode_view_label', parent=self.mmode_panel,
              pos=wx.Point(184, 0), size=wx.Size(50, 16), style=0)
        self.mmode_view_label.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Microsoft Sans Serif'))

        self.percent_O2 = wx.StaticText(id=wxID_FRAME1PERCENT_O2, label='0.0',
              name='percent_O2', parent=self.mmode_panel, pos=wx.Point(556, 56),
              size=wx.Size(32, 29), style=0)
        self.percent_O2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))
        self.percent_O2.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.warning_O2 = wx.StaticText(id=wxID_FRAME1WARNING_O2,
              label='No target pO2 set', name='warning_O2',
              parent=self.mmode_panel, pos=wx.Point(500, 100), size=wx.Size(126,
              20), style=0)
        self.warning_O2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))
        self.warning_O2.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.O2_label = wx.StaticText(id=wxID_FRAME1O2_LABEL, label='% Oxygen',
              name='O2_label', parent=self.mmode_panel, pos=wx.Point(548, 24),
              size=wx.Size(61, 16), style=0)
        self.O2_label.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Microsoft Sans Serif'))

        self.cam_view_label = wx.StaticText(id=wxID_FRAME1CAM_VIEW_LABEL,
              label='Microscope view', name='cam_view_label',
              parent=self.camera_panel, pos=wx.Point(288, 24), size=wx.Size(115,
              20), style=0)
        self.cam_view_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 264), size=wx.Size(424, 576), style=0)

        self.engine1 = wx.Window(id=wxID_FRAME1ENGINE1, name='engine1',
              parent=self.panel1, pos=wx.Point(24, 128), size=wx.Size(160, 120),
              style=0)
        self.engine1.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.engine2 = wx.Window(id=wxID_FRAME1ENGINE2, name='engine2',
              parent=self.panel1, pos=wx.Point(88, 280), size=wx.Size(80, 120),
              style=0)
        self.engine2.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('./gui/template.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(256, 280),
              size=wx.Size(80, 120), style=0)

        self.curr_fly_label = wx.StaticText(id=wxID_FRAME1CURR_FLY_LABEL,
              label='Current Fly', name='curr_fly_label', parent=self.panel1,
              pos=wx.Point(104, 264), size=wx.Size(50, 13), style=0)
        self.curr_fly_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.template_label = wx.StaticText(id=wxID_FRAME1TEMPLATE_LABEL,
              label='Template', name='template_label', parent=self.panel1,
              pos=wx.Point(272, 264), size=wx.Size(44, 13), style=0)
        self.template_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.trace_label = wx.StaticText(id=wxID_FRAME1TRACE_LABEL,
              label='Trace', name='trace_label', parent=self.panel1,
              pos=wx.Point(88, 112), size=wx.Size(28, 13), style=0)
        self.trace_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.engine_view_label = wx.StaticText(id=wxID_FRAME1ENGINE_VIEW_LABEL,
              label='Engine', name='engine_view_label', parent=self.panel1,
              pos=wx.Point(176, 8), size=wx.Size(50, 20), style=0)
        self.engine_view_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Microsoft Sans Serif'))

        self.engine3 = wx.Window(id=wxID_FRAME1ENGINE3, name='engine3',
              parent=self.panel1, pos=wx.Point(24, 424), size=wx.Size(160, 120),
              style=0)
        self.engine3.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.engine4 = wx.Window(id=wxID_FRAME1ENGINE4, name='engine4',
              parent=self.panel1, pos=wx.Point(208, 424), size=wx.Size(160,
              120), style=0)
        self.engine4.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.pinpoint_label = wx.StaticText(id=wxID_FRAME1PINPOINT_LABEL,
              label='Pinpoint Motion', name='pinpoint_label',
              parent=self.panel1, pos=wx.Point(264, 408), size=wx.Size(73, 13),
              style=0)
        self.pinpoint_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.accum_label = wx.StaticText(id=wxID_FRAME1ACCUM_LABEL,
              label='Accumulated Motion', name='accum_label',
              parent=self.panel1, pos=wx.Point(56, 408), size=wx.Size(97, 13),
              style=0)
        self.accum_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(424, 264), style=0)

        self.auto_label = wx.StaticText(id=wxID_FRAME1AUTO_LABEL,
              label='Auto Detection', name='auto_label', parent=self.panel2,
              pos=wx.Point(144, 0), size=wx.Size(107, 20), style=0)
        self.auto_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))

        self.auto = wx.Button(id=wxID_FRAME1AUTO, label='Start', name='auto',
              parent=self.panel2, pos=wx.Point(120, 24), size=wx.Size(75, 23),
              style=0)

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME1STATICLINE2,
              name='staticLine2', parent=self.panel2, pos=wx.Point(0, 256),
              size=wx.Size(384, 2), style=0)

        self.LoadSlide = wx.Button(id=wxID_FRAME1LOADSLIDE, label='Load Slide',
              name='LoadSlide', parent=self.panel2, pos=wx.Point(8, 192),
              size=wx.Size(75, 23), style=0)
        self.LoadSlide.Bind(wx.EVT_BUTTON, self.OnLoadSlideButton,
              id=wxID_FRAME1LOADSLIDE)

        self.anesth = wx.Button(id=wxID_FRAME1ANESTH, label='Anesthetize',
              name='anesth', parent=self.panel2, pos=wx.Point(8, 64),
              size=wx.Size(75, 23), style=0)
        self.anesth.Bind(wx.EVT_BUTTON, self.OnAnesthButton,
              id=wxID_FRAME1ANESTH)

        self.findFlies = wx.Button(id=wxID_FRAME1FINDFLIES, label='Measure',
              name='findFlies', parent=self.panel2, pos=wx.Point(8, 112),
              size=wx.Size(75, 23), style=0)
        self.findFlies.Bind(wx.EVT_BUTTON, self.OnFindFliesButton,
              id=wxID_FRAME1FINDFLIES)

        self.move_left = wx.BitmapButton(bitmap=wx.Bitmap('./gui/left.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1MOVE_LEFT, name='move_left',
              parent=self.panel2, pos=wx.Point(144, 144), size=wx.Size(24, 56),
              style=wx.BU_AUTODRAW)
        self.move_left.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.move_left.Bind(wx.EVT_BUTTON, self.OnMove_leftButton,
              id=wxID_FRAME1MOVE_LEFT)

        self.focus_out_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/outbig.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1FOCUS_OUT_COARSE,
              name='focus_out_coarse', parent=self.panel2, pos=wx.Point(168,
              160), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.focus_out_coarse.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.focus_out_coarse.Bind(wx.EVT_BUTTON, self.OnFocus_out_coarseButton,
              id=wxID_FRAME1FOCUS_OUT_COARSE)

        self.focus_in_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/inbig.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1FOCUS_IN_COARSE,
              name='focus_in_coarse', parent=self.panel2, pos=wx.Point(184,
              176), size=wx.Size(24, 24), style=wx.BU_AUTODRAW)
        self.focus_in_coarse.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.focus_in_coarse.Bind(wx.EVT_BUTTON, self.OnFocus_in_coarseButton,
              id=wxID_FRAME1FOCUS_IN_COARSE)

        self.focus_out_fine = wx.BitmapButton(bitmap=wx.Bitmap('./gui/outsmall.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1FOCUS_OUT_FINE,
              name='focus_out_fine', parent=self.panel2, pos=wx.Point(200, 144),
              size=wx.Size(16, 16), style=wx.BU_AUTODRAW)
        self.focus_out_fine.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.focus_out_fine.Bind(wx.EVT_BUTTON, self.OnFocus_out_fineButton,
              id=wxID_FRAME1FOCUS_OUT_FINE)

        self.focus_in_fine = wx.BitmapButton(bitmap=wx.Bitmap('./gui/insmall.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1FOCUS_IN_FINE,
              name='focus_in_fine', parent=self.panel2, pos=wx.Point(216, 160),
              size=wx.Size(16, 16), style=wx.BU_AUTODRAW)
        self.focus_in_fine.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.focus_in_fine.Bind(wx.EVT_BUTTON, self.OnFocus_in_fineButton,
              id=wxID_FRAME1FOCUS_IN_FINE)

        self.move_up = wx.BitmapButton(bitmap=wx.Bitmap('./gui/up.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1MOVE_UP, name='move_up',
              parent=self.panel2, pos=wx.Point(168, 120), size=wx.Size(64, 24),
              style=wx.BU_AUTODRAW)
        self.move_up.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.move_up.Bind(wx.EVT_BUTTON, self.OnMove_upButton,
              id=wxID_FRAME1MOVE_UP)

        self.move_right = wx.BitmapButton(bitmap=wx.Bitmap('./gui/right.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1MOVE_RIGHT, name='move_right',
              parent=self.panel2, pos=wx.Point(232, 144), size=wx.Size(24, 56),
              style=wx.BU_AUTODRAW)
        self.move_right.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.move_right.Bind(wx.EVT_BUTTON, self.OnMove_rightButton,
              id=wxID_FRAME1MOVE_RIGHT)

        self.move_down = wx.BitmapButton(bitmap=wx.Bitmap('./gui/down.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1MOVE_DOWN, name='move_down',
              parent=self.panel2, pos=wx.Point(168, 200), size=wx.Size(64, 24),
              style=wx.BU_AUTODRAW)
        self.move_down.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.move_down.Bind(wx.EVT_BUTTON, self.OnMove_downButton,
              id=wxID_FRAME1MOVE_DOWN)

        self.manual_label = wx.StaticText(id=wxID_FRAME1MANUAL_LABEL,
              label='Manual Controls', name='manual_label', parent=self.panel2,
              pos=wx.Point(144, 64), size=wx.Size(115, 20), style=0)
        self.manual_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))

        self.slideview = wx.Window(id=wxID_FRAME1SLIDEVIEW, name='slideview',
              parent=self.panel1, pos=wx.Point(56, 40), size=wx.Size(272, 50),
              style=0)
        self.slideview.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.slide_label = wx.StaticText(id=wxID_FRAME1SLIDE_LABEL,
              label='Slide', name='slide_label', parent=self.panel1,
              pos=wx.Point(24, 56), size=wx.Size(23, 13), style=0)
        self.slide_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.graph1 = wx.Window(id=wxID_FRAME1GRAPH1, name='graph1',
              parent=self.panel1, pos=wx.Point(208, 128), size=wx.Size(160,
              120), style=0)
        self.graph1.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.outline_label = wx.StaticText(id=wxID_FRAME1OUTLINE_LABEL,
              label='Outline and axis', name='outline_label',
              parent=self.panel1, pos=wx.Point(256, 112), size=wx.Size(75, 13),
              style=0)
        self.outline_label.SetBackgroundColour(wx.Colour(236, 233, 216))

        self.staticLine3 = wx.StaticLine(id=wxID_FRAME1STATICLINE3,
              name='staticLine3', parent=self.panel2, pos=wx.Point(0, 56),
              size=wx.Size(384, 2), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.camera_panel, pos=wx.Point(40,
              586), size=wx.Size(680, 2), style=0)

        self.deposit = wx.Button(id=wxID_FRAME1DEPOSIT, label='Deposit',
              name='deposit', parent=self.panel2, pos=wx.Point(8, 88),
              size=wx.Size(75, 23), style=0)
        self.deposit.Bind(wx.EVT_BUTTON, self.OnDepositButton,
              id=wxID_FRAME1DEPOSIT)

        self.left_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/left.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1LEFT_COARSE,
              name='left_coarse', parent=self.panel2, pos=wx.Point(120, 144),
              size=wx.Size(24, 56), style=wx.BU_AUTODRAW)
        self.left_coarse.Bind(wx.EVT_BUTTON, self.OnLeft_coarseButton,
              id=wxID_FRAME1LEFT_COARSE)

        self.down_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/down.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1DOWN_COARSE,
              name='down_coarse', parent=self.panel2, pos=wx.Point(168, 224),
              size=wx.Size(64, 24), style=wx.BU_AUTODRAW)
        self.down_coarse.Bind(wx.EVT_BUTTON, self.OnDown_coarseButton,
              id=wxID_FRAME1DOWN_COARSE)

        self.right_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/right.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1RIGHT_COARSE,
              name='right_coarse', parent=self.panel2, pos=wx.Point(256, 144),
              size=wx.Size(24, 56), style=wx.BU_AUTODRAW)
        self.right_coarse.Bind(wx.EVT_BUTTON, self.OnRight_coarseButton,
              id=wxID_FRAME1RIGHT_COARSE)

        self.up_coarse = wx.BitmapButton(bitmap=wx.Bitmap('./gui/up.bmp',
              wx.BITMAP_TYPE_BMP), id=wxID_FRAME1UP_COARSE, name='up_coarse',
              parent=self.panel2, pos=wx.Point(168, 96), size=wx.Size(64, 24),
              style=wx.BU_AUTODRAW)
        self.up_coarse.Bind(wx.EVT_BUTTON, self.OnUp_coarseButton,
              id=wxID_FRAME1UP_COARSE)

        self.skip = wx.Button(id=wxID_FRAME1SKIP, label='Skip Fly', name='skip',
              parent=self.panel2, pos=wx.Point(312, 192), size=wx.Size(75, 23),
              style=0)
        self.skip.Bind(wx.EVT_BUTTON, self.OnSkipButton, id=wxID_FRAME1SKIP)

        self.stop = wx.Button(id=wxID_FRAME1STOP, label='Stop', name='stop',
              parent=self.panel2, pos=wx.Point(208, 24), size=wx.Size(75, 23),
              style=0)
        self.stop.Bind(wx.EVT_BUTTON, self.OnStopButton, id=wxID_FRAME1STOP)

        self.reset = wx.Button(id=wxID_FRAME1RESET, label='Reset Focus',
              name='reset', parent=self.panel2, pos=wx.Point(8, 168),
              size=wx.Size(75, 23), style=0)
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton, id=wxID_FRAME1RESET)

        self.new = wx.Button(id=wxID_FRAME1NEW, label='New Slide', name='new',
              parent=self.panel2, pos=wx.Point(312, 64), size=wx.Size(75, 23),
              style=0)
        self.new.Bind(wx.EVT_BUTTON, self.OnNewButton, id=wxID_FRAME1NEW)

        self.add = wx.Button(id=wxID_FRAME1ADD, label='Add Fly', name='add',
              parent=self.panel2, pos=wx.Point(312, 88), size=wx.Size(75, 23),
              style=0)
        self.add.Bind(wx.EVT_BUTTON, self.OnAddButton, id=wxID_FRAME1ADD)

        self.movie = wx.Button(id=wxID_FRAME1MOVIE, label='Capture Movie',
              name='movie', parent=self.panel2, pos=wx.Point(304, 136),
              size=wx.Size(88, 23), style=0)
        self.movie.Bind(wx.EVT_BUTTON, self.OnMovieButton, id=wxID_FRAME1MOVIE)

        self.gas = wx.Button(id=wxID_FRAME1GAS, label='Gas', name='gas',
              parent=self.panel2, pos=wx.Point(8, 216), size=wx.Size(75, 23),
              style=0)
        self.gas.Bind(wx.EVT_BUTTON, self.OnGasButton, id=wxID_FRAME1GAS)

        self.heart_rate = wx.StaticText(id=wxID_FRAME1HEART_RATE, label='0.0',
              name='heart_rate', parent=self.mmode_panel, pos=wx.Point(452, 56),
              size=wx.Size(32, 29), style=0)
        self.heart_rate.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))
        self.heart_rate.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Heart Rate', name='staticText2', parent=self.mmode_panel,
              pos=wx.Point(436, 24), size=wx.Size(65, 16), style=0)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))

        self.measure_fly = wx.Button(id=wxID_FRAME1MEASURE_FLY,
              label='Measure Fly', name='measure_fly', parent=self.panel2,
              pos=wx.Point(312, 112), size=wx.Size(75, 23), style=0)
        self.measure_fly.Bind(wx.EVT_BUTTON, self.OnMeasure_flyButton,
              id=wxID_FRAME1MEASURE_FLY)

    def __init__(self, parent, flags, slide):
        self._init_ctrls(parent)
        self.flags  = flags
        self.slide  = slide

        self.CamViewDib = ImageWin.Dib("L", (640,480))
        self.camviewDC = wx.ClientDC(self.camview)
        self.MModeViewDib = ImageWin.Dib("L", (256,160))
        self.mmodeviewDC = wx.ClientDC(self.mmodeview)
        self.slideviewDib = ImageWin.Dib("L", (272,50))
        self.slideviewDC = wx.ClientDC(self.slideview)
        
        self.engine1ViewDib = ImageWin.Dib("L", (160,120))
        self.engine1DC = wx.ClientDC(self.engine1)
        self.engine2ViewDib = ImageWin.Dib("L", (80,120))
        self.engine2DC = wx.ClientDC(self.engine2)
        self.engine3ViewDib = ImageWin.Dib("L", (160,120))
        self.engine3DC = wx.ClientDC(self.engine3)
        self.engine4ViewDib = ImageWin.Dib("L", (160,120))
        self.engine4DC = wx.ClientDC(self.engine4)
        
        self.graph1ViewDib = ImageWin.Dib("L", (160,120))
        self.graph1DC = wx.ClientDC(self.graph1)
        
    def OnClick(self,event):
        print vars(event)

    def displayCam(self,frame,draw_mask):
        f = frame.copy()
        frameDraw = ImageDraw.Draw(f)
        for mask in draw_mask:
            frameDraw.point(mask,fill=128)  #draws MMode line on frame
        if self.CamViewDib:
            self.CamViewDib.paste(f)
            self.CamViewDib.expose(self.camviewDC.GetHDC())
        del frameDraw

    def displayMMode(self, MMode_Img):
        self.MModeViewDib.paste(MMode_Img)
        self.MModeViewDib.expose(self.mmodeviewDC.GetHDC())

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

    def displayGraph1(self, im):
        self.graph1ViewDib.paste(im.resize((160,120)))
        self.graph1ViewDib.expose(self.graph1DC.GetHDC())
        
    def displayHR(self, rate):
        rate_str = '%4.2f'%rate       
        self.heart_rate.SetLabel(rate_str)
        
    def displayO2(self, O2):
        O2_str = '%2.2f'%O2       
        self.percent_O2.SetLabel(O2_str)

    def warnO2(self,percentage,alert=False):
        message = 'Target O2 = '+ str(percentage)
        if alert: self.warning_O2.SetBackgroundColour(wx.Colour(255, 0, 0))
        else: self.warning_O2.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.warning_O2.SetLabel(message)        
        
    def OnAutoButton(self, event):
        self.flags.set('AUTO')
                
    def OnLoadSlideButton(self, event):
        if self.flags.get('LOAD'):
            self.slide.moveToStart()
            self.flags.reset('LOAD')
        else:
            self.slide.loadSlide()
            self.flags.set('LOAD')
                
    def OnFindFliesButton(self, event):
        self.flags.toggle('FIND FLIES')

    def OnNext_flyButton(self, event):
        self.flags.set('NEXT')

    def OnMmodeButton(self, event):
        self.flags.toggle('MMODE')

    def onCamViewClick(self, event):
        if self.flags.get('FREEZE'): return
        " Moves stage to center on the pixel that was clicked"
        displace_x,displace_y = event.GetPosition()
        displace_x = (displace_x - 320)*self.slide.scales['XPIX2MICR']
        displace_y = (displace_y - 240)*self.slide.scales['YPIX2MICR']
        self.slide.refresh()
        self.slide.displace([displace_x,displace_y,0])

    def OnMove_leftButton(self, event):
        if self.flags.get('FREEZE'): return
        self.slide.refresh()
        self.slide.displace([-640*self.slide.scales['XPIX2MICR'],0,0])
        
    def OnMove_rightButton(self, event):
        if self.flags.get('FREEZE'): return
        self.slide.refresh()
        self.slide.displace([640*self.slide.scales['XPIX2MICR'],0,0])

    def OnMove_upButton(self, event):
        if self.flags.get('FREEZE'): return
        self.slide.refresh()
        self.slide.displace([0,-480*self.slide.scales['YPIX2MICR'],0])

    def OnMove_downButton(self, event):
        if self.flags.get('FREEZE'): return
        self.slide.refresh()
        self.slide.displace([0,480*self.slide.scales['YPIX2MICR'],0])

    def OnFocus_in_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displace([0,0,self.slide.scales['FOCUS_STEP_COARSE']])

    def OnFocus_out_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displace([0,0,-1*self.slide.scales['FOCUS_STEP_COARSE']])

    def OnFocus_in_fineButton(self, event):
        self.slide.refresh()
        self.slide.displace([0,0,self.slide.scales['FOCUS_STEP_FINE']])

    def OnFocus_out_fineButton(self, event):
        self.slide.refresh()
        self.slide.displace([0,0,-1*self.slide.scales['FOCUS_STEP_FINE']])

    def OnWxframe1Close(self, event):
        self.flags.reset('FIND FLIES')
        self.flags.set('CLOSE')
        self.slide.moveToStart()
        self.Destroy()            

    def OnAnesthButton(self, event):
        self.flags.set('ANESTH')

    def OnDepositButton(self, event):
        self.flags.set('DEPOSIT')

    def OnLeft_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displaceX(-2000)

    def OnDown_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displaceY(2000)

    def OnRight_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displaceX(2000)

    def OnUp_coarseButton(self, event):
        self.slide.refresh()
        self.slide.displaceY(-2000)

    def OnSkipButton(self, event):
        self.flags.set('SKIP')

    def OnStopButton(self, event):
        self.flags.set('STOP')

    def OnResetButton(self, event):
        self.slide.resetFocus()

    def OnDetect_fliesButton(self, event):
        self.flags.set('DETECT')

    def OnSaveButton(self, event):
        self.flags.set('SAVE')

    def OnMovieButton(self, event):
        self.flags.set('MOVIE')

    def OnNewButton(self, event):
        self.flags.set('NEW')

    def OnAddButton(self, event):
        self.flags.set('ADD')

    def OnGasButton(self, event):
        if self.flags.get('FREEZE'): return
        self.flags.toggle('GAS')

    def OnMeasure_flyButton(self, event):
        self.flags.set('MEASURE FLY')

    def OnCamviewLeftDown(self, event):
        if self.flags.get('FREEZE'): return
        " Moves stage to center on the pixel that was clicked"
        displace_x,displace_y = event.GetPosition()
        displace_x = (displace_x - 320)*self.slide.scales['XPIX2MICR']
        displace_y = (displace_y - 240)*self.slide.scales['YPIX2MICR']
        self.slide.refresh()
        self.slide.displace([displace_x,displace_y,0])
