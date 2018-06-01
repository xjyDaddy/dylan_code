 #!/usr/bin/env python
import wx 
import praticleSystem
import Config
class Mywin(wx.Frame): 
    ID_TIMER = 1
    DELAT_TIME =  1000 /60
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title,size = Config.screenSize)  
        self.ps = praticleSystem.PariticleSystem()
        self.InitUI() 
    def __del__(self):
        self.timer.Stop()
    def InitUI(self): 
        self.timer = wx.Timer(self, self.ID_TIMER)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER , self.OnTimer , id = self.ID_TIMER)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnErase) 
        self.Centre() 
        self.Show(True)
        self.timer.Start(self.DELAT_TIME)
        self.fpsLabel = wx.StaticText(self, wx.NewId(), self.getFPSText(), (10 ,Config.screenSize[1]-70))
        #self.CollisionDetectNumLabel = wx.StaticText(self, wx.NewId(), self.getCollisionDetectNum()  , (10 ,Config.screenSize[1]-100)) 
    #解决擦除背景闪烁的问题
    def OnErase(self ,event):
        pass
    def OnPaint(self, e):
        dc = wx.BufferedPaintDC(self)
        brush = wx.Brush("white")  
        dc.SetBackground(brush)  
        dc.Clear() 
        self.ps.draw(dc)
    def getFPSText(self):
        return 'FPS:{:.0f}' .format(1000/self.DELAT_TIME)
    def getCollisionDetectNum(self):
        return 'CollisionDetectNum:{0}' .format(Config.collisionDetectTimes)
    def OnTimer(self , event):
        if event.GetId() == self.ID_TIMER:
            Config.collisionDetectTimes = 0
            dt = event.GetInterval()/ 1000.0
            self.ps.update(dt)
            self.Refresh()
            ##self.CollisionDetectNumLabel.SetLabelText(self.getCollisionDetectNum())
ex = wx.App() 
Mywin(None,'Drawing Demo - dylan_xi') 
ex.MainLoop()