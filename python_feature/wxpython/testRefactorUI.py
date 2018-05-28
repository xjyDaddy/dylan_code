#!/usr/bin/env python
#Date:2018/5/16
#Author:dylan_xi
#Desc:learn python gui wxpython
#references:https://wiki.woodpecker.org.cn/moin/WxPythonInAction/ChapterFive
import unittest
import refactorUIExample
import wx

class TestExample(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frame = refactorUIExample.RefactorExample(parent = None , id = -1)
    def tearDown(self):
        self.frame.Destroy()
    def testModel(self):
        self.frame.OnFirst(None)
        self.assertEqual("dylan" , self.frame.model.first ,
        msg = "First is wrong")
        self.assertEqual("xi" , self.frame.model.last) 
    def testEvent(self):
        panel = self.frame.GetChildren()[0]
        btn = None
        for each in panel.GetChildren():
            if each.GetLabel() == 'First':
                btn = each
                break
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED , btn.GetId())
        btn.GetEventHandler().ProcessEvent(event)
        self.assertEqual('dylan' , self.frame.model.first)
def suite():
    suite = unittest.makeSuite(TestExample , "test")
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')