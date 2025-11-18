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

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def info(self):
        brand = self.brand
        year = self.year
        print(f'Car: {brand}, year: {year}')
        
car1 = Car('BMW', 2018)
car1.info()


# Створи клас User, який має:
# Атрибути:name,balance (початково передається в конструкторі)Методи:add_balance(amount) — додає гроші, info() — повертає:"User: Alex, balance: 200"

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def add_balance(self,amount):
        self.balance += amount
        
    def info(self):
        return f'User: {self.name}, balance: {self.balance}'
        
user1 = User('Alex',100)
user1.add_balance(50)
print(user1.info())

# Створи клас Product, який має: Атрибути:name, price Метод:discount(percent) — зменшує ціну на відсоток

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def discount(self, persent):
        
        self.price = round(self.price * (1 - persent / 100), 2)
    
product_1 = Product('Laptop', 1000)
print(product_1.__dict__)
product_1.discount(10)
print(product_1.price)