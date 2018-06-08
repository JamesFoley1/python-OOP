class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
            

    def displayAll(self):
        print("Price: "+str(self.price))
        print("Speed: "+str(self.speed)+" mph")
        if self.fuel <= 5:
            print("Fuel: Empty")
        elif self.fuel >= 5 and self.fuel <=12:
            print("Fuel: Not full")
        elif self.fuel >= 12 and self.fuel <= 18:
            print("Fuel: Kind of Full")
        elif self.fuel >= 18:
            print("Fuel: Full")
        print("Mileage: "+str(self.mileage)+" mpg")
        if self.price >= 10000:
            self.tax = 0.15
            print("Tax: "+str(self.tax))
        else:
            self.tax = 0.12
            print("Tax: "+str(self.tax))
        


car1 = Car(2000, 35, 18, 15)
car1.displayAll()

car2 = Car(2000, 5, 8, 105)
car2.displayAll()

car3 = Car(2000, 15, 15, 95)
car3.displayAll()

car4 = Car(2000, 25, 18, 25)
car4.displayAll()

car5 = Car(2000, 45, 18, 25)
car5.displayAll()

car6 = Car(20000000, 35, 0, 15)
car6.displayAll()