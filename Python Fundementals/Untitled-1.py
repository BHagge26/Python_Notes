
import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}') 


if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')


drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

drawers.append("records")
print(drawers)


my_list = [1,5,2,8,4,3,477,53,4,6,7,878867,45,5563,335,223,5,64,64,56,99]
my_list.pop(2)
my_list.sort() 
print(my_list)


my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])



    
for x in my_list:
    print(x)
for count in range(0,5):
    print("looping =", count)


for x in range(0, 10, 2):
    print(x)

for x in range(5, 1, -3):
    print(x)

class: user 






# declare a class and give it name User
class User:
    def __init__(self):
        self.first_name = "Branden"
        self.last_name = "Hagge"
        self.age = 30
        self.DOB = 4-20-1992
        self.birth_city = "Valencia"


Branden = User()
print(Branden)


# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

user_ada = User 


class User:
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

user_ada = User()
print(user_ada)

