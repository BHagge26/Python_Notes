info1 = {
    "first_name": "Branden",
    "last_name" : "hagge",
    "email" : "bhagge26@gmail.com",
    "age" : 30
}

info2 = {
    "first_name": "Sally",
    "last_name" : "May",
    "email" : "redriver@gmail.com",
    "age" : 24
}

info3 = {
    "first_name": "Derell",
    "last_name" : "Johnson",
    "email" : "mooselodge@gmail.com",
    "age" : 39
}



class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        

    def display_info(self):
            print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
            return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

user1 = User("Branden", "Hagge", "bhagge26@", 30 )
user2 = User("Lindsey", "Lohan", "marstraveler26@", 30 )
user3 = User("Alex", "Makechef", "doglover4626@", 30 )

user1.enroll()
user1.spend_points(50)
user1.display_info()

user2.enroll()
user2.spend_points(80)
user2.display_info()

user3.enroll()
user3.spend_points(180)
user3.display_info()



user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
