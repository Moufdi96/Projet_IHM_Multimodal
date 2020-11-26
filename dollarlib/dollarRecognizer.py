from dollarpy import Recognizer, Template, Point
import sys
sys.path.append("/home/moufdi/dollarlib")
from createCanvas import CreateCanvas 
from jsonFile_templates import*


drawShape = CreateCanvas()
templates = loadJsonFile()
sampleNumber = 12
temp = []
cloud = []
drawnFigure = []

for k in templates:   
    for p in k[0]:
        cloud.append(Point(p[0],p[1],p[2]))
        #print(points)
    temp.append(Template(k[1],cloud))
#print(temp)

drawShape.setCanvasWindow(600,400)

for k in drawShape.listFigurePoints:
    drawnFigure.append(Point(k[0],k[1],k[2]))

recognizer = Recognizer(temp)
result = recognizer.recognize(drawnFigure,n=sampleNumber)
print(result)



