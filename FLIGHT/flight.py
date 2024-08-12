class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
        
    def add_passenger(self, name):
        if not self.counter():
            return False
       
        self.passenger.append(name)
        return True
        
    def counter(self):
        return self.capacity - len(self.passenger)
    


    