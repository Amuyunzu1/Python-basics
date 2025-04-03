class BankAccount:
    def __init__(self, owner, balance):  # Fixed method name (double underscores)
        self.owner = owner
        self.__balance = balance  # Private attribute (cannot be accessed directly)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance  # Access private attribute using a method

# Creating an account object
account = BankAccount("John Doe", 1000)
print(f"Account owner: {account.owner}")
print(f"Initial balance: {account.get_balance()}")
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # This should show "Insufficient funds!"

# Creating an account object

# class Animal:
#     def __init__(self, name):  
#         self.name = name

#     def make_sound(self):
#         print("Some generic sound")

# # Child class inheriting from Animal
# class Dog(Animal):
#     def make_sound(self):  # Method Overriding
#         print("Woof! Woof!")

# # Create objects
# generic_animal = Animal("Generic")
# generic_animal.make_sound()  # Output: Some generic sound

# dog = Dog("Buddy")
# dog.make_sound()  # Output: Woof! Woof!

# class Bird:
#     def fly(self):
#         print("Some birds can fly")

# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow flies fast")

# class Penguin(Bird):
#     def fly(self):
#         print("Penguins cannot fly!")

# # Using polymorphism
# for bird in [Sparrow(), Penguin(), Bird()]:
#     bird.fly()

# Abstract class

# class BankAccount:
#     def __init__(self, owner, balance):  # Fixed method name (double underscores)
#         self.owner = owner
#         self.__balance = balance  # Private attribute (cannot be accessed directly)

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited: {amount}, New Balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient funds!")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew: {amount}, Remaining Balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance  # Access private attribute using a method

# # Creating an account object
# account = BankAccount("John Doe", 1000)
# print(f"Account owner: {account.owner}")
# print(f"Initial balance: {account.get_balance()}")
# account.deposit(500)
# account.withdraw(200)
# account.withdraw(2000)  # This should show "Insufficient funds!"

# Creating an account object

# polymorphism 
class Animal:
     def __init__(self, name):  
         self.name = name

     def make_sound(self):
         print("Some generic sound")

# Child class inheriting from Animal
class Dog(Animal):
     def make_sound(self):  # Method Overriding
         print("Woof! Woof!")

 # Create objects
generic_animal = Animal("Generic")
generic_animal.make_sound()  # Output: Some generic sound

dog = Dog("Buddy")
dog.make_sound()  # Output: Woof! Woof!

class Bird:
     def fly(self):
         print("Some birds can fly")

class Sparrow(Bird):
     def fly(self):
         print("Sparrow flies fast")

class Penguin(Bird):
     def fly(self):
         print("Penguins cannot fly!")

 # Using polymorphism
for bird in [Sparrow(), Penguin(), Bird()]:
    bird.fly()

# # Abstract class

# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):
#     def __init__(self, name):  

#     @abstractmethod
#     def start(self):
#         pass  # Abstract method (must be implemented by subclasses)

#     @abstractmethod
#     def stop(self):
#         pass  # Abstract method (must be implemented by subclasses)

# # Concrete class (inheriting from Vehicle)
# class Car(Vehicle):
#     def start(self):
#         print(f"{self.name} is starting with a key.")

#     def stop(self):
#         print(f"{self.name} is stopping by applying brakes.")

# # Another concrete class
# class Bike(Vehicle):
#     def start(self):
#         print(f"{self.name} is starting with a self-start button.")

#     def stop(self):
#         print(f"{self.name} is stopping using disc brakes.")

# # Create objects
# my_car = Car("Toyota")
# my_bike = Bike("Yamaha")

# my_car.start()  # Output: Toyota is starting with a key.
# my_car.stop()   # Output: Toyota is stopping by applying brakes.

# my_bike.start() # Output: Yamaha is starting with a self-start button.
# my_bike.stop()  # Output: Yamaha is stopping using disc brakes.