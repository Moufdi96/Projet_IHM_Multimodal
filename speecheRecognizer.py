import speech_recognition as sr
from state import State
from ClientThread import*
import threading
    
class VoiceRecognizer:
    State.event = 'create'

    def __init__(self):
        self.client = ClientThread()
        self.r = sr.Recognizer()
        self.speech = ''
        self.recognitionResult = ''
        self.dictionary = ["draw","click","clear","delete","delete all","right","left","up","middle","down","red","white","green","pink","create","create here","create this here",
        "create that here","create that shape","create shape here","create this shape",
        "create that shape here","create the shape here","in the right","in the left","in the middle"]

    def recognize_voice(self):
        
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            print("\n")
            print("Microphone activated...") 
            print("Recognizing what's been said...") 
            audio = self.r.listen(source,phrase_time_limit=3)
            try:
                self.recognitionResult = self.r.recognize_google(audio)
                print('You said : {}'.format(self.recognitionResult))
                print("\n")
            except:
                print("please say it again !")

    def sendData(self):
        
        while(True):
            if(self.recognitionResult in self.dictionary):
                self.client.send(self.recognitionResult)
                self.recognitionResult = ''

            
    def startVoiceReco(self):
        new_thread = threading.Thread(target=self.sendData)
        new_thread.start() 
        while(True):
            self.recognize_voice()
          
            

