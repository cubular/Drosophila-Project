#Boa:Frame:wxFrame1

from wxPython.wx import *

from os import getcwd
import Image, ImageWin, ImageDraw
import EnginewxFrame

def create(parent, flags, slide):
    return wxFrame1(parent, flags, slide)

[wxID_WXFRAME1, wxID_WXFRAME1ACCUM_LABEL, wxID_WXFRAME1ADD, 
 wxID_WXFRAME1ANESTH, wxID_WXFRAME1AUTO, wxID_WXFRAME1AUTO_LABEL, 
 wxID_WXFRAME1CAMERA_PANEL, wxID_WXFRAME1CAMVIEW, wxID_WXFRAME1CAM_VIEW_LABEL, 
 wxID_WXFRAME1CURR_FLY_LABEL, wxID_WXFRAME1DEPOSIT, wxID_WXFRAME1DETECT_FLIES, 
 wxID_WXFRAME1DOWN_COARSE, wxID_WXFRAME1DURATION_LABEL, wxID_WXFRAME1ENGINE1, 
 wxID_WXFRAME1ENGINE2, wxID_WXFRAME1ENGINE3, wxID_WXFRAME1ENGINE4, 
 wxID_WXFRAME1ENGINE_VIEW_LABEL, wxID_WXFRAME1FINDFLIES, 
 wxID_WXFRAME1FOCUS_IN_COARSE, wxID_WXFRAME1FOCUS_IN_FINE, 
 wxID_WXFRAME1FOCUS_OUT_COARSE, wxID_WXFRAME1FOCUS_OUT_FINE, wxID_WXFRAME1GAS, 
 wxID_WXFRAME1GRAPH1, wxID_WXFRAME1HEART_RATE, wxID_WXFRAME1LEFT_COARSE, 
 wxID_WXFRAME1LOADSLIDE, wxID_WXFRAME1MANUAL_LABEL, wxID_WXFRAME1MEASURE_FLY, 
 wxID_WXFRAME1MMODE, wxID_WXFRAME1MMODEVIEW, wxID_WXFRAME1MMODE_DIR_LABEL, 
 wxID_WXFRAME1MMODE_DIR_LABEL2, wxID_WXFRAME1MMODE_PANEL, 
 wxID_WXFRAME1MMODE_VIEW_LABEL, wxID_WXFRAME1MOVE_DOWN, 
 wxID_WXFRAME1MOVE_LEFT, wxID_WXFRAME1MOVE_RIGHT, wxID_WXFRAME1MOVE_UP, 
 wxID_WXFRAME1MOVIE, wxID_WXFRAME1NEW, wxID_WXFRAME1NEXT_FLY, 
 wxID_WXFRAME1O2_LABEL, wxID_WXFRAME1OUTLINE_LABEL, wxID_WXFRAME1PANEL1, 
 wxID_WXFRAME1PANEL2, wxID_WXFRAME1PERCENT_O2, wxID_WXFRAME1WARNING_O2,
 wxID_WXFRAME1PINPOINT_LABEL, 
 wxID_WXFRAME1RESET, wxID_WXFRAME1RIGHT_COARSE, wxID_WXFRAME1SAVE, 
 wxID_WXFRAME1SKIP, wxID_WXFRAME1SLIDEVIEW, wxID_WXFRAME1SLIDE_LABEL, 
 wxID_WXFRAME1STATICBITMAP1, wxID_WXFRAME1STATICLINE1, 
 wxID_WXFRAME1STATICLINE2, wxID_WXFRAME1STATICLINE3, wxID_WXFRAME1STATICTEXT2, 
 wxID_WXFRAME1STOP, wxID_WXFRAME1TEMPLATE_LABEL, wxID_WXFRAME1TIME_LABEL, 
 wxID_WXFRAME1TRACE_LABEL, wxID_WXFRAME1UP_COARSE, wxID_WXFRAME1ZERO_LABEL, 
] = map(lambda _init_ctrls: wxNewId(), range(68))

class wxFrame1(wxFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wxPoint(127, 65), size=wxSize(1116, 856),
              style=wxDEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetClientSize(wxSize(1108, 822))

        self.camera_panel = wxPanel(id=wxID_WXFRAME1CAMERA_PANEL,
              name='camera_panel', parent=self, pos=wxPoint(424, 0),
              size=wxSize(696, 608), style=wxTAB_TRAVERSAL)
        self.camera_panel.SetToolTipString('camera panel')
        self.camera_panel.SetBackgroundColour(wxColour(236, 233, 216))

        self.camview = wxWindow(id=wxID_WXFRAME1CAMVIEW, name='camview',
              parent=self.camera_panel, pos=wxPoint(32, 56), size=wxSize(640,
              480), style=0)
        self.camview.SetToolTipString('camera view')
        self.camview.SetBackgroundColour(wxColour(128, 128, 128))
        EVT_LEFT_DOWN(self.camview, self.onCamViewClick)

        self.mmode_panel = wxPanel(id=wxID_WXFRAME1MMODE_PANEL,
              name='mmode_panel', parent=self, pos=wxPoint(424, 608),
              size=wxSize(688, 216), style=wxTAB_TRAVERSAL)
        self.mmode_panel.SetToolTipString('M-mode panel')

        self.mmodeview = wxWindow(id=wxID_WXFRAME1MMODEVIEW, name='mmodeview',
              parent=self.mmode_panel, pos=wxPoint(80, 24), size=wxSize(256,
              160), style=0)
        self.mmodeview.SetBackgroundColour(wxColour(128, 128, 128))

        self.mmode_dir_label = wxStaticText(id=wxID_WXFRAME1MMODE_DIR_LABEL,
              label='up/left', name='mmode_dir_label', parent=self.mmode_panel,
              pos=wxPoint(32, 8), size=wxSize(40, 13), style=0)

        self.mmode_dir_label2 = wxStaticText(id=wxID_WXFRAME1MMODE_DIR_LABEL2,
              label='down/right', name='mmode_dir_label2',
              parent=self.mmode_panel, pos=wxPoint(16, 184), size=wxSize(51,
              13), style=0)

        self.time_label = wxStaticText(id=wxID_WXFRAME1TIME_LABEL, label='time',
              name='time_label', parent=self.mmode_panel, pos=wxPoint(200, 184),
              size=wxSize(19, 13), style=0)

        self.zero_label = wxStaticText(id=wxID_WXFRAME1ZERO_LABEL, label='0',
              name='zero_label', parent=self.mmode_panel, pos=wxPoint(80, 184),
              size=wxSize(6, 13), style=0)

        self.duration_label = wxStaticText(id=wxID_WXFRAME1DURATION_LABEL,
              label='2 s', name='duration_label', parent=self.mmode_panel,
              pos=wxPoint(336, 184), size=wxSize(14, 13), style=0)

        self.mmode_view_label = wxStaticText(id=wxID_WXFRAME1MMODE_VIEW_LABEL,
              label='M-mode', name='mmode_view_label', parent=self.mmode_panel,
              pos=wxPoint(184, 0), size=wxSize(50, 16), style=0)
        self.mmode_view_label.SetFont(wxFont(10, wxSWISS, wxNORMAL, wxNORMAL,
              False, 'Microsoft Sans Serif'))

        self.percent_O2 = wxStaticText(id=wxID_WXFRAME1PERCENT_O2, label='0.0',
              name='percent_O2', parent=self.mmode_panel, pos=wxPoint(556, 56),
              size=wxSize(32, 29), style=0)
        self.percent_O2.SetFont(wxFont(18, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))
        self.percent_O2.SetBackgroundColour(wxColour(255, 255, 255))

        self.warning_O2 = wxStaticText(id=wxID_WXFRAME1WARNING_O2, label='No target pO2 set',
              name='warning_O2', parent=self.mmode_panel, pos=wxPoint(500, 100),
              size=wxSize(100, 29), style=0)
        self.warning_O2.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))
        self.warning_O2.SetBackgroundColour(wxColour(255, 255, 255))
        
        self.O2_label = wxStaticText(id=wxID_WXFRAME1O2_LABEL, label='% Oxygen',
              name='O2_label', parent=self.mmode_panel, pos=wxPoint(548, 24),
              size=wxSize(61, 16), style=0)
        self.O2_label.SetFont(wxFont(10, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))

        self.cam_view_label = wxStaticText(id=wxID_WXFRAME1CAM_VIEW_LABEL,
              label='Microscope view', name='cam_view_label',
              parent=self.camera_panel, pos=wxPoint(288, 24), size=wxSize(115,
              20), style=0)
        self.cam_view_label.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxNORMAL,
              False, 'Microsoft Sans Serif'))

        self.panel1 = wxPanel(id=wxID_WXFRAME1PANEL1, name='panel1',
              parent=self, pos=wxPoint(0, 264), size=wxSize(424, 576),
              style=wxTAB_TRAVERSAL)

        self.engine1 = wxWindow(id=wxID_WXFRAME1ENGINE1, name='engine1',
              parent=self.panel1, pos=wxPoint(24, 128), size=wxSize(160, 120),
              style=0)
        self.engine1.SetBackgroundColour(wxColour(128, 128, 128))

        self.engine2 = wxWindow(id=wxID_WXFRAME1ENGINE2, name='engine2',
              parent=self.panel1, pos=wxPoint(88, 280), size=wxSize(80, 120),
              style=0)
        self.engine2.SetBackgroundColour(wxColour(128, 128, 128))

        self.staticBitmap1 = wxStaticBitmap(bitmap=wxBitmap('./gui/template.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wxPoint(256, 280),
              size=wxSize(80, 120), style=0)

        self.curr_fly_label = wxStaticText(id=wxID_WXFRAME1CURR_FLY_LABEL,
              label='Current Fly', name='curr_fly_label', parent=self.panel1,
              pos=wxPoint(104, 264), size=wxSize(50, 13), style=0)
        self.curr_fly_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.template_label = wxStaticText(id=wxID_WXFRAME1TEMPLATE_LABEL,
              label='Template', name='template_label', parent=self.panel1,
              pos=wxPoint(272, 264), size=wxSize(44, 13), style=0)
        self.template_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.trace_label = wxStaticText(id=wxID_WXFRAME1TRACE_LABEL,
              label='Trace', name='trace_label', parent=self.panel1,
              pos=wxPoint(88, 112), size=wxSize(28, 13), style=0)
        self.trace_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.engine_view_label = wxStaticText(id=wxID_WXFRAME1ENGINE_VIEW_LABEL,
              label='Engine', name='engine_view_label', parent=self.panel1,
              pos=wxPoint(176, 8), size=wxSize(50, 20), style=0)
        self.engine_view_label.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxNORMAL,
              False, 'Microsoft Sans Serif'))

        self.engine3 = wxWindow(id=wxID_WXFRAME1ENGINE3, name='engine3',
              parent=self.panel1, pos=wxPoint(24, 424), size=wxSize(160, 120),
              style=0)
        self.engine3.SetBackgroundColour(wxColour(128, 128, 128))

        self.engine4 = wxWindow(id=wxID_WXFRAME1ENGINE4, name='engine4',
              parent=self.panel1, pos=wxPoint(208, 424), size=wxSize(160, 120),
              style=0)
        self.engine4.SetBackgroundColour(wxColour(128, 128, 128))

        self.pinpoint_label = wxStaticText(id=wxID_WXFRAME1PINPOINT_LABEL,
              label='Pinpoint Motion', name='pinpoint_label',
              parent=self.panel1, pos=wxPoint(264, 408), size=wxSize(73, 13),
              style=0)
        self.pinpoint_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.accum_label = wxStaticText(id=wxID_WXFRAME1ACCUM_LABEL,
              label='Accumulated Motion', name='accum_label',
              parent=self.panel1, pos=wxPoint(56, 408), size=wxSize(97, 13),
              style=0)
        self.accum_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.panel2 = wxPanel(id=wxID_WXFRAME1PANEL2, name='panel2',
              parent=self, pos=wxPoint(0, 0), size=wxSize(424, 264),
              style=wxTAB_TRAVERSAL)

        self.auto_label = wxStaticText(id=wxID_WXFRAME1AUTO_LABEL,
              label='Auto Detection', name='auto_label', parent=self.panel2,
              pos=wxPoint(144, 0), size=wxSize(107, 20), style=0)
        self.auto_label.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))

        self.auto = wxButton(id=wxID_WXFRAME1AUTO, label='Start', name='auto',
              parent=self.panel2, pos=wxPoint(120, 24), size=wxSize(75, 23),
              style=0)
        EVT_BUTTON(self.auto, wxID_WXFRAME1AUTO, self.OnAutoButton)

        self.staticLine2 = wxStaticLine(id=wxID_WXFRAME1STATICLINE2,
              name='staticLine2', parent=self.panel2, pos=wxPoint(0, 256),
              size=wxSize(384, 2), style=0)

        self.LoadSlide = wxButton(id=wxID_WXFRAME1LOADSLIDE, label='Load Slide',
              name='LoadSlide', parent=self.panel2, pos=wxPoint(8, 224),
              size=wxSize(75, 23), style=0)
        self.LoadSlide.SetToolTipString('Move stage into position to load a new slide')
        EVT_BUTTON(self.LoadSlide, wxID_WXFRAME1LOADSLIDE,
              self.OnLoadSlideButton)

        self.anesth = wxButton(id=wxID_WXFRAME1ANESTH, label='Anesthetize',
              name='anesth', parent=self.panel2, pos=wxPoint(8, 64),
              size=wxSize(75, 23), style=0)
        self.anesth.SetToolTipString('Starts automatic anesthetization and mounting')
        EVT_BUTTON(self.anesth, wxID_WXFRAME1ANESTH, self.OnAnesthButton)

        self.findFlies = wxButton(id=wxID_WXFRAME1FINDFLIES, label='Measure',
              name='findFlies', parent=self.panel2, pos=wxPoint(8, 112),
              size=wxSize(75, 23), style=0)
        self.findFlies.SetToolTipString('Click to find and measure flies')
        EVT_BUTTON(self.findFlies, wxID_WXFRAME1FINDFLIES,
              self.OnFindFliesButton)

        self.move_left = wxBitmapButton(bitmap=wxBitmap('./gui/left.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1MOVE_LEFT, name='move_left',
              parent=self.panel2, pos=wxPoint(144, 144), size=wxSize(24, 56),
              style=wxBU_AUTODRAW)
        self.move_left.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.move_left, wxID_WXFRAME1MOVE_LEFT,
              self.OnMove_leftButton)

        self.focus_out_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/outbig.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1FOCUS_OUT_COARSE,
              name='focus_out_coarse', parent=self.panel2, pos=wxPoint(168,
              160), size=wxSize(24, 24), style=wxBU_AUTODRAW)
        self.focus_out_coarse.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.focus_out_coarse, wxID_WXFRAME1FOCUS_OUT_COARSE,
              self.OnFocus_out_coarseButton)

        self.focus_in_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/inbig.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1FOCUS_IN_COARSE,
              name='focus_in_coarse', parent=self.panel2, pos=wxPoint(184, 176),
              size=wxSize(24, 24), style=wxBU_AUTODRAW)
        self.focus_in_coarse.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.focus_in_coarse, wxID_WXFRAME1FOCUS_IN_COARSE,
              self.OnFocus_in_coarseButton)

        self.focus_out_fine = wxBitmapButton(bitmap=wxBitmap('./gui/outsmall.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1FOCUS_OUT_FINE,
              name='focus_out_fine', parent=self.panel2, pos=wxPoint(200, 144),
              size=wxSize(16, 16), style=wxBU_AUTODRAW)
        self.focus_out_fine.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.focus_out_fine, wxID_WXFRAME1FOCUS_OUT_FINE,
              self.OnFocus_out_fineButton)

        self.focus_in_fine = wxBitmapButton(bitmap=wxBitmap('./gui/insmall.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1FOCUS_IN_FINE,
              name='focus_in_fine', parent=self.panel2, pos=wxPoint(216, 160),
              size=wxSize(16, 16), style=wxBU_AUTODRAW)
        self.focus_in_fine.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.focus_in_fine, wxID_WXFRAME1FOCUS_IN_FINE,
              self.OnFocus_in_fineButton)

        self.move_up = wxBitmapButton(bitmap=wxBitmap('./gui/up.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1MOVE_UP, name='move_up',
              parent=self.panel2, pos=wxPoint(168, 120), size=wxSize(64, 24),
              style=wxBU_AUTODRAW)
        self.move_up.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.move_up, wxID_WXFRAME1MOVE_UP, self.OnMove_upButton)

        self.move_right = wxBitmapButton(bitmap=wxBitmap('./gui/right.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1MOVE_RIGHT, name='move_right',
              parent=self.panel2, pos=wxPoint(232, 144), size=wxSize(24, 56),
              style=wxBU_AUTODRAW)
        self.move_right.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.move_right, wxID_WXFRAME1MOVE_RIGHT,
              self.OnMove_rightButton)

        self.move_down = wxBitmapButton(bitmap=wxBitmap('./gui/down.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1MOVE_DOWN, name='move_down',
              parent=self.panel2, pos=wxPoint(168, 200), size=wxSize(64, 24),
              style=wxBU_AUTODRAW)
        self.move_down.SetBackgroundColour(wxColour(255, 255, 255))
        EVT_BUTTON(self.move_down, wxID_WXFRAME1MOVE_DOWN,
              self.OnMove_downButton)

        self.manual_label = wxStaticText(id=wxID_WXFRAME1MANUAL_LABEL,
              label='Manual Controls', name='manual_label', parent=self.panel2,
              pos=wxPoint(144, 64), size=wxSize(115, 20), style=0)
        self.manual_label.SetFont(wxFont(12, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))

        self.slideview = wxWindow(id=wxID_WXFRAME1SLIDEVIEW, name='slideview',
              parent=self.panel1, pos=wxPoint(56, 40), size=wxSize(272, 50),
              style=0)
        self.slideview.SetBackgroundColour(wxColour(128, 128, 128))

        self.slide_label = wxStaticText(id=wxID_WXFRAME1SLIDE_LABEL,
              label='Slide', name='slide_label', parent=self.panel1,
              pos=wxPoint(24, 56), size=wxSize(23, 13), style=0)
        self.slide_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.graph1 = wxWindow(id=wxID_WXFRAME1GRAPH1, name='graph1',
              parent=self.panel1, pos=wxPoint(208, 128), size=wxSize(160, 120),
              style=0)
        self.graph1.SetBackgroundColour(wxColour(128, 128, 128))

        self.outline_label = wxStaticText(id=wxID_WXFRAME1OUTLINE_LABEL,
              label='Outline and axis', name='outline_label',
              parent=self.panel1, pos=wxPoint(256, 112), size=wxSize(75, 13),
              style=0)
        self.outline_label.SetBackgroundColour(wxColour(236, 233, 216))

        self.staticLine3 = wxStaticLine(id=wxID_WXFRAME1STATICLINE3,
              name='staticLine3', parent=self.panel2, pos=wxPoint(0, 56),
              size=wxSize(384, 2), style=0)

        self.staticLine1 = wxStaticLine(id=wxID_WXFRAME1STATICLINE1,
              name='staticLine1', parent=self.camera_panel, pos=wxPoint(40,
              586), size=wxSize(680, 2), style=0)

        self.deposit = wxButton(id=wxID_WXFRAME1DEPOSIT, label='Deposit',
              name='deposit', parent=self.panel2, pos=wxPoint(8, 88),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.deposit, wxID_WXFRAME1DEPOSIT, self.OnDepositButton)

        self.left_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/left.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1LEFT_COARSE,
              name='left_coarse', parent=self.panel2, pos=wxPoint(120, 144),
              size=wxSize(24, 56), style=wxBU_AUTODRAW)
        EVT_BUTTON(self.left_coarse, wxID_WXFRAME1LEFT_COARSE,
              self.OnLeft_coarseButton)

        self.down_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/down.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1DOWN_COARSE,
              name='down_coarse', parent=self.panel2, pos=wxPoint(168, 224),
              size=wxSize(64, 24), style=wxBU_AUTODRAW)
        EVT_BUTTON(self.down_coarse, wxID_WXFRAME1DOWN_COARSE,
              self.OnDown_coarseButton)

        self.right_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/right.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1RIGHT_COARSE,
              name='right_coarse', parent=self.panel2, pos=wxPoint(256, 144),
              size=wxSize(24, 56), style=wxBU_AUTODRAW)
        EVT_BUTTON(self.right_coarse, wxID_WXFRAME1RIGHT_COARSE,
              self.OnRight_coarseButton)

        self.up_coarse = wxBitmapButton(bitmap=wxBitmap('./gui/up.bmp',
              wxBITMAP_TYPE_BMP), id=wxID_WXFRAME1UP_COARSE, name='up_coarse',
              parent=self.panel2, pos=wxPoint(168, 96), size=wxSize(64, 24),
              style=wxBU_AUTODRAW)
        EVT_BUTTON(self.up_coarse, wxID_WXFRAME1UP_COARSE,
              self.OnUp_coarseButton)

        self.skip = wxButton(id=wxID_WXFRAME1SKIP, label='Skip Fly',
              name='skip', parent=self.panel2, pos=wxPoint(312, 184),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.skip, wxID_WXFRAME1SKIP, self.OnSkipButton)

        self.stop = wxButton(id=wxID_WXFRAME1STOP, label='Stop', name='stop',
              parent=self.panel2, pos=wxPoint(208, 24), size=wxSize(75, 23),
              style=0)
        EVT_BUTTON(self.stop, wxID_WXFRAME1STOP, self.OnStopButton)

        self.reset = wxButton(id=wxID_WXFRAME1RESET, label='Reset Focus',
              name='reset', parent=self.panel2, pos=wxPoint(8, 176),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.reset, wxID_WXFRAME1RESET, self.OnResetButton)

        self.next_fly = wxButton(id=wxID_WXFRAME1NEXT_FLY, label='Next Fly',
              name='next_fly', parent=self.panel2, pos=wxPoint(312, 160),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.next_fly, wxID_WXFRAME1NEXT_FLY, self.OnNext_flyButton)

        self.detect_flies = wxButton(id=wxID_WXFRAME1DETECT_FLIES,
              label='Detect Flies', name='detect_flies', parent=self.panel2,
              pos=wxPoint(312, 64), size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.detect_flies, wxID_WXFRAME1DETECT_FLIES,
              self.OnDetect_fliesButton)

        self.mmode = wxButton(id=wxID_WXFRAME1MMODE, label='Capture M-mode',
              name='mmode', parent=self.panel2, pos=wxPoint(304, 208),
              size=wxSize(88, 23), style=0)
        self.mmode.SetToolTipString('Click to find and measure flies')
        EVT_BUTTON(self.mmode, wxID_WXFRAME1MMODE, self.OnMmodeButton)

        self.save = wxButton(id=wxID_WXFRAME1SAVE, label='Save Fly',
              name='save', parent=self.panel2, pos=wxPoint(312, 136),
              size=wxSize(75, 23), style=0)
        EVT_BUTTON(self.save, wxID_WXFRAME1SAVE, self.OnSaveButton)

        self.new = wxButton(id=wxID_WXFRAME1NEW, label='New Slide', name='new',
              parent=self.panel2, pos=wxPoint(8, 200), size=wxSize(75, 23),
              style=0)
        EVT_BUTTON(self.new, wxID_WXFRAME1NEW, self.OnNewButton)

        self.add = wxButton(id=wxID_WXFRAME1ADD, label='Add Fly', name='add',
              parent=self.panel2, pos=wxPoint(312, 88), size=wxSize(75, 23),
              style=0)
        EVT_BUTTON(self.add, wxID_WXFRAME1ADD, self.OnAddButton)

        self.movie = wxButton(id=wxID_WXFRAME1MOVIE, label='Capture Movie',
              name='movie', parent=self.panel2, pos=wxPoint(304, 232),
              size=wxSize(88, 23), style=0)
        EVT_BUTTON(self.movie, wxID_WXFRAME1MOVIE, self.OnMovieButton)

        self.gas = wxButton(id=wxID_WXFRAME1GAS, label='Gas', name='gas',
              parent=self.panel2, pos=wxPoint(8, 136), size=wxSize(75, 23),
              style=0)
        EVT_BUTTON(self.gas, wxID_WXFRAME1GAS, self.OnGasButton)

        self.heart_rate = wxStaticText(id=wxID_WXFRAME1HEART_RATE, label='0.0',
              name='heart_rate', parent=self.mmode_panel, pos=wxPoint(452, 56),
              size=wxSize(32, 29), style=0)
        self.heart_rate.SetFont(wxFont(18, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))
        self.heart_rate.SetBackgroundColour(wxColour(255, 255, 255))

        self.staticText2 = wxStaticText(id=wxID_WXFRAME1STATICTEXT2,
              label='Heart Rate', name='staticText2', parent=self.mmode_panel,
              pos=wxPoint(436, 24), size=wxSize(65, 16), style=0)
        self.staticText2.SetFont(wxFont(10, wxSWISS, wxNORMAL, wxNORMAL, False,
              'Microsoft Sans Serif'))

        self.measure_fly = wxButton(id=wxID_WXFRAME1MEASURE_FLY,
              label='Measure Fly', name='measure_fly', parent=self.panel2,
              pos=wxPoint(312, 112), size=wxSize(75, 23), style=0)
        self.measure_fly.SetToolTipString('Click to find and measure flies')
        EVT_BUTTON(self.measure_fly, wxID_WXFRAME1MEASURE_FLY,
              self.OnMeasure_flyButton)

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
        
        self.graph1ViewDib = ImageWin.Dib("L", (160,120))
        self.graph1DC = wxClientDC(self.graph1)
        
    def OnClick(self,event):
        print vars(event)

    def displayCam(self,frame,draw_mask):
        f = frame.copy()
        frameDraw = ImageDraw.Draw(f)
        for mask in draw_mask:
            frameDraw.point(mask,fill=128)  #draws MMode line on frame
        self.CamViewDib.paste(f)
        self.CamViewDib.expose(self.camviewDC.GetHDC())    

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
        rate_str = '%4.2f'%rate       # Displays instantaneous and ave. HRs in top left corner
        self.heart_rate.SetLabel(rate_str)
        
    def displayO2(self, O2):
        O2 = O2*100
        O2_str = '%2.2f'%O2       # Displays instantaneous and ave. HRs in top left corner
        self.percent_O2.SetLabel(O2_str)

##    def warnO2(self,percentage):
##        warning = 'Adjust O2 level to target percentage of '+ percentage
##        self.warning_O2.SetBackgroundColour(wxColour(255, 0, 0))
##        self.warning_O2.SetLabel(warning)
        
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
    
