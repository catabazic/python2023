# ---------------------------------- Execrcitiul 1

import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# ---------------------------------- Execrcitiul 2

class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} credited to the account.")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")


# ---------------------------------- Execrcitiul 3

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def calculate_mileage(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"{self.towing_capacity} pounds"


# ---------------------------------- Execrcitiul 4

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}")

    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id)
        self.salary = salary
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print(f"Position: Manager\nSalary: ${self.salary}\nBonus: ${self.bonus}")

    def calculate_salary(self):
        return self.salary + self.bonus


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, technical_skill_level):
        super().__init__(name, employee_id)
        self.salary = salary
        self.technical_skill_level = technical_skill_level

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer\nSalary: ${self.salary}\nTechnical Skill Level: {self.technical_skill_level}")

    def calculate_salary(self):
        return self.salary + (self.technical_skill_level * 1000)


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission_rate, sales_amount):
        super().__init__(name, employee_id)
        self.salary = salary
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount

    def display_info(self):
        super().display_info()
        print(
            f"Position: Salesperson\nSalary: ${self.salary}\nCommission Rate: {self.commission_rate}%\nSales Amount: ${self.sales_amount}")

    def calculate_salary(self):
        return self.salary + (self.commission_rate / 100 * self.sales_amount)


# ---------------------------------- Execrcitiul 5

class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

    def move(self):
        print(f"{self.name} is moving.")


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

    def make_sound(self):
        print(f"{self.name} makes mammal sounds.")


class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        super().__init__(name, habitat)
        self.feather_color = feather_color

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

    def make_sound(self):
        print(f"{self.name} sings a bird song.")


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def lay_eggs(self):
        print(f"{self.name} is laying eggs in the water.")

    def make_sound(self):
        print(f"{self.name} makes bubbling sounds.")


# ---------------------------------- Execrcitiul 6

class LibraryItem:
    def __init__(self, title, item_id, is_checked_out=False):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = is_checked_out

    def display_info(self):
        print(f"Item ID: {self.item_id}\nTitle: {self.title}\nChecked Out: {'Yes' if self.is_checked_out else 'No'}")

    def check_out(self):
        if not self.is_checked_out:
            print(f"{self.title} has been checked out.")
            self.is_checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            print(f"{self.title} has been returned.")
            self.is_checked_out = False
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}\nNumber of Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, runtime, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.director = director
        self.runtime = runtime

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}\nRuntime: {self.runtime} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_date, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.issue_date = issue_date

    def display_info(self):
        super().display_info()
        print(f"Issue Date: {self.issue_date}")
