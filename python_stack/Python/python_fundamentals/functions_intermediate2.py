# Functions Intermediate II

# 1. Given -
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1a. How would you change the value 10 in x to 15?
#     Once you're done x should then be [ [5,2,3], [15,8,9] ].

#print(z)
#z[0]['x'] = 15
#print(z)

# 1b. How would you change the last_name of the first student from 'Jordan' to "Bryant"?

#print(students[0])
#students[0]['last_name'] = 'Bryant'
#print(students[0])

# 1c. For the sports_directory, how would you change 'Messi' to 'Andres'?

#print(sports_directory['soccer'])
#sports_directory['soccer'][0] = 'Andres'
#print(sports_directory['soccer'])

# 1d. For z, how would you change the value 20 to 30?

#print(z[0])
#z[0]['y'] = 30
#print(z[0])

#

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list
#    and prints each key and the associated value.

#def iterateDictionary(students):
#    for count in range(len(students)):
#        for keyVal in students[count]:
#            print(keyVal + " - " + students[count][keyVal])

#iterateDictionary([{'first_name':  'Michael', 'last_name' : 'Jordan'},
#    {'first_name' : 'John', 'last_name' : 'Rosales'},
#    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#    {'first_name' : 'KB', 'last_name' : 'Tonel'}])

#

# 3. Create a function that given a list of dictionaries and a key name,
#    it outputs the value stored in that key for each dictionary.

#def iterateDictionary2(students):
#    for count in range(len(students)):
#        for keyVal in students[count]:
#            if len(keyVal) % 2 == 0:
#                print(students[count][keyVal])
#            else:
#                continue

#iterateDictionary2([{'first_name':  'Michael', 'last_name' : 'Jordan'},
#    {'first_name' : 'John', 'last_name' : 'Rosales'},
#    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#    {'first_name' : 'KB', 'last_name' : 'Tonel'}])

#

# 4.  Say that 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#     Create a function that prints the name of each location and also how many locations the Dojo currently has.
#     Have the function also print the name of each instructor and how many instructors the Dojo currently has.

def printDojoInfo(dojo):
    for count in dojo:
        sum = 0
        for val in dojo[count]:
            print(val)
            sum += 1
        print(sum)

printDojoInfo(dojo)
