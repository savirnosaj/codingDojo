# Assignment: Car

# Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string.
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.variable_to_store_price = price
        self.variable_to_store_speed = speed
        self.variable_to_store_fuel = fuel
        self.variable_to_store_mileage = mileage
        self.tax = 0.12
        if self.variable_to_store_price > 10000:
            self.tax = 0.15
        Car.display_all(self)
    
    def display_all(self):
        print("*"*30)
        print(f"Price: ${self.variable_to_store_price}")
        print(f"Speed: {self.variable_to_store_speed}mph")
        print(f"Fuel: {self.variable_to_store_fuel}")
        print(f"Milage: {self.variable_to_store_mileage}mpg")
        print(f"Tax: {self.tax}")

car_1 = Car(2000, 35, "Full", 15)
car_2 = Car(2000, 5, "Not Full", 105)
car_3 = Car(2000, 15, "Kind of Full", 95)
car_4 = Car(2000, 25, "Full", 25)
car_5 = Car(2000, 45, "Empty", 25)
car_6 = Car(20000000, 35, "Empty", 15)
