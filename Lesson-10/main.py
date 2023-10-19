import datetime

# -- Продвинутое использование функций в Python --
print('-' * 40)
# -- Вложенные функции -- (функции объявленные внутри другой функции)
# Например
# Объявляем внешнюю функцию outer()
def outer():
    # Печатаем информацию о вызове внешней функции
    print('Called outer function')
    # Объявляем внутреннюю функцию innouter()
    def inner():
        # Печатаем информацию о вызове внутренней функции
        print('Called inner function')
    # Вызываем внутреннюю функцию inner()
    inner() # внутреннюю функцию, чтобы она работала нужно также объявлять внутри тела
outer()

print('-' * 40)
# Еще пример
# Во внешней функции (объемлющей) будем печатать результат расчета корня числа
def print_root(value, n=2):
    # внутренняя функция (расчитывает сам корень)
    def root(value, n):
        result = value ** (1/n)
        return result

    res = root(value, n)
    print(f"Root of power {n} from {value} equals: {res}")

# Далее вызываем внешнюю функцию
print_root(13, 2) # 3.61
print_root(81, 4) # 3

# Если же мы попытаемся достучаться до внутренней функции из-вне, то интерпретатор ее просто не увидит (т.к. область видимости только внутри print_root())
# В Python существует «право на владение» объектом — функцией или переменной. Если объект находится в некоторой функции,
# то не из каждой точки программы можно будет к нему обратиться.

print('-' * 40)
def min_of_cubes(x, y):
    def cube(a):
        result = a**3
        return result

    return min(cube(x), cube(y))
print(min_of_cubes(x=5, y=3))

print('-' * 40)
# Задание 2.3 (написать программу, которая будет определять, на каком из языков лучше всего написать одну и ту же фразу.
# Определять, какой вариант «лучше» или «хуже», будем по количеству уникальных букв во фразе. При этом регистр не имеет значения.)
# Объемлющая функция
def get_count_unique_symbols(input_str):
    input_str = input_str.lower() # К нижнему регистру
    input_str = input_str.replace(' ', '') # Убираем пробелы
    result = len(set(input_str)) # считаем кол-во уникальных символов
    print(result)

get_count_unique_symbols('Это простая строка') ## 9
get_count_unique_symbols('This is a simple string') ## 12

print('-' * 40)
# Задание 2.4
def get_min_string(s1, s2):
    def get_count_unique_symbols(input_str):
        input_str = input_str.lower()  # К нижнему регистру
        input_str = input_str.replace(' ', '')  # Убираем пробелы
        result = len(set(input_str))  # считаем кол-во уникальных символов
        return result

    s1_len = get_count_unique_symbols(s1)
    s2_len = get_count_unique_symbols(s2)

    if s1_len == s2_len:
        return (s1, s2)
    elif s1_len > s2_len:
        return s2
    elif s1_len < s2_len:
        return s1

print(get_min_string(s1='Это простая строка', s2='This is a simple string')) ## Это простая строка
print(get_min_string(s1='Отличная фраза', s2='Great phrase')) ## Great phrase
print(get_min_string(s1='школа', s2='school')) ## ('школа', 'school')

print('-' * 40)
# -- Разрешение переменных (область видимости) --
# Пример (имитация занесения сотр. в БД)
# Внешняя функция
def register_employee(name, surname):
    # Внутренняя функция (для промежуточных вычислений)
    def create_full_name():
        # Функция использует переменные (name, surname)
        sep = ' ' # Разделитель между имененм и фамилией
        result = name + sep + surname
        return result
    full_name = create_full_name() # Вызываем внутреннюю функцию
    # Выводим результат на экран используя внешнюю переменную company_name
    print(f"Employee {full_name} is registered in the company {company_name}")

company_name = "Apple"
register_employee('John', 'Wick')
#  Стои более подробно разобрать разрешение переменных.
# 1. name, surname  являются локальными по отношению к register_employee
# 2. create_full_name - локальная функция внутри register_employee
# 3. нелокальные переменные name, surname по отношению к функции create_full_name
# 4. глобальные переменные company_name (объявлена в основной части программы вне всех функций)
# 5. встроенные функции - функции встроенные в язык (len(), string.replace(), print() и т.д.)
# Разрешение переменных — процесс поиска интерпретатором объекта, который скрывается за названием переменной.
print('-' * 40)
# Пример вывода всех встроенных функций в язык
print(dir(__builtins__))

# Иллюстрация правила LEGB (Local, Enclosed, Global, Build-In)
print('-' * 40)
# 1 ---
value = 'global'
def outer():
    def inner():
        print(value)
    inner()

# Вызов функции outer()
outer() # 'global'

print('-' * 40)
# 2. ---
value = 'global'
def outer():
    value = 'enclosing'
    def inner():
        print(value)
    inner()

# Вызов функции outer()
outer() # 'enclosing'

print('-' * 40)
# 3. ---
value = 'global'
def outer():
    value = 'enclosing'
    def inner():
        value = 'local'
        print(value)
    inner()
# Вызов функции outer()
outer() # 'local'

print('-' * 40)
# Задание 2.9
def calculate_area_circle(r):
    area = pi * (r ** 2)
    return round(area, 3)

def calculate_area_ellipse(a, b):
    area = pi * a * b
    return round(area, 3)

pi = 3.1416
print(calculate_area_circle(r=5)) ## 78.54
print(calculate_area_ellipse(a=3, b=2.5)) ## 23.562

pi = 3.14
print(calculate_area_circle(r=5)) ## 78.5
print(calculate_area_ellipse(a=3, b=2.5)) ## 23.55

print('-' * 40)
# -- Изменение переменных вне области видимости --
# Функция не может изменить значение переменной, которая находится вне своей локальной области видимости.
# Вместо изменения значения глобальной переменной создаётся новая локальная переменная с тем же именем.

# Пример
# Глобальная переменная
count = 10
def function():
    # Объявляем локальную переменную count
    count = 100

# Вызываем функцию
function()
# Смотрим изменилась ли переменная count (глобальная)
print(count) # 10

# Однако функция может скорректировать объект изменяемого типа, находящийся за пределами её локальной области видимости,
# если изменит его содержимое.
# К неизменяемым встроенным в Python типам данных относятся int, float, str, tuple;
# К изменяемым типам относятся list, dict, set.

print('-' * 40)
# Пример
# Объявляем глобальную переменную
words_list = ['foo', 'bar', 'baz']
def function():
    words_list[1] = 'fuunc'
function()
print(words_list) # ['foo', 'fuunc', 'baz'] - изменено

print('-' * 40)
# Однако если внутри function() попытаться перезаписать значение переменной words_list, то она вновь создаст новое
# локальное имя и не изменит глобальный words_list.
# Пример
# Объявляем глобальную переменную
words_list = ['foo', 'bar', 'baz']
def function():
    # Изменяем элемент списка
    words_list = ['foo', 'quux', 'baz']
# Вызываем функцию
function()
print(words_list) # ['foo', 'bar', 'baz'] - не изменено

# Но что, если нам действительно необходимо изменять значение в глобальной области видимости при вызове функции?
# Оказывается, если в коде функции происходит переопределение глобальной или нелокальной переменной, то необходимо просто
# указать, что та или иная переменная является глобальной или нелокальной. Для этого используются ключевые слова global и nonlocal

# -- Объявление GLOBAL --
# Создадим глобальную переменную, изначально она равна 0
global_count = 0
# Создадим функцию, которая прибавляет 1 к переменной global_count
def add_item():
    # Здесь мог бы быть код для добавления товара в базу данных
    # Увеличим общее количество товаров на 1
    # Для того, чтобы исправить ошибку нужно добавить оператор global в функцию перед той переменной, которую хотим изменить глобально.
    global global_count
    # Далее присваиваем значение
    global_count = global_count + 1

# Вызовем функцию add_item()
add_item()
# Напечатаем значение переменной global_count
# print(global_count) # UnboundLocalError: local variable 'global_count' referenced before assignment (до присваивания global)
print(global_count) # UnboundLocalError: local variable 'global_count' referenced before assignment (после присваивания global)

print('-' * 40)
# А вот ещё один фокус. Благодаря инструкции global мы можем объявлять глобальные переменные непосредственно внутри функций.
# Создадим функцию которая прибавляет 1 к переменной global_count
def add_item():
    # Здесь мог бы быть код для добавления товара в базу данных
    # Указываем, что global_count является глобальной переменной
    global global_count
    global_count = 0
    # Увеличиваем общее количество товаров на 1
    global_count = global_count + 1
# Вызываем функцию add_item()
add_item()
# Напечатаем значение переменной global_count
print(global_count) # 1
# Важно отметить, что несмотря на то что объявление переменной global_count и находится внутри функции, благодаря объявлению
# global эта переменная была создана именно в глобальном пространстве имён. Поэтому переменная не уничтожается по завершении
# работы функции и мы можем к ней обращаться из любой части программы.
# Однако, несмотря на то, что глобальные переменные есть возможность изменять стандарты python крайне не рекомендуют этого делать!

# Лучше с глобальными переменными, если их нужно изменять, получать ссылку через аргументы, а присваивать значения через return
# Пример

print('-' * 40)
# ПЛОХО!
num_students = 250
def add_new_students(num_new):
    global num_students
    num_students += num_new

add_new_students(50)
print(num_students) # 300

print('-' * 40)
# ХОРОШО
num_students = 250
def add_new_students(num_students, num_new):
    num_students += num_new
    return num_students

num_students = add_new_students(num_students, 50)
print(num_students) # 300

print('-' * 40)
# Задача 3.2
def cash(less_money):
    global money
    money -= less_money
    return money

money = 200000
print(cash(1000)) # 199000

money = 200000
print(cash(1000)) # 199000

money = 30240
print(cash(240)) # 30000

print('-' * 40)
# Задача 3.3
# Словарь с курсами валют (по отношению к рублю)
currencies = {'USD': 74, 'EUR': 88, 'GBP': 98 , 'CHF': 82}
# Общее количество денег на счету, которое нужно конвертировать
money = 100000
# Функция для конвертации валюты, аргумент - наименование валюты
def convert(currencies, money, currency):
    # Производим конвертацию - делим количество денег на счету на соответствующий курс
    money = money / currencies[currency]
    return money

# Вызываем функцию для конвертации валюты
convert_money = convert(currencies, money, currency='USD')
print(convert_money) # 1351.3513513513512

convert_money = convert(currencies, money, currency='EUR')
print(convert_money)  # 1136.3636363636363

print('-' * 40)
# -- Объявление NONGLOBAL --
# Пример
def outer():
    # Создадим переменную, относящуюся к внешней функции
    enclosing_count = 0
    # Внутренняя функция
    def inner():
        nonlocal enclosing_count
        # Прибавим 1 к enclosing_count
        enclosing_count = enclosing_count + 1
        # Напечатаем значение enclosing_count
        print(enclosing_count)
        # Запустим внутреннюю функцию из внешней
    inner()

# Запустим внешнюю функцию
# outer() # UnboundLocalError: cannot access local variable 'enclosing_count' where it is not associated with a value

# Ожидаемо получили ошибку, однако чтобы указать интерпретатору, что мы хотим изменить значение именно нелокальной переменной,
# используется ключевое слово nonlocal.
outer() # 1

print('-' * 40)
# Имена, определённые после ключевого слова nonlocal, ссылаются на переменные из ближайшей нелокальной (объемлющей) области видимости.
# Рассмотрим более практичный пример
# Функция для вычисления стоимости
# Аргументы — cost (стоимость), sale (размер скидки)
# def calculate_cost(cost, sale):
#     # Считаем итоговую стоимость и возвращаем её
#     # (стоимость — стоимость * скидка)
#     return cost - cost * sale
#
# Пусть вместо sale на вход будет либо строка, либо целое число, либо дробное число, для этого чтоит внутри функции
# реализовать вспомогательную функцию
# print(calculate_cost(1330, '15%'))
# print(calculate_cost(1330, 15))
# print(calculate_cost(1330, 0.15))
# Внешняя функция для вычисления итоговой стоимости
def calculate_cost(cost, sale):
    # Внутренняя функция для предобработки аргумента sale
    def preprocessing_sale():
        nonlocal sale
        # Если sale — строка
        if type(sale) == str:
            sale = float(sale.replace('%', ''))
            sale = sale / 100
        # Если sale — целое число
        elif type(sale) == int:
            sale = sale / 100
        # elif (type(sale) is not str or
        #       type(sale) is not int or
        #       type(sale) is not float):
        #     raise ValueError("Некорректный формат скидки")
    preprocessing_sale()
    # Считаем итоговую стоимость и возвращаем её
    # (стоимость — стоимость * скидка)
    return cost - cost * sale
print(calculate_cost(1330, '15%')) # 1130.5
print(calculate_cost(1330, 15)) # 1130.5
print(calculate_cost(1330, 0.15)) # 1130.5
# print(calculate_cost(1330, sale=[])) # ValueError: Некорректный формат скидки

print('-' * 40)
# Задание 3.5
# Функция для вычисления количества символов (symbol) в строке s
def count_occurrences(s, symbol):
    # Внутренняя функция для предобработки строки s
    def preprocessing_s():
        nonlocal s
        # Удаляем пробелы из строки
        s = s.replace(' ', '')
        # Приводим строку к нижнему регистру
        s = s.lower()
    # Вызываем функцию для предобработки аргумента s
    preprocessing_s()
    # Считаем количество символов symbol в строке s и возвращаем результат
    return s.count(symbol)

print(count_occurrences('This is simple string', symbol='t')) # 2

# -- Изменение значений встроенных переменных --
# Такое возможно сделать в python, однако не рекомендуется, т.к. теряется доступ к возможностям исходной функции
# Пример
my_list = [1, 4, 5, 7]
# Запишем в переменную с названием
# len длину списка my_list,
# полученную с помощью встроенной функции len
len = len(my_list)
print(len) # 4, а не 3 как должно быть!

# # Попробуем снова воспользоваться функцией len:
# # Создадим ещё один список
# new_list = ['Ivan', 'Sergej', 'Maria']
# # Также узнаем его длину с помощью функции len
# length = len(new_list)
# print(length) # TypeError: 'int' object is not callable
# # Из-за того, чтобы переопределили функцию len, то в итоге за именем len в программе теперь скрывается число,
# # а не встроенная в Python функция для вычисления длины списка.

# Вывод! Старайтесь никогда не переопределять имена встроенных объектов в своих программах!!!
print('-' * 40)
# Задание 3.7
advertising_campaigns = {'ютуб': [212, 248], 'вк': [514, 342], 'радио': [339, 125]}

# Создаём новый пустой словарь
advertising_campaigns_max = {}
# Создаём цикл по ключам исходного словаря
for key in advertising_campaigns:
    # Вычисляем максимум в списке, лежащем по ключу key
    maximum_count = max(advertising_campaigns[key])
    # Добавляем максимум в новый словарь
    advertising_campaigns_max[key] = maximum_count

print(advertising_campaigns_max) # {'ютуб': 248, 'вк': 514, 'радио': 339}

print('-' * 40)
print('-' * 40)
# -- Практика --
# Задача 1
def register(surname, name, date, middle_name=None, registry=None):
    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Вспомогательная функция для предобработки даты
    def preprossesing_date(date):
        def check_date(date, month, year):
            # Проверка на целочисленный тип
            if type(date) is not int or type(month) is not int or type(year) is not int:
                return False
            # Проверка на нули в дате
            if date == 00 or month == 00 or year == 0000:
                return False
            # Если высокосный год, то в феврале не 28, а 29 дней
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if month == 2 and date > 29:
                    return False
            # Если год обычный
            else:
                # Дата не может быть меньше 1 и больше 31;
                # Месяц не может быть меньше 1 и больше 12;
                # Год рождения не может быть меньше 1900 и больше 2022
                if (1 < date > 31) or (1 < month > 12) or (1900 <= year >= 2022):
                    return False
                # В феврале 28 дней
                if month == 2 and date > 28:
                    return False
                # В 4, 6, 9 и 11 месяцах по 30 дней
                if (month in [4,6,9,11]) and (date > 30):
                    return False
            # Если все проверки пройдены
            return True
        # Разделяем строку по символу точки
        date, month, year = date.split('.')
        # Преобразуем все данные к типу данных int
        date, month, year = int(date), int(month), int(year)
        is_correct = check_date(date, month, year)
        # Если проверка пройдена возвращаем кортеж
        if is_correct: return date, month, year
        else: raise ValueError("Invalid Date!")

    # Разделяем дату на составляющие
    date, month, year = preprossesing_date(date)
    # Добавляем данные в список
    registry.append((surname, name, middle_name, date, month, year))
    # Возвращаем результат
    return registry

reg = register('Petrova', 'Maria', '13.03.2003', 'Ivanovna')
reg = register('Ivanov', 'Sergej', '24.09.1995', registry=reg)
reg = register('Smith', 'John', '13.02.2003', registry=reg)
reg = register('Smith', 'John', '29.02.2020', registry=reg)
print(reg)
# [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995),
# ('Smith', 'John', None, 13, 2, 2003), ('Smith', 'John', None, 29, 2, 2020)]

print('-' * 40)
# Задание 4.4
def check_date(date, month, year):
    def is_leap(year):
        # Если высокосный год
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    # Проверка на целочисленный тип
    if type(date) is not int or type(month) is not int or type(year) is not int:
        return False
    # Проверка на нули в дате
    if date == 00 or month == 00 or year == 0000:
        return False
    # Если высокосный год, то в феврале не 28, а 29 дней
    if is_leap(year):
        if month == 2 and date > 29:
            return False
    # Если год обычный
    else:
        # Дата не может быть меньше 1 и больше 31;
        # Месяц не может быть меньше 1 и больше 12;
        # Год рождения не может быть меньше 1900 и больше 2022
        if (1 < date > 31) or (1 < month > 12) or (1900 <= year >= 2022):
            return False
        # В феврале 28 дней
        if month == 2 and date > 28:
            return False
        # В 4, 6, 9 и 11 месяцах по 30 дней
        if (month in [4, 6, 9, 11]) and (date > 30):
            return False
    # Если все проверки пройдены
    return True

print(check_date(18, 9, 1999)) # True
print(check_date(29, 2, 2000)) # True
print(check_date(29, 2, 2021)) # False
print(check_date(13, 13, 2021)) # False
print(check_date(13.5, 12, 2021)) # False

print('-' * 40)
# Задача 2
# Функция принимающая координаты точек треугольника и возвращать длинны сторон треугольника, его периметр, площадь в виде словаря
# Вычисление для треугольника (объемлющая функция)
def triangle(p1, p2, p3):
    # Проверка на входные параметры
    if (type(p1) is not tuple) or (type(p2) is not tuple) or (type(p3) is not tuple):
        raise ValueError("Input args are not tuples!")

    # Проверка получается ли треугольник из входных параметров
    def check_exist_triangle(a, b, c):
        # Из математики известно, что треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    # Вычисление длинн сторон треугольника
    def sides(p1, p2, p3):
        # Вычисление длинн сторон треугольника
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        # Стороны по формуле:
        # a = P1 P2 = √((x2 - x1) ** 2 + (y2 - y1) ** 2) (√ - корень)
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        # b = P1 P3 = √((x3 - x1) ** 2 + (y3 - y1) ** 2) (√ - корень)
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        # c = P2 P3 = √((x3 - x2) ** 2 + (y3 - y2) ** 2) (√ - корень)
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5  # ** 0.5 вычисляем корень
        return a, b, c

    # Вычисление периметра
    def calculate_perimeter_triangle(a, b, c):
        # Периметр по формуле P = a + b + c (сумма всех сторон треугольника)
        perimeter = (a + b + c)
        return perimeter

    # Вычисление площади
    def calculate_area_triangle(a, b, c):
        # p = P / 2 или (a + b + c / 2) (p - полупериметр, P - периметр) (Вычисляем полупериметр)
        p = perimeter / 2
        # Если есть периметр треугольника, то его площадь можно вычислить по формуле Герона
        # S = √p(p - a)(p-b)(p-c) (√ - корень)
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

    # Вычисляем стороны треугольника
    a, b, c = sides(p1, p2, p3)
    if check_exist_triangle(a, b, c):
        # Вычисляем периметр треугольника
        perimeter = calculate_perimeter_triangle(a, b, c)
        # Вычисляем площадь треугольника
        area = calculate_area_triangle(a, b, c)
        result = {'a': a, 'b': b, 'c': c, 'perimeter': perimeter, 'area': area}
        return result
    else:
        raise ValueError("Треугольник не существует")

print(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
# {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
print(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
# {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}

print('-' * 40)
# Задание 4.6
# Проверка получается ли треугольник из входных параметров
def check_exist_triangle(a, b, c):
    # Из математики известно, что треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(check_exist_triangle(a=3, b=4, c=5))
## True
print(check_exist_triangle(a=1.8, b=1.8, c=3.6))
## False

print('-' * 40)
print(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
# {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
print(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
# {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}
# print(triangle(p1=(2.5, 2), p2=(4, 1), p3=(1, 3)))
## ValueError: Треугольник не существует

print('-' * 40)
# Задание 4.8 (Вычисление радиуса)
def radius(p1, p2):
    # Проверка на входные параметры
    if (type(p1) is not tuple) or (type(p2) is not tuple):
        raise ValueError("Input args are not tuples!")
    # Точки окружности
    x1, y1 = p1
    x2, y2 = p2
    # Вычисляем радиус по формуле Пифагора
    # r = √(x2 - x1) ** 2 + (y2 - y1) ** 2
    radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return radius

print(radius(p1=(3, 2.5), p2=(4, 4.5)))
# 2.23606797749979
print(radius(p1=(0, 0), p2=(1, 1)))
# 1.4142135623730951

print('-' * 40)
# Задание 4.9 (Вычисление площади и периметра окружности)
def circle(p1, p2):
    # Проверка на входные параметры
    if (type(p1) is not tuple) or (type(p2) is not tuple):
        raise ValueError("Input args are not tuples!")
    global pi
    # Вычисляем радиус
    def radius(p1, p2):
        # Точки окружности
        x1, y1 = p1
        x2, y2 = p2
        # Вычисляем радиус по формуле Пифагора
        # r = √(x2 - x1) ** 2 + (y2 - y1) ** 2
        radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return radius

    # Вычисляем длинну окружности
    def calculate_circumference(radius):
        # функция для вычисления длины окружности (по сути периметра) по формуле: L = 2πr
        circumference = 2 * pi * radius
        return circumference

    # Вычисляем площадь окружности
    def calculate_area_circle(radius):
        # вычисления площади окружности по формуле: S = πr²
        area_circle = pi * radius ** 2
        return area_circle

    # Радиус
    radius = radius(p1, p2)
    # Длинна окружности
    circumference = calculate_circumference(radius)
    # Площадь окружности
    area_circle = calculate_area_circle(radius)

    result = {'radius': round(radius, 3), 'circumference' : round(circumference, 3), 'area': round(area_circle, 3)}
    return result

pi = 3.1416
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
# {'radius': 2.236, 'circumference': 14.05, 'area': 15.708}

pi = 3.1416
print(circle(p1=(0, 0), p2=(1, 1)))
# {'radius': 1.414, 'circumference': 8.886, 'area': 6.283}

pi = 3.14
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
# {'radius': 2.236, 'circumference': 14.043, 'area': 15.7}

print('-' * 40)
# * Задача 4.10 (Эллипс)
# Проверка является ли точка координата p1 центром эллипса
def check_ellipse_center(p1, p2, p3):
    h, k = p1
    x, y = p2
    a, b = p3
    # Вычисление с помощью уравнения эллипса
    # x^2 / a^2 + y^2 / b^2 = 1 (a, b - полуоси)
    try:
        p = ((x - h ** 2) / a ** 2) + ((y - k ** 2) / b ** 2)
    except ZeroDivisionError:
        p = 0
    finally:
        if (p > 1):
            return False
        if (p == 1):
            return False
        else:
            return True
def semi_axes(p1, p2, p3):
    # Проверка на входные параметры
    if (type(p1) is not tuple) or (type(p2) is not tuple):
        raise ValueError("Input args are not tuples!")
    # if check_ellipse_center(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Вычисляем длинны полуосей по теореме Пифагора
    # a = √(x2 - x1) ** 2 + (y2 - y1) ** 2 (√ - корень, ** 2 - в степени 2)
    # b = √(x2 - x1) ** 2 + (y2 - y1) ** 2 (√ - корень, ** 2 - в степени 2)
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # ( ** 0.5 - корень)
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5 # ( ** 0.5 - корень)
    return (a, b)
print(semi_axes(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5))) # (1.5, 1.0)
print(semi_axes(p1=(0, 0), p2=(0, 1), p3=(1, 0))) # (1.0, 1.0)

print('-' * 40)

pi = 3.1416
# * Задача 4.11 (Эллипс)
# Объемлющая функция по расчету площади и длинны окружности эллипса
def ellipse(p1, p2, p3):
    # Проверка на входные параметры
    if (type(p1) is not tuple) or (type(p2) is not tuple):
        raise ValueError("Input args are not tuples!")
    global pi

    # Функция проверки точки p1 на вхождение в эллипс
    def check_ellipse_center(p1, p2, p3):
        h, k = p1
        x, y = p2
        a, b = p3
        # Вычисление с помощью уравнения эллипса
        # x^2 / a^2 + y^2 / b^2 = 1 (a, b - полуоси)
        try:
            p = ((x - h ** 2) / a ** 2) + ((y - k ** 2) / b ** 2)
        except ZeroDivisionError:
            p = 0
        finally:
            if (p > 1):
                return False
            if (p == 1):
                return False
            else:
                return True

    # Функци вычисления полуосей
    def semi_axes(p1, p2, p3):
        # Проверка на входные параметры
        if (type(p1) is not tuple) or (type(p2) is not tuple):
            raise ValueError("Input args are not tuples!")
        # if check_ellipse_center(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        # Вычисляем длинны полуосей по теореме Пифагора
        # a = √(x2 - x1) ** 2 + (y2 - y1) ** 2 (√ - корень, ** 2 - в степени 2)
        # b = √(x2 - x1) ** 2 + (y2 - y1) ** 2 (√ - корень, ** 2 - в степени 2)
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # ( ** 0.5 - корень)
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5  # ( ** 0.5 - корень)
        return (a, b)

    # Функция для вычисления эллипса
    def calculate_area_ellipse(a, b):
        # Вычисление по формуле S = πab
        area = pi * a * b
        return area

    # Функция для вычисления длины окружности
    def calculate_length_ellipse(a, b):
        # Рассчитываеся по формуле L = 2 * pi √(a ** 2 + b ** 2) / 2
        length = (2 * pi) * ((a ** 2 + b ** 2) / 2) ** 0.5
        return length

    # Проверка если p1 центр эллипса
    if check_ellipse_center(p1, p2, p3):
        # Полуоси окружности
        a, b = semi_axes(p1, p2, p3)
        # Площадь окружности
        area = calculate_area_ellipse(a, b)
        # длинна окружности
        length = calculate_length_ellipse(a, b)
    return {'a': a, 'b': b, 'length': round(length, 3), 'area': round(area, 3)}

pi = 3.1416
print(ellipse(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5))) # {'a': 1.5, 'b': 1.0, 'length': 8.01, 'area': 4.712}
pi = 3.1416
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0))) # {'a': 1.0, 'b': 1.0, 'length': 6.283, 'area': 3.142}
pi = 3.14
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0))) # {'a': 1.0, 'b': 1.0, 'length': 6.28, 'area': 3.14}