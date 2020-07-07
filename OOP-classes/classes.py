
# class house
class House:
                #defining attributes
    def __init__(self, number_of_bathroom, number_of_bedroom):
        #default attributes 
        self.number_of_floors = 2
        self.kitchen = 1
        #self points to the class object itself
        self.bathrooms = number_of_bathroom
        self.bedrooms = number_of_bedroom
        self.has_pool = False
        self.num_furniture = 0
    # method add pool
    def add_pool(self):
        self.has_pool = True
    # method add furniture
    def add_furniture(self, count):
        self.num_furniture += count
        return self
# objects are instances of House class
dream_house1 = House(2,3)
dream_house2 = House(1,2)
dream_house3 = House(3,4)
# print(dream_house1.bedrooms)
# print(dream_house2.bedrooms)
# print(dream_house2.backyard)
# print((dream_house1.bedrooms) - (dream_house2.bedrooms))
dream_house1.ad_pool();
print(dream_house1.has_pool)
print(dream_house2.has_pool)

dream_house1.add_furniture(2)       # 2
print(dream_house1.num_furniture)
dream_house1.add_furniture(3)       # 5
print(dream_house1.num_furniture)

# CHAINING
dream_house2.add_furniture(4).add_furniture(4).add_furniture(4)
print(dream_house2.num_furniture)

#dream_house2.add_furniture(4).add_furniture(4).add_furniture(4).add_pool(1)
#won't return the add_pool doesn't return self

""" print all in class """
print(dream_house1.__dict__)


print('='*80)
# class User:		# declare a class and give it name User
#     def __init__(self): #__init__, which method is called when a new object is instantiated.
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0


# guido = User()
# print(guido.name)       #the name still Michael
# guido.name = "Guido"    #Guido name assigned

# monty = User()
# monty.name = "Monty"    #Monty name assigned

# print(guido.name)
# print(monty.name)

# class BankClient:
#     def __init__(self, username, email_address):# now our method has 2 parameters!
#         self.name = username			# and we use the values passed in to set the name attribute
#         self.email = email_address		# and the email attribute
#         self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
#     def make_deposit(self, amount): 	# takes an argument that is the amount of the deposit
#         self.account_balance += amount	# the specific user's account increases by the amount of the value received       
# yuriy = BankClient("yuriy kozak", "ykozak@gmail.com")
# yuriy.account_balance = 1290000
# print(yuriy.account_balance)
# print(yuriy.email)
# print(f"{yuriy.name} is making $1mln deposit")
# yuriy.make_deposit(1000000)
# print(yuriy.account_balance)
d
