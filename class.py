class Announce():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
    def add_passenger(self, name):
        if not self.cheaker():
            return False
        self.passenger.append(name)
        return True
    
    def cheaker(self):
       return self.capacity - len(self.passenger)
    
f = Announce(3)

names = ['john', 'sandra', 'kyle', 'lax', 'jewel']

for name in names:
    success = f.add_passenger(name)
    if success:
        print(f"{name} is added")
    else:
        print(f"the sit is full, {name} is not added")
