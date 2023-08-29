from print_my_info import print_my_info

# Домашние задания:
print("-----")
# input info <----
#salary = '29000 руб.'
#salary = '35000 руб.'
#salary = '128500 руб.'
salary = '45580 руб.'

# 1. split input info into "list" form
input_info_split = salary.split(" ")
salary_number_str = input_info_split[0] # "128500"
currency_name_str = input_info_split[1] # руб.

# 2. Convert from this form (128500) to this form (128.5)
salary_number = float(salary_number_str) / 1000

print(f"Salary: {salary_number} "
      f"- type: {type(salary_number)} "
      f"Currency Name: {currency_name_str} "
      f"- type: {type(currency_name_str)}")

print("-----")

# input info <----
experience = 'Work experience 202 months'
#experience = 'Work experience 60 months'
#experience = 'Work experience 3 months'

experience_year = int(experience.split(" ")[2]) // 12
experience_month = int(experience.split(" ")[2]) % 12

print(f"{experience_year} years")
print(f"{experience_month} months")

print("-----")

description = 'Male , 39 years old , born on November 27 , 1979'
description = 'Woman , 36 years old , born on August 12 , 1982'
description = 'Male , 38 years old , born on June 25 , 1980'

description_splited = description.split(" , ")

gender = description_splited[0].lower()
age = int(description_splited[1].split(" ")[0])
year_of_birth = int(description_splited[3])

print("--")

def sayHello(message):
      print(f"Hello-world! {message}")

sayHello("From Alexander with love ^_^")

num = 36.35634
print(round(num, 3))

a = 33
b = 32.56
c = a+b
print(f"res: {c}, type: {type(c)}")

# --Введение в типы данных (cписки, кортежи)--

# Cписок в python это отдельная структура данных (изменяемая коллекция упорядоченных элементов произвольных типов)
# Список (List)
my_list1 = list()

# Либо так (сахар)
my_list2 = []

# Заполняем список
my_list3 = [3, 4, 4.55, "Hello"]
print_my_info(my_list3)

vowels = ['a', 'b', 'c', 'd', 'e']
print_my_info(vowels)

# Важно отметить, что в Python есть конструкция — генератор целочисленных списков определённой длины.
# То есть мы можем задать первый элемент, последний элемент, а также шаг и получить готовый список для работы.
rnd = range(0, 10)
print(rnd.start) # 0
print(rnd.stop) # 10

print("Range...")
my_range_list = list(rnd)
print_my_info(my_range_list)

# методы list():
# list.append() - добавить элемент
# list.clear() - стереть элемент
# list.count() - получить кол-во элементов в коллекции
# list.copy() - копировать коллекцию
# list.reverse() - повернуть элементы обратной стороной с конца к началу
# list.sort() - сортировка (упорядочивание) элементов

empty_list = list()
print(empty_list)

another_empty_list = []
print(another_empty_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

languages = ['Java', 'C', 'Python', 'C++', 'Visual Basic.NET', 'C#']

a = range(0, 10, 2)
res = list(a)
print_my_info(res)

# также можно сгененрировать список в обратном порядке
b = range(100, 0, -1)
rnd_res = list(b)

print_my_info(rnd_res)

b = list(range(50, 20, -2))
print_my_info(b)

# Индексация
arr = ['a','b','c','d','e','f']

print(arr[:2]) # ['a', 'b'] получили срез
print(arr[0:4:2]) # ['a', 'c'] 'b' сюда не включается т.к. шаг 2

print("---------")
my_list_ = list(range(1, 11))
print_my_info(my_list_)

print(my_list_[:2])
print('++++++')
num_lst = list(range(-5, 6))
print_my_info(num_lst)
# [-1, 0, 1, 2, 3]
num_lst_slice = num_lst[4:9]
print(num_lst_slice)
print("---")
new_lst = list(range(-3, 7))
print_my_info(new_lst)
slice = new_lst[::-1]
print(slice)

str = 'hello kitty'
hello_kitty = str.split()
print(hello_kitty)
sl = hello_kitty[-1:]
print(sl)

# --Методы list--
example_list = ["order1", "order2", "order3", "order4",
                "order5", "order6", "order6", "order7",
                "order8", "order6", "order9", "order10",
                "order6", "order6"]
print_my_info(example_list)

# append
print("append:")
example_list.append("order_300")
print_my_info(example_list)

# count
print("count:")
print(example_list.count("order6"))

# copy (стоит отметить, что копия и оригинал будут ссылаться на разные участки памяти. Это и правда будет копией)
print("copy:")
example_list_copy_1 = example_list.copy()
print_my_info(example_list_copy_1)
# или с помощью "сахара"
example_list_copy_2 = example_list[:]
print_my_info(example_list_copy_2)

# extend (расширение одного списка за счет другого или добавление одного к другому)
print("extend:")
example_a = ["a", "b", "c"]
example_b = ["d", "e"]
example_a.extend(example_b)
print_my_info(example_a)

# reverse - разворачивание списка наоборот
print("reverse:")
example_list.reverse()
print_my_info(example_list)
# или
example_list.reverse()
print_my_info(example_list[::-1]) #сахар

# sort
print("sort:")
example_unsorted_list = [8, 3, 4, 10, 7, 2, 11, 5, 1, 6, 0, 12, 9]
example_unsorted_list.sort()
print_my_info(example_unsorted_list)

# clear
print("clear:")
example_list.clear()
print_my_info(example_list)

list1 = [5, 0.2, 'hello there', [1,2,3,4], 'bye']
print(list1)

# --Кортеж (tuple)--
# В python кортеж неизменяемая структура данных (нельзя вносить изменение во время выполнения кода),
# так же занимает меньше память по сравнению со списками

lst = [1, 2]
print(f"lst: {lst.__sizeof__()}") # 56

# Кортежи используются в качетве ключей для словаря
tup = (1, 2)
print(f"tuple: {tup.__sizeof__()}") # 40

# Создается кортеж так же как и списки двумя способами
tup_1 = tuple()

tup_2 = ()

# Чтобы создать кортеж с одним элементом нужно написать так:
tup_one_el = ("a",)
print(tup_one_el, type(tup_one_el))

# иначе это будет строка с одним элементом (особенность синтаксиса)
one_el = ("a")
print(one_el, type(one_el))

tpl13 = (15,22,0)
print(tpl13)

print("------dictionary------")

# --Словарь (В более ранних версиях Python (до версии 3.7) не гарантируется, что ключи в словаре всегда будут находиться
# в том порядке, в котором были добавлены, — порядок может меняться. Следует обращать на это внимание, если вы работаете
# с более ранними версиями языка.)--
# Именно по этому у словаря нет метода sort, т.е. сортировка этого типа данных не имеет смысла
# создание словаря как и со списком - два варианта

my_dict_1 = dict(a="значение1")
print(f"1: {my_dict_1['a']}")

my_dict_1_1 = dict({'22': "значение1.1"})
print(f"1.1: {my_dict_1_1['22']}")

# или
my_dict_2 = {"ключ":"значение2"}
print(f"2: {my_dict_2['ключ']}")

# При этом, как и в других языках ключ обязан быть уникальным!
# если все-таки ключ в словаре будет дублироваться, то в ошибку не упадет, но выведет последнее значение
my_dict_3 = {"a":1, "b":33, "с":666}

# получение значения по ключу
print(my_dict_3["a"]) # 1

# изменение значения по ключу
my_dict_3["a"] = 300
print(my_dict_3["a"]) # 300

# дополнить словарь новой информацией
my_dict_3["d"] = 5607
print(my_dict_3["d"])

print_my_info(my_dict_3)

# Продолжая тему "сортировки словарей", вы можете отдельно сортировать ключи и значения словаря в виде списка
# (предварительно применив функцию list()). Чтобы выделить ключи и значения словаря, используются методы .keys() и .values().
# Например:
friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156, "Alex":180}
friends_keys = list(friends.keys())
friends_keys.sort()
print(friends_keys) # ['Alex', 'Dima', 'Kolya', 'Marina', 'Misha', 'Nina', 'Yana']

hash_name = "Alexander".__hash__()
print(hash_name)

print("------------------------------------------")
print()
# --Методы работы со словарями--

friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156, "Alex":180}
print(friends)

# keys() - возвращает объект (list c ключами) с ключами выбранного словаря
print("keys:")
friends_keys = friends.keys()
print(friends_keys)

# values() - тоже самое только со значениями выбранного словаря
print("values:")
friends_values = friends.values()
print(friends_values)

# get() - по сути это тоже самое обращение к словарю по ключу my_dict['22'], но при отсутствии ключа в словаре,
# не выбрасывает исключение
print("get:")
print(friends.get('Marina')) # 176
print(friends.get('Pupkin')) # none
# либо если нам надо выводить определенное сообщение при отсутствии ключа
print(friends.get("Pupkin", "There is no such value!"))

# update() - метод принимает в качетсве аргумента новый словарь (часть словаря), которую нужно добавить к существующему
# или обновить данные текущего словаря
print("update:")
friends.update({"Vasiliy": 300, "Petya": 130})
print(friends)
# обновляем данные (нужно указать действующий ключ словаря)
friends.update({"Kolya": 200, "Petya": 199})
print(friends)

# pop() - удаляет из структуры данных элементы
print("pop:")
del_kolya_info = friends.pop("Kolya")
print(friends)
print(del_kolya_info) # так можно вывести значение удаленного элемента, если это требуется

# setdefault() - в основном используется в циклах и условных операциях.
# Например, вы хотите обновить рост друга в существующем словаре, но не уверены, что он там действительно есть
# (мало ли, вдруг вы забыли его добавить, отвлекаясь на какие-то повседневные дела).
# Устанавливается по-умолчанию setdefault(key,value)
# если ключа такого в словаре нет метод создаст его за вас
# если такой ключ имеется, то значение не поменяется
print("setdefault:")
friends.setdefault("Petya")
print(friends)
friends.setdefault("Zelda", 10000)
print(friends)

# clear() - просто стирает все данные настоящего словаря
print("clear:")
friends.clear()
print(friends)

# Важный момент! В качестве значения может выступать любой тип данных. В качестве ключа только неизменяемый тип данных
# (числа, строки, кортежи).

print("-----------")
test_dict3 = dict()
test_dict3['info'] = [10, 15, 27]
test_dict3['about'] = {'game': 'football', 'period': 5}
test_dict3['about'] = 'dont know'

print(test_dict3)