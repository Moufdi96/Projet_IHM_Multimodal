from createCanvas import CreateCanvas 
from jsonFile_templates import* 
 
#class LearnShape:
#
#    def __init__(self):
#        
#        self.templates = []
#        self.stroke = 0
#        self.listFigurePoints = []
#        
#        
#    def loadJsonFile(self):
#        jsonText = ''    
#        with open("/home/moufdi/dollarlib/templates_file.json", "r") as templates_file:
#            #templates = json.load(templates_file)
#            jsonText = templates_file.read()
#            self.templates = json.loads(jsonText)

#    def saveTemplate(self,templateName):
#        with open("/home/moufdi/dollarlib/templates_file.json", "w") as templates_file:
#            self.templates.append((self.listFigurePoints,templateName))
#            json.dump(self.templates,templates_file)

templateName = ''
canvas = CreateCanvas()
 
while(templateName != 'stop'):
    templateName = input("enter the name\n")
    templates = loadJsonFile()
    canvas.setCanvasWindow(600,400)
    listFigurePoints = canvas.listFigurePoints
    saveTemplate(templates,listFigurePoints,templateName)

    
    









    

