class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # @classmethod
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member Status: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        return self

    # @classmethod
    def enroll(self):
        if(self.is_rewards_member == True):
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(self.is_rewards_member)
            print(self.gold_card_points)
        return self

    # @classmethod
    def spend_points(self,points):
        if(points < self.gold_card_points):
            self.gold_card_points -= points
            print(self.gold_card_points)
        else:
            print("Not enough points!")
        return self

user_1 = User("Mark", "Jacobs","mjacobs@gmail.com",33)
user_2 = User("Marc","Anthony","manthony@gmail.com",54)
user_3 = User("Daisy","Ridley","dridley@gmail.com",31)

user_1.display_info().enroll().enroll().spend_points(201).spend_points(50)
user_2.enroll().spend_points(80).display_info()
user_3.display_info().spend_points(40)