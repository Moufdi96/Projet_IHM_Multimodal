class State(object):
    event = ''

    def __init__(self):
        print ('processing current state : ',str(self))
        pass
    
    def on_event(self,event):
        pass

    def action(self):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
