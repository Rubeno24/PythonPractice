class Car_Class:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")
    
    def stop(self):
        print("This car is stopped")

    def repaint(self,color):
        self.color=color

    def print(self):
        print("Car Make:",self.make)
        print("Car Model:",self.model)
        print("Car Year:",self.year)
        print("Car Color:",self.color)
        