# --Циклы--
# Вместо одно и того же действия прописывая построчно, необходимо использовать циклы например обход списка:
names_list = ["Alex", "Bella", "Claudia", "Dave", "Eatan", "Fox", "George", "Hellen"]
# Вместо
print("---Вместо---")
print(names_list[0], names_list[1], names_list[2]) # и т.д.
#  Цикл
print("---Цикл---")
for name in names_list: print(name)

# Надо отметить, что в python предусмотрено лишь два варианта циклов for и while

# --FOR--
# Говоря подробнее цикл выглядить так:
# for value in iterator:
    # тут "тело цикла"
    # some code (value)

# Итераторами могут быть разные структуры данных которые нам нужно проитерировать: list, tuple, string, dictionary или любые другие структуры данных
# Цикл будет работать проводить итерацию за итерацией пока не закончится список, после этого цикл завершится.

# ДЛИННАЯ ЗАПИСЬ	        СОКРАЩЁННАЯ ЗАПИСЬ
# value = value + a	        value += a
# value = value - a	        value -= a
# value = value / a	        value /= a
# value = value * a	        value *= a
# value = value ** a	    value **= a

# Задача 1
result = 0.0
incomes = [120, 38.5, 40.5, 80]
ite = 0
for elem in incomes:
    print(f"Current ite: {ite}")
    result += elem
    print(f"middle res: {elem}")
    ite = ite + 1

print(f"Total result is: {result}")

# Задание 2.2
p = 1
num_list = [98, 24, 23, 12, 3]
## p = 1947456

#num_list = [1, 10, 0.5, 21, 0.13]
## p = 13.65

for elem in num_list:
    p *= elem

print(p)
n = 10
natural_numbers = list(range(1, n + 1))
result = 0
for n in natural_numbers:
    result += n

print(result)

# Задание 2.4 (факториал числа)

n = 3
## p = 6
#n = 5
## p = 120
#n = 100
## p = 3628800

# C рекурсией
def factorial_recursion(n):
    if n == 1:
        return n
    return factorial_recursion(n - 1) * n

print(f"factorial_recursion: {factorial_recursion(n)}")

# С циклом
def factorial_cicle(n):
    for num in range(1, n):
        n = num * n

    return n

print(f"factorial_cicle: {factorial_cicle(n)}")

# Задание 2.5 (лесенка из символов *)

n = 3
#*
#**
#***

#n = 4
#*
#**
#***
#****

# С циклом
def print_stars(n):
    star = "*"
    for i in range(1, n + 1):
        print(star)
        star += "*"

print_stars(n)

# Задача 3 (распределение товаров по весу между автомобилями)
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
max_weight = 100
num = 1

print("---")
# Вариант 1
for weight in weight_of_products:
    if weight >= max_weight:
        print(f"грузовой автомобиль: product_number: {num}; weight: {weight}")
    else:
        print(f"легковой автомобиль: roduct_number: {num}; weight: {weight}")
    num += 1

print("---")
# Вариант 2 (по индексам списка)
num = 1
lst_leight = len(weight_of_products)
for elem in range(lst_leight):
    if weight_of_products[elem] >= max_weight:
        print(f"грузовой автомобиль: product_number: {num}; weight: {weight_of_products[elem]}")
    else:
        print(f"легковой автомобиль: roduct_number: {num}; weight: {weight_of_products[elem]}")
    num += 1

# Задача 4
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
]

location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
n = len(location)
for elem in range(n):
    country = location[places[elem]]
    if country != 'Russia':
        places[elem] = 'Unavailable'

print(places)

my_list = []
for number in range(0, 10):
    my_list.append(number**2)
print(my_list)

my_list = [1]
for elem in range(10):
    my_list.append(my_list[elem] * 2)

print(my_list)

print("----")
num_list = [1, 10, 3, -5]
## element 0: -5
## element 1: 1
## element 2: 3
## element 3: 10

num_list.sort()

elem = 0
for elem in num_list:
    print(f"element {elem}: {elem}")
    elem += 1

# Посчитать количество четных элементов
#num_list = list(range(0, 100, 3))
## count_even = 17

#num_list = [10, 4, 4, 21, 2, 0, -10]
## count_even = 6

#num_list = list(range(0, 81, 5))
## count_even = 9
count_even = 0
for elem in num_list:
    if elem % 2 == 0:
        count_even += 1

print(count_even)

# Посчитать количество элементов типа строка
#mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
## count_str = 3

mixture_list = ['My', 'Simple', -10, True, 'False', 'string_1', False, 2.5, [1, 2], 'True']
## count_str = 5
count_str = 0
for elem in mixture_list:
    if type(elem) is str:
        count_str += 1
print(count_str)

# Поставить вместо условного обозначения "EOS" точку, построить предложение с помощью цикла
word_list = ["My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
## text = "My name is Sergei. I'm from Moscow."

# word_list = ["Человек", "он", "умный", "EOS", "Но", "чтоб", "умно", "поступать", "одного", "ума", "мало", "EOS"]
## "Человек он умный. Но чтоб умно поступать одного ума мало."

text = ""
n = len(word_list)
for elem in range(n):
    if word_list[elem] == "EOS":
        text += "."
    else:
        text += " " + word_list[elem]
print(text)

print()
# -- Цикл while --
# Такой цикл ещё называют циклом с предусловием.
# Цикл while имеет следующий вид:
# while условие :
    # Начало блока кода с телом цикла
    # Пока условие истинно цикл выполняется
    # ...
    # Конец блока кода с телом цикла

# Пример:
lst = ['a', 'b', 'c', 'd', 'e', 'f']
# Создать цикл с условием, что длинна списка больше 2
while len(lst) > 2:
    lst.pop(0)
    print(lst)

# Еще один пример (нужно определить сколько раз добавить 2, чтобы x стало больше y)
x = 21
y = 55
# Количество итераций сколько раз необходимо пройтись циклу, чтобы x стал больше y
count = 0
# Т.е. мы говорим буквально следующее: выполняй цикл пока x не станет больше y
while x < y:
    x += 2
    count += 1

print(count)

# Задача 1
weight = 67
max_weight = 400
s = 0
while s < max_weight:
    s += weight
    print(f'Current weight is: {s}')
print(f'Overweight {s - max_weight} kg')

# Задача 3.2
volume = 10
## cost = 3.1999999999999993

# volume = 15
## cost = 1.5

cost = 0
while cost < volume:
    cost += 0.0033 * 1000

print(cost - volume)

# Задача 2 (складывать натуральные числа пока их сумма не превысит 500)

natural_numbers = list(range(1, 500))
count = 0
max_value = 500
ite = 0

while count <= max_value:
    count += natural_numbers[ite]
    ite += 1
    print("Still counting...")

# Отделяем промежуточный вывод от результата пустой строкой
print()
# Выводим результирующую сумму
print("Sum is: ", count)
# Выводим результирующее количество чисел
print("Numbers total: ", ite)

# Создаём накопительную переменную, в которой будем считать сумму.
S = 0
# Задаём текущее натуральное число
n = 1

# Создаём цикл, который будет работать, пока сумма не превысит 500.
while S < 500:  # делай, пока …
    # Увеличиваем сумму, равносильно S = S + n
    S += n
    # Увеличиваем значение натурального числа
    n += 1
    # Выводим строку ожидания
    print("Still counting...")
# Отделяем промежуточный вывод от результата пустой строкой
print()
# Выводим результирующую сумму
print("Sum is: ", S)
# Выводим результирующее количество чисел
print("Numbers total: ", n - 1)

# Задача 3.3
# value = 10
## number = 4

# value = 159
## number = 13

value = 1000
## number = 32

number = 0
while value > number ** 2:
    print(f"Степень 2: {number ** 2}")
    number += 1

print(number)

is_work = True
n = 1

# Задача 3

# secret_passwords = {
#     'Enot': 'ulybaka',
#     'Agent12': '1password1',
#     'MouseLulu': 'myshkanaruhka'
# }
#
# while True:
#     call_sign = str(input('Назовите свой позывной: '))
#     if call_sign in secret_passwords.keys():
#         password = str(input('Назовите свой пароль: ').lower())
#         if password in secret_passwords[call_sign]:
#             print("WELCOME TO THE CLUB!")
#             break
#         else:
#             print("Wrong password!")
#             # continue
#     else:
#         print("wrong call_sign!")
#         # continue

# Задание 3.4
value = 10
## number = 4

# value = 159
## number = 13

# value = 1000
## number = 32

number = 0
while True:
    print(f"Number: {number}")
    if value < number * number:
        break
    number += 1

# Задача 3.8 (выводит 'Hello' n раз)
n = 3
## Hello
## Hello
## Hello

# n = 5
## Hello
## Hello
## Hello
## Hello
## Hello

elem = 0
while elem < n:
    print('Hello')
    elem += 1

# Задача 3.9
## Введите свое решение ниже
n = 10
## 10
# n = 156
## 78
# n = 12
## 6

# Задаём начальное значение x
x = 1
# Создаём цикл, который будет выполняться до тех пор, пока квадрат x не будет нацело делиться на n.
while x ** 2 % n != 0:
    # Увеличиваем x на 1
    x += 1
# Выводим результат на экран
print(x)


# Задача 3.10
value = 1000
## p = 5040

# value = 178
## p = 720

# value = 10
## 24

n = 0
p = 1
while p < value:
    n += 1
    p = p * n

print(p)

# Задача 3.11
# money = 1000
# target_money = 3000
## year_count = 15

money = 8000
target_money = 15000
## year_count = 9

# money = 1500
# target_money = 300
## year_count = 0
year_count = 0
while target_money > money:
    money += money / 100 * 8 # прибавляем 8 процентов от суммы вклада
    year_count += 1

print(year_count)

# Задача 3.12
health = 500
damage = 80
## seconds_num = 7

# health = 3014
# damage = 174
## seconds_num = 18
seconds_num = 0
while health > 0:
    health -= damage
    seconds_num += 1

print(seconds_num)

# Задача 3.13 (числа Фибоначчи)
# n = 3
## fibonacci_list = [1, 1, 2]

n = 5
## fibonacci_list = [1, 1, 2, 3, 5]

# n = 9
## fibonacci_list =[1, 1, 2, 3, 5, 8, 13, 21, 34]
a = 1
b = 1
elem = 2
fibonacci_list = [a, b]
while elem < n:
    sum = a + b
    a = b
    b = sum
    elem += 1
    fibonacci_list.append(b)
print(fibonacci_list)

# -- Вложенные циклы --
# Для доступа к элементам:
# - по индексу строки
# - по индексу столбца

# Например:
# Данная "матрица" три строки и два столбца!
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

print('-------')
# Есть два способа "пройтись" по нашему списку с помощью цикла for
# 1
# row текущее значение из списка
for row in matrix:
    print(f'Current row {row}')
    # elem текущее значение из списка row (внутренний цикл)
    for elem in row:
        print(f'Current elem in row {elem}')

print('-------')
# 2 (циклы по индексам строк и столбцов)
N = len(matrix) # длинна внешнего списка
M = len(matrix[0]) # длинна внутреннего списка
# внешний цикл
for i in range(N):
    #print(f'iteration {i}')
    print(f'Current i {matrix[i]}')
    # внутренний цикл
    for j in range(M):
        #print(f'iteration {j}')
        print(f'Current j {matrix[i][j]}')

print("-------")
# Задача 1
# Задание: поставить будильники особым образом. Будильники должны звонить каждые пять часов, начиная с 10 часов утра.
# Причём будильник должен прозвенеть дважды в час с перерывом в полчаса. Например, в 15:00 и 15:30.
# hours — это будут числа в диапазоне от 10 до 24 с шагом 5 (в одних сутках 24 часа, и нам нужно ставить
# будильники каждые пять часов, начиная с 10 утра).
hours = list(range(10, 24, 5))

# minutes — это будут числа в диапазоне от 0 до 60 с шагом 30 (в одном часе 60 минут, и нам нужно ставить
# будильники каждые полчаса).
minutes = list(range(0, 60, 30))

for h in hours:
    for m in minutes:
        if m == 0: print(f'Alarm is set {h}:{m}{m}')
        else: print(f'Alarm is set {h}:{m}')

print("-------")
# Задание 4.2
# Пусть пользователь заводит будильники на каждые два часа, начиная с 9 часов утра. Причём будильники должны звонить
# четырежды в указанный час (интервал 15 минут), например в 11:00, 11:15, 11:30 и 11:45.
hours = list(range(9, 24, 2))
minutes = list(range(0, 60, 15))

for h in hours:
    for m in minutes:
        if m == 0: print(f'Alarm is set {h}:{m}{m}')
        else: print(f'Alarm is set {h}:{m}')

# Задача 2
# Вариант 1
# Дан список строк str_list = ['text', 'morning', 'notepad', 'television', 'ornament'].
# Необходимо подсчитать, сколько всего раз во всех строках списка встречается буква 'e'.
str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
count = 0
for elem in str_list:
    count += elem.count('e')
print(count)

print("-------")
# Вариант 2
count = 0
for word in str_list:
    for char in word:
        if char == 'e':
            count += 1
print(count)

print("-------")
# Задача 4.3
# Дан список строк text_list. Посчитайте, сколько раз во всех строках списка встречается буква 'a'.
text_list = [
    'afbaad',
    'faaf',
    'afaga',
    'agag'
]
count = 0
for word in text_list:
    count += word.count('a')
print(count)

# Задача 3 (Давайте попробуем реализовать алгоритм для поиска минимумов. Дана двумерная матрица 3x3 (список списков).
# Необходимо определить минимумы в каждой её строке.)
random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

print("-----")
# Вариант 1 (мой)
for num in random_matrix:
    num.sort()
    print(num[0])

print("-----")
# Вариант 2 (сложнее)
for row in random_matrix:
    min_value = row[0]
    for el in row:
        if min_value > el:
            min_value = el

    print(min_value)

# Вариант 2.1 (c записью минимальных значений в массив)
min_value_rows = []
for row in random_matrix:
    min_value = row[0]
    for el in row:
        if min_value > el:
            min_value = el

    min_value_rows.append(min_value)
print(min_value_rows)

# Задание 4.4 (найти максимумы в каждой строке двумерного массива)
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
## max_value_rows = [9, 5, 8]

random_matrix = [
    [9, 121, 1, 10, 42],
    [91, 5, 3, 34, -1],
    [-8, 98, 5, 24, -420]
]
## max_value_rows = [121, 91, 98]

print("-------------------------")
max_value_rows = []
for row in random_matrix:
    # row.sort()
    max_value = row[0]
    for num in row:
        if num > max_value:
            max_value = num
    max_value_rows.append(max_value)

print(max_value_rows)

print("---------------------------------")
# Задача 4 (даны данные пяти студентов по трем экзаменам, записаны в двумерный список)
# первый — математика, второй — информатика, третий — русский язык
# Необходимо найти средний балл студентов по каждому из экзаменов и общий средний балл по всем экзаменам.
student_scores = [
    [56, 90, 80],
    [80, 86, 92],
    [91, 76, 89],
    [91, 42, 60],
    [65, 30, 90]
]
# Вариант 1
count_of_students = len(student_scores) # кол-во студентов
count_of_exams = len(student_scores[0]) # кол-во экзаменов
math_exam = 0
info_exam = 0
rus_exam = 0
sum = 0
for exam in student_scores:
    math_exam += exam[0]  # математика (складываем все экзамены)
    info_exam += exam[1]  # информатика
    rus_exam += exam[2]  # русский
    for curr_score in exam:
        sum += curr_score
# Выводим средний балл по математике
print('Average math score', math_exam / count_of_students)
# Выводим средний балл по информатике
print('Average info score', info_exam / count_of_students)
# Выводим средний балл по русскому языку
print('Average rus score', rus_exam / count_of_students)
# Выводим общий средний балл
print('Average score', sum / (count_of_students * count_of_exams))

print("---------------------------------")
# Вариант 2
N = len(student_scores) # кол-во студентов
M = len(student_scores[0]) # кол-во предметов
math_sum = 0 # общее кол-во баллов по математике
info_sum = 0 # общее кол-во баллов по информатике
rus_sum = 0 # общее кол-во баллов по русскому языку
sum = 0 # общая сумма баллов
for i in range(N): # i — индекс строки
    math_sum += student_scores[i][0]   # общее кол-во баллов по математике
    info_sum += student_scores[i][1]  # общее кол-во баллов по информатике
    rus_sum += student_scores[i][2]   # общее кол-во баллов по русскому языку
    for j in range(M): # j — индекс столбца
        sum += student_scores[i][j]
# Выводим средний балл по математике
print('Average math score', math_sum / N)
# Выводим средний балл по информатике
print('Average info score', info_sum / N)
# Выводим средний балл по русскому языку
print('Average rus score', rus_sum / N)
# Выводим общий средний балл
print('Average score', sum / (N * M))

# Задание 4.8 (определить является ли матрица квадратной или нет. Квадратная - где кол-во строк совпадает с кол-вом столбцов)
# test_matrix = [
#     [1, 2, 3],
#     [7, -1, 2],
#     [123, 2, -1]
# ]
## is_square = True

# test_matrix = [
#     [1, 2, 3],
#     [7, -1, 2],
#     [123, 2, -1],
#     [123, 5, 1]
# ]
## is_square = False

test_matrix = [
    [1, 2, 3,  4],
    [7, -1, 2, 5],
    [123, 2, -1, 3],
    [123, 5, 1]
]
## is_square = False
is_square = None
N = len(test_matrix)
for i in range(N):
    M = len(test_matrix[i])
    if N == M:
        is_square = True
    else:
        is_square = False
print(is_square)

# Задача 4.9 (заменить все отрицательные значения на положительные)
temp = [[25, 27, 28, 26, 27, -26, -25, -2, 26],
        [21, 22, 28, 27, 28, 26, 25, 19, 26],
        [-19, 21, 25, -27, 28, 25, 21, 20, 26]]
# После обработки
## temp = [[25, 27, 28, 26, 27, 26, 25, 2, 26],
# [21, 22, 28, 27, 28, 26, 25, 19, 26],
# [19, 21, 25, 27, 28, 25, 21, 20, 26]]

N = len(temp)
M = len(temp[0])
for i in range(N):
    for j in range(M):
        if temp[i][j] < 0:
            temp[i][j] = -temp[i][j]
print(temp)

# * Задание 4.10
customer_satisfaction = [
    [0.87, 0.56, 0.77],
    [0.22, 0.46, 0.56, 0.89, 0.95],
    [0.45, 0.44, 0.68],
    [0.73, 0.88, 0.95, 0.49]
]

## month_satisfaction = [0.73, 0.62, 0.52, 0.76]
## max_satisfaction = 0.76
month_satisfaction = []
max_satisfaction = 0
sum = 0
for month in customer_satisfaction:
    count_of_scores = len(month)
    for score in month:
        sum += score
    average_value = (sum / count_of_scores)
    month_satisfaction.append(round(average_value, 2))
    sum = 0
print(month_satisfaction)
def find_max(array):
    max = array[0]
    for num in array:
        if num > max:
            max = num
    return max

print(find_max(month_satisfaction))
