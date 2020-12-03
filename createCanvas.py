from tkinter import *
import json 

class CreateCanvas:

    def __init__(self):
        self.master = Tk()
        self.templates = {}
        self.stroke = 0
        self.listFigurePoints = []
        self.color  ='red'
        
    #def loadJsonFile(self):
    #    jsonText = ''    
    #    with open("/home/moufdi/dollarlib/templates_file.json", "r") as templates_file:
    #        #templates = json.load(templates_file)
    #        jsonText = templates_file.read()
    #        self.templates = json.loads(jsonText)
            

    def setCanvasWindow(self,canvas_width,canvas_height):
        
        self.master.title('Painting in python')
        
        self.canvasWindow = Canvas(self.master, width=canvas_width, height=canvas_height,bg='black')
        self.canvasWindow.pack(expand=YES, fill=BOTH)
        paint_id = self.canvasWindow.bind('<B1-Motion>',self.paint)
        self.canvasWindow.bind('<B1-ButtonRelease>',self.reinit)
        #self.canvasWindow.bind('<B2-ButtonRelease>',self.close)
        message = Label(self.master,text='Press and Drag to draw your shape')
        message.pack(side=BOTTOM)
        self.master.mainloop()

    def paint (self,event):
        
        x1,y1 = (event.x-1), (event.y-1)
        x2,y2 = (event.x+1), (event.y+1)
        self.canvasWindow.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)
        oval_centerX = (x1+x2)/2
        oval_centerY = (y1+y2)/2
        stroke = self.stroke
        self.listFigurePoints.append((oval_centerX,oval_centerY,stroke))
       
    
    def reinit(self,event):
        self.stroke = self.stroke + 1
        #self.master.destroy()
        #c.unbind('<B1-Motion>', paint_id)
        print(self.stroke)
    
    def close(self):
        self.master.destroy()



    #def saveTemplate(self,templateName):
    #    with open("/home/moufdi/dollarlib/templates_file.json", "w") as templates_file:
    #        self.templates[templateName] = self.listFigurePoints
    #        json.dump(self.templates,templates_file)


#templateName = input("enter the name\n")
#createTemplate = CreateTemplate()
#createTemplate.loadJsonFile()
#createTemplate.setCanvasWindow(600,400)
#createTemplate.saveTemplate(templateName)

    
    









    

