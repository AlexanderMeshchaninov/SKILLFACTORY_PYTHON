# --- Библиотека Collections/NumPy ---

# NumPy позволяет проводить вычисления с однотипными наборами данных гораздо быстрее, чем с использованием встроенных возможностей Python.
# При решении рабочих задач скорость вычислений часто будет иметь критическое значение.
# К тому же NumPy вы будете использовать в машинном обучении, которое вам предстоит освоить в дальнейших модулях.

from collections import Counter

print('-' * 40)
# Создаем пустой экземпляр класса Collections
c = Counter()

c['Red'] += 1
print(c)
# С такой структурой данных как Counter так получится сделать.

print('-' * 40)
# Если попробовать сделать тоже самое со словарем, то
d = dict()

# При добавлении значения к ключу 'Blue' возникнет ошибка (KeyError: 'Blue'), т.к. ключ еще не будет создан, поэтому нужно добавить
d['Blue'] = 0
d['Blue'] += 1
print(d)

print('-' * 40)
# Еще пример
c = Counter()

cars = ['red', 'black', 'black', 'green', 'blue', 'white', 'red', 'red', 'yellow', 'green']
for car in cars:
    c[car] += 1
print(c)

print('-' * 40)
# Стоит отметить, что при использовании counter можно даже не писать цикл for в данном случае
car = Counter(cars)
print(car)

# Если нужно вывести определенный объект, то и даже если задать не существующий ключ, то ошибки не возникнет, как со словарем
print(car['black'])

# Если нужна сумма всех машин
print(sum(car.values())) # Всего 10 машин

print('-' * 40)
# Eще другой пример
cars_in_moscow = ['black', 'green', 'blue', 'white', 'red', 'black', 'black', 'green', 'blue', 'white', 'red', 'black', 'green', 'magenta', 'blue', 'white', 'red', 'yellow', 'green']
cars_in_spb = ['blue', 'white', 'blue', 'white', 'red', 'yellow', 'green', 'red', 'yellow','blue', 'white', 'red', 'yellow', 'green', 'green']

moscow_counter = Counter(cars_in_moscow)
spb_counter = Counter(cars_in_spb)

# Просто обычный вывод двух разных результатов
print(moscow_counter)
print(spb_counter)

print('-' * 40)
# Если обратить внимание, то в счетчике Москвы есть один цвет magenta. 
# В счетчике Спб его нет, однако и даже при таком варианте проблем не будет.
# Однако, если нам нужно сложить результат двух разных источников данных, то
print(moscow_counter + spb_counter) 

print('-' * 40)
# Стоит отметить, что если мы воспользуемся обычной операцией вычитания, то отрицательных значений не будет
print(moscow_counter - spb_counter)

print('-' * 40)
# Если нам нужно вычесть результаты из двух счетчиков (из счетчика Москвы вычитаем Спб)
moscow_counter.subtract(spb_counter)
print(moscow_counter) # Появились отрицательный значения, это происходит потому, что данных цветов в счетчике Спб больше чем в Moscow

print('-' * 40)
# После оперций вычитания нужно заново инициализировать результаты
cars_in_moscow = ['black', 'green', 'blue', 'white', 'red', 'black', 'black', 'green', 'blue', 'white', 'red', 'black', 'green', 'magenta', 'blue', 'white', 'red', 'yellow', 'green']
cars_in_spb = ['blue', 'white', 'blue', 'white', 'red', 'yellow', 'green', 'red', 'yellow','blue', 'white', 'red', 'yellow', 'green', 'green']

moscow_counter = Counter(cars_in_moscow)
spb_counter = Counter(cars_in_spb)

# Если нужно вывести все "ключи" счетчика
print(*moscow_counter.elements()) # Выводится в алфавитном порядке, но с соблюдением колиства элементов

# Если нужно получить уникальные элементы, просто добать счетчик в список
print(list(moscow_counter))

# Преобразовать в словарь
print(dict(moscow_counter))

print('-' * 40)
# Если нужно получить часто встречающиеся элементы
print(moscow_counter.most_common())
print('-' * 40)
# или
print(moscow_counter.most_common(2)) # наиболее часто встречающиеся значения, считается от введенного N

# Clear
moscow_counter.clear
spb_counter.clear

print('-' * 40)
from collections import defaultdict
# --- Default Dict ---
# Словарь который позволяет задать структуру данных по-умолчанию, которая будет в нем храниться
#  Cловарь содержащий кортежи студентов (фамилия, номер группы)
students = [('Ivanov', 1),('Smirnov', 4),('Petrov', 3),('Kuznetsova', 1),('Nikitina', 2), ('Markov', 3), ('Pavlov', 2)]

groups = dict()
# Нам необходимо например получить словать где ключом является номер группы, а значением студенты {1: ('Ivanov',' Kuznetsova')}
# Если использовать стандартные методы
for student, group in students:
    if group not in groups:
        groups[group] = list()
    groups[group].append(student)

print(groups)

print('-' * 40)
# Та же задача с помощью defaultdict (отсутствует проверка if). 
# По-умолчанию в контруктор класса defaultdict устанавливаем тот тип данных который нужен
groups_def_dict = defaultdict(list)

for student, group in students:
    groups_def_dict[group].append(student)

print(groups_def_dict)
d = defaultdict()
print(d)

# Далее можно пользовать методами словарей, однако с defaultdict если запросили несуществующий ключ, то ошибки не будет, будет []

print('-' * 40)
# --- OrderDict ---
from collections import OrderedDict

# OrderDict в отличие от обычного встроенного словаря гарантирует, что порядок ключей при выводе будет сохраняться в той 
# последовательности в которой их туда добавили
# Нужно отметить, что функционал гарантированного вывода элементов до версии python 3.7 не было, поэтому если нужен такой
# функционал в работе более ранних версиях python, то стоит использовать OrderDict
# Это важно для обратной совместимости, то есть для корректной работы программы со старыми версиями интерпретатора.

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]

client_ages_dict = dict(data)
print(client_ages_dict)

# Создаем OrderDict
# Сортируем по второму значению (возрасту)
client_ages_ord_dict = OrderedDict(sorted(data, key=lambda x: x[1]))
print(client_ages_ord_dict)

print('-' * 40)
from collections import deque
# --- Deque (очередь) ---
# Класс Deque в python объединяет в себе как Stack, так и Deque т.е. очередь

# Очередь — это упорядоченный тип данных, который обладает двумя ключевыми функциями: добавление 
# элемента в конец очереди и извлечение самого первого элемента из очереди. То есть очередь 
# подразумевает, что тот элемент, который первым добавлен в очередь, будет первым потом и обработан. 
# Всё как в обычной очереди! Этот принцип сокращённо также называется FIFO (от англ. First In — First Out, 
# «первым пришёл — первым ушёл»).

# Стек (от англ. stack — стопка) — это упорядоченный тип данных, который обладает двумя основными функциями: 
# добавление элемента в конец стека и извлечение элемента из конца стека. Эта структура данных также называется 
# рюкзаком. Действительно, представьте себе, что вы набили вещами рюкзак. Теперь, когда вы решите достать из него 
# самую верхнюю вещь, что это будет за вещь? Верно — та самая, которую вы убрали в рюкзак последней. Поэтому принцип 
# стека (рюкзака) также сокращённо называется LIFO (Last In — First Out, «последним пришёл — первым ушёл»).

dq = deque()
print(dq) #deque([])

# В очередь можно выставлять ее размер, например
dq_max3 = deque(maxlen=3)
print(dq_max3)

print('-' * 40)
# Пример
clients = deque()

# Добавляем клиентов
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Meshchaninov')
clients.append('Sidorova')
print(clients)

# К очереди можно обращаться по элементу
print(clients[2]) # Meshchaninov

print('-' * 40)
# Выборку элементов можно делать с помощью метода popleft()
first_client = clients.popleft()
second_client = clients.popleft()
print(f'first_client {first_client}')
print(f'second_client {second_client}')

print(clients) # deque(['Meshchaninov', 'Sidorova'])
# Таким образом popleft убирает из очередь элементы слева

print('-' * 40)
# Если есть необходимость добавить элемент в очередь (в начало), нужно воспользовать методом appendleft()
clients.appendleft('Pupkin')
clients.appendleft('Tikhomirov')

print(clients) # deque(['Tikhomirov', 'Pupkin', 'Meshchaninov', 'Sidorova'])

print('-' * 40)
# С помощью функции pop() можно удалить элемент с правого конца очереди
clients.pop()

print(clients) # deque(['Tikhomirov', 'Pupkin', 'Meshchaninov']), удалили Sidorova

print('-' * 40)
# Если есть необходимость добавления (расширения очереди) с помощью другого итерируемого объекта, то сделать
# это можно с помощью метода extend()
initial_data_deque = deque([1,2,3,4,5,6,7,8,9,10])
other_data_deque = deque([11, 12, 13, 14, 15])

# В этом случае объекты добавяться вправо
initial_data_deque.extend(other_data_deque)
print(initial_data_deque) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print('-' * 40)
# Есть есть необходимость добавить список справа, то можно воспользоваться методом extendleft, однако есть особенность
initial_data_deque.extendleft(other_data_deque)

print(initial_data_deque) # deque([ ---> 15, 14, 13, 12, 11, < --- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print('-' * 40)
# Очередь с ограниченной длинной
dq_max3 = deque(maxlen=3)
print(dq_max3) # deque([], maxlen=3)

print('-' * 40)
# Если сделать так, то в очереди останутся последние три элемента, остальные 
# не попадут в очередь и ошибки не будет
dq_max3 = deque([1,2,3,4,5], maxlen=3)
print(dq_max3) # deque([3, 4, 5], maxlen=3)

print('-' * 40)
# Еще пример
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

# Посчитаем динамику средней температуры с усреднением за каждые последние 7 дней для каждого рассматриваемого дня. 
# Для этого воспользуемся очередью с параметром maxlen=7
seven_days = deque(maxlen=7)

for temp in temps:
    # Добавляем температуру в очередь
    seven_days.append(temp)
    # Если длинна очереди оказалась длинне 7 дней, то мы печатаем среднюю температуру за 7 дней
    if len(seven_days) == seven_days.maxlen:
        # Округляем, получаем среднюю температуру
        print(round(sum(seven_days) / len(seven_days), 2), end='; ')
print("")

print('-' * 40)
dq = deque([1,2,3,4,5])
# Для очередей есть другие методы
# Развернуть очередь
dq.reverse()
print(dq) # deque([5, 4, 3, 2, 1])

print('-' * 40)
dq = deque([1,2,3,4,5])
print(dq) # до переноса deque([1, 2, 3, 4, 5])
# Развернуть очередь
# с помощью rotate(2) можно перенести элементы с левой части в правую в скобках указывается 
# кол-во элементов которые нужно перенести
dq.rotate(2)
print(dq) # после переноса deque([4, 5, 1, 2, 3])

print('-' * 40)
dq = deque([1,2,3,4,5])
print(dq) # до переноса deque([1, 2, 3, 4, 5])
# Развернуть очередь
# с помощью rotate(-2) можно перенести элементы с правой части в левую т.е. конец очереди в скобках указывается отрицательное значение
# кол-во элементов которые нужно перенести
dq.rotate(-2)
print(dq) # после переноса deque([3, 4, 5, 1, 2])

print('-' * 40)
dq = deque([1,2,3,4,5,3,3,3])
# Для очереди используются те же методы, что и для списков, например count(3)
# с помощью которого можно получить количество вхождений данного элемента в очередь
print(dq.count(3)) # три элемента входят в очередь

print('-' * 40)
dq = deque([1,2,3,4,5,3,3,3])
# Для очереди используются те же методы, что и для списков, например index(3)
# с помощью которого можно получить первое вхождение данного элемента в очередь
print(dq.index(3)) # 2

# Стоит отметить, что если запросить не существующий элемент, то как и в списке, возникнет ошибка ValueError

print('-' * 40)
# Очередь можно очистить с помощью clear
dq.clear()
print(dq) # deque([])

print('-' * 40)
# Задание 3.2
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
# Напишите функцию check(temps), которая будет выводить словарь, 
# в котором ключи — годы, а значения — показатели температуры. 
# Ключи необходимо отсортировать в порядке убывания соответствующих им температур.

def check_temps(temps):
    return OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))

print(check_temps(temps))
# OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

print('-' * 40)
# Задание 4.3
# Вариант 1
# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок line правильной
def brackets(line):
    try:
        stack = deque()
        for s in line:
            # Если скобка открывающаяся кладем ее в стек (т.е. в конец)
            if s == '(': 
                stack.append(s)
            # Если скобка закрывающаяся извлекаем из стека (т.е. из конца)
            if s == ')': 
                stack.pop()
        # Символы в строке line закончились и стек пустой, то правильная последовательность
        if len(stack) == 0:
            return True
        # Символы в строке line закончились и стеке остались скобки, то последовательность неправильная
        else: 
            return False
        # При попытки извлечения из стека отсутствующего элемента 
        # (в данном случае если стек пустой, то есть извлечь скобку нельзя, последовательность неправильная)
    except IndexError:
        return False
        
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False

print('-' * 40)
# Вариант 2
def brackets(line):
    # Напишите тело функции
    stack = deque()
    for i in line:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False

print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False

print('-' * 40)
# Задание 4.9
# Дан список кортежей ratings с рейтингами кафе. Кортеж состоит из названия и рейтинга кафе.
# Необходимо отсортировать кортеж по убыванию рейтинга. Если рейтинги совпадают, то отсортировать 
# кафе дополнительно по названию в алфавитном порядке.

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

cafes = sorted(ratings, key=lambda x: (-x[1], x[0]))
print(cafes)

# OrderedDict([('WokAndRice', 4.9), ('WokToWork', 4.9), ('General Foods', 4.8), 
# ('New Age', 4.6), ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), 
# ('CakeTime', 4.1), ('Nice Cakes', 3.9), ('Old Gold', 3.3), ('Old Wine Cellar', 3.3), ('Old York', 3.3)])

print('-' * 40)
# Задание 4.10

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False),
(50000, 'voltage', True)]

def task_manager(tasks):
    tasks_dict = defaultdict(deque)
    
    for task in tasks:
        task_number, server_name, priority  = task

        if priority:
            tasks_dict[server_name].appendleft(task_number)
        else:
            tasks_dict[server_name].append(task_number)
            
    return tasks_dict

print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})

print('-' * 40)
# --- Модуль Numpy ---
# Импортируем numpy
import numpy as np
# Данная библиотека предназначена для точной и быстрой работы с числами

# Небольшое отступление, для информации:
# Информация обрабатывающаяся процессором состоит из последовательностей 0101010101100010101010...
# 0 или 1 - бит;
# 01010101 - это 1 байт (последовательность из 8 битов)
# 1 байт может содержать в себе 256 различных чисел - последовательностей

# Чтобы узнать сколько чисел поместится в 1 бите можно вычеслить по формуле 2 ** (кол-во бит)
# Nmin = - (2 ** n) / 2
# Nmax = (2 ** n) / 2 - 1
print('-8-')
bit_8 = (2 ** 8) / 2 - 1
print(bit_8)
print()

print('-16-')
bit_16 = (2 ** 16) / 2 - 1
print(bit_16)
print()

print('-32-')
bit_32 = (2 ** 32) / 2 - 1
print(bit_32)
print()

print('-64-')
bit_64 = (2 ** 64) / 2 - 1
print(bit_64)
print()

print('-128-')
bit_128 = (2 ** 128) / 2 - 1
print(bit_128)
print()

print('-' * 40)
# --- INT ---
# тут мы явно опеределяем тип данных причем это int8
# int - тип данных, а 8 сколько бит памяти отводится переменной т.е. 8 бит
a = np.int8(25)
print(a) # 25 
print(type(a)) # <class 'numpy.int8'>

print('-' * 40)
# Для определения возможностей того или иного типа данных можно использовать методы iinfo(), finfo() и т.д.
print(np.iinfo(np.int8)) # Для типа int
print(np.iinfo(a))

print('-' * 40)
# В NumPy доступны и беззнаковые целочисленные типы данных. Они имеют корень uint (unsigned int — беззнаковое целое). 
# uint доступны также с выделением памяти в 8, 16, 32 и 64 бита. При этом максимально возможное число оказывается 
# в два раза больше, чем для соответствующего int, поскольку отрицательные числа исключены из типа данных uint.
b = np.uint8(132)
print(b) # 30
print(np.iinfo(np.uint8))

print('-' * 40)
# Стоит обратить внимание на следующую особенность, например
numpy_int = np.int32(1_000)
print(numpy_int, type(numpy_int)) # Тип данных int32 формат numpy
# Однако, если поместить в эту же переменную просто число 1_000
numpy_int = 1_000
print(numpy_int, type(numpy_int)) # Тип данных привычный python просто int

# Если совершать математические действия с numpy типами данных
a = np.int32(500)
b = a + 50 # 50 при сложении число 50 представляется в numpy представлении как дефолтное - int64
print(b, type(b)) # 550 <class 'numpy.int64'>
# Почему int32 поменялся на int64? По-умолчанию для int типа данных в numpy отводится 64 бита памяти

print('-' * 40)
# Еще пример
a = np.int32(1_000)
b = np.int8(25)
c = a + b
print(c, type(c)) # 1025 <class 'numpy.int32'>
# В данном случае при сложении двух numpy типов данных будет выбран старший т.е. не int8, а int32.

print('-' * 40)
# Если складывать например два numpy типа данных с пограничными для них значениями, то получится 
# "переполнение типов" и ответ будет не корректным!
#a = np.int8(250)
#b = np.int8(255)
#c = a + b
#print(c, type(c)) # -7 <class 'numpy.int8'> (will give the desired result (the cast overflows))

print('-' * 40)
# --- FLOAT ---
a16 = np.float16(4.12)
print(a16, type(a16))
print(np.finfo(a16))

print('-' * 40)
a32 = np.float32(4.12)
print(a32, type(a32))
print(np.finfo(a32))

print('-' * 40)
# Стоит иметь ввиду, что если указанное число не влезает в тот объем данных который мы указали, то точность не сохраняется
print(np.float16(4.13)) #4.13
print(np.float16(4.123)) # 4.12
print(np.float16(4.124)) # 4.125
print(np.float16(4.125)) # 4.125

print('-' * 40)
# Посмотреть все типы данных в библиотеки numpy можно с помощью метода sctypeDict()
#print(np.sctypeDict)
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
print('-' * 40)
# Стоит отметить, что в numpy есть также тип bool, однако пишется как bool_
is_num_bool = np.bool_(True)
print(is_num_bool, type(is_num_bool))

# int8
a = np.int8(124)
print(a, np.iinfo(a))

# uint8
a = np.uint8(124)
print(a, np.iinfo(np.uint64))

print(np.finfo(np.float128))

print('-' * 40)
# --- Numpy массивы ---
# массив - упорядоченный набор однотипных данных
# Чтобы получить массив (напоминание самому себе, массив в отличии от 
# списков и подобных им структур, хранит данные только одно типа)
# одномерный
arr = np.array([1,2,3,4,5,6,8,9,10])
print(arr.dtype) # int64 тип данных (по-умолчанию)
print(arr, type(arr)) # [ 1  2  3  4  5  6  8  9 10] <class 'numpy.ndarray'> nd означает n dimensional (n мерный)

print('-' * 40)
# Двухмерный массив
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [8,9,10]])
print(arr2d, type(arr2d)) # [[ 1  2  3][ 4  5  6][ 8  9 10]] <class 'numpy.ndarray'>

print('-' * 40)
# Особенность! Если мы вносим изменение в массив c опредленным типом данных
arr = np.array([1,2,3,4,5], dtype=np.int8)
arr[2] = 2000
print(arr, type(arr), arr.dtype) # [  1   2 -48   4   5] <class 'numpy.ndarray'> int8
# Как видно по выводу 2000 просто не влезло в тот тип, который мы установили (int8), поэтому -48

print('-' * 40)
# Можно сделать преобразование действующего массива в другой тип
arr_float128 = np.float128(arr)
print(arr_float128, type(arr_float128), arr_float128.dtype)

print('-' * 40)
# Еще пример
arr_1d = np.array([12321, -1234, 3435, -214, 100], dtype=np.int32)
print(arr_1d, arr_1d.dtype)
# А теперь об "артефактах", если мы преобразуем из типа int32 в тип int8 т.е. 
# в меньший по объему тип данных, то некоторые числа не влезут
print(np.int8(arr_1d)) # [ 33  46 107  42 100]

print('-' * 40)
# Методы работы с массивами в numpy
# Одномерный массив
arr_1d = np.array([1,2,3,4,5], dtype=np.int8) 

# C помощью метода ndim можно узнать размерность массива
print(arr_1d.ndim) # 1
# Кол-во элементов в массиве
print(arr_1d.size) # 5
# Shape возвращает форму массива в виде кортежа
print(arr_1d.shape) # (5,) - формат кортежа
print(arr_1d.itemsize) # Сколько байт отведено для чисел в пямяти (1 байт = 8 бит, все верно)

print('-' * 40)
# Двумерный массив
arr_2d = np.array([[11,22,33],
                   [55,66,77],
                   [99,10,11],
                   [13,23,45]], dtype=np.int16)

print(arr_2d.ndim) # 2
print(arr_2d.size) # 12
print(arr_2d.shape) # (4,3) - формат кортежа (4 - строки, 3 - столбцы)
print(arr_2d.itemsize) # Сколько байт отведено для чисел в пямяти (2 байта = 16 бит, все веrрно)

print('-' * 40)
# Посколько создать пустой массив сразу не предствляется возможным, а заранее знать числа тоже не всегда удается. 
# Для этого есть метод zeros
arr_1d = np.zeros(5)
print(arr_1d) # [0. 0. 0. 0. 0.]
arr_3d = np.zeros((3,4,5), dtype=np.int32) # - (3 уровня, 4 строки в каждом уровне, 5 столбцов в каждом уровне)
print(arr_3d)

print('-' * 40)
# Можно задать числа автоматом, например задав правую границу от 0....до N не включительно
print(np.arange(5)) # [0 1 2 3 4]

print('-' * 40)
# В отличие от стандартного arange в numpy можно задавать дробные числа
print(np.arange(4.5, 10, dtype=np.float16)) # [4.5 5.5 6.5 7.5 8.5 9.5]

print('-' * 40)
# Чтобы задать шаг нужно вверсти третий аргумент
print(np.arange(1, 11, 2)) # [1 3 5 7 9]

print('-' * 40)
# Документация numpy не рекомендует использовать в качестве шага дробные числа, лучше вместо этого использовать
# linspace
# (начало, конец, то число элементов которые хотим получить)
print(np.linspace(1, 2, 10)) # [1.         1.11111111 1.22222222 1.33333333 1.44444444 
# 1.55555556 1.66666667 1.77777778 1.88888889 2.        ]

print('-' * 40)
print(np.linspace(1, 2, 10, endpoint=False)) # endpoint=False должен ли последнее число содержать правую границу 

print('-' * 40)
# Чтобы получить информацию о шаге
arr, step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
print(arr)
print(step) # Получаем шаг 0.1

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step, 2))

print('-' * 40)
# --- Действия с массивами ---
arr = np.arange(8)
print(arr) # [0 1 2 3 4 5 6 7]
# Если есть необходимость другую форму массива (из 1d в 2d например), можно воспользоваться shape

arr.shape = (2, 4)
print(arr) # [[0 1 2 3] [4 5 6 7]]

print('-' * 40)
# Если нужно на основе предыдущего создать новый массив, то можно воспользоваться методом reshape
arr = np.arange(16)
print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

arr_new = arr.reshape(2, 8)
print(arr_new) # [ 0  1  2  3  4  5  6  7] [ 8  9 10 11 12 13 14 15]]

print('-' * 40)
# В отличие от shape, reshape имеет ряд дополнительных аргументов, например с помощью order='F'
# можно поменять логику создания массива, в данном случае массив числа получили форму по столбцам
print(arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
arr_new_2 = arr.reshape(2, 8, order='F')
print(arr_new_2) 
# [[ 0  2  4  6  8 10 12 14]
# [ 1  3  5  7  9 11 13 15]]

print('-' * 40)
# Транспонирование - замена строк и столбцов местами. Метод не меняет исходный массив, а создает новый
arr.shape = (2, 8)
print(arr)
# [[ 0  1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14 15]]
arr_transpose = arr.transpose()
print(arr_transpose)
# [[ 0  8]
#  [ 1  9]
#  [ 2 10]
#  [ 3 11]
#  [ 4 12]
#  [ 5 13]
#  [ 6 14]
#  [ 7 15]]

print('-' * 40)
# Индексация и срезы массивов
arr = np.linspace(1, 2, 6)
print(arr) # [1.  1.2 1.4 1.6 1.8 2. ]
# Чтобы получить элемент, традиционно смотрим по индексу
print(arr[2]) # 1.4

print('-' * 40)
# Также можно использовать срезы
print(arr[2:4]) # [1.4 1.6]
# С помощью срезов так же как и в стандартном python можно реверсировать массив
print(arr[::-1]) # [2.  1.8 1.6 1.4 1.2 1. ]

print('-' * 40)
# Еще пример
nd_array = np.linspace(0, 6, 12, endpoint=False).reshape(3, 4)
print(nd_array)
# [[0.  0.5 1.  1.5]
#  [2.  2.5 3.  3.5]
#  [4.  4.5 5.  5.5]]

print('-' * 40)
# Получение элемента из двухмерного массива
print(nd_array[2][2]) # 5.0
# более элегантное решение
print(nd_array[2, 2]) # 5.0

print('-' * 40)
# Например нам нужно получить срез например от первого "измерения" до конца элементы с 0 по 2 т.е. 0, 0.5, 2, 2.5, 3, 4.5
print(nd_array[0:, 0:2])


print('-' * 40)
# Сортировка массива
arr = np.array([0,10,2,3,1,4,6,78,9,11,2,3,4,4,4,10,12])
print(arr) # [ 0 10  2  3  1  4  6 78  9 11  2  3  4  4  4 10 12]
arr_sorted = np.sort(arr)
print(arr_sorted) # [ 0  1  2  2  3  3  4  4  4  4  6  9 10 10 11 12 78]

# Если же нужно отсортировать исходный массив, то просто применить метод к переменной без присвоения
arr.sort()
print(arr)

# Чтобы извлеч квадратные корени из элементов массива
arr = np.linspace(1, 24)
roots = np.sqrt(arr)
print(roots)

# nan (None) - в библиотеки numpy особый формат числа, он указывает на отсутствие числа в модуле numpy
print(type(np.nan)) # Причем это не просто специальный тип данный, как в python, а этом тип float


# (== это оператор сравнения, который проверяет равенство значений двух объектов (object equality))
# is это оператор, который проверяет идентичность двух объектов (object identity). Здесь проверяется, 
# что обе переменные указывают на один и тот же объект в памяти.

# Интересные особенности
print(type(None), None == None) # <class 'NoneType'> True 
print(None is None) # True (Здесь ссылаются на одну и ту же область памяти)

print(type(np.nan), np.nan == np.nan) # <class 'float'> False (Здесь ссылки не равны, области памяти разные)
print(np.nan is np.nan) # True (Здесь ссылаются на одну и ту же область памяти)

# Можно применить данный тип nan к массиву, чтобы посмотреть есть ли в нем этот тип
arr = np.linspace(1, 30)
print(np.isnan(arr)) # Вернется массив из bool

arr_2 = np.array([1,2,3,4,5,6,7,8,9,10, np.nan, np.nan, np.nan])
print(np.isnan(arr_2))

# Этот функционал можно применять следующим образом, заменим np.nan числом, однако надо иметь ввиду, 
# что все nan в массиве будут заменены на наше число
arr_2[np.isnan(arr_2)] = 600
print(arr_2)

print('-' * 40)
# Задание 7.2
mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

# Провести с этим массивом следующие манипуляции:
# 1. В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца
# 2. В переменную last сохраните элемент из последней строки последнего столбца
# 3. В переменную line_4 сохраните строку 4
# 4. В переменную col_2 сохраните предпоследний столбец
# 5. Из строк 2-4 (включительно) получите столбцы 3-5 (включительно). Результат сохраните в переменную part
# 6. Сохраните в переменную rev последний столбец в обратном порядке
# 7. Сохраните в переменную trans транспонированный массив

elem_5_3 = mystery[4, 2]
print(elem_5_3) # 30305
last = int(mystery[-1:, -1:])
print(last) # -32037
line_4 = mystery[3, :]
print(line_4) # [13240  7994 32592 20149 13754 11795  -564]
col_2 = mystery[:, -2:-1]
print(col_2.reshape(len(col_2)))
# [[-17182]
#  [ 15790]
#  [ 25397]
#  [ 11795]
#  [ 12578]
#  [   -47]]
part = mystery[1:4, 2:5]
print(part)
# [[-1297 -4593  6451]
#  [28655 -6012 21762]
#  [32592 20149 13754]]
rev = mystery[:, -1:]
print(rev[::-1])
trans = mystery.transpose()
print(trans)

print(np.nan is np.nan)

print('-' * 40)
# Задание 7.4
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

# 1 Получите булевый массив nans_index с информацией о np.nan в массиве mystery: 
#   True - значение пропущено, False - значение не пропущено

# 2 В переменную n_nan сохраните число пропущенных значений

# 3 Скопируйте массив mystery в массив mystery_new. 
#   Заполните пропущенные значения в массиве mystery_new нулями

# 4 Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int

# 5 Отсортируйте значения в массиве mystery по возрастанию и сохраните результат в переменную array

# 6 Сохраните в массив table двухмерный массив, полученный из массива array. 
#   В нём должно быть 5 строк и 3 столбца. 
#   Причём порядок заполнения должен быть по столбцам!

# 7 Сохраните в переменную col средний столбец из table

# 1
nans_index = np.isnan(mystery)

# 2
n_nan = len(mystery[np.isnan(mystery)])

# 3
mystery_new = np.array(mystery, copy=True)
mystery_new[np.isnan(mystery_new)] = 0

# 4
mystery.dtype = np.int32
mystery_int = np.array(mystery)
mystery.dtype = np.float32

# 5
array = np.sort(mystery)

# 6
table = np.reshape(array, (5, 3), order='F')

# 7
table_col = table[:, 1:2]
col = np.reshape(table_col, (len(table_col),))

print('-' * 40)
# --- Numpy операции с векторами ---
# В классической математике вектором считается направленный отрезок. В программировании под вектором 
# может подразумеваться одномерный массив.
vector1 = np.array([2, 4, 7, 2.5])
vector2 = np.array([12, 6, 3.6, 13])

# Векторы (одномерный массивы) можно складывать, вычитать, умножать и делить. 
# Все вычисления происходят поэлементно.
result1 = vector1 + vector2
print(result1) # [14.  10.  10.6 15.5]
result2 = vector1 - vector2
print(result2) # [-10.   -2.    3.4 -10.5]
result3 = vector1 * vector2
print(result3) # [24.  24.  25.2 32.5]
result4 = vector1 / vector2
print(result4) # [0.16666667 0.66666667 1.94444444 0.19230769]

print('-' * 40)
# Если бы мы попытались сложить два списка
lst1 = [2, 4, 7, 2.5]
lst2 = [12, 6, 3.6, 13]
res = lst1 + lst2
print(res) # Получили бы просто объединенный список
# Если бы пришлось все же складывать все элементы, то нужно было бы сделать следующее
res = [x + y for x, y in (zip(lst1, lst2))]
print(res) # Тогда результат был бы такой

# При математических операциях над векторами (для получения корректного результата) 
# нужно иметь ввиду, что векторы должны быть одинаковыми по длинне
# Например
vector1_longer = np.array([2, 4, 7, 2.5, 12, 10, 5])
vector2 = np.array([12, 6, 3.6, 13, 8, 9])
# res = vector1_longer + vector2
# print(res) ValueError: operands could not be broadcast together with shapes (7,) (6,)
# Получится ошибка, т.к. один вектор будет длинне, а операции произв. над каждым вектором

print('-' * 40)
# Однако есть исключения, если мы производим операцию например сложения вектора с одним числом
vector1 = np.array([1, 2, 3, 4, 5])
num = 10
result1 = vector1 * num
print(result1)
result2 = vector1 ** num
print(result2)

print('-' * 40)
# Вектора можно сравнивать (так же будут сравниваться по элементно)
vector1 = np.array([2, 4, 7, 2.5])
vector2 = np.array([12, 6, 3.6, 13])
print(vector1 > vector2)
print(vector1 < vector2)
print(vector1 == vector2)
print(vector1 is vector2)
# С одним числом
print(vector1 >= 7)

print('-' * 40)
# В линейной алгебре есть некоторые функции, например длинна вектора, в numpy они тоже присутствуют
# Длинна вектора - такая величина, которая получается путем суммирования квадратов элементов вектора, 
# а затем извлечение квадратного корня из полученного числа
vector = np.array([3, 4])
# Возводим все элементы вектора в квадрат;
# Суммируем квадраты элементов;
# Извлекаем квадратный корень из полученного результата
vector_lenght = np.sqrt(np.sum(vector ** 2))
print(vector_lenght)
# norm - норма вектора (длинна вектора)
# Однако в numpy есть функции из линейной алгебры np.linalg.norm
lenght = np.linalg.norm(vector)
print(lenght)

print('-' * 40)
vector1 = np.array([2, 4, 7, 2.5])
vector2 = np.array([12, 6, 3.6, 13])
# Расстояние между двумя векторами
distance1 = np.sqrt(np.sum((vector1 - vector2) ** 2))
print(distance1)

# С помощью функционала numpy находим расстояние векторов
distance2 = np.linalg.norm(vector1 - vector2)
print(distance2)

print('-' * 40)
# Скалярное произведение - на выходе после произведения двух векторов получается число (скаляр), затем скаляры суммируются
vec1 = np.arange(1, 6)
vec2 = np.linspace(10, 20, 5)

scalar_product1 = np.sum(vec1 * vec2)
print(scalar_product1)

# Поскольку функция скалярных произведений часто используется в numpy она уже реализована, даже не на уровне linalg
# dot product (c англ.) - скалярное произведение
scalar_product2 = np.dot(vec1, vec2)
print(scalar_product2)

print('-' * 40)
# Статистические свойства векторов
# Например минимальное/максимальное/среднее значения вектора
vector1 = np.array([2, 4, 7, 2.5])
vector2 = np.array([12, 6, 3.6, 13])

print(vector1.min())
print(vector2.max())
print(vector2.mean()) 
print(np.median(vector1)) # Медиана - значение середины массива (в том числе и для нечетных массивов)

# Стандартное отклонение – это мера, на которую элементы набора отклоняются или расходятся от среднего значения
print(np.std(vector1))

print('-' * 40)
# 8.4 определить сонаправленность векторов a, b, c
# Вариант 1
a = np.array([23, 34, 27])
b = np.array([-54, 1, 46])
c = np.array([46, 68, 54])

# Косинуса угла более чем достаточно, так как он сам по себе является мерой сонаправленности векторов. 
# Для параллельных векторов косинус угла будет равен единицы = 1
ab = np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)
print(ab)
ac = np.dot(a, c) / np.linalg.norm(a) / np.linalg.norm(c)
print(ac) # Сонаправленный

ba = np.dot(b, a) / np.linalg.norm(b) / np.linalg.norm(a)
print(ba)
bc = np.dot(b, c) / np.linalg.norm(b) / np.linalg.norm(c)
print(bc)

ca = np.dot(c, a) / np.linalg.norm(c) / np.linalg.norm(a)
print(ca) # Сонаправленный
cb = np.dot(c, b) / np.linalg.norm(c) / np.linalg.norm(b)
print(cb)

# Вариант 2
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])
 
len_a = np.linalg.norm(a)
len_b = np.linalg.norm(b)
len_c = np.linalg.norm(c)
 
len_a_b = np.linalg.norm(a + b)
len_b_c = np.linalg.norm(b + c)
len_a_c = np.linalg.norm(a + c)
 
print(len_a_b == len_a + len_b)
# False
print(len_b_c == len_b + len_c)
# False
print(len_a_c == len_a + len_c)
# True

print('-' * 40)
# Задание 8.5 (найти пару векторов расстояние между которыми больше 100)
distance_ab = np.linalg.norm(a - b)
print(distance_ab)
distance_ac = np.linalg.norm(a - c)
print(distance_ac)

distance_ba = np.linalg.norm(b - a)
print(distance_ba)
distance_bc = np.linalg.norm(b - c)
print(distance_bc)

distance_ca = np.linalg.norm(c - a)
print(distance_ca)
distance_cb = np.linalg.norm(c - b)
print(distance_cb)

print('-' * 40)
# Задание 8.5 (найдите пару перпендикулярных векторов с помощью скалярного произведения (оно должно быть равно нулю)).
dot_ab = np.dot(a, b)
print(dot_ab)
dot_ac = np.dot(a, c)
print(dot_ac)

dot_ba = np.dot(b, a)
print(dot_ba)
dot_bc = np.dot(b, c)
print(dot_bc)

dot_ca = np.dot(c, a)
print(dot_ca)
dot_cb = np.dot(c, b)
print(dot_cb)

# Округление round()
# До сотых - round(num, 2)
# До тысячных - round(num, 3)

print('-' * 40)
# --- Случайные числа numpy ---
# Генерация случайных (псевдослучайных) чисел
rnd_float = np.random.rand()
print(rnd_float)

print('-' * 40)
# Можно выставить размерность итогового массива
rnd_float = np.random.rand(5)
print(rnd_float)

print('-' * 40)
# Можно выставить размерность итогового массива
rnd_float = np.random.rand(5)
print(rnd_float)

print('-' * 40)
# Можно задать хоть шестимерный массив указав следующие аргументы
rnd_float = np.random.rand(2, 3, 4, 10, 11, 12)
print(rnd_float)

print('-' * 40)
# Можно задать хоть шестимерный массив указав следующие аргументы
rnd_float = np.random.rand(2, 3, 4, 10, 11, 12)
print(rnd_float)

# В обычном варианте random не принимает форму массива ввиде кортежа shape, более того, если его передать возникнет ошибка
# Поэтому, если есть необходимость передавать форму массива, как с np.array в виде кортежа, то вместо rand пишем sample
print('-' * 40)
# Можно задать хоть шестимерный массив указав следующие аргументы
shape = (3, 3)
rnd_float = np.random.sample(shape)
print(rnd_float)

# Uniform более продвинутый метод по сравнению с sample или rand
print('-' * 40)
# Если запустить без аргументов, будет обычное число
# uniform(low=0.0, high=1.0, size=None)
rnd_float = np.random.uniform()
print(rnd_float)

# Можно устанавливать границы значений случайного числа, например
print('-' * 40)
rnd_float = np.random.uniform(-30, 130)
print(rnd_float)

# Можно устанавливать размер массива (size=N)
print('-' * 40)
rnd_float = np.random.uniform(-30, 130, size=3)
print(rnd_float)

# Можно устанавливать форму массива с помощью кортежа (size=(2, 5))
print('-' * 40)
rnd_float = np.random.uniform(-30, 130, size=(2, 5))
print(rnd_float)

# Выше мы генерировали float значения, но можно генерировать и целочисленные значения int
print('-' * 40)
rnd_int = np.random.randint(-30, 130, size=(2, 3))
print(rnd_int)

print('-' * 40)
# В numpy можно сразу применять действия к массивам, например метод shuffle (перемешивание), например:
arr = np.array([1,2,3,4,5])
print(arr)
# Перемешаем элементы случайным порядком
np.random.shuffle(arr)
print(arr)

# Если нужно получать новый перемешанный массив, то следует использовать метод permutation
print('-' * 40)
playlist = np.array(["Metallica", "Aria", "PinkFloyd", "Manowar", "Kino"])
shuffled_playlist = np.random.permutation(playlist)
print(shuffled_playlist)

print('-' * 40)
# В методе permutation можно не задавать "вилку" значений которые должны быть перемешаны, 
# вместо этого указывается одно верхнее число (не включительно)
shuffle = np.random.permutation(12)
print(shuffle)

print('-' * 40)
# Метод choice случайным образом выбирает подмножества из массива
# choice(a, size=None, replace=True)
arr = np.array([1,2,3,4,5,6,7,8,9,10,100,1000,10000])
choice = np.random.choice(arr)
print(choice)

print('-' * 40)
# Еще пример (выбирается случайное число от 0 до 4, размером 2, 3)
choice_numbers = np.random.choice(5, (2, 3))
print(choice_numbers)

print('-' * 40)
# Еще пример (тут случайным образом будет выбран массив из двух элементов)
workers = np.array(["Bob", "John", "Alex", "Marry", "Sam"])
# replace=False означает выборку без повторений
choice_workers = np.random.choice(workers, size=2, replace=False)
print(choice_workers)

print('-' * 40)
# Функция random генерирует псевдослучайные числа для генерации которых изначально используется seed (зерно) начальное число
# Зная seed можно добиться воспроизводимости результата вычислений т.е. повторимости последовательности случайных чисел
# задать промежуток для числа seed можно от 0 до 2**32-1 (отрицательные нельзя)
np.random.seed(0)
rnd_num = np.random.randint(10, size=(3, 4))
print(rnd_num) # Будем получать один и тот же результат, т.к. мы используем строко определенный seed

print('-' * 40)
# Задание 9.6
# 1. В simple сохраните случайное число в диапазоне от 0 до 1
# 2. Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
# 3. Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
# 4. В переменную even сохраните четные числа от 2 до 16 (включительно)
# 5. Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
# 6. Получите из even 3 числа без повторений. Сохраните их в переменную select
# 7. Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)

np.random.seed(2021)

print('-' * 40)
simple = np.random.uniform(0, 1)
print(simple)

print('-' * 40)
randoms = np.random.uniform(-150, 2021, size=120)
print(randoms)

print('-' * 40)
shape = (3, 2)
table = np.random.randint(1, 101, size=shape)
print(table)

print('-' * 40)
even = np.arange(2, 17, 2)
print(even)

print('-' * 40)
mix = even
mix = np.random.permutation(mix)
print(mix)

print('-' * 40)
select = np.random.choice(even, size=3, replace=False)
print(select)

print('-' * 40)
triplet = np.random.permutation(select)
print(triplet)

print(even)
# [ 2  4  6  8 10 12 14 16]

print('-' * 40)
# Задание 10.6 (Напишите функцию get_chess(a), которая принимает на вход длину стороны квадрата a и возвращает 
# двумерный массив формы (a, a), заполненный 0 и 1 в шахматном порядке. В левом верхнем углу всегда должен быть ноль.)

def get_chess(a):
    arr = np.zeros((a, a), dtype=np.float16)
    
    # [(строки)каждый второй элемент начиная с 0(строки), (столбцы)начинается с 1 элем кажый второй элемент(столбцы)]
    arr[::2, 1::2] = 1
    # [(строки)каждый второй элемент начиная с 1(строки), (столбцы)начинается с 0 элем кажый второй элемент(столбцы)]
    arr[1::2, ::2] = 1
    
    return arr

print(get_chess(8))

print('-' * 40)
# Задание 10.7 (Вы разрабатываете приложение для прослушивания музыки. Конечно же, там будет доступна функция 
# перемешивания плейлиста. Пользователю может настолько понравиться перемешанная версия плейлиста, что он 
# захочет сохранить его копию. Однако вы не хотите хранить в памяти новую версию плейлиста, а просто хотите 
# сохранять тот seed, с которым он был сгенерирован.)

def shuffle_seed(array):
    current_seed = np.random.randint(0, 2**32 - 1)
    np.random.seed(seed=current_seed)
    shuffled_array = np.random.permutation(array)
    
    return (shuffled_array, current_seed)

array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# (array([1, 3, 2, 4, 5]), 2332342819)
print(shuffle_seed(array))
# (array([4, 5, 2, 3, 1]), 4155165971)

print('-' * 40)
# Задание 10.8 (Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов 
# через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины. Функция возвращает
# минимальное и максимальное расстояние между векторами в виде кортежа.)

def min_max_dist(*vectors):
    distances = []
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            vec_dist = np.linalg.norm(vectors[i] - vectors[j])
            distances.append(vec_dist)
    dist_min = min(distances)
    dist_max = max(distances)
    return (dist_min, dist_max)

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)

print('-' * 40)
# Задание 10.9 (Напишите функцию any_normal, которая принимает на вход неограниченное число векторов 
# через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины. Функция возвращает 
# True, если есть хотя бы одна пара перпендикулярных векторов. Иначе возвращает False)
def any_normal(*vectors):
    dot_vectos = []
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            dot_result = np.dot(vectors[i], vectors[j])
            dot_vectos.append(dot_result)
            
    return True if 0.0 in dot_vectos else False

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True

print('-' * 40)
# Задание 10.10 (Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых 
# чисел от 1 до 100 (включительно). Это поля для игры в лото. Трёхмерный массив должен состоять 
# из таблиц чисел формы 5х5, то есть итоговая форма — (num, 5, 5). Функция возвращает полученный массив.)
def get_loto(num):
    shape = (num, 5, 5)
    arr_3d = np.random.randint(1, 101, size=shape)
    return arr_3d

print(get_loto(3))

# array([[[ 35,  66,  38,  11,  32],
#        [ 32,   7,  37,  83,  42],
#        [ 89,  37,  19,  51,  89],
#        [ 70, 100,  83,   5,  11],
#        [ 20,  13,  60,  26,  41]],
 
#       [[ 23,  49,  76,  44,  43],
#        [ 59,  63,  99,  92,   2],
#        [ 83,   4,  25,  73,  19],
#        [ 10,  18,  40,  11,  21],
#        [ 58,  45,  73,  93,  61]],
 
#       [[100,  88,  70,  34,  51],
#        [  5,  35,  36,  85,  88],
#        [ 72,  23,  87,  30,  40],
#        [ 29,  21,  51,  73,  81],
#        [ 91,  19,  87,  60,  27]]])

print('-' * 40)
# Задание 10.11 (Напишите функцию get_unique_loto(num). Она так же, как и функция в задании 10.10, 
# генерирует num полей для игры в лото, однако теперь на каждом поле 5х5 числа не могут повторяться. 
# Функция также должна возвращать массив формы num x 5 x 5.)
# Вариант 1
def get_unique_loto(num):
    shape = (num, 5, 5)
    arr_3d = np.random.choice(500, size=shape, replace=False, p=None)
    return arr_3d

print(get_unique_loto(10))
print(np.shape(get_unique_loto(10)))

a = get_unique_loto(10)

check = []
for i in a:
  check.append(len(set(i.flatten())))
print(check)

# array([[[26, 91, 73,  7, 16],
#        [46, 85, 78, 77, 51],
#        [84, 86, 55, 71, 58],
#        [17, 61, 50, 30, 97],
#        [66, 29, 38, 41, 32]],
 
#       [[49, 32,  3, 21, 85],
#        [45,  8, 94, 46, 96],
#        [41, 38, 58, 37, 98],
#        [66, 77, 54, 80, 26],
#        [62, 63, 72,  5, 43]],
 
#       [[55, 60,  6, 80, 97],
#        [23, 69, 94,  9, 24],
#        [17, 98, 27, 63, 79],
#        [84, 74, 51, 39, 54],
#        [77, 30, 48, 75, 85]]])

# Вариант 2
def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
    res = np.array(res)
    return res

print(get_unique_loto(10))
print(np.shape(get_unique_loto(10)))

a = get_unique_loto(10)

check = []
for i in a:
  check.append(len(set(i.flatten())))
print(check)