# This is my comment
"""
I can type what i want on 
multiple lines

"""

snake_case = "all lower cqase, seperated by undercores"
print("hello") 
GLOBAL_VAR = 'ALL CAPS'

#Primitive

#Composite

inter = 6
float_num = 6.8

#booleans

#strings
"A collection of characters"
format_str = f"now we can put variables in this {inter}"
print(format_str)
concat_str = "concat var" + str(inter)
print(concat_str)

#composite
"""
list --- a collection of elements accessed by index
dictionaries-----
tuples
"""
list = [1,2,3,4,5,6,7,8]
print(list)

# list functions
len(list)
#returns length of the list
min(list) # minimum
max(list) # maximum

list.append(393)
print(list)

#dictionaires
# a sequence of key value pairs
#unindexed

dict = {
    'name': 'Buster',
    'age' : 3,
    'breed' : 'Golden Retreiver'
}

print(dict['name'])
dict['color'] = 'Goldenrod'

print(dict)

if "color" in dict:
    print(dict['color'])
else:
    print("key not found")

dict.clear()

list.pop(3)


x = 8 
if x == 5:
    print("whats up man")
elif x < 5:
    print("here we go bois")
else:
    print("guessnot")

"""
None instead of null
not instead of !
or instead of ||
and instead of &&
is vs ==
== vs ===
"""