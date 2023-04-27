class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print(f"Price: ${str(self.price)}")
        print(f"Max Speed: {str(self.max_speed)}mph")
        print(f"Miles: {str(self.miles)}")

    def ride(self):
        self.miles += 10
        print("Riding")
        return self
    
    def reverse(self):
        while self.miles != 0:
            self.miles -= 5
            print("Reversing")
            return self
        else:
            print("You've reached zero miles")
            return

bike_1 = Bike(1000, 160, 0)
bike_1.ride()
bike_1.ride()
bike_1.ride()
bike_1.reverse()
bike_1.displayInfo()

bike_2 = Bike(10000, 240, 0)
bike_2.ride()
bike_2.ride()
bike_2.reverse()
bike_2.reverse()
bike_2.displayInfo()

bike_3 = Bike(6000, 125, 0)
bike_3.reverse()
bike_3.reverse()
bike_3.reverse()
bike_3.displayInfo()
