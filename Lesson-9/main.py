# --- Функции ---
# Функции позволяют:
# - выполнять один и тот же набор инструкций (фрагмент исходного кода) несколько раз;
# - выполнять одни и те же действия с различными входными данными;
# - структурировать исходный код.

print('-' * 40)
# Например:
def first_function():
    print("Hello function!")

first_function()
first_function()

# Описание функции начинается со слова:
# def [имя функции] (аргументы функции) :
     # Код... (тело функции)

# Важно отметить, что название функции (или сигнатура) не должна повторяться и не должна копировать имена встроенных в pyhton методов (функций)
# Если в коде будет две одинаковые по сигнатуре и по аргументам функции, но с разным кодом внутри, то действовать будет последняя!
# Так же важно различать объявление функции и ее использование (т.е. нужно сначала написать объявить def ....(), а уже потом использовать ....)
# Пример:

print('-' * 40)
# Объявление
def print_hours(minutes):
    hours = minutes // 60
    left_minutes = minutes % 60
    print(f"Hours: {hours}")
    print(f"Left Minutes: {left_minutes}")

# Использование
print_hours(90)

print('-' * 40)
# Есть функции возвращающие результат
def get_time(distance, speed):
    result = distance / speed
    return result # С помощью оператора return возвращаем результат в переменную time_result

time_result = get_time(100, 25)
print(time_result) # 4.0

print('-' * 40)
# Чтобы вернуть два аргумента из функции (если есть такая необходимость), то
def get_time_tuple(distance, speed):
    hours = distance // speed
    distance_left = distance % speed
    kms_per_minute = speed / 60
    minutes = round(distance_left / kms_per_minute) # округляем результат
    return hours, minutes # С помощью оператора return возвращаем результат в переменную time_result в виде кортежа

hours_res, minutes_res = get_time_tuple(120, 100)
print(f"Hours to travel: {hours_res}")
print(f"Minutes to travel: {minutes_res}") # 1, 12

print('-' * 40)
# Так же стоит отметить, что функция без оператора return тоже будет кое что возвращать и это объект None (т.е. ничего)
# Пример
def say_hello_print(message):
    print(message)
result_1 = say_hello_print("Hello from 1")
# Hello from 1
print(result_1) # None

def say_hello(message):
    return message
result_2 = say_hello("Hello from 2")
print(result_2) # Hello from 2

print('-' * 40)
# Еще пример (функция ищет объект в списке)
# list_in — список, в котором будем искать объект
# Интуитивно хотелось бы назвать аргумент для списка
# словом list, однако это привело бы к изменению встроенного
# объекта list, что очень нежелательно
# obj — аргумент, содержащий объект, который ищет функция
def in_list(list_in, obj):
    for elem in list_in:
        if obj == elem:
            print("Element is found!")
            return True
            print("This won’t be printed")
    print("Element is NOT found!")
    return False
    print("This will not be printed either")

my_list = [1,15,"hey",1,2,5,7,10]
result = in_list(my_list, "hey")
print(result)
# True
result = in_list(my_list, 3)
# Element is NOT found!
print(result)
# False
result = in_list(my_list, 7)
# Element is found!
print(result)
# True

# Задание 2.3
print('-' * 40)
def get_total(units, price):
    return units * price
print(get_total(15, 50))

print('-' * 40)
# -- Аргумента по умолчанию и проверка аргументов --
# Пример (создадии словарь с оценками учеников и обратимся к нему по ключу которого не существует. Возникнет ошибка)
grades = {'Ivanov': 5, 'Smirnov': 3, 'Kuznetsova': 4, 'Tihonova': 5}
# print(grades['Pavlov'])
# Возникнет исключение KeyError: 'Pavlov'
# Оно означает, что переданного ключа (слово "Pavlov")
# нет в словаре
# В этом случае можно обернуть код в try / except
try:
    print(grades['Pavlov'])
except KeyError:
    print("Student does not exists")

print('-' * 40)
# Аргументы по умолчанию
def get_coca_cola(with_ice = True):
    if with_ice:
        print("You have got coca cola with ice... Mmmmhh")
    else:
        print("You have got coca cola with out ice... Beeahh")

get_coca_cola() # You have got coca cola with ice... Mmmmhh
get_coca_cola(False) # You have got coca cola with out ice... Beeahh

# Аргументы по умолчанию дают возможность заранее устанавливать необходимое значение для предотвращения возникновения ошибок

# Еще пример (напишем функцию извлекающую корень из числа)
# Поставим по умолчанию квадратный корень, т.к. это самый распространенный вариант расчетов. Стоит отметить, что
# аргументы по умолчанию указываются только после объявления основных аргументов

# !!!Нельзя в качестве аргументов по умолчанию использовать изменяемые типы: списки, словари, множества!!!
# В качестве аргументов по умолчанию точно можно использовать «простые» типы данных, которые не содержат в себе
# дополнительные значения, такие как int, float, str, bool, None.
def get_root(value, n):
    result = value ** (1 / n)
    return result

print(get_root(27, 3))

print('-' * 40)
# Введите свое решение ниже
def get_time(distance, speed):
    if distance < 0 or speed < 0:
        raise ValueError("Distance or speed cannot be below 0!")
    if distance <= 0 or speed <= 0:
        raise ValueError("Speed cannot be equal to 0!")
    result = distance / speed
    return result

print(get_time(100, 10))

print('-' * 40)
# Cамопроверка (Модифицируем функцию root так, чтобы передавать степень корня было необязательно.
# Если степень корня не передана, функция должна возвращать значение квадратного корня.)
def get_root(value, n = 2):
    result = value ** (1/n)
    print(result)
get_root(81) # 9.0
get_root(81, 2) # 9.0

print('-' * 40)
# Пример того, как делать не нужно (добавление оценки в словарь)
def add_mark(name, mark, journal={}):
    journal[name] = mark
    return journal

# Создадим пустой словарь, в который будем
# сохранять оценки группы 1
group1 = {}
# Добавим оценки двух студентов
group1 = add_mark('Ivanov', 5, group1)
group1 = add_mark('Tihonova', 4, group1)
print(group1)
# Будет напечатано:
# {'Ivanov': 5, 'Tihonova': 4}

# А теперь не будем передавать пустой журнал изначально в качестве аргумента — он ведь и так создаётся по умолчанию (как будто бы):
print('-' * 40)
# Добавим в журнал для новой группы оценку Смирнову
# Сам журнал не передаём в виде аргумента
# Пустой журнал будет использован как аргумент по умолчанию
group2 = add_mark('Smirnov', 3)
print(group2)
# Будет напечатано:
# {'Smirnov': 3}

# Аналогично для новой группы 3 добавим оценку Кузнецовой
group3 = add_mark('Kuznetsova', 5)
print(group3)
# Будет напечатано:
# {'Smirnov': 3, 'Kuznetsova': 5}

print('-' * 40)
# Мы думали, что будет два отдельных словаря, но используется на самом деле один, при первом вызове функции
# Таким образом мы модифицировали ранее созданный словарь
# Давайте сделаем так, чтобы каждый раз при запуске функции без словаря всё-таки создавался пустой словарь, а не использовался однажды созданный.
def add_mark(name, mark, journal=None):
    if journal == None:
        journal = {}
    journal[name] = mark
    return journal

group2 = add_mark('Smirnov', 3)
print(group2)
# Будет напечатано:
# {'Smirnov': 3}

group3 = add_mark('Kuznetsova', 5)
print(group3)
# Будет напечатано:
# {'Kuznetsova': 5}

# Теперь все как надо!
print('-' * 40)
def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if journal is None:
        journal = {}
        lst = [2, 3, 4, 5]
    if mark not in lst:
        raise ValueError("Invalid Mark!")
    journal[name] = mark
    return journal

print(add_mark('Ivanov', 5))
# ValueError: Invalid Mark!

# -- Продвинутая передача аргументов --
# Пример

print('-' * 40)
def root_plus(value, n=2, verbose=False):
    result = value ** (1 / n)
    if verbose:
        print(result)
    return result
res = root_plus(25)
print(res) # 5.0
root_plus(25, 2, True) # 5.0
# Либо можно игнорировать аргумент по умолчанию n и написать так
root_plus(25, verbose=True) # 5.0
# Стоит отметить, что вначала, при создании функции, нужно указывать сначала порядковые аргументы, а потом именованные т.е.
# сначала value (порядковый), затем versose=True (именованный - ключ-значение)
# Однако, мы все же может поменять местами аргументы, но с явным указанием, например:
print('-' * 40)
root_plus(25, verbose=True, n=3) # 2.924017738212866

print('-' * 40)
# Пример с функцией print
print(90, 60, 90, sep=',') # Вывод будет через запятую
# Вместо
print("Shopping list:")
print("break", "milk", "coffee")

print('-' * 40)
# Можно указать
print("Shopping list:", end=' ')
print("break", "milk", "coffee", sep=', ', end='.')

# -- Продвинутая обработка аргументов --
# На вход (если заранее неизвестно) можно создать неограниченное кол-во аргументов т.н. *args
# Звездочка означает оператор распаковки
# Пример
def mean(*args):
    is_type = type(args)
    result = sum(args) / len(args)
    return f"{result} - { is_type}"

print(mean(24, 500, 99))
print(mean(2, 1))
print(mean(1,2,3,4,6,9000))

print('-' * 40)
# Еще пример
def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    return f"{name}, {result}"
print(mean_mark("Alexander", 5,5,5,5))
print(mean_mark("Alice", 2,4,5))

# Стоит отметить, что правила расстановки аргументов тут действуют так же как и выше т.е.
# mean_mark(5,6,5,4, "Alex") - будет ошибка!
# если необходимо поменять местами объявление аргументов то их необходимо объявлять явно
# mean_mark(5,6,5,4, name="Alex") - так можно
# Все аргументы становятся автоматические именованными после *args (будет кортежем)

print('-' * 40)
# Еще интересный момент
lang = ["C#", "Python", "Golang", "C", "Fortran"]
print(lang) # передавая в функцию без звездочки мы передаем как один аргумент (в данном случае список)
# ['C#', 'Python', 'Golang', 'C', 'Fortran']
print(*lang) # так мы производим упаковку и на выходе будет как-будто мы написали несколько аргументов
# C# Python Golang C Fortran

print('-' * 40)
# Так же можно передавать разное число именованных аргументов с помощью не одной а двух звездочек **
# **kwargs - стандартное название для совокупности именованных аргументов (будет словарем)
def schedule_lang(**kwargs):
    print(kwargs, sep=",")

schedule_lang(monday="Python", tuesday="C#", wednesday="Swift", thursday="relax", friday="Python")

print('-' * 40)
def schedule_print(**kwargs):
    print("My language week:")
    for key in kwargs: print(key, kwargs[key], sep=" - ")

schedule_print(monday="Python", tuesday="C#", wednesday="Swift", thursday="relax", friday="Python")

print('-' * 40)
# Еще пример где мы указываем сначала порядковые аргументы *args, затем именованные **kwargs
def print_args(*args, **kwargs):
    print(args, end=" - ")
    print(kwargs, end=".")

print_args(2,3,4,5, tuesday="C#", wednesday="Swift")

print()
print('-' * 40)
# Задание 5.1 (напишите функцию mult, которая считает произведение переданных в неё чисел через запятую.
# Особое указание: посчитайте результат с использованием цикла for)
def mult(*args):
    n = 1
    for num in args:
        n *= num
    return n

print(mult(3,5,10))

print('-' * 40)
marks = [4,5,5,5,5,3,4,4,5,4,5]
print(mean_mark("Kuznetsov", *marks))

print('-' * 40)
# -- Lambda-функции --
# В python это короткие функции без объявления оператора return (однострочные) используещиеся как правило для быстрых и коротких задач.
# Например (обычная функция)
def root_double_simple(num):
    return num ** (1/2)
print(root_double_simple(13))

print('-' * 40)
# Лямбда функция (использование ключевого слова lambda обязательно), ключевое слово return не требуется
# Cинтаксис: [переменная] = lambda [название аргумента/тов] : код
root_1 = lambda num: num ** (1/2)
print(root_1(13))

print('-' * 40)
# Лямбда функция с двумя аргументами
root_2 = lambda value, num: value ** (1/num)
print(root_2(13, 2))

print('-' * 40)
# Лямбда (четное / нечетное число)
is_even = lambda num: 'even' if num % 2 == 0 else 'odd'
print(is_even(84)) # even (четное)

print('-' * 40)
# Лямбда может принимать неограниченное число аргументов (* и **) - операторы распаковки
result = lambda *args : args
print(result(4, 22, 13, 4, 88, 90, 1000))

print('-' * 40)
# Еще пример где пишем делится ли указанное число на 2 и 3
scary_func = lambda num: 'divided by 2 and 3' \
if num % 6 == 0 \
else 'divided by 2' if num % 2 == 0 \
else 'divided by 3' if num % 3 == 0 \
else 'not divided by 2 and 3'
print(scary_func(6))

print('-' * 40)
# Лямбда функцию можно использовать в качестве аргумента для другого метода, пример:
# Нам нужно отсортировать список, но не по алфавиту (как в sort), а по длинне
names = ['Ivan','Kim','German','Margarita','Simon']
names.sort()
print(names)

print('-' * 40)
# Тут мы передали в качестве аргумента лямбда
names.sort(key=lambda name:len(name))
print(names)

print('-' * 40)
# Еще пример
new_list = ['bbb','ababa','aaa','aaaa','cc']
new_list.sort(key=lambda word:len(word))
print(new_list)

print('-' * 40)
# Тут в качестве ключа возвращается лямбда кортеж где первый элемент длинна слова, а второй само слово
# Отсортируется сначала по длинне слова, потом по алфавиту
new_list.sort(key=lambda word:(len(word), word))
print(new_list)

print('-' * 40)
# Задание 6.3
hyp = lambda a, b: (a ** 2 + b ** 2) ** (1/2)

print(hyp(3,4))
print(hyp(1,9))

print('-' * 40)
# Задание 6.4 (Напишите функцию sort_sides(l_in), которая сортирует переданный в неё список l_in.
# Входной список состоит из кортежей с парами чисел — длинами катетов прямоугольных треугольников.
# Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз треугольников)
def sort_sides(l_in):
    l_in.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2) ** (1/2))
    return l_in

print(sort_sides([(3,4), (1,2), (10,10)])) # [(1, 2), (3, 4), (10, 10)]
print(sort_sides([(1, 10), (2, 9), (5, 12), (3, 4)])) # [(3, 4), (2, 9), (1, 10), (5, 12)]

print('-' * 40)
# Задание 7.9 (Напишите функцию get_less, которая принимает на вход через запятую список, состоящий из чисел, и ещё одно число.
# Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. Если такого числа нет,
# необходимо вернуть None.)
def get_less(list_in, num):
    for n in list_in:
        if n < num:
            return n
    return None
l = [1, 5, 8, 10]
print(get_less(l, 8)) # 1
print(get_less(l, 0)) # None
print(get_less(list_in = [1, 2, 4, 5, 8, 10], num = 6)) # 1
print(get_less(list_in = [25, 26, 24, 1, 0], num = 25)) # 24

print('-' * 40)
# Задача 7.10 (Напишите функцию split_date(date), которая принимает на вход строку, задающую дату, в формате ддммгггг без разделителей.
# Функция должна вернуть кортеж из чисел (int): день, месяц, год.)
def split_date(date):
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:8])
    return day, month, year

print(split_date("31012019"))
# (31, 1, 2019)

print('-' * 40)
# Задача 7.11 (Напишите функцию is_prime(num), которая проверяет, является ли число простым.)
def is_prime(num):
    # Если число больше чем 1
    if num > 1:
        # Итерация от 2 до N / 2
        for i in range(2, int(num / 2) + 2):
            # Если число делится на число между 2 и N / 2, это число сложносоставное (не простое)
            if num % i == 0:
                return False
            else:
                return True
    else:
        return False

print(is_prime(1)) # False
print(is_prime(3)) # True
print(is_prime(10)) # False
print(is_prime(13)) # True

print('-' * 40)
# Задача 7.12 (Напишите функцию between_min_max(...), которая принимает на вход числа через запятую. Функция возвращает
# среднее арифметическое между максимальным и минимальным значением этих чисел, то есть (max + min)/2.)
def between_min_max(*args):
    min = args[0]
    max = 0
    for n in args:
        if n < min:
            min = n
        elif n > max:
            max = n
    result = (max + min) / 2
    return result

print(between_min_max(10)) # 10.0
print(between_min_max(1,2,3,4,5)) # 3.0
print(between_min_max(12, 5, 0, 16, 7)) # 8.0

print('-' * 40)
# Задание 7.13 (Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов имена
# студентов и их номера в рейтинге (нагляднее в примере). Необходимо вернуть фамилию студента с минимальным номером по рейтингу.)
def best_student(**kwargs):
    result = sorted(kwargs.items(), key=lambda x:x[1])
    result = result[0]
    return list(result)[0]

print(best_student(Tom=12, Mike=3)) # Mike
print(best_student(Tom=12)) # Tom
print(best_student(Tom=12, Jerry=1, Jane=2)) # Jerry

print('-' * 40)
# Задача 7.14
is_palindrom = lambda x: 'yes' if x[:len(x)] == x[::-1] else 'no'
print(is_palindrom(x = '121')) # yes
print(is_palindrom('121')) # yes
print(is_palindrom('1234')) # no
print(is_palindrom('12321')) # yes

print('-' * 40)
# Задача 7.15
area = lambda a,b: a*b
print(area(12,5)) # 60

print('-' * 40)
# Задача 7.16
between_min_max = lambda *args: (max(args) + min(args)) / 2
print(between_min_max(1,2,3,4,5)) # 3.0

print('-' * 40)
# Задача 7.17 (Напишите функцию sort_ignore_case, которая принимает на вход список и сортирует его без учёта регистра по алфавиту.
# Функция возвращает отсортированный список.)
def sort_ignore_case(ls):
    ls.sort(key=lambda s:s.lower())
    return ls

print(sort_ignore_case(['Acc', 'abc'])) # ['abc', 'Acc']

print('-' * 40)
# Задание 7.18 (Повышенной сложности)
# Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), сумму в рублях (rub)
# и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар. Например, курс 85.46 означает, что один доллар
# стоит 85 рублей и 46 копеек.
# В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, должна возникнуть ошибка
# ValueError('Not enough arguments'). Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').

def exchange(usd=None, rub=None, rate=None):
    # try:
        if rub == None and usd != None and rate != None:
            result = usd * rate
            return result
        if usd == None and rub != None and rate != None:
            result = rub / rate
            return result
        if rate == None and usd != None and rub != None:
            result = rub / usd
            return result
        if usd != None and rub != None and rate != None:
            raise ValueError('Too many arguments')
        else:
            raise ValueError('Not enough arguments')
    # except ValueError as ex:
    #     return f'ValueError: {ex}'

print(exchange(usd=100, rub=8500)) # 85.0
print(exchange(usd=100, rate=85)) # 8500
print(exchange(rub=1000, rate=85)) # 11.764705882352942
print(exchange(rub=1000, rate=85, usd=90)) # ValueError: Too many arguments
print(exchange(rub=1000)) # ValueError: Not enough arguments

# def exchange(usd=None, rub=None, rate=None):
#     if (usd is not None) and (rub is not None) and (rate is not None):
#         raise ValueError('Too many arguments')
#     not_enough_error = ValueError('Not enough arguments')
#     if usd is not None:
#         if rub is not None:
#             return rub/usd
#         if rate is not None:
#             return usd * rate
#     if rub is not None:
#         if rate is not None:
#             return rub/rate
#     raise not_enough_error
