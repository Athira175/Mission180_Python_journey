class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def display_vechicle(self):
        print("Brand:",self.brand)

class car(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model
    def display_car(self):
        self.display_vechicle()
        print("Model:",self.model)
car1=car("Toyota","Corolla")
car1.display_car()