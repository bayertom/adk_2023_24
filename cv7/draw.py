from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from Edge import *
from QPoint3DF import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = [] 
        self.dt = []
        self.contours = []
    
    
    def mousePressEvent(self, e:QMouseEvent):
        #Get cursor position
        x = e.position().x()
        y = e.position().y()

        #Create new point
        p = QPoint3DF(x,y , 0.0)

        #Add point to point cloud
        self.points.append(p)
            
        #Repaint screen
        self.repaint()


    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)

        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.green)
        qp.setBrush(Qt.GlobalColor.transparent)

        #Draw Delaunay triangulation
        for e in self.dt:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()),int(e.getEnd().x()), int(e.getEnd().y()))
        
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.lightGray)
        qp.setBrush(Qt.GlobalColor.transparent)

        #Draw contour lines
        for e in self.contours:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()),int(e.getEnd().x()), int(e.getEnd().y()))
         
        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw points
        r = 10
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
        
        #Draw slope
        
        #Draw aspect
      
        qp.end()
        
        
    def getPoints(self):
        #Return points
        return self.points
    
      
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear triangles
        self.dt.clear()
                
        #Repaint screen
        self.repaint()
        
    
    def setDT(self, dt:list[Edge]):
        #Set DT
        
        self.dt = dt
    
    def getDT(self):
        #Get DT
        return self.dt
    
    def setContours(self, contours:list[Edge]):
        #Set contour lines
        
        self.contours = contours
        