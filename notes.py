#Object Oriented Notes 5/21
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 =param1
        self.param2 = param2
    
    def some_method(self):
        print(self.param1)
mylist = [1,2,3]

#constructors with parameters given at use. can hold multiple of
#  anything
class Dog():
    #class object attribute
    #same for any instance of a class
    species = "mammal"

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        #boolean expected
        self.spots = spots
    #OPERATIONS / ACTIONS ----> 'METHOD'

    def bark(self,number):
        print("WOOF! MY NAME IS {} and the number is {}".format(self.name,number))



my_dog = Dog(breed = 'epic',name = 'Gamer', spots = True)
print(my_dog.breed)
my_dog.bark(10)


class Circle():
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    #Method
    def get_circumference(self):
        return self.radius * Circle.pi *2
epicCircle = Circle(420)
print(epicCircle.area,'\n',epicCircle.radius,'\n',epicCircle.get_circumference())

###part 4###
mylist = [1,2,3]
len(mylist)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
booky = Book('How to be epic', 'Fortnite', 420)
print(booky)
print(len(booky)," pages")


class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"Account owner:     {self.name}\nAccount balance:      {self.balance}"  
    def add_money(self,plus): 
        self.balance = plus + self.balance
        return "Accepted"
    def withdraw_money(self,minus):
        if self.balance - minus < 0:
            print("Insufficient funds.")
        else: 
            self.balance = self.balance - minus
            return "Accepted"

acct1 = Account('Ivan',100)
print(acct1)
print(acct1.balance)
acct1.withdraw_money(69)
acct1.add_money(420)
print(acct1.balance)
acct1.withdraw_money(6969)
print(acct1.balance)
acct1.add_money(9001)
print(acct1)
##EXCEPTION HANDLING##
def ask_int():

    while True:
        try:
            result = int(input("Enter a number"))
        except:
            print("That's not a number")
            continue
        else: 
            print("Yes thanks")
            break
        finally:
            print("End of try/except/finally statement")
            print("This always runs")