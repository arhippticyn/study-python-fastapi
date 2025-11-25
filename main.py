# Урок 2: Основи синтаксису Python: змінні, оператори, типи даних.
# num_1 = 5
# print(type(num_1))

# num_2 = 3.14
# print(type(num_2))

# string = 'hello'

# print(type(string))

# check = True
# print(type(check))

# list = ['hello', 'my', 'world']
# print(type(list))

# tpl = (1,2,3)
# print(type(tpl))

# dct = {'name': 'Jonh', 'age': 23}
# print(type(dct))

# set_ex = {1,2,3}
# print(type(set_ex))

# print(type(None))

# class Person:
#     pass

# a = Person()
# print(type(a))


# lst = [1,2,3,4,5]
# dct = {'name': 'Tom', 'age': 5}
# name = 'Tom'
# tpl = ('n', 'a', 'g')


# print(dct['name'] == name and dct['age'] in lst)


# num_1 = '1'
# print(type(num_1))
# num_1 = int(num_1)
# print(type(num_1))
# num_1 = float(num_1)
# print(num_1)
# print(type(num_1))

# string = 'hello world'
# print(len(string))
# string = string.upper()
# print(string)
# string = string.lower()
# print(string)
# string = string.capitalize()
# print(string)
# string = string.replace('d', 'f')
# print(string)
# string = string.split()
# print(string)
# # string = string.count('o')
# # print(string)
# string = '  '.join(string)
# print(string)
# string = string.count('o')
# print(string)
# string = 1
# string = str(string)
# print(type(string))

# base_list = [1,2,3]
# print(len(base_list))

# base_list.append(4)
# print(base_list)

# base_list.extend([5,6,7])
# print(base_list)

# print(base_list.index(4))

# base_dict = {'name': 'Tom', 'age': 40, 'high': 180}
# print(base_dict.keys())
# print(base_dict.values())
# print(base_dict.items())

# print(base_dict['name'], base_dict.get('animal', 'No'))
# print(base_dict['animal'])

# num_1 = '1'
# string = 'Hello world!'
# num_1 = int(num_1)
# num_1 = len(string)
# base_dict = {'world': string, 'letter': num_1}
# print(base_dict.values())
# print(base_dict['letter'])

# list = ['age', 'goat', 'car']
# list.append('gear')
# print(list)
# print(list.index('gear'))
# print(len(list))
# print(len(list) == 4 and base_dict['letter'] != 12)

# Урок 3: Управляючі конструкції: умовні оператори та цикли.

# string = 'Hello world'

# if 'Hello' not in string: 
#     print('Hello in string')
# elif 'world' in string:
#     print('World in string')
# else: 
#     print('Word not in')

# a = 10 
# b = 20

# if a == 11 and b == 20 or b < 30:
#     print(a + b)
# else: 
#     print('Wrong condition')

# test_list = ['hello', 'test', 1,2,3]

# if 'hello' in test_list and 1 in test_list:
#     print('hello 1')
# elif 'test' in test_list and 4 not in test_list:
#     print('Test not 4')
# else: 
#     print('wrong')
    
# print('End')

# a = 10
# b = 20
# c = 'chat is active'
# d = 'count of users'
# print(len(c), len(d))

# if len(c) >= b:
#     print(c)
# elif len(d) <= a:
#     print(d)
# else:
#     print('wrong condition')

# user_1 = {
#     'name': 'Tom',
#     'age': 21,
#     'Balance': 20000,
#     'currency': 'USD',
#     'status': True
# }

# user_2 = {
#     'name': 'Jonh',
#     'age': 17,
#     'Balance': 5000,
#     'currency': 'EUR',
#     'status': False
# }

# user_3 = {
#     'name': '',
#     'age': 30,
#     'Balance': 100000,
#     'currency': 'UAH',
#     'status': True
# }

# list_of_current = ['USD', 'EUR', 'UAH']

# if user_3.get('name', None) and user_3['age'] >= 18 and user_3['status']:
#     if user_3['Balance'] >= 10000 and user_3['currency'] in list_of_current:
#         print(f'Hello! {user_3["name"]}')
#     elif user_3['Balance'] >= 1000 and user_3['currency'] in list_of_current:
#         print('You need more money')
#     else:
#         print('Money critical not enought')
# elif not user_3.get("name", None):
#     print('Please, enter your name')
# elif user_3['age'] < 18:
#     print('For register binance you have to be 18 years old')
# else:
#     print('Something went wrong')


# test_list = [1,2,3,4,5,6]

# for num in test_list:
#     print(f'You got a {num}')


# test_list = [1,2,3,4,5]

# while len(test_list) < 10:
#     test_list.append(3)
#     print(test_list)


# test_list = ['test', 'python', 'code']

# for s in test_list:
#     print(s, '<') 
#     if s == 'test':
#         print(s)
#     elif s == 'python':
#         print(s)
#     else: 
#         print(s)

# a = 0
# add_list = []

# while len(add_list) < 100:
#     print(f'len {len(add_list)}')
#     add_list.append(a)
#     a += 1
#     if len(add_list) == 50:
#         print('you middle')

# user_1 = {
#     'user_name': 'tester',
#     'role': 'admin',
#     'account_connection': True
# }

# user_2 = {
#     'user_name': 'junior',
#     'role': 'user',
#     'account_connection': False
# }

# user_3 = {
#     'user_name': 'middle',
#     'role': 'pro_user',
#     'account_connection': True
# }

# list_of_users = [user_1, user_2, user_3]

# for user in list_of_users:
#     print(f'work with {user['user_name']} >-<')
#     if not user['account_connection']:
#        count_of_tries = 10
#        while count_of_tries != 0: 
#             print('Try to connect to user')
#             count_of_tries -= 1
#             if count_of_tries == 5:
#                     print('Middle of tries')
#                     continue
#             print('Count left', count_of_tries)
#     elif user['role'] == 'admin':
#         print(f'Hello in system {user['user_name']}')
#     else:
#         print('welcome')
        
# print('All users were check')

# Урок 4: Структури даних: списки, кортежі, словники.

# a = [1,2,3,4,5]
# b = ['apple', 'banana', 'cherry']

# print(a[0], a[1], a[-1])
# print(b[1])

# print(a[1:4], a[::2])
# print(b[::2])

# print(a[::-1])
# print(b[::-1])

# a.append(6)
# b.append('tomato')
# print(a,b)

# a.insert(3,7.4)
# b.insert(3, 'bottle')

# print(a,b)

# a.remove(7.4)
# b.remove('bottle')
# print(a,b)

# last_elem_1 = a.pop(0)
# last_elem_2 = b.pop(0)
# print(last_elem_1, last_elem_2)
# print(a.index(3), b.index('banana'))

# a.extend([5,5,5])
# b.extend(['cherry', 'banana', 'banana'])
# print(a.count(5), b.count('banana'), b.count('cherry'))

# print(a,b)
# a.sort(reverse=True)
# b.sort(reverse=True)
# print(a,b)
# a.reverse()
# b.reverse()
# print(a,b)

# a = (1,2,3,4,5,5,4)
# print(a[0], a[1],a[2])
# print(a[:2], a[-2:])

# print(a.count(5), a.count(4))
# print(a.index(4))

# test_dict = {'user': 'Oleg', 'age': 21, 'country': 'Poland'}
# print(test_dict['user'], test_dict['age'], test_dict.get('country'))
# print(test_dict.get('animal', 'key not'))
# test_dict['age'] = 30
# print(test_dict['age'])
# test_dict['animal'] = 'cat'
# print(test_dict)
# animal = test_dict.pop('animal')
# print(test_dict)
# print(animal)
# copy_test = test_dict.copy()
# print(copy_test)
# test_dict.clear()
# print(test_dict)

# for key, value in copy_test.items():
#     print(f'key: {key}, Value: {value}')
    
# wrong_key = copy_test.pop('currency', 'key not')
# print(wrong_key)

# dict_update = {'new role': 'admin', 'salary': 10000}
# copy_test.update(dict_update)
# print(copy_test)


# Урок 4: Структури даних: списки, кортежі, словники.(практика)

#1
# nums = [10, 20, 30, 40, 50]

# print(nums[1:4])

#2
# data = (5, 10, 15, 20, 25)
# print(data[2])

#3

# person = {"name": "Max", "age": 18, "city": "Kyiv"}

# person_age = person.get('age')
# print(person_age)

#4

# numbers = [3, 7, 2, 9, 5]

# numbers.append(10)
# numbers.remove(7)
# numbers.sort()

# print(numbers)

#5

# t = (1, 2, 3, 4, 5)

# list = list(t)
# list.append(6)

# print(tuple(list))

# #6

# user = {
#     'name': 'Anna',
#     'age': 21,
#     'city': 'Lviv'
# }

# user_update = {
#     'is_student': True
# }

# user.update(user_update)

# print(user)


# Урок 5: Функції та модулі.

# def say_hello(username, age):
#     print(f'Hello {username} welcome')
#     print(f'Your age is {age}')
#     print('-----------------')
    
# def print_numbers(start, stop):
#     for num in range(start, stop):
#         print(f'Current num is {num}')
        
#     print('-----------------')
        
# user_data = {'Dima':25, 'Sarah': 34, 'Tom': 11}
# list_of_ranges = [(1,10), (2,9), (0,100)] 


# # for name, age in user_data.items():
# #     say_hello(name, age)
    
# for start_pos, stop_pos in list_of_ranges:
#   print_numbers(start_pos, stop_pos)


# def check_connection(username,count_tries, priority):
#     if priority >= 10:
#         finish = 5
#         for attemt in range(1, count_tries + 1):
#             if attemt == finish:
#                 print('Connect was successfully')
#                 break
#             print(f'Attemp: {attemt} to connect to {username}')
            
#     elif priority >= 5 and priority < 10:
#         finish = 3
#         for attemt in range(1,6):
#             if attemt == finish:
#               print('Connect was successfully')
#             print(f'Attemp: {attemt} to connect to username')
            
#     else: 
#         print('Yout username has so low priority')
        
# check_connection(count_tries=10, username='Oleg', priority=100)

# import turtle

# def drawSquare(size, color):
#     turtle.speed(1)
#     turtle.color(color)
#     turtle.begin_fill()
#     def move(len):
#         turtle.forward(len)
#         turtle.left(90)
        
#     for _ in range(1,5):
#         move(size)
        
#     turtle.end_fill()

# drawSquare(100, 'red')
# turtle.goto(100,100)
# drawSquare(200, 'blue')

# Урок 5: Функції та модулі. (практика)

# Створи функцію filter_even(numbers), яка приймає список чисел і повертає новий список, що містить тільки парні числа.

# def filter_even(numbers):
#     num_par = []
    
#     for num in numbers:
#         if num % 2 == 0:
#             num_par.append(num)    
#             print(num_par)
            
# filter_even([1, 2, 3, 4, 5, 6])  # → [2, 4, 6]

# Напиши функцію count_vowels(s), яка повертає кількість голосних (a, e, i, o, u) у рядку.

# def count_vowels(s):
#     gol = 'aeiouAEIOU'
    
#     count = 0
#     for let in s:
#         if let in gol:
#             count += 1
#     return count        
            
# print(count_vowels("hello world"))


# Створи функцію buy(product_name, amount), яка:перевіряє, чи є такий товар,перевіряє, чи вистачає кількості,
# якщо так — зменшує кількість, якщо ні — виводить відповідне повідомлення

# products = {
#     "apple": 10,
#     "banana": 5,
#     "milk": 2
# }

# def buy(product_name, amount): 
#     if product_name not in products:
#         return 'Products not found'
        
#     current_amount = products[product_name]
#     if current_amount < amount:
#         return f"Помилка: На складі лише {current_amount} одиниць товару '{product_name}', а ви просите {amount}."
    
#     products[product_name] -= amount
    
#     return f'Yoy buy {product_name} is prev amount {amount}, now your amount {products[product_name]}'
   
    
# print(buy("apple", 3))  
# print(buy("orange", 1))
# print(buy("milk", 5))


# Урок 6: Введення в ООП. Класи та об'єкти.


# class Person:
#     """Class for creation persons"""
#     name = 'Tom'
#     age = 18
#     high = 180
    
# print(Person.name)
# print(Person.age)
# Person.age = 50
# print(Person.name)
# print(Person.age)

# print(Person.__dict__)

# person1 = Person()
# person1.is_animal = False
# print(person1.__dict__)
# print(Person.__dict__)

# person2 = Person()
# print(person2.__dict__)
# print(person1.where_is)
# print(getattr(person1, 'name'))
# print(getattr(person1, 'where_is', False))

# person1.age = 59
# person1.color = 'black'
# print(person1.__dict__)

# setattr(person1, 'high', 100)
# print(person1.high)
# print(person1.__dict__)

# print(hasattr(person1, 'name'))
# print(hasattr(person1, 'where_is'))

# del Person.high
# print(Person.__dict__)
# print(hasattr(Person, 'high'))

# delattr(Person, 'age')
# print(hasattr(Person, 'age'))

# getattr, setattr, hasattr, delattr

# print(Person.__doc__)

# class Person:
#     '''Class for creation persons'''
    
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
        
#     def print_attrs(self):
#         print(f'>>> {self} <<<')
#         print(self.name, self.age)
        
# person1 = Person('Tom', 18)
# print(person1)
# person1.print_attrs()

# person2 = Person('oleg', 50)
# print(person2)
# person2.print_attrs()

# class Point: 
#     '''Class for create and set coords'''
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.get_attrs()
#         self.check_coords()
        
#     def check_coords(self):
#         for attr in self.__dict__:
#             if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr],str):
#                 print('coord cant be less than 0')
#                 setattr(self, attr, 0)
#             elif getattr(self, attr, False) > 100 and not isinstance(self.__dict__[attr],str):
#                 print('coord cant be great than 100')
#                 setattr(self, attr, 100)
#             print(self.__dict__)
            
#     def get_attrs(self):
#         print(self.__dict__)
        
#     def set_attrs(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.check_coords()
        
    
        
# coord_1 = Point(-1,101,50)
# coord_1.get_attrs()
# coord_1.check_coords()
# print('-------')
# coord_1.set_attrs(1000, 1000, -5)
# coord_1.get_attrs()
# coord_1.check_coords()

# Урок 6: Введення в ООП. Класи та об'єкти. (практика)

# 1 Створи клас Car, який має: Атрибути:brand (марка),year (рік випуску) Метод: info() — повертає рядок: "Car: <brand>, year: <year>"

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
        
#     def info(self):
#         brand = self.brand
#         year = self.year
#         print(f'Car: {brand}, year: {year}')
        
# car1 = Car('BMW', 2018)
# car1.info()


# # Створи клас User, який має:
# # Атрибути:name,balance (початково передається в конструкторі)Методи:add_balance(amount) — додає гроші, info() — повертає:"User: Alex, balance: 200"

# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
        
#     def add_balance(self,amount):
#         self.balance += amount
        
#     def info(self):
#         return f'User: {self.name}, balance: {self.balance}'
        
# user1 = User('Alex',100)
# user1.add_balance(50)
# print(user1.info())

# # Створи клас Product, який має: Атрибути:name, price Метод:discount(percent) — зменшує ціну на відсоток

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def discount(self, persent):
        
#         self.price = round(self.price * (1 - persent / 100), 2)
    
# product_1 = Product('Laptop', 1000)
# print(product_1.__dict__)
# product_1.discount(10)
# print(product_1.price)


# Урок 7: Наслідування та поліморфізм.

# class A:
#     '''Class A'''
#     name_a = 'class A is parent'
#     is_main_class = True
    
#     def print_hello(self):
#         print('Hello from A')

# class B(A):
#     '''Class B'''
#     name_b = 'class B is child'
#     is_main_class = False
    
#     def print_hello(self):
#         print('hello fron B')
    
# class C(B):
#     '''Class C'''
#     pass

# test_ex = C()

# print(test_ex.name_a)
# print(test_ex.name_b)
# print(test_ex.is_main_class)
# test_ex.print_hello()


# class Vehicle:
#     '''It's a base class for Vehecle'''
    
#     def __init__(self, type, color, left_of_life = 100):
#         self.type = type
#         self.color = color
#         self.left_of_life = left_of_life
        
#     def move(self):
#         print('Your vehicle is moving')
        
#     def fix(self):
#         if self.left_of_life <= 50:
#           print(f'{self.type} need to fix')
#         else:
#             print(f'Your {self.type} is good')
        
# class Car(Vehicle):
#     '''Class Car'''
    
#     def __init__(self, type, color,left_of_life, cost=0):
#         super().__init__(type, color, left_of_life)
#         self.cost = cost
        
#     def move(self):
#         print(f'{self.color} {self.type} is driving')
#         print(f'Cost of this car {self.cost}')
        
# class Bicycle(Vehicle):
#     '''Class Bicycle'''
    
#     def __init__(self, type, color,left_of_life, count_of_wheels):
#         super().__init__(type, color, left_of_life)
#         self.count_of_wheels = count_of_wheels
        
#     def move(self):
#         print('You are so fast')
        
# car_1 = Car('car', 'black',70, 10000)
# car_1.move()
# car_1.fix()
# bicycle_1 = Bicycle('road_bicycle','blue',30, 2000)
# bicycle_1.move()
# bicycle_1.fix()

# class Counter:
#     '''Count of something'''
    
#     def __init__(self, count_obj, type_obj, max_elements):
#         self.count_obj = count_obj
#         self.type_obj = type_obj
#         self.max_elements = max_elements
        
#     def counter(self):
#         print(f'Type of object: {self.type_obj}')
#         if isinstance(self.count_obj, (list, dict, str, tuple)):
#             count= len(self.count_obj)
#             if count > self.max_elements:
#                 print('Count elements of your object more than need')
#                 print(f'More on {count - self.max_elements}')
#             else:
#                 print(f'Count of elements {count}')
#         else:
#             print('Your object must be iterable')
            
#     def get_attrs(self):
#         print(self.__dict__)
        
#     def set_attr(self, attr, value):
#         if hasattr(self, attr):
#             setattr(self, attr, value)
#         else:
#             print('Check your attrs')
            
# class ListElements(Counter):
#     '''Class for lists elements'''
    
#     def __init__(self, count_obj, type_obj, max_elements):
#         super().__init__(count_obj, type_obj, max_elements)
#         pass
    
#     def counter(self):
#         super().counter()
        
#         print('Operation was ended')
        
#     def get_attrs(self):
#         super().get_attrs()
#         print('Operation was ended')
        
# list_ex = ListElements([1,2,3,4], list, 10)
# list_ex.counter()
# list_ex.get_attrs()
# list_ex.set_attr('count_obj', [1,2,3,4,5,6])

# class BaseInterface:
#     '''Base class'''
    
#     def __init__(self):
#         pass
        
#     def get_attr(self):
#         pass
        
#     def print_model(self):
#         pass
    
#     def count_of_price(self):
#         pass
    
#     def call_to_support(self):
#         pass
    
# class SiteInterface(BaseInterface):
#     '''Interface of our site'''
    
#     def __init__(self, number, model, price):
#         super().__init__()
#         self.number = number
#         self.model = model
#         self.price = price
        
#     def print_model(self):
#         print(f'Model of site {self.model}')
        
#     def count_of_price(self):
#         print(f'Count of site price: {self.price ** 2}')
        
#     def call_to_support(self):
#         print(f'number of support is {self.number}')
#         print(f'Your can call from 8 am to 19 pm')
        
# class AppInterface(BaseInterface):
#     '''Interface of our app'''
    
#     def __init__(self, number, model, price):
#         super().__init__()
#         self.number = number
#         self.model = model
#         self.price = price
        
#     def print_model(self):
#         print(f'Model of app: {self.model}')
        
#     def count_of_price(self):
#         print(f'Count of app price: {self.price ** 2}')
        
#     def call_to_support(self):
#         print(f'number of support is {self.number}')
#         print(f'Your can call from 8 am to 19 pm')
        
# site_user = SiteInterface(12345, 'shop', 1000)
# app_user = AppInterface(322324, 'android', 5000)

# for user in (site_user, app_user):
#     user.print_model()
#     user.count_of_price()
#     user.call_to_support()
#     print('-------------')

# Урок 7: Наслідування та поліморфізм.(практика)

# Створи базовий клас Animal з методом: sound()
# У підкласах Dog та Cat перевизнач звук:Dog → "Woof!" Cat → "Meow!"

# class Animal:
#     def __init__(self):
#         pass
    
#     def sound(self):
#         pass
    
# class Dog(Animal):
#     def sound(self):
#         return 'Woof!'
        
# class Cat(Animal):
#     def sound(self):
#         return 'Meow'
        
# animals = [Dog(), Cat(), Dog()]

# for animal in animals:
#     print(animal.sound())
    
    
# # Створи: Клас Vehicle:атрибут: speed метод: info() → "Speed: <speed>"
# # Клас Car (успадковує Vehicle):атрибут: fuel метод: info() → "Speed: <speed>, Fuel: <fuel>"
# # Клас ElectricCar (успадковує Car):атрибут: battery метод: info() → "Speed: <speed>, Battery: <battery>"

# class Vehicle: 
#     def __init__(self,speed):
#         self.speed = speed
        
#     def info(self):
#         return f'Speed: {self.speed}'
    
# class Car(Vehicle):
#     def __init__(self, speed, fuel):
#         super().__init__(speed)
#         self.fuel = fuel
        
#     def info(self):
#         return f'{super().info()}, Fuel: {self.fuel}'
    
# class ElectricCar(Car):
#     def __init__(self, speed, fuel, battery):
#         super().__init__(speed, fuel)
#         self.battery = battery
        
#     def info(self):
#         return f'{super().info()}, battery: {self.battery}'
    
# ec = ElectricCar(120, 'none', 80)
# print(ec.info())

# # Створи базовий клас Shape з методом: area()
# # І створи: Клас Circle: приймає radius, area → 3.14 * r * r
# # Клас Rectangle: приймає width, height,area → width * height

# import math

# class Shape: 
#     def __init__(self):
#         pass
    
#     def area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
        
#     def area(self):
#         return round(math.pi * (self.radius ** 2), 2)
    
# class Rectange(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height
    
# shapes = [Circle(5), Rectange(4,6)]

# for shape in shapes:
#     print(shape.area())
#     print('--------------')
    
# # Є базовий клас:

# # Product:name, price, метод: get_price()
# # Створи підкласи: DiscountProduct: атрибут: percent, get_price() → повертає ціну з урахуванням знижки
# # LimitedProduct:атрибут: limited_count,get_price() → якщо limited_count = 0 → повернути "No stock" інакше повернути звичайну ціну

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def get_price(self):
#         pass
    
# class DiscountProduct(Product):
#     def __init__(self, name, price, percent):
#         super().__init__(name, price)
#         self.percent = percent
        
#     def get_price(self):
#         return round(self.price * (1 - self.percent / 100), 2)
    
# class LimitedProduct(Product):
#     def __init__(self, name, price, limited_count):
#         super().__init__(name, price)
#         self.limited_count = limited_count
        
#     def get_price(self):
#         if self.limited_count == 0:
#             return 'No stock'
#         else:
#             return self.price
        
# products = [DiscountProduct('iphone', 1000, 18), LimitedProduct('mac', 1300, 2), LimitedProduct('mac', 1300, 0)]
# for product in products:
#     print(product.get_price())
#     print('------------')

# Урок 8: Інкапсуляція та абстракція

# class Card:
#     '''Class Card for users card'''
    
#     def __init__(self, card_number, balance):
#         if self.__check_attribuite_type(card_number, str):
#            self._card_number = card_number
#         if self.__check_attribuite_type(balance, float):
#            self.__balance = balance
        
#     def get_cart_data(self):
#         return self.__dict__
    
#     def set_card_data(self, attr, value):
#         if self.__check_attribuite_type(attr, str):
#            self.__dict__[attr] = value
#            return {attr: self.__dict__[attr]}
#         else:
#             return 'Attribute must be string type'
        
#     def __check_attribuite_type(self, attr, should_be):
#         if type(attr) == should_be:
#             return True
#         else:
#             raise TypeError(f'Attribute must be {should_be}')
        
# user_card_1 = Card('3424 2414 1451 1553', 1000.0)
# print(user_card_1.get_cart_data())
# print(user_card_1.set_card_data('card_number', '0000 0000 0000 0000'))
# print(user_card_1.set_card_data('balance', 100))
# print(user_card_1.__balance)

# Урок 8: Інкапсуляція та абстракція(практика)

# Створи клас BankAccount, де:
# Приватні атрибути: __balance (початково 0)
# Методи:deposit(amount) — додає гроші (якщо amount > 0)
# withdraw(amount) — знімає гроші (якщо є достатньо)
# get_balance() — повертає баланс
# Використай інкапсуляцію (приватний баланс).



# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return self.__balance
#         else:
#             return 'Мало грошей'
        
#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return self.__balance
#         else:
#             return 'Недостаньо грошей'
        
#     def get_balance(self):
#         return self.__dict__
    
# acc = BankAccount()
# acc.deposit(100)
# acc.withdraw(30)
# print(acc.get_balance())

# Створи абстрактний клас Device, де:
# Абстрактний метод: turn_on()
# Створи два класи:
# Phone:метод turn_on() → "Phone is turning on"
# Laptop:метод turn_on() → "Laptop is booting"

# from abc import ABC, abstractclassmethod

# class Device(ABC):
#     @abstractclassmethod
#     def turn_on(self):
#         pass
    
    
# class Phone(Device):
#     def turn_on(self):
#         return "Phone is turning on"
    
# class Laptop(Device):
#     def turn_on(self):
#         return 'Laptop is booting'
    
# devices = [Phone(), Laptop()]

# for device in devices:
#     print(device.turn_on())
    
# Створи клас User, де:
# Приватні атрибути:__name,__age
# Методи:get_name(),set_name(new_name) (перевірка: ім’я не пусте)
# get_age()set_age(new_age) (перевірка: new_age ≥ 0)

# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
        
#     def get_name(self):
#         return self.__name
    
#     def set_name(self, new_name):
#         if new_name.strip():
#             self.__name = new_name
#             return self.__name
#         else:
#             return 'please write name'
        
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age >= 0:
#             self.__age = new_age
#             return self.__age
        
# u = User('Alex', 15)
# u.set_age(16)
# print(u.get_age())

# Урок 9: Принципи SOLID в ООП.

# Принцип єдиного обов'язку

# class Journal:
#     def __init__(self):
#         self.entries = []
#         self.count = 0
        
#     def add_entry(self, text):
#         self.count += 1
#         self.entries.append(f'{self.count}: {text}')
    
#     def remove_entry(self, pos):
#         del self.entries[pos]
        
#     def __str__(self):
#         return '\n'.join(self.entries)
    
# class SaveFiles:
#     @staticmethod
#     def save_to_file(journal, filename):
#         with open(file = filename,mode = 'w') as file:
#             file.write(journal)
            
# class LoadFiles:
#     @staticmethod
#     def load_file(self):
#         pass
    
# j = Journal()
# j.add_entry('I ate today')
# j.add_entry('I slept yesterday')
# print(f'Count of entries:\n{j}')

# Принцип відкритості/закритості

# Неправильно


# from enum import Enum


# class Product(Enum):
#     SHIRT = 1
#     TSHIRT = 2
#     PANT = 3
    
# class DiscountCalculator:
#     def __init__(self, product_type, cost):
#         self.product_type = product_type
#         self.cost = cost
        
#     def get_discount(self):
#         if self.product_type == Product.SHIRT:
#             return self.cost - (self.cost * 0.10)
#         elif self.product_type == Product.TSHIRT:
#             return self.cost - (self.cost * 0.15)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost * 0.20)
        
# dc_shirt = DiscountCalculator(Product.SHIRT, 100)
# print(dc_shirt.get_discount())
# dc_tshirt = DiscountCalculator(Product.TSHIRT, 200)
# print(dc_tshirt.get_discount())
# dc_pant = DiscountCalculator(Product.PANT, 300)
# print(dc_pant.get_discount())


# Приавильно

# from abc import ABC, abstractmethod

# class Product(ABC):
#     @abstractmethod
#     def get_discount(self):
#         pass
    
# class DiscountCalculatorShirt(Product):
#     def __init__(self, cost, sale):
#         self.cost = cost
#         self.sale = sale
        
#     def get_discount(self):
#         return self.cost - (self.cost * self.sale)
    
# class DiscountCalculatorTShirt(Product):
#     def __init__(self, cost, sale):
#         self.cost = cost
#         self.sale = sale
        
#     def get_discount(self):
#         return self.cost - (self.cost * self.sale)
    
# class DiscountCalculatorPant(Product):
#     def __init__(self, cost, sale):
#         self.cost = cost
#         self.sale = sale
        
#     def get_discount(self):
#         return self.cost - (self.cost * self.sale)
    
# shirt = DiscountCalculatorShirt(1000, 0.15)
# t_shirt = DiscountCalculatorTShirt(2000, 0.30)
# pant = DiscountCalculatorPant(500, 0.10)

# clouses = [shirt, t_shirt, pant]

# for clouse in clouses:
#     print(clouse.get_discount())
    
    
# Принцип підстановки Барбари Лісков

# class Car:
#     def __init__(self,type):
#         self.type = type
#         self.properties = {}
        
#     def set_properties(self, color, cost, capacity):
#         self.properties = {'Color': color, 'Cost': cost, 'Capacity': capacity}
        
#     def get_properties(self):
#         return self.properties
    
# class PetrolCar(Car):
#     def __init__(self, type):
#         self.type = type
#         self.properties = {}
        
# car = Car('SKODA')
# car.set_properties('Black', 10000, 5)

# petrol_car = PetrolCar('Nissan')
# petrol_car.set_properties('Blue', 8000, 3)

# cars = [car, petrol_car]

# def get_color_car(color):
#     count = 0
#     car_type = []
#     for car in cars:
#         if car.properties['Color'] == color:
#             count += 1
#             car_type.append(car.type)
            
#     print(f'Count of {color} cars: {count} \n {color} cars: {car_type}')

 
# get_color_car('Black')

# Принцип розділення інтерфейсу

# from abc import ABC, abstractmethod

# class MakeCall(ABC):
#     @abstractmethod
#     def make_call(self):
#         pass
    
    
# class SendSms(ABC): 
#     @abstractmethod
#     def send_sms(self):
#         pass
    
# class GetInternet(ABC):
#     @abstractmethod
#     def get_internet(self):
#         pass
    
# class MobilePhone(MakeCall, SendSms, GetInternet):
#     def make_call(self):
#         print('calling abonent')
        
#     def send_sms(self):
#         print('Sending sms')
        
#     def get_internet(self):
#         print('connct to internet')
        
# class StacionarPhone(MakeCall):
#     def make_call(self):
#         print('calling')
        
                
# mobile_phone = MobilePhone()
# mobile_phone.make_call()
# mobile_phone.send_sms()
# mobile_phone.get_internet()

# print('------------------')

# stacionar_phone = StacionarPhone()
# stacionar_phone.make_call()

# Принцип інверсії залежностей

# from enum import Enum
# from abc import ABC, abstractmethod


# class Teams(Enum):
#     BLUE_TEAM = 1
#     RED_TEAM = 2
#     GREEN_TEAM = 3
    
# class TeamMembershipLookUp(ABC):
#     @abstractmethod
#     def find_all_students(self, team):
#         pass
    
# class Student:
#     def __init__(self, name):
#         self.name = name
        
# class TeamMemberShips(TeamMembershipLookUp):
#     def __init__(self):
#         self.team_memberships = []
        
#     def add_team_memberships(self, student, team):
#         self.team_memberships.append((student,team))
        
#     def find_all_students(self, team):
#         for members in self.team_memberships:
#             if members[1] == team:
#                 yield members[0].name 
                
                                       
# class Analysys:
#     def __init__(self, team_member_ship_lookup):
#         # memberships = team_student_membership.team_memberships
#         # for member in memberships:
#         #     if member[1] == Teams.RED_TEAM:
#         #         print(f'{member[0].name} is in red team')
#         for student in team_member_ship_lookup.find_all_students(Teams.RED_TEAM):
#             print(f'{student} is in Red team')
                
                
# student_1 = Student('Oleg')
# student_2 = Student('Dima')
# student_3 = Student('Serega')

# team_memberships = TeamMemberShips()
# team_memberships.add_team_memberships(student_1, Teams.RED_TEAM)
# team_memberships.add_team_memberships(student_2, Teams.RED_TEAM)
# team_memberships.add_team_memberships(student_3, Teams.RED_TEAM)

# Analysys(team_memberships)

# Задача 1 — SRP

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
    

# class SaveFile:
#     @staticmethod
#     def save_to_file(name, email):
#         with open("users.txt", "a") as f:
#             f.write(name + " " + email + "\n")
            
# Задача 2 — OCP (розширення без зміни)
# from abc import ABC, abstractmethod

# class Discount(ABC):
#     @abstractmethod
#     def get(self):
#         pass
    
# class DiscountNew(Discount):
#     def __init__(self, price, sale):
#         self.price = price
#         self.sale = sale
        
#     def get(self):
#         return self.price - (self.price * self.sale)
        
# class DiscountVip(Discount):
#     def __init__(self, price, sale):
#         self.price = price
#         self.sale = sale
        
#     def get(self):
#         return self.price - (self.price * self.sale)
    
# new = DiscountNew(100, 0.10)
# print(new.get())
# vip = DiscountVip(1825,0.15)
# print(vip.get())

# Задача 3 — DIP (залежність від абстракцій)

# from abc import ABC, abstractmethod

# class Sender(ABC):
#     @abstractmethod
#     def send(self,msg):
#         pass
    
# class SmsSender(Sender):
#     def send(self, msg):
#         print(f'Send SMS: {msg}')

# class EmailSender(Sender):
#     def send(self, msg):
#         print(f"Send email: {msg}")


# class Notifier:
#     def __init__(self, sender: Sender):
#         self._sender = sender
    
#     def notify(self, msg):
#         self._sender.send(msg)
        

# sms_sendler = SmsSender()        
# notifer = Notifier(sms_sendler)
# notifer.notify('Hello world!')

# email_sendler = EmailSender()
# notifer = Notifier(email_sendler)
# notifer.notify('Bello bello')


# Декоратори




# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Что то случилось перед функцией')
#         result =  func(*args, **kwargs)
#         print('Функция прошла')
#         return result
    
#     return wrapper

# def say_hello():
#     print('Hello')
    
# my_decorator(say_hello)()



# @my_decorator
# def add_numbers(a, b)-> None:
#     print('Adding number')
#     return a + b



# print(add_numbers(2,3))


# import time
# import requests
# from requests.exceptions import RequestException

# API_KEY = 'AZ8HWXQ5HHPK4XDVR7FD5CYM3'

# def retry(func):
#     def wrapper_retry(*args, **kwargs):
#         retries = [5, 30]
#         for seconds in retries:
#             try:
#                 return func(*args, **kwargs)
#             except RequestException:
#                 print(f'Failed to get data, Retrying in {seconds} seconds')
#                 time.sleep(seconds)
                
#         return func(*args, **kwargs)
#     return wrapper_retry

# @retry
# def get_weather_by_hours_for_day_from_api(date, city):
#     url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?key={API_KEY}'
#     response = requests.get(url)
#     weather_by_day = response.json()['days']
#     weather_by_hours = weather_by_day[0]['hours']
#     return weather_by_hours
    
    
# def farengeit_to_celsius(farengeit):
#     return round((farengeit - 32) * 5 / 9)

# def get_dangerous_hours(weather_by_hours) -> int:
#     dangerous = []
#     for weather in weather_by_hours:
#         uvindex = weather['uvindex']
#         time = weather['datetime']
#         celsius_tempurature = farengeit_to_celsius(weather['temp'])
#         if uvindex >= 3:
#             dangerous.append({'time': time, 'uvindex': uvindex, 'tempurature': celsius_tempurature})
#     return dangerous

# date = '2025-11-23'
# city = 'Singapore'
# weather_by_hour = get_weather_by_hours_for_day_from_api(date, city)
# dangerous_hours = get_dangerous_hours(weather_by_hour)
# print(dangerous_hours)

# декораторы практика

# Напиши декоратор uppercase, який робить текст функції великими літерами

# def uppercase(func):
#     def wrapper(name):
#         print('Hello')
#         result = func(name)
#         result_upper = result.upper()
#         print('GoodBye')
#         return result_upper
        
#     return wrapper

# @uppercase
# def get_name(name):
#     return f'name: {name}'

# print(get_name('arhip'))

# Напиши декоратор timer, який вимірює, скільки часу виконується функція.

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f'time func: {end - start:.6f}s')
#         return result
#     return wrapper

# @timer
# def func():
#     time.sleep(1)

# func()

# 



# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f'Вызываю {func.__name__}')
#         result = func(*args, **kwargs)
#         return f'result: {result}'
#     return wrapper

# @debug
# def add(a, b):
#     return a + b

# print(add(2,5))

# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.



# site = 'https://jsonplaceholder.typicode.com/posts/1'
# response_get = requests.get(site)
# print(response_get.headers)
# for header, value in response_get.headers.items():
#     print(f'Header: {header}, --> value: {value}')
# print(response_get.text)
# print('----------------')
# body = {
#     'userId': 12,
#     'title': 'test',
#     'body': 'test',
# }
# headers = {
#     'Content-Type': 'application/json; charset=utf-8'
# }
# response_post = requests.post(site, json=body, headers=headers)
# print(response_post.status_code)
# print('-----------------')
# print(response_post.reason)
# print('-----------------')
# print(response_post.text)
# print('-----------------')

# data = {
#     'title': 'test_put'
# }
# response_put = requests.put(site, data=data)
# print(response_put.status_code)
# print(response_put.reason)
# print(response_put.text)

# print('----------------')

# response_patch = requests.patch(site, data=data)
# print(response_patch.status_code)
# print(response_patch.reason)
# print(response_patch.text)

# print('----------------')

# response_delete = requests.delete(site)
# print(response_delete.status_code)
# print(response_delete.reason)
# print(response_delete.text)

# Задание 1: Получение данных с API

# import requests

# url = 'https://jsonplaceholder.typicode.com/posts'

# response_get = requests.get(url=url)
# print(response_get.json())
# print('--------------------')
# print(response_get.json()[0]['title'])

# Задание 2: Создание нового поста

# data = {
#     'id': 11,
#     'title':'This is my first post',
#     'body': 'Text post',
# }

# response_post = requests.post(url=url, json=data)
# print(response_post.status_code)
# print('---------')
# print(response_post.reason)
# print('-----------')
# print(response_post.text)
# print('-----------')

# Урок 2: Введення до FastAPI. Встановлення та перша програма.




# @app.get('/')
# def root():
#     return {'message': 'Hello world'}

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {'item_id': item_id}

# @app.get("/items/{item_id}")
# async def read_items(item_id: int):
#     return {'item_id': item_id}

# @app.get('/models/{model_name}')
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {'model_name': model_name, 'message': 'good'}
#     if model_name.value == 'lenet':
#          return {'model_name': model_name, 'message': 'Lenet'}
     
#     return {'model_name': model_name, 'message': 'Have some reduals'}

# fale_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]

# @app.get('/items/')
# async def read_item(skip: int = 0, limit: int = 5):
#     return fale_items_db[skip: skip + limit]

# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {'item_id': item_id, 'q': q}
#     return {'item_id': item_id}

# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {'item_id': item_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update({'description': 'This is amazing item has long descr'})
#     return item

# @app.get('/users/{user_id}/items/{item_id}')
# async def read_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {'item_id': item_id, 'owner_id': user_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update({'description': 'This is amazing item has long descr'})
#     return item

# @app.get('/items/{item_id}')
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: int | None = None
# ):
#     item = {'item_id': item_id, "needy": needy, 'skip': skip, 'limit': limit}
#     return item 

# Урок 2: Введення до FastAPI. Встановлення та перша програма. (практика)