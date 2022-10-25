# What is OOP?
# Creating objects in our code using clases, attributes, and methods?
# grouping data functionality together into one single entity called an 'object'
#what is a class?
#--

dog_1 = {
    "name": "spot",
    "age": 3,
    "breed": "Corgi"
}

dog_2 = {
    "name": "Buster",
    "age": 2,
    "breed": "Dalmation"
}

class Dog:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']

    def bark(self):
        print(f"{self.name} makes a loud bark")
        return self

    def __repr__(self) -> str:
        return f"{self.name} is a dog object {self.age} {self.breed}"

    def birthday(self):
    self.age += 1,
    


dog_3 = Dog(dog_1)


print(dog_3)


dog_3.bark().bark().bark()



#blue prints
#what is an attribute

#--characteristic of our object, sp,e [iece of data we are tracking about our object]
#what is a method?