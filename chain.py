#Assignment: Chaining Methods
# For this assignment you will create the user class and add a couple of methods!

class User:
    def __init__(self, first_name, last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_reward_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Available Points: {self.gold_reward_points}")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print('Already a member')
            return False
        
        self.is_rewards_member = True
        self.gold_reward_points = 200
        return self

    def spend_points(self,amount):
        if self.gold_reward_points < amount:
            "Insufficient Points"
            return 
        self.gold_reward_points -= amount 
        return self

    


my_user = User("Alexander","Borges","borges2721@gmail.com",31)
my_user.display_info().enroll().display_info().spend_points(150).display_info()
#my_user.enroll()
#my_user.display_info()
#my_user.spend_points(150)
#my_user.display_info()