 #!/usr/bin/env python
import wx 
 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (500,300))  
      self.InitUI() 
         
   def InitUI(self): 
      print("InitUI")
      self.Bind(wx.EVT_PAINT, self.OnPaint) 
      self.Bind(wx.EVT_MOUSE_EVENTS , self.OnMouseClick)
      self.Centre() 
      self.Show(True)
		
   def OnMouseClick(self , e):
      self.Refresh()
      print(e)

   def OnPaint(self, e):
      print('OnPaint') 
      dc = wx.PaintDC(self) 
      brush = wx.Brush("white")  
      dc.SetBackground(brush)  
      dc.Clear() 
        
      dc.DrawCircle(300,125,50) 
      dc.SetBrush(wx.Brush(wx.Colour(255,255,255))) 
      dc.DrawCircle(300,125,30) 
		
      font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
      dc.SetFont(font) 
      dc.DrawText("Hello wxPython",200,10) 

		
      pen = wx.Pen(wx.Colour(0,0,255)) 
      #dc.SetPen(pen) 
      dc.SetBrush(wx.Brush(wx.Colour(0,255,255)))
      dc.DrawLine(200,50,350,50) 
      dc.SetBrush(wx.Brush(wx.Colour(0,255,0), wx.CROSS_HATCH)) 
      dc.DrawRectangle(380, 15, 90, 60) 
		
ex = wx.App() 
Mywin(None,'Drawing Demo - www.yiibai.com') 
ex.MainLoop()