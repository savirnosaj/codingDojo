# Math Dojo

# Create a Python class called MathDojo that has the methods add and subtract.
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md.
# It should be able to do the following task:

# x = md.add(2).add(2,5,1).subtract(3,2).result()
# print(x) # should print 5

class md():
  def add(self, *args):
    for count in args:
      self += count
    return self
  def subtract(self, *args):
    for count in args:
      self -= count
    return self

x = md.add(2,5,1)
print(x) # should print 8

class CalculatorFunctions():
  def sum(self):
    print("Sum called")
    return self
  def difference(self):
    print("Difference called")
    return self
  def product(self):
    print("Product called")
    return self
  def quotient(self):
    print("Quotient called")
    return self
   
calculator = CalculatorFunctions() 
# Chaining all methods of CalculatorFunctions 
calculator.sum().difference().product().quotient()
