#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import _winreg

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, 
 wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, 
] = [wx.NewId() for _init_ctrls in range(24)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='Frame1', parent=prnt,
              pos=wx.Point(365, 286), size=wx.Size(468, 214),
              style=wx.DEFAULT_FRAME_STYLE, title='DMCXP')
        self.SetClientSize(wx.Size(460, 187))
        self.SetBackgroundColour(wx.Colour(211, 211, 211))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Demineur Cheat (XP) -  By Murf :', name='staticText1',
              parent=self, pos=wx.Point(8, 24), size=wx.Size(157, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=' Mode debutant :', name='staticText2', parent=self,
              pos=wx.Point(24, 72), size=wx.Size(83, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Mode Intermediaire :', name='staticText3', parent=self,
              pos=wx.Point(8, 112), size=wx.Size(100, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Mode Expert :', name='staticText4', parent=self,
              pos=wx.Point(40, 152), size=wx.Size(68, 13), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(17, 56),
              size=wx.Size(423, 2), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='Nom :', name='staticText5', parent=self, pos=wx.Point(120,
              72), size=wx.Size(28, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(152, 72), size=wx.Size(100, 21),
              style=0, value='')
        self.textCtrl1.SetMaxLength(10)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='Temps :', name='staticText6', parent=self,
              pos=wx.Point(272, 72), size=wx.Size(38, 16), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(320, 72), size=wx.Size(56, 21), style=0,
              value='')
        self.textCtrl2.SetMaxLength(3)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label='Secondes', name='staticText7', parent=self,
              pos=wx.Point(384, 72), size=wx.Size(46, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label='Nom :', name='staticText8', parent=self, pos=wx.Point(120,
              112), size=wx.Size(28, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label='Nom :', name='staticText9', parent=self, pos=wx.Point(120,
              152), size=wx.Size(28, 13), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(152, 112), size=wx.Size(100, 21),
              style=0, value='')
        self.textCtrl3.SetMaxLength(8)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label='Temps :', name='staticText10', parent=self,
              pos=wx.Point(272, 112), size=wx.Size(40, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label='Temps :', name='staticText11', parent=self,
              pos=wx.Point(272, 152), size=wx.Size(38, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label='Secondes', name='staticText12', parent=self,
              pos=wx.Point(384, 112), size=wx.Size(46, 13), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label='Secondes', name='staticText13', parent=self,
              pos=wx.Point(384, 152), size=wx.Size(46, 13), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(320, 112), size=wx.Size(56, 21),
              style=0, value='')
        self.textCtrl4.SetMaxLength(3)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(152, 152), size=wx.Size(100, 21),
              style=0, value='')
        self.textCtrl5.SetMaxLength(8)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(320, 152), size=wx.Size(56, 21),
              style=0, value='')
        self.textCtrl6.SetMaxLength(3)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(ID=wxID_FRAME1GENBITMAPTEXTBUTTON1,
              bitmap=wx.Bitmap('C:/rh/demineur/icone.bmp', wx.BITMAP_TYPE_BMP),
              label='Appliquer !', name='genBitmapTextButton1', parent=self,
              pos=wx.Point(192, 8), size=wx.Size(112, 40), style=0)
        self.genBitmapTextButton1.SetBackgroundColour(wx.Colour(212, 212, 212))
        self.genBitmapTextButton1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, 'Tahoma'))
        self.genBitmapTextButton1.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton1Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label='Laissez les champs vides', name='staticText14',
              parent=self, pos=wx.Point(328, 16), size=wx.Size(117, 13),
              style=0)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label='pour ne pas les modifier.', name='staticText15',
              parent=self, pos=wx.Point(328, 32), size=wx.Size(118, 13),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton1Button(self, event):
        nom1 = self.textCtrl1.GetValue()
        nom2 = self.textCtrl3.GetValue()
        nom3 = self.textCtrl5.GetValue()
        score1 = self.textCtrl2.GetValue()
        score2 = self.textCtrl4.GetValue()
        score3 = self.textCtrl6.GetValue()
        score1=int(score1)
        score2=int(score2)
        score3=int(score3)
        if nom1 != "":  
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Name1', 0, _winreg.REG_SZ, nom1)
            _winreg.CloseKey(key)
        if nom2 != "":
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Name2', 0, _winreg.REG_SZ, nom2)
            _winreg.CloseKey(key)
        if nom3 != "":
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Name3', 0, _winreg.REG_SZ, nom3)
            _winreg.CloseKey(key)
        if score1 != "":
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Time1', 0, _winreg.REG_DWORD, score1)
            _winreg.CloseKey(key)
        if score2 != "":
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Time2', 0, _winreg.REG_DWORD, score2)
            _winreg.CloseKey(key)
        if score3 != "":
            key = _winreg.CreateKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
            _winreg.SetValueEx(key, 'Time3', 0, _winreg.REG_DWORD, score3)
            _winreg.CloseKey(key)
        event.Skip()
