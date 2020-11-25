from tkinter import *
from createCanvas import CreateCanvas 
import json 

class LearnShape:

    def __init__(self):
        
        self.templates = []
        self.stroke = 0
        self.listFigurePoints = []
        self.color  ='red'
        
    def loadJsonFile(self):
        jsonText = ''    
        with open("/home/moufdi/dollarlib/templates_file.json", "r") as templates_file:
            #templates = json.load(templates_file)
            jsonText = templates_file.read()
            self.templates = json.loads(jsonText)

    def saveTemplate(self,templateName):
        with open("/home/moufdi/dollarlib/templates_file.json", "w") as templates_file:
            self.templates.append((self.listFigurePoints,templateName))
            json.dump(self.templates,templates_file)

templateName = ''
canvas = CreateCanvas()
learnShape = LearnShape()

while(templateName != 'stop'):
    templateName = input("enter the name\n")
    learnShape.loadJsonFile()
    canvas.setCanvasWindow(600,400)
    learnShape.saveTemplate(templateName)

    
    









    

