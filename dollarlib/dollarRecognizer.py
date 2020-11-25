from dollarpy import Recognizer, Template, Point
import matplotlib.pyplot as plt
import json
import sys
sys.path.append("/home/moufdi/dollarlib")

from createCanvas import CreateCanvas 


drawShape = CreateCanvas()
drawShape.loadJsonFile()

temp = []
cloud = []
for k in testShape.templates:   
    for p in k[0]:
        cloud.append(Point(p[0],p[1],p[2]))
        #print(points)
    
    temp.append(Template(k[1],cloud))
#print(temp)

testShape.setCanvasWindow(600,400)

drawnFigure = []
for k in testShape.listFigurePoints:
    #print(k[0])
    #print(k[1])
    #plt.plot(k[0]/100,k[1]/100,'.')
    drawnFigure.append(Point(k[0],k[1],k[2]))

#plt.show()



# Define 'Template' gestures, each consisting of a name and a list of 'Point' elements.
# These 'Point' elements have 'x' and 'y' coordinates and optionally the stroke index a point belongs to.

# Create a 'Recognizer' object and pass the created 'Template' objects as a list.
#print('cloud samples')

recognizer = Recognizer(temp)

# Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.

#points_test = [] 
#for i in range(len(listFigurePointsX)):
#    points_test.append(Point(listFigurePointsX[i],listFigurePointsY[i]))
#print(len(drawnFigure))
result = recognizer.recognize(drawnFigure,n=12)
print(result)



