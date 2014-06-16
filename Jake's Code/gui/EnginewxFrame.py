#Boa:Frame:wxFrame1

##  This frame opens when 'Engine' button is clicked, useful for visualizing filters, etc.

from wxPython.wx import *
import ImageWin

def makeBasicSizer(parentWin, Name, DisplaysList):
    sizer = wxBoxSizer(wxVERTICAL)
    win = wxScrolledWindow(parent=parentWin, id=1010, pos=wxPoint(145, 158),
            size=wxSize(int(640/1.5), int(480/1.5)), style=wxHSCROLL | wxVSCROLL)
    win.SetVirtualSize(wxSize(640, 480))
    win.SetScrollRate(10,10)
    im = ImageWin.Dib('L', (640,480))
    sizer.AddWindow(win,1,wxEXPAND)
    sizer.Add(wxStaticText(parent=parentWin, id=1111, label=Name))
    DisplaysList[Name] = [win,im]
    return sizer

def makeGridSizer(parentWin, image_labels, DisplayList):
    row = (len(image_labels)/2)+(len(image_labels)%2)
    col = 2
    grid = wxGridSizer(col,row)
    for Name in image_labels:
        grid.AddSizer(makeBasicSizer(parentWin, Name, DisplayList), 1, wxEXPAND)
    h_size = ((640/2)+5) * col
    v_size = ((480/2)+5) * row
    parentWin.SetVirtualSize(wxSize(v_size, h_size))
    return grid

def create(parent, hButton):
    return wxFrame1(parent, hButton)

[wxID_WXFRAME1, wxID_WXFRAME1SCROLLEDWINDOW1, 
] = map(lambda _init_ctrls: wxNewId(), range(2))

class wxFrame1(wxFrame):
    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wxFrame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wxPoint(145, 158), size=wxSize(768, 558),
              style=wxDEFAULT_FRAME_STYLE, title='wxFrame1')
        self._init_utils()
        self.SetClientSize(wxSize(900, 700))
        EVT_CLOSE(self, self.OnClose)

        self.scrolledWindow1 = wxScrolledWindow(id=wxID_WXFRAME1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self, pos=wxPoint(0, 0),
              size=wxSize(760, 531), style=wxHSCROLL | wxVSCROLL)
        self.scrolledWindow1.SetScrollRate(10,10)

    def __init__(self, parent, hButton):
        self._init_ctrls(parent)
        self.sizer = None
        self.image_labels = ['Motion','Thresholded']
        self.DisplaysList = {}
        self.hButton = hButton
        self.Make()
        
    def Make(self):
        if self.sizer:
            self.sizer.Destroy()
        self.grid = makeGridSizer(self.scrolledWindow1, self.image_labels, self.DisplaysList)
        self.scrolledWindow1.SetSizer(self.grid)
        self.grid.Fit(self.scrolledWindow1)
        

    def DisplayEngine(self,images):
        for label in self.image_labels:
            if images.has_key(label):
                win = self.DisplaysList[label][0]
                dib = self.DisplaysList[label][1]
                dc = wxClientDC(win)
                dib.paste(images[label])
                win.PrepareDC(dc)
                dib.expose(dc.GetHDC())

    def OnClose(self, event):
        #if self.hButton:                   make this a toggle button and uncomment
        #    self.hButton.SetValue(False)
        self.Destroy()
