Tricher au demineur :) (modifier le registre d'xp)--------------------------------------------------
Url     : http://codes-sources.commentcamarche.net/source/36376-tricher-au-demineur-modifier-le-registre-d-xpAuteur  : z_MurfDate    : 06/09/2013
Licence :
=========

Ce document intitulé « Tricher au demineur :) (modifier le registre d'xp) » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Code source pour tricher au demineur (interface graphique)
<br />
<br />Necess
ite wxPython
<br /><a name='source-exemple'></a><h2> Source / Exemple : </h2>

<br /><pre class='code' data-mode='basic'>
#Alors, vous me demandez des commen
taires, comme la dis ECONS, toute la partie App1, ca sert juste de &quot;noyau&q
uot;, il 
#affiche frame1, frame1 contient des lignes pour l'interfaces :

se
lf.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
label='Demineur Cheat
 (XP) -  By Murf :', name='staticText1',
parent=self, pos=wx.Point(8, 24), size
=wx.Size(157, 13), style=0)

#etc...

#Les lignes importantes sont celles la
 :

#Quand on clique sur le bouton :

    def OnGenBitmapTextButton1Button(s
elf, event):

#Je definis des variables avec les valeurs des editbox de la fra
me:

        nom1 = self.textCtrl1.GetValue()
        nom2 = self.textCtrl3.G
etValue()
        nom3 = self.textCtrl5.GetValue()
        score1 = self.textC
trl2.GetValue()
        score2 = self.textCtrl4.GetValue()
        score3 = se
lf.textCtrl6.GetValue()
        score1=int(score1)
        score2=int(score2)

        score3=int(score3)

#On verifie si la valeur n'est pas nulle ...

i
f nom1 != &quot;&quot;:

#On a cree (ou remplace) la clée du  registre compten
ant les nom des recordman

key = _winreg.CreateKey( _winreg.HKEY_USERS,'S-1-5-
21-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
_winreg
.SetValueEx(key, 'Name1', 0, _winreg.REG_SZ, nom1)
_winreg.CloseKey(key)
if no
m2 != &quot;&quot;:            key=_winreg.CreateKey(_winreg.HKEY_USERS,'S-1-5-2
1-1554517956-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
_winreg.
SetValueEx(key, 'Name2', 0, _winreg.REG_SZ, nom2)
_winreg.CloseKey(key)
if nom
3 != &quot;&quot;:
key=_winreg.CreateKey(_winreg.HKEY_USERS,'S-1-5-21-155451795
6-2739884901-447938988-1008\\Software\\Microsoft\\winmine')
_winreg.SetValueEx(
key, 'Name3', 0, _winreg.REG_SZ, nom3)
_winreg.CloseKey(key)
if score1 != &quo
t;&quot;:           

#on fait pareil pour les autres, la difference est que l
es scores sont une valeur numerique, 
#il ne faut pas oublier de convertir la v
ariable &quot;time1&quot; en entier:

key = _winreg.CreateKey( _winreg.HKEY_US
ERS,                           'S-1-5-21-1554517956-2739884901-447938988-1008\\S
oftware\\Microsoft\\winmine')
_winreg.SetValueEx(key, 'Time1', 0, _winreg.REG_D
WORD, score1)
_winreg.CloseKey(key)
if score2 != &quot;&quot;:
key=_winreg.Cr
eateKey(_winreg.HKEY_USERS,'S-1-5-21-1554517956-2739884901-447938988-1008\\Softw
are\\Microsoft\\winmine')
_winreg.SetValueEx(key, 'Time2', 0, _winreg.REG_DWORD
, score2)
_winreg.CloseKey(key)
if score3 != &quot;&quot;:
key = _winreg.Crea
teKey( _winreg.HKEY_USERS, 'S-1-5-21-1554517956-2739884901-447938988-1008\\Softw
are\\Microsoft\\winmine')
_winreg.SetValueEx(key, 'Time3', 0, _winreg.REG_DWORD
, score3)
_winreg.CloseKey(key)
event.Skip()

#et voila, c'est juste une pet
ite manipulation du registre, on pourrais refaire ce genre de programme en batch
 (sans #inteface graphique)...
</pre>
<br /><a name='conclusion'></a><h2> Conc
lusion : </h2>
<br />copiez App1.py et Frame1.py dans le meme rep et lancez Ap
p1
