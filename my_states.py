from state import State
from dollarRecognizer import ShapeReconizer
#from pynput.mouse import Listener
from speecheRecognizer import VoiceRecognizer
from drawInCanvas import*
#from ivy.std_api import*
from serverThread import*
import threading
import socket
import sys
import time


serverThread = ServerThread()
shapes = ["rectangle","cercle","line","triangle"]
colors = ["red","white","green","pink"]
sound = ["draw","create","delete all","create here","create this here",
        "create that here","create shape here","create this shape here",
        "create this shape","create the shape"]
positions = ["in the right","in the left","in the middle","right","left","up","down","middle"]

clear = ["clear","delete"]
class Fusion_State(State):
    def __init__(self):
        State.__init__(self)
        self.fusionData = {'gesture':'','soundCreate':'','color':'','soundPosition':''}
        self.clickPosition = []
        self.canvas = None
        self.canvasOpen = False
    def on_event(self,event):
        return Idle()

    def action(self):
        
        while(True):
            gesture = Idle.fusion.fusionData.get('gesture')
            color = Idle.fusion.fusionData.get('color')
            soundCreate = Idle.fusion.fusionData.get('soundCreate')
            soundPosition = Idle.fusion.fusionData.get('soundPosition')
            
            soundCreate
            if(len(gesture) != 0 and len(color) != 0 and len(soundCreate) != 0):
                if(self.canvas == None and self.canvasOpen == False):
                    self.canvasOpen = True
                    self.canvas = canvasResult()
                    self.canvas.setCanvasWindow(800,600,gesture,color,soundPosition)
                    ServerThread.data = "click"
            


class Idle(State):
    fusion = Fusion_State()
    def on_event(self,event):
        if(event in sound):
            return Creer_State()
        elif (event in shapes):
            return Geste_State(self)
        elif (event == "click"):
            return Click_Position_State(self)
        elif (event in ["clear","Clear"]):
            return Supression_State()
        return self
    
    def action(self,TODO):
        for key in Idle.fusion.fusionData:
            Idle.fusion.fusionData[key] = ''
        Idle.fusion.canvasOpen = False
        return self
        
    
        
class Geste_State(State):
    def __init__(self,previousState):
        State.__init__(self)
        self.previousState = previousState

    def on_event(self,event):
        if (event in clear):
            return Supression_State()
        
    
    def action(self,gesture):
        Idle.fusion.fusionData['gesture'] = gesture
        print("fusion state {}".format(Idle.fusion.fusionData))
        return self.previousState          

class Creer_State(State):
    def on_event(self,event):
        if(event in shapes):
            return Geste_State(self)
        elif (event in colors):
            return Couleur_State()
        elif (event == "click"):
            return Click_Position_State(self)
        elif (event in positions):
            return Son_Position_State()
        elif (event in clear):
            return Supression_State()
        return self
    
    def action(self,soundCreate):
        Idle.fusion.fusionData['soundCreate'] = soundCreate
        print("fusion state {}".format(Idle.fusion.fusionData))
        return self

class Couleur_State(State):
    def on_event(self,event): 
        if(event in shapes):
            return Geste_State(self)
        elif (event == "click"):
            return Click_Position_State(self)
        elif(event in positions):
            return Son_Position_State()    
        elif (event in clear):
            return Supression_State()    
        return self
    
    def action(self,color):
        Idle.fusion.fusionData['color'] = color
        print("fusion state {}".format(Idle.fusion.fusionData))
        return self


class Son_Position_State(State):
    def on_event(self,event):
        if(event in shapes):
            return Geste_State(self)
        elif (event == "click"):
            return Click_Position_State(self)
        #elif (event in "fusion"):
            #return Fusion_State()
        elif (event == "feedback"):
            return Feedback()
        elif (event in clear):
            return Supression_State()
        elif (event in colors):
            return Couleur_State()
        return self
    
    def action(self,soundPosition):
        Idle.fusion.fusionData['soundPosition'] = soundPosition
        print("fusion state {}".format(Idle.fusion.fusionData))
        return self

class Click_Position_State(State):
    def __init__(self,previousState):
        State.__init__(self)
        self.previousState = previousState
    def on_event(self,event):
        if (event in clear):
            return Supression_State()

    def action(self,clickPosition):
        return self.previousState

class Supression_State:
    def __init__(self):
        State.__init__(self)

    def on_event(self,event):
        pass

    def action(self,event):
        Idle.fusion.canvas.canvasWindow.delete("all")
        for key in Idle.fusion.fusionData:
            Idle.fusion.fusionData[key] = ''
        Idle.fusion.canvasOpen = False
        return Idle()

class Move_Shape: #TODO
    def __init__(self):
        State.__init__(self)

    def on_event(self,event):
        pass

    def action(self,event):
        pass
    

class Feedback(State):
    def on_event(self,event):
        return Idle()

    def action(self,TODO):
        return self
    
    
        