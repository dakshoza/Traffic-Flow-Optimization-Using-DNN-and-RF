class TrafficSignal:
    def __init__(self):
        self.state = 0 # 0 - red, 1 - green
    
    def changeState(self):
        if self.state:
            self.state = 0
        else:
            self.state = 1
        
        print(self.state)
            
            
A0 = TrafficSignal()
A1 = TrafficSignal()
A2 = TrafficSignal()
A3 = TrafficSignal()
B0 = TrafficSignal()
B1 = TrafficSignal()
B2 = TrafficSignal()
