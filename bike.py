class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print("This bike's price is "+str(self.price))
        print("The maximum speed of this bike is "+str(self.max_speed)+" mph")
        print("Total miles: "+str(self.miles))
    
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing")
        if self.miles >= 5:
            self.miles -= 5
        return self


bike1 = Bike(200, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(19.95, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(900, 45)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()