# --Множества--
# Структура данных состоящая только из уникальных элементов.
# Типы внутри структуры могут только неизменяемые (числа, строки, кортежи), порядок элементов не фиксирован.

my_set_1 = set("Hello")
print(my_set_1) # {'H', 'l', 'e', 'o'}

# множество так же можно создавать с помощью фигурных скобок {}, однако внутри должен быть хотя бы один элемент иначе будет словарь
guess_dict = {}
print(type(guess_dict)) # <class 'dict'>
guess_set = {1}
print(type(guess_set)) # <class 'set'>

# --Методы множества SET--
# Add()
my_set_add = set([1,2,3])
my_set_add.add(4)
print(my_set_add)

# Update()
my_set_update = {1,2,3,4}
lst = [5,6,7,8,5,4,]
my_set_update.update(lst)
print(my_set_update) # при этом все элементы множества по прежнему будут уникальны

# Методы удаления Discard() и Remove()
# Отличия состоят в том, что если удаляемого элемента нет во множетстве, то:
# - Discard не выкинет ошибку (неявное)
# - Remove выкинет ошибку (явное)
# Какой метод использовать зависит от задачи, нужно ли отслеживать повторное удаление элемента или нет
my_set_discard = set([2,4,3,2,1,5])
my_set_discard.discard("Hello")
print(my_set_discard) # {1, 2, 3, 4, 5}

my_set_remove = set ([2,4,3,2,1,5])
#my_set_remove.remove("Hello!")
print(my_set_remove) # KeyError: 'Hello!'

# --Операции работы со множествами--
# Union (объединение) - при объединении двух множеств дубли не попадут в объединенное множество
cluster_1 = {"unit1","unit2","unit3","unit4"}
cluster_2 = {"unit2","unit3","unit5","unit7"}
united_cluster = cluster_1.union(cluster_2)
print(united_cluster) # {'unit7', 'unit4', 'unit3', 'unit5', 'unit1', 'unit2'} дубли отсутствуют

# Intersection (пересечение) - берутся только те элементы которые присутствуют в обоих множествах
cluster_1 = {"unit1","unit2","unit3","unit4"}
cluster_2 = {"unit2","unit3","unit5","unit7"}
intersected_cluster = cluster_1.intersection(cluster_2)
print(intersected_cluster) # {'unit2', 'unit3'} получили дубли обоих множеств

# Difference (разница между двумя множиствами) - выбираются только те элементы из первого множества которых нет во втором множестве
cluster_1 = {"unit1","unit2","unit3","unit4","unit5"}
cluster_2 = {"unit3","unit4","unit5","unit6"}
difference_cluster = cluster_1.difference(cluster_2)
print(difference_cluster) # {'unit2', 'unit1'}

# Issubset (является ли первое множетсво подмножеством второго) - все ли элементы из первого множества есть во втором множестве?
# Возвращает True/False
cluster_1 = {"unit1","unit2","unit3"}
cluster_2 = {"unit2","unit3","unit4","unit5","unit6"}
issubset_cluster = cluster_1.issubset(cluster_2)
print(issubset_cluster) # False (ответ верный, т.к в первом только три элемента совпадают со вторым, остальные вообще отсутствуют)

# --Приведение типов--

# 5 (int) - целочисленный тип
# 5.0 (float) - вещественный тип

# --Целые числа в числа в плавающей точкой--
# Явное преобразование
int_var = 10 # 10
float_var = float(10) # Явное, когда мы явно прописываем нужное для преобразования число 10 --> 10.0
print(float_var) # 10.0

float_var1 = 10.2 # 10.2
float_var2 = float(5) # 5 --> 5.0
print(float_var1 + float_var2) # 15.2

# Неявное преобразование
int_var = 5 # 5
float_var = 10.2 # 10.2
print(int_var + float_var) # 15.2 (интерпретатор сам неявно преобразовал int_var к числу с плавающей точкой)

# --Числа с плавающей точкой к целым числам--
float_var = 7.5 # 7.5
int_var = int(float_var) # 7.5 --> 7
# (функция int() не округляет, а «обрубает» вещественную часть.
# То есть после применения функции int() на числах 7.4, 7.6 на выходе получится одно и тоже число (7).)
print(int_var) # 7

# --Преобразование чисел в строки--
int_var = 5 # 5
str_var = str(int_var) # 5 --> '5'
print(f"result: {str_var}, type: {type(str_var)}") # result: 5, type: <class 'str'>

# Если нужно создать строку, которая будет содержать и строку, и числа, нужно сделать преобразование:
str_var_1 = "I am"
int_var = 10
str_var_2 = "years old"

# Если сложить три переменные (строку, число, строку) str_var1 + int_var + str_var2, получим ошибку
# TypeError: can only concatenate str (not "int") to str.
# Python неявно может преобразовывать числа, однако с числами и строками возникают проблемы, поэтому нужно привести число к строке
str_int_var = str_var_1 + str(int_var) + str_var_2
print(str_int_var) # I am10years old (без пробелов)

# --Преобразование строк в числа--
#my_date = "1990"
#mom_date = "1957"
# mom_date - my_date # TypeError: unsupported operand type(s) for -: 'str' and 'str' ошибка
# т.к. строки складывать нельзя, как и другие математические операции

my_date = "1990.0" # перепишем в вещественное число
mom_date = "1957"
int_mom_date = int(mom_date)
float_my_date = float(my_date)

# Если попытаться преобразовать целое (строчное) число в число с плавающей точкой, то можно получить ошибку
# ValueError: invalid literal for int() with base 10: ‘1990.0’

result_date = float_my_date - int_mom_date
print(result_date) # 33.0

# --Преобразование кортежей в списки--
# Можно использовать две функции (tuple() и list()) для преобразования структур в кортежи и списки.

dictionary = {"Anne": 15, "Sam": 30, "Marie": 22}
only_keys = dictionary.keys()
print(only_keys)

#only_keys = only_keys + ['Tom', 'Curt']
#print(only_keys) # # TypeError: unsupported operand type(s) for +: 'dict_keys' and 'list'

# Поскольку при использовании метода keys(), values() и т.д. на выход мы получаем свою структуру данных не совместимую
# напрямую со списками. Для того, что работать с полученным результатом необходимо привести этот тип данных к списку.
only_keys = list(only_keys)
only_keys = only_keys + ['Tom', 'Curt']
print(only_keys) # ['Anne', 'Sam', 'Marie', 'Tom', 'Curt']

# А что насчёт кортежей? Помните, мы обсуждали, что списки не могут выступать в качестве ключей словаря, а вот
# кортежи — могут? Представим, что мы получили список на вход, но очень хотим использовать его в качестве ключа.
my_dict = {("Amanda", 22, "NY"): "3rd place"}

# На вход получил список, но пока этот ключ в виде списка.
input_list = ["Collin", 23, "LA"]
# также определяем значение для нового ключа.
input_place = "2nd place"

#my_dict[input_list] = input_place # TypeError: unhashable type: 'list'
# Возникает ошибка, так как список не может быть ключом для словаря — нужно преобразовать список в кортеж:
input_list_as_tuple = tuple(input_list) # список в кортеж

my_dict[input_list_as_tuple] = input_place
print(my_dict) # {('Amanda', 22, 'NY'): '3rd place', ('Collin', 23, 'LA'): '2nd place'}

print("-----")
num = 15
result = "age is " + str(num)
print(result)

print("---Условные операторы---")
# --Условный операторы--
# выражение -->[операнд-->(x) оператор-->(+,-,>,< и т.д)<--оператор (y)<--операнд]
# Все операторы делятся на:

# Унарные — операторы, которые для своей работы требуют одно значение (операнд).
# Например, оператор not (логическое отрицание):
# not True

# Бинарные — операторы, которые для своей работы требуют два значения (операнда).
# Большинство операторов являются бинарными, например сложение, вычитание, деление и т.д.:
# 10 + 15

# Тернарные — операторы, которые возвращают свой второй или третий операнд в зависимости от значения логического выражения,
# заданного первым операндом. О них мы ещё поговорим отдельно, а пока приведём пример записи тернарного оператора:
# a = 1 if 2 > 3 else 0

# ----Операторы сравнения----
# < (меньше) будет true если [первый операнд] < (меньше) [второго операнда], иначе false
# > (больше) будет true если [первый операнд] > (больше) [второго операнда], иначе false
# <= (меньше либо равно) будет true если [первый операнд] <= (меньше либо равен) [второму операнду], иначе false
# >= (больше либо равно) будет true если [первый операнд] >= (больше либо равен) [второму операнду], иначе false
# == (равны) будет true если [первый операнд] == (оба равны) [второй операнд], иначе false
# != (не равны) будет true если [первый операнд] != (не равны) [второй операнд], иначе false

# Примеры
income_2019 = 15
income_2020 = 16.5
income_2021 = 16.5

# ==
print('==')
print(income_2019==income_2020) # False
print(income_2020==income_2021) # True

# !=
print('!=')
print(income_2019!=income_2020) # True
print(income_2020!=income_2021) # False

# >
print('>')
print(income_2019>income_2020) # False
print(income_2020>income_2021) # False

# <
print('<')
print(income_2019<income_2020) # True
print(income_2020<income_2021) # False

# <=
print('<=')
print(income_2019<=income_2020) # True
print(income_2020<=income_2021) # True

# >=
print('>=')
print(income_2019>=income_2020) # False
print(income_2020>=income_2021) # True

# cравнения строк
# При сравнении строк мы сравниваем не сами слова но цифровое представления букв
print(ord('A')) # 65
print(ord('a')) # 97

name_user_1029 = 'Andrey'
name_user_1040 = 'Vladimir'
name_user_1042 = 'Andrey'

print(name_user_1029==name_user_1040) # False
print(name_user_1029==name_user_1042) # True

# один и тот же текст в разных регистрах Python будет считать двумя различными не равными друг другу строками!
test_str_lower = 'hello_world'
test_str_upper = 'HELLO_WORLD'

print(test_str_lower==test_str_upper) # False

# --Сравнения коллекций--
# Равенство для упорядоченных коллекций объектов, таких как [списки] и [кортежи], означает полное равенство их содержимого
# и порядка элементов.

languages_list_1 = ['Python', 'C++', 'C#', 'Java']
languages_list_2 = ['Python', 'C++', 'C#', 'Java']
print(languages_list_1==languages_list_2) # True

# Равенство для неупорядоченных коллекций объектов, таких как [словари] и [множества], означает равенство их содержимого,
# порядок внесения элементов при создании коллекции значения не имеет.

store_list_1 = {'Яблоки': 158, 'Мандарины': 178, 'Хлеб': 56}
store_list_2 = {'Хлеб': 56, 'Яблоки': 158, 'Мандарины': 178}
print(store_list_1==store_list_2) # True

print("-----")

def is_palindrome(input_str):
    if input_str != "":
        target_str = input_str.lower().replace(" ", "")
        target_str_reversed = target_str
        if target_str==target_str_reversed[::-1]:
            return True
        else:
            return False
    else:
        print('error')

#target_string = 'кот кота ниже живота'
# result = False
target_string = 'коту тащат уток'
# result = True
#target_string = 'Шалаш'
# result = True
#target_string = 'кота тащат в шалаш'
# result = False
result = is_palindrome(target_string)
print(result)

# --Логические операторы--
# not - логическое "НЕ" возвращает противоположное значение, унарный оператор
if not (236 == "Hello"):
    print("Правда, число НЕ ЯВЛЯЕТСЯ строкой!")

# or - логическое "ИЛИ" возвращает True, если одна из хотя бы двух операндов True
num_1 = 5
num_2 = 15
if num_1 > 0 or num_2 > 0:
    print("Как минимум одно из чисел не является отрицательным!")

# and - логическое "И" возвращает True, если оба операнда True
num_1 = 10
num_2 = 10
if num_1 > 0 and num_1 == num_2:
    print("Оба числа не отрицательные и больше нуля и равны между собой")

# in, not in - "проверка принадлежности" возвращает True, если проверяемая переменная
# содержится/не содержится в последовательности (списки, кортежи, строке)
search_symbol = "e"
res_1 = search_symbol in "Hello"
res_2 = search_symbol in "python"
print(res_1 and res_2) # False т.к. во второй строке символа нет

# is, is not - "проверка тождественности" возвращает True, если проверяемые объекты эквивалентны/не эквивалентны т.е.
# если переменные ссылаются на один и тот же адрес в памяти (одинаковые идентификаторы)
a = "Alexander"
b = a
print(id(a), id(b)) # одинаковые идентификаторы участков памяти
print(a is b) # True

# Интересный момент!
# В целях оптимизации интерпретатор Python при инициализации создаёт некоторое количество
# часто используемых констант, например целые числа от -5 до 256 включительно.

# Проверяем равенство и эквивалентность двух объектов
x = 256
y = 256
print(x == y, x is y)
## True True

w = 257
v = 257
# Однако если мы выйдем за этот диапазон, то участки памяти для переменных будут разными!
# Проверяем равенство и эквивалентность двух объектов
print(w == v, w is v)
## True False

#a, b, c = 2, 5, 10
# result = False
#a, b, c = 3, 5, 8
# result = True
a, b, c = 1, 5, 8
# result = True

def is_checking_numbers(a, b, c):
    return a * a > b and a * a > c

result = is_checking_numbers(a,b,c)
print(result)

#diagnosis_1, diagnosis_2, diagnosis_3 = 'yes', 'yes', 'no'
# result = True
#diagnosis_1, diagnosis_2, diagnosis_3 = 'no', 'no', 'no'
# result = False
diagnosis_1, diagnosis_2, diagnosis_3 = 'no', 'no', 'yes'
# result = False

def is_deseased(diagnosis_1, diagnosis_2, diagnosis_3):
    return ('yes' in diagnosis_1 or 'yes' in diagnosis_2 or 'yes' in diagnosis_3)

result = is_deseased(diagnosis_1, diagnosis_2, diagnosis_3)
print(result)


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b, a == c, a is b, a is c)

# --Проверка на вхождение элемента в последовательность--
# -1.
orders = {
    '2022-10-10': ['F124', 'D89D', '142L'],
    '2022-10-11': ['H241', 'OR24', 'BE14', '348F'],
    '2022-10-12': ['H429', 'JAS2']
}

# Необходимо узнать, поступал ли за указанный период заказ с идентификатором 'BE14'.
target_order = 'BE14'

print(target_order in orders['2022-10-12']) # False
print(target_order in orders['2022-10-11']) # True
print(target_order in orders['2022-10-10']) # False

# Или можно объединить запрос (для переноса строк кода при объявлении переменных можно использовать обратный слэш (\).)
united_result = (target_order in orders['2022-10-12']) or \
                (target_order in orders['2022-10-11']) or \
                (target_order in orders['2022-10-10'])
print(united_result)

# -2.
message = 14093530013530593

# Необходимо выяснить содержит ли данное сообщение в первых 6 цифрах число 5
int_to_str = str(message) # переводим данное int число в строку, т.к. вхождение проверить на целом числе не возможно (это не последовательность)
print('5' in int_to_str[:6]) # True (проверяем '5' как строку, т.к мы число перевели в строку далее [:6] - первые 6 цифр)

# или если нам нужно исключить данное сообщение содержащее цифру 5, то
print('5' not in int_to_str[:6]) # False

# -3.1.
N = 12043879584

# Входят ли цифры 3 и 7 в последовательность
contains = ('3' in str(N)) and ('7' in str(N))
print(contains)

# -3.2.
# Координатам по горизонтальной и вертикальной осям шахматной доски, в которые должна переместиться фигура, соответствуют
# переменные x и y: x, y = 'F', 7
# условие проверки корректности хода. Ход считается корректным, если новые координаты фигуры не выходят за пределы шахматной доски.
x, y = 'F', 7

move_is_correct = ((x in "ABCDEFGH") and (str(y) in "1234567"))
print(f"move is correct: {move_is_correct}")

# --Проверка делимости чисел--

# В одной упаковке карандашей содержится 13 карандашей. Количество упаковок в наличии на складе хранится в переменной available_packages.
# Количество произведённых карандашей хранится в переменной total_count.
# Необходимо реализовать условие, которое проверяет, удастся ли распределить все карандаши по упаковкам без остатка и хватит ли упаковок вообще.

# -3.2.
available_packages = 105
total_count = 1677

# Удастся ли распределить все карандаши по упаковкам без остатка?
# Нам нужно узнать, делится ли число total_count на количество карандашей в упаковке — 13 без остатка:

# Проверяем, что все карандаши удастся распределить по упаковкам
condition_1 = total_count % 13 == 0 # True
print(condition_1)

#Хватит ли упаковок?
#Нам нужно нацело разделить общее количество карандашей на 13 и сравнить его со значением доступного количества упаковок:
# Проверяем, достаточно ли у нас упаковок на складе
condition_2 = total_count // 13 <= available_packages # False
print(condition_2)

# Объединение условия
result = condition_1 and condition_2
print(result)

# -3.3.
# Дано n-значное целое число N. Реализуйте условие для проверки того, начинается ли число N с четной цифры
N = 45901
first_num_str = str(N)[:1]
first_is_even = (int(first_num_str) % 2 == 0)
print(first_is_even)

# -3.4.
# Написать проверку, что год является високосным
# Известно, что год является високосным при выполнении хотя бы одного из следующих условий:
# - Номер года делится (без остатка) на 400.
# - Номер года делится (без остатка) на 4 и не делится на 100 одновременно.
year = 2015
r_1 = (year % 400 == 0)
r_2 = (year % 4 == 0) and not (year % 100 == 0)
r_3 = (year % 100 == 0)

year_is_leap = ((year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)))
print(year_is_leap)

# -3.5.
n, m, k = 5, 4, 25

# m - кол-во по вертикали
# n - кол-во по горизонтали
# k - кол-во долек после разделения шоколадки (по горизонтали или по вертикали)

choco_square = (n * m) # площадь всей шоколадки (общее кол-во долек)
condition_1 = (k <= choco_square) # Должно соблюдаться! True
# Чтобы можно было разделить шоколадку либо по вертикали, либо по горизонтали общее количество долек (k) должно нацело (//)
# делиться либо на кол-во по горизонтали (m), либо по вертикали (n)
condition_2 = (k % n == 0) or (k % m == 0) # Должно соблюлаться! True
result = condition_1 and condition_2
print(result)

# --Проверка эквивалентности--
# Одно из самых распространенных применений оператора is — так называемая "проверка на None".
# Этот подход имеет ещё одно преимущество в использовании, связанное с памятью. Оказывается, что в момент инициализации
# интерпретатора под объект None создаётся отдельная ячейка оперативной памяти и все переменные, объявленные как None,
# ссылаются на эту ячейку.
# Чтобы показать, что какое-то значение не определено (является пустым), в Python принято использовать не пустые строки,
# 0 или что-то ещё, а специальный объект — None, означающий пустоту.

# Кроме того, в проверке тождественности:
# my_value == None - НЕПРАВИЛЬНО!
# my_value is None - ПРАВИЛЬНО

unknown = 'jkdskjh'
print(type(unknown) is str) # True
print(type(unknown) is int) # False
print(type(unknown) is list) # False

# Функция print оказывается, тоже возвращает объект
lst = ['C++', 'Python', 'Java']
append_result = lst.append('C#')
print(append_result) # None

# Так же есть специальные методы которые вместо значения выдают None (get())
product_dict = {'Сок яблочный': 15, 'Сок тыквенный': 10, 'Сок ананасовый': 5}
value = product_dict.get('Сок яблочный')
print(value)

value_none = product_dict.get('Сок березовый')
print(value_none)

arrival_of_goods = {
    '148902': {
        'Футболка с принтом': 180,
        'Свитшот черный': 245,
        'Джинсы серые': 252
    },
    '893516': {
        'Футболка с принтом': 43,
        'Свитшот черный': 64,
        'Джинсы черные': 102
    },
    '893481': {
        'Кружка керамическая': 35,
        'Свитшот черный': 10,
        'Джинсы сервые': 14
    }
}

#invoice_number = '148902'
# invoice_exists = True

invoice_number = '892421'
# invoice_exists = False

invoice_exists = (arrival_of_goods.get(invoice_number) is not None)
print(invoice_exists)