#from my_states import Geste_State
from my_states import*
from serverThread import*

serverThread = ServerThread()
currentState = Idle()
new_thread = threading.Thread(target=serverThread.startServer)
new_thread_fusion = threading.Thread(target=Idle.fusion.action)
new_thread.start()
new_thread_fusion.start()
event = ''

while(True):
    while(ServerThread.data == ""):
        pass
    event = serverThread.data
    currentState = currentState.on_event(event)
    currentState = currentState.action(event)
    ServerThread.data = ""