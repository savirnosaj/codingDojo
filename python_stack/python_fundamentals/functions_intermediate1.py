# Functions Intermediate I
# Create beCheerful().  Within it, print string "good morning!" 98 times.

#def beCheerful(name='', time='', repeat=1):
	#print(f"Good {time} {name}\n"*repeat)

#beCheerful(name="Sir", time="morning", repeat=98)

# As part of this assignment, please create a function randInt() where:
import random

# 1. creating_randInt() returns a random integer between 0 to 100
#def creating_randInt():
#    return int(random.random()*100)

#print(creating_randInt())

# 2. creating_randInt(max=50) returns a random integer between 0 to 50
#def creating_randInt(max=""):
#    result = 0
#    result = random.random()*max
#    return int(result)

#print(creating_randInt(max=50))

# 3. creating_randInt(min=50) returns a random integer between 50 to 100
#def creating_randInt(min="", max=""):
#    result = 0
#    result = random.random() * (max - min) + min
#    return int(result)

#print(creating_randInt(min=50, max=100))

# 4. creating_randInt(min=50, max=500) returns a random integer between 50 and 500
def creating_randInt(min="", max=""):
    result = 0
    result = random.random() * (max - min) + min
    return int(result)

print(creating_randInt(min=50, max=500))
