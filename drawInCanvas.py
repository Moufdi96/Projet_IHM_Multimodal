from createCanvas import*



class canvasResult(CreateCanvas):
    def __init__(self):
        CreateCanvas.__init__(self)
        self.mouseClickX = 0
        self.mouseClickY = 0
        self.canvas_width = 0
        self.canvas_height = 0
        self.shape = ''
        self.color = ''
        self.soundCreate = ''
    
    def setCanvasWindow(self,canvas_width,canvas_height,shape,color,soundPoistion):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.color = color
        self.shape = shape
        self.soundPosition = soundPoistion
        self.master.title('IHM Multimodale')
        self.canvasWindow = Canvas(self.master, width=canvas_width, height=canvas_height,bg='black')
        self.canvasWindow.pack(expand=YES, fill=BOTH)
        if(len(self.soundPosition) != 0):
            if(self.soundCreate in ['right','in the right']):
                self.createShape(self.shape,self.canvas_width-150,self.canvas_height/2,self.color)
            elif(self.soundPosition in ['left','in the left']):
                self.createShape(self.shape,150,self.canvas_height/2,self.color)                
            elif(self.soundPosition == 'up'):
                self.createShape(self.shape,self.canvas_width/2,150,self.color)
            elif(self.soundPosition == 'down'):
                self.createShape(self.shape,self.canvas_width/2,self.canvas_width-150,self.color)                
            elif(self.soundPosition ['middle','in the middle']):
                self.createShape(self.shape,self.canvas_width/2,self.canvas_height/2,self.color)                
    
        mouseClick = self.canvasWindow.bind('<B1-Motion>',self.mouseClickCoordinates)
        message = Label(self.master,text='Click to show where to draw your shape')
        message.pack(side=BOTTOM)
        self.master.mainloop()
    
    def mouseClickCoordinates(self,event):
        x1,y1 = (event.x-1), (event.y-1)
        x2,y2 = (event.x+1), (event.y+1)
        self.mouseClickX = (x1+x2)/2
        self.mouseClickY = (y1+y2)/2
        self.createShape(self.shape,self.mouseClickX,self.mouseClickY,self.color)
        print(self.mouseClickX)
        print(self.mouseClickY)


    def createShape(self,shape,x,y,color):
        if(shape == 'line'):
            self.drawLine(x,y,color)
        elif(shape == 'rectangle'):
            self.drawRectangle(x,y,color)
        elif(shape == 'cercle'):
            self.drawCircle(x,y,color)
        
    
    def drawLine(self,x,y,color):
        self.canvasWindow.create_line(x-100,y,x+100,y,fill=color)
    
    def drawRectangle(self,x,y,color):
        self.canvasWindow.create_rectangle(x-100,y-60,x+100,y+60,fill=color)
    
    def drawCircle(self,x,y,color):
        self.canvasWindow.create_oval(x-100,y-100,x+100,y+100,fill=color)


