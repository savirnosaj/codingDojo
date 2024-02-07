# Objectives:
# Start coding in Python right away
# Learn how to use basic for loop statements in Python
# Start implementing some basic algorithms in Python

# Create a python file called for_loop_basic1.py that performs the following tasks:

# 1. Basic - Print all the numbers/integers from 0 to 150
# for count in range(0,151):
#    print(count)

# 2. Mulitples of Five - Print all the multiples of 5 to 1,000
#count = 0
#for i in range(5):
#    count = count + 5
#    print(count)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print "Dojo".
#for count in range(1, 101):
#    if count % 10 == 0:
#        print("Coding")
#        print("Dojo")#
#    elif count % 5 == 0:
#        print("Coding")
#    else:
#        print(count)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500, and print the final sum.
#sum = 0
#for count in range(501):
#    if count % 2 == 1:
#        sum += count
#    else:
#        continue
#print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
#count = 2018
#sum = 0
#while count > 0:
#    if count % 2 == 0:
#        sum += count
#        count -= 4
#    else:
#        continue
#print(sum)

# 6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop. For (2, 9, 3), print 3 6 9 (on successive lines).
#for count in range(2, 10):
#    if count % 3 == 0:
#        print(count)
#    else:
#        continue

# A common mistake?
# Now, please predict the output for the following codes.

# 1.
#list = [3,5,1,2]
#for i in list:
#    print(i)

# Prediction: 3, 5, 1, 2

# 2.
#list = [3,5,1,2]
#for i in range(list):
#    print(i)

# Prediction: 4
# error returned; "'list' cannot be interpreted as an integer"
# range only works with integers, not arrays

# 3.
# list = [3,5,1,2]
# for i in range(len(list)):
#     print(i)

# Prediction: 0, 1, 2, 3
