from dollarpy import Recognizer, Template, Point
import sys
from createCanvas import CreateCanvas 
from jsonFile_templates import*
from state import State
from ClientThread import*
import os
from tkinter import*

class ShapeReconizer(CreateCanvas):
     
    def __init__(self):
        CreateCanvas.__init__(self)
        self.client = ClientThread()
        #self.drawShape = CreateCanvas()
        button = Button(self.master, text="send",command=self.sendData)
        button.pack()
        self.templates = loadJsonFile()
        self.sampleNumber = 12
        self.temp = []
        self.cloud = []
        self.drawnFigure = []
        self.recognitionResult = []
        self.setCanvasWindow(600,400)
        
       

    def recognize_shape(self):
        for k in self.templates:   
            for p in k[0]:
                self.cloud.append(Point(p[0],p[1],p[2]))
                #print(points)
            self.temp.append(Template(k[1],self.cloud))
        #print(temp)

        for k in self.listFigurePoints:
            self.drawnFigure.append(Point(k[0],k[1],k[2]))

        recognizer = Recognizer(self.temp)
        self.recognitionResult = recognizer.recognize(self.drawnFigure,n=self.sampleNumber)
        

    def sendData(self):
        
        self.recognize_shape()
        if(len(self.recognitionResult[0])>=0):
            self.client.send(self.recognitionResult[0])
            self.canvasWindow.delete("all")





