#loops

#FOR
#for ____ in ____:

#Blank #1 iterative variable -- will mean different thing for different data types
#blank 2 -- sequence or collection that you are iterating over
"""
start -- stop -- step
stop is required, exclusive
step is how much you incriment by -- can be positive or negativbe
"""


#for i in range(100,0,-10):
#    print(i)

foods = ['pizza','nachos', 'sushi','orange chicken','sushi']

for one_food in foods:
    print(one_food)

print(foods)

for i in range(len(foods)):
    print(foods[i])
    foods[i]

print(foods)

cat1 = {
    'name': 'cinnamon',
    'age': 2,
    'color': 'orange'
}

cat2 = {
    'name': 'Binx',
    'age': 2,
    'color': 'black'
}

for key in cat1:
    print(f'The Key is {key} and the value is {cat1[key]}')

for key, val, in cat1.items():
    print(f'the key is {key} the value is {val}')

    list_of_cats = [cat1,cat2]
    name = list_of_cats[1]['name']
    for cat_dict in list_of_cats:
        for key in cat_dict:
            print(f'the key is {key} the value is {cat_dict[key]}')

"""
while(condition):
    pass
"""

x = 5
while (x > 0):
    print(x)
    x-= 1

#Functions
def function_name(paramter_1,parameter2):
    #logic
    return

def multiply(num_1, num_2):
    return num_1 * num_2

print(multiply(10,20))


#MAKING CHANGES 