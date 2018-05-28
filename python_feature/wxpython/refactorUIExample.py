#!/usr/bin/env python
#Date:2018/5/16
#Author:dylan_xi
#Desc:learn python gui wxpython

import wx

class RefactorExample(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self , parent, id ,'RefactorExample' , size = (340 , 200))
        panel = wx.Panel(self , -1)
        panel.SetBackgroundColour('White')
        self.textFields = {}
        self.CreateButtonBar(panel)
        self.CreateMenu(panel)
        self.createTextFields(panel)
        self.model = SimpleName()
        self.model.addListener(self.OnUpdate)
    def ButtonData(self):
        return (('First' , self.OnFirst ),
                ('  PREV', self.OnPrev),
                ("NEXT" , self.OnNext),
                ("Last" , self.OnLast))
    def CreateButtonBar(self , panel , yPos = 0):
        xPos = 0
        for eachLabel , eachHandler in self.ButtonData():
            pos = (xPos , yPos)
            button = self.buildOneButton(panel , eachLabel , eachHandler , pos)
            xPos += button.GetSize().width    
    def buildOneButton(self , parent , label , handler , pos = (0 , 0)):
        button = wx.Button(parent , -1 , label , pos)
        self.Bind(wx.EVT_BUTTON , handler , button)
        return button
    def MenuData(self):
        return (("&File",
            ("&Open", "Open in status bar", self.OnOpen),
            ("&Quit", "Quit", self.OnCloseWindow)),
            ("&Edit",
            ("&Copy", "Copy", self.OnCopy),
            ("&Cut", "Cut", self.OnCut),
            ("&Paste", "Paste", self.OnPaste),
            ("", "", ""),
            ("&Options", "DisplayOptions", self.OnOptions)))
    def CreateMenu(self, parent):
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1:]
            menuBar.Append(self.buildOneMenu(menuItems) , menuLabel)
        self.SetMenuBar(menuBar)
    def buildOneMenu(self , menuData):
        menu = wx.Menu()
        for eachLabel , eachStatus , eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1 , eachLabel ,eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu
    def textFieldData(self): #文本数据
            return (("First Name", (10, 50)),
                    ("Last Name", (10, 80)))
    #创建文本
    def createTextFields(self, panel):
            for eachLabel, eachPos in self.textFieldData():
                    self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
            static = wx.StaticText(panel, wx.NewId(), label, pos)
            static.SetBackgroundColour("White")
            textPos = (pos[0] + 75, pos[1])
            self.textFields[label] =  wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1), pos=textPos)
    def OnFirst(self, event):
        self.model.set("dylan" , "xi")
    def OnPrev(self, event):
        self.model.set("li" , "lei")
    def OnNext(self, event):
        self.model.set("da" , "ming")
    def OnLast(self, event):
        self.model.set("chen" , "jia")
    def OnOpen(self , event): pass
    def OnCloseWindow(self , event): pass
    def OnCopy(self , event): pass
    def OnCut(self , event): pass
    def OnPaste(self , event): pass
    def OnOptions(self , event): pass    
    def OnUpdate(self , model):
        self.textFields['First Name'].SetValue(model.first)
        self.textFields['Last Name'].SetValue(model.last )
class AbstractModel(object):
    def __init__(self, *args, **kwargs):
        self.listeners = []
    def addListener(self , listenerFunc):
        self.listeners.append(listenerFunc)
    def removeListner(self , listenerFunc):
        self.listeners.remove(listenerFunc)
    def update(self):
        for eachFunc in self.listeners:
            eachFunc(self)

class SimpleName(AbstractModel):
    def __init__(self,first = '' , last = ''):
        AbstractModel.__init__(self)
        self.set(first , last)
    def set(self, first , last):
        self.first = first
        self.last  = last
        self.update()

if __name__ == '__main__':
    app = wx.App()
    frame = RefactorExample(parent = None , id = -1)
    frame.Show()
    app.MainLoop()



