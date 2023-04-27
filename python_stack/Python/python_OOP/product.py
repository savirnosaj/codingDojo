# Assignment: Product

# The owner of a store wants a program to track products.
# Create a product class to fill the following requirements.

# Attributes:

    # Price
    # Item Name
    # Weight
    # Brand
    # Status: default "for sale"

class Product:
    def __init__(self, price, item_name, weight_measurement, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.weight_measurement = weight_measurement
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        Product.add_Tax(self)
        self.status = "Sold"
        print("*"*20)
        print(f"Status Update for {self.item_name}: **{self.status}**")
        Product.display_Info(self)
        return self

    def add_Tax(self):
        self.price = ((self.price / 100) * 5) + self.price
        return self
    
    def return_Item(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason == "like new":
            self.status = "For Sale"
            self.price = self.price - ((self.price / 100) * 5) # need assistance with the math to solve this correctly
            print(f'{self.item_name} has been returned as: "{reason}"')
        elif reason == "opened":
            self.status == "Used"
            self.price = self.price - ((self.price * 20) / 100)
            print("*"*20)
            print(f'{self.item_name} has been returned as: "{reason}"')

        Product.display_Info(self)
        return self
    
    def display_Info(self):
        if self.status == "For Sale" or self.status == "Used":
            print("*"*20)
            print(f"Item: {self.item_name}")
            print(f"Price: ${self.price}")
            print(f"Weight: {self.weight} {self.weight_measurement}")
            print(f"Brand: {self.brand}")
        elif self.status == "Sold":
            print(f"Total: ${self.price}")
            print(f"Weight: {self.weight} {self.weight_measurement}")
            print(f"Brand: {self.brand}")
        elif self.status == "Defective":
            print("*"*20)
            print("No longer available:")
            print(f"{self.item_name} has been marked as: {self.status}")

product_1 = Product(60, "Super Smach Bros. Ultimate", "ounces", 1.80, "Nintendo")
product_1.display_Info() # run mandatory to see changes with methods being run
product_1.sell() # run mandatory to see changes with methods being run

#product_1.return_Item("defective")
#product_1.return_Item("like new")
#product_1.return_Item("opened")
