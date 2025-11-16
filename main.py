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

test_dict = {'user': 'Oleg', 'age': 21, 'country': 'Poland'}
# print(test_dict['user'], test_dict['age'], test_dict.get('country'))
# print(test_dict.get('animal', 'key not'))
# test_dict['age'] = 30
# print(test_dict['age'])
# test_dict['animal'] = 'cat'
# print(test_dict)
# animal = test_dict.pop('animal')
# print(test_dict)
# print(animal)
copy_test = test_dict.copy()
print(copy_test)
test_dict.clear()
print(test_dict)

for key, value in copy_test.items():
    print(f'key: {key}, Value: {value}')
    
wrong_key = copy_test.pop('currency', 'key not')
print(wrong_key)

dict_update = {'new role': 'admin', 'salary': 10000}
copy_test.update(dict_update)
print(copy_test)