import numpy as np

# Объекты
number = 2.5

print('_' * 40)
# Вызовем метод is_integer. Он скажет нам, является ли number целым числом
print(number.is_integer()) #False

print('_' * 40)
# Давайте попробуем представить number как обыкновенную дробь
print(number.as_integer_ratio()) # (5, 2) действительно 2.5 = 5/2

print('_' * 40)
# Посмотрим на список: он хранит данные своих элементов, мы можем совершать над ними действия встроенными методами.
peoples_list = ['Pavel', 'Lilianna', 'Vasiliy', 'Alexander', 'Vasiliy']

# Посчитаем число Василиев с помощью метода count
print(peoples_list.count('Vasiliy')) # 2

print('_' * 40)
# Теперь отсортируем cписок
peoples_list.sort()
print(peoples_list) # ['Alexander', 'Lilianna', 'Pavel', 'Vasiliy', 'Vasiliy']

print('_' * 40)
number = 2.5  
print(number.__class__) # => <class 'float'>  

people = ["Vasiliy", "Stanislav", "Alexandra", "Vasiliy"]  
print(people.__class__) # => <class 'list'>

# Определим пустой класс: он не делает ничего, но позволит нам посмотреть на синтаксис.
class SaveReport():
    pass

# Сравните это с определением пустой функции  
# Команда pass не делает ничего; на её месте могли быть другие инструкции  
# Мы используем её только потому, что синтаксически python требует, чтобы там было хоть что-то  
def build_report():  
    pass

# И давайте определим ещё один класс  
# Для имён классов традиционно используются имена в формате CamelCase, где начала слов отмечаются большими буквами  
# Это позволяет легко отличать их от функций, которые пишутся в формате snake_case  
class SkillFactoryStudent():
    pass

print('_' * 40)
# Объекты из классов
# Вызываем класс и получаем новый объект аналогично тому, как вызывается функция. Получаем результат.
alex_student_1 = SkillFactoryStudent()

alex_srudent_2 = SkillFactoryStudent()

# О чем это говорит? О том, что хоть и класс один, но его экземпляры (instance) разные (полиморфизм)
print(alex_student_1 == alex_srudent_2) # False

print('_' * 40)
# АТРИБУТЫ И МЕТОДЫ
# Мы создали объект по пустому классу. Давайте добавим ему данные. Сделаем класс для отчётов по продажам SalesReport. 
# Пусть у нас в компании есть менеджеры по продажам, которые заключают сделки, и мы хотим посчитать для них метрики 
# общего объёма продаж.

# По-прежнему пока создаём пустой класс  
class SalesReport_():
    pass

# Создаем экземпляр класса (отчет по продажам)
report = SalesReport_()

# Мы добавим новый атрибут объекту.  
# Для этого через точку напишем имя атрибута и дальше как с обычной переменной
report.amount = 10

# То же самое делаем для второго отчёта.
report_2 = SalesReport_()
report_2.amount = 20

# Создадим вспомогательную функцию, она будет печатать общую сумму из отчёта 
def print_amount(report):
    print(f'Report amount is: {report.amount}')

print_amount(report) # Report amount is: 10
print_amount(report_2) # Report amount is: 20

print('_' * 40)
# Для разных отчётов вывелись разные значения, хотя объекты создавались из одного класса. 
# Функция print_report делает операцию над отчётом. Так как классы увязывают данные и действия 
# над ними, положим print_report внутрь класса.

class SalesReport__():
    # Наш новый метод внутри класса.  
    # Мы определяем его похожим образом с обычными функциями,  
    # но только помещаем внутрь класса и первым аргументом передаём self
    def print_report(self):
        print(f'Report amount is: {self.amount}')

report = SalesReport__()
report.amount = 100

report_2 = SalesReport__()  
report_2.amount = 200

report.print_report()
report_2.print_report()

# Методы в целом похожи на обычные функции, но их ключевое отличие — доступ к самому объекту и создание внутри класса.

print('_' * 40)
# Для примера определим ещё пару методов:
class SalesReport():
    # Позволим добавлять много разных сделок
    def add_deal(self, amount):
        # На первой сделке создадим список для хранения всех сделок
        if not hasattr(self, 'deals'):
            self.deals = []
        # Добавим текущую сделку
        self.deals.append(amount)
    # Посчитаем сумму всех сделок
    def total_amount(self):
        return sum(self.deals)
    
    # Вывод результата
    def print_report(self):
        print("Total sales:", self.total_amount())
        
# Используем наши новые возможности  
# Добавим две сделки и распечатаем отчёт
report = SalesReport()
report.add_deal(10_000)
report.add_deal(25_000)
report.add_deal(30_000)
report.print_report()

# Атрибут deals, определённый в одном методе, становится доступен сразу во всех методах класса. 
# Через self становятся доступны и остальные методы, например print_report использует метод total_amount. 
# Это позволяет компактно упаковывать логику внутри класса: внешнее использование становится гораздо лаконичнее.

print('_' * 40)

# Задание 4.1
from statistics import mean

class DepartmentReport_():
       
    def add_revenue(self, amount):
        """
        Метод для добавления выручки отдела в список revenues.
        Если атрибута revenues ещё не существует, метод должен создавать пустой список перед добавлением выручки.
        """
        if not hasattr(self, 'revenues'):
            self.revenues = []
        self.revenues.append(amount)
    
    def average_revenue(self):
        """
        Метод возвращает среднюю выручку по отделам.
        """
        return mean(self.revenues)

report = DepartmentReport_()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# [1000000, 400000]
print(report.average_revenue())
# 700000.0

print('_' * 40)
# Возвращаясь к классу SalesReport(), если мы вызовем total_amount до add_deal, то список сделок ещё не будет создан, 
# и мы получим ошибку. Также проверка на наличие списка в методе add_deal не кажется оптимальным решением, потому 
# что создать список нужно один раз, а проверять его наличие мы вынуждены на каждой сделке.

report = SalesReport()
# report.total_amount() # AttributeError: 'SalesReport' object has no attribute 'deals'
# report.print_report()

# Обе проблемы решились бы, если задавать атрибутам исходное значение. 
# Для этого у классов есть метод инициализации __init__. Если мы определим метод с таким именем, 
# код в нём вызовется при создании объекта.
class SalesReportMod_():
    # Своеобразный конструктор, как в C#
    def __init__(self) -> None:
        self.deals = []
    # Позволим добавлять много разных сделок
    def add_deal(self, amount):            
        # Добавим текущую сделку
        self.deals.append(amount)
    # Посчитаем сумму всех сделок
    def total_amount(self):
        return sum(self.deals)
    
    # Вывод результата
    def print_report(self):
        print("Total sales:", self.total_amount())
        
report = SalesReportMod_()  
print(report.deals) # []  
report.total_amount() # 0

print('_' * 40)
# __init__ — это технический метод, поэтому его имя начинается и заканчивается двумя подчёркиваниями. 
# Он получает первым аргументом сам объект, в нём могут выполняться любые операции. Оставшиеся аргументы 
# он получает из вызова при создании если мы напишем report = SalesReportMod("Info", 20), то вторым и 
# третьим аргументом в __init__ передадутся "Info" и 20.

class SalesReportMod():
    # Своеобразный конструктор, как в C#
    # Будем принимать в __init__ ещё и имя менеджера  
    def __init__(self, manager_name) -> None:
        self.deals = []
        self.manager_name = manager_name
    # Позволим добавлять много разных сделок
    def add_deal(self, amount):            
        # Добавим текущую сделку
        self.deals.append(amount)
    # Посчитаем сумму всех сделок
    def total_amount(self):
        return sum(self.deals)
    
    # Вывод результата
    def print_report(self):
        # И добавлять это имя в отчёт  
        print("Manager:", self.manager_name)
        print("Total sales:", self.total_amount())
        
report = SalesReportMod('Alexander')
print(report.deals) # []  
report.add_deal(900_000_000)
report.print_report()

print('_' * 40)
# Кроме __init__ у классов можно определить ряд технических методов, которые также называют "магическими". 
# Дело в том, что они не вызываются напрямую, но позволяют реализовать операции сложения object_1 + object_2 
# или сравнения object_1 > object_2.

# Задание 4.2
class DepartmentReport():

    def __init__(self, company_name):
        """
        Метод инициализации класса. 
        Создаёт атрибуты revenues и company
        """
        self.revenues = []
        self.company = company_name
    
    def add_revenue(self, amount):
        """
        Метод для добавления выручки отдела в список revenues.
        """
        self.revenues.append(amount)
    
    def average_revenue(self):
        """
        Вычисляет average_revenue — среднюю выручку по отделам — округляя до целого.
        Метод возвращает строку в формате:
        'Average department revenue for <company>: <average_revenue>'
        """
        return f"Average department revenue for {self.company}: {round(mean(self.revenues))}"

report = DepartmentReport(company_name="Danon")
print(report.company)
# Danon

report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())
# Average department revenue for Danon: 700000

print('_' * 40)
# Добавим метрик в наш класс SalesReportNew()
class SalesReportNew():
    def __init__(self, employee_name):
        self.deals = []
        self.employee_name = employee_name
        
    def add_deal(self, company, amount):
        self.deals.append({'company': company, 'amount': amount})
    
    def total_amount(self):
        return sum(deal['amount'] for deal in self.deals)
    
    def average_deal(self):
        return self.total_amount()/len(self.deals) 
    
    def all_companies(self):
        return list(deal['company'] for deal in self.deals)
    
    def print_report(self):  
        print("Employee: ", self.employee_name)  
        print("Total sales:", self.total_amount())  
        print("Average sales:", self.average_deal())
        print("Companies:", self.all_companies())
        
report = SalesReportNew("Ivan Semenov")
  
report.add_deal("PepsiCo", 120_000)  
report.add_deal("SkyEng", 250_000)  
report.add_deal("PepsiCo", 20_000)  
  
report.print_report()

# Мы расширили отчёт, но внешний код использования классов не увеличился. 
# Отчёт, который мы вывели, достаточно простой, но можно автоматически генерировать 
# презентацию с данными и графиками в PDF, при этом внешний интерфейс не менялся бы. 
# Мы просто передаём данные на вход и на выходе получаем отчёт.

print('_' * 40)
# Есть база клиентов с основной информацией; в реальном времени нам приходит информация о покупках. 
# Запустим промокампанию, чтобы поощрить старых клиентов, которые сделали у нас много заказов, и выдать им скидку:
class Client():
    # Базовые данные
    def __init__(self, email, order_num, registration_year):
        self.email = email
        self.order_num = order_num
        self.registration_year = registration_year
        self.discount = 0
        
    # Оформление заказа
    def make_order(self, price):
        self.update_discount()
        self.order_num += 1
        # Здесь было бы оформление заказа, но мы просто выведем его цену  
        discounted_price = price * (1 - self.discount)
        print(f"Order price for {self.email} is {discounted_price}")
    
    # Назначение скидки
    def update_discount(self):
        if self.registration_year < 2018 and self.order_num >= 5:
            self.discount = 0.1
            
# Применение
# Сделаем подобие базы
client_db = [
    Client("max@gmail.com", 2, 2019),  
    Client("lova@yandex.ru", 10, 2015),  
    Client("german1@sberbank.ru", 4, 2017),
    Client("german2@sberbank.ru", 4, 2015),  
    Client("alexander1@sberbank.ru", 4, 2019),
    Client("alexander_freeman@yandex.ru", 4, 2024)
]

# Сгенерируем заказы
client_db[0].make_order(1_000)
client_db[1].make_order(1_100)
client_db[2].make_order(1_500)
client_db[3].make_order(5_000)
client_db[4].make_order(8_900)
client_db[5].make_order(10_000)

print('_' * 40)
# Задание 5.1
# Мы разрабатываем приложение, которое подразумевает функционал авторизации пользователя, 
# а также управление балансом его балансом на некотором виртуальном счете.
# Определите класс для пользователей User.

# У него должны быть:
# атрибуты email, password и balance, которые устанавливаются при инициализации в методе __init__();
# метод login(), который реализует проверку почты и пароля. Метод должен принимать в качестве аргументов емайл (email) и пароль (password). 
# Если они совпадают с атрибутами объекта, он возвращает True, а иначе — False;
# метод update_balance(), который должен принимать в качестве аргумента amount некоторое число и изменять текущий баланс счёта 
# (атрибут balance) на величину amount.
# В случае правильного описания класса код, приведённый ниже, должен выдать следующий результат:

class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
    
    def login(self, email, password):
        if email == self.email and password == self.password:
            return True
        else:
            return False
    
    def update_balance(self, amount):
        self.balance += amount

user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123")) # False
print(user.login("gosha@roskino.org", "qwerty")) # True
user.update_balance(200)
user.update_balance(-500)
print(user.balance) # 19700

print('_' * 40)
# У нас есть численные данные из разных источников. Если они в виде строк, то нужно привести их к числам, 
# а пропуски — заполнить значениями. Сделаем доступ к медиане, среднему значению и стандартному отклонению:

import statistics as st

class DataFrame():
    def __init__(self, column, fill_value=0):
        # Инициализируем атрибуты
        self.column = column
        self.fill_value = fill_value
        # Заполним пропуски
        self.fill_missed()
        # Конвертируем все элементы в числа
        self.to_float()
    
    def fill_missed(self):
        for i, value in enumerate(self.column):
            if value is None or value == '':
                self.column[i] = self.fill_value
    
    def to_float(self):
        self.column = [float(value) for value in self.column]
    
    def median(self):
        return st.median(self.column)
    
    def mean(self):
        return st.mean(self.column)
    
    def deviation(self):
        return st.stdev(self.column)
    
# Воспользуемся классом  
df = DataFrame(["1", 17, 4, None, 8])

print(df.column) # [1.0, 17.0, 4.0, 0.0, 8.0]
print(df.deviation()) # 6.892024376045111
print(df.mean())# 6.0


print('_' * 40)
# Тут получился очень лаконичный интерфейс для использования класса. 
# В __init__ мы использовали значение по умолчанию для fill_value, а методы
# позволяют нам определять необязательные параметры.

# Задание 5.2
# Определите класс IntDataFrame, который в момент инициализации объектов принимает 
# список неотрицательных чисел и приводит к целым значениям все числа в этом списке, 
# отрезая дробную часть с помощью встроенной функции int().
# Результирующий список должен быть сохранен в виде атрибута с именем column.
# Также класс должен содержать следующие методы:
# count(), который возвращает количество ненулевых элементов в списке column;
# unique(), который возвращает число уникальных элементов в списке в списке column.

class IntDataFrame():
    def __init__(self, numbers_lst=[]):
        self.column = [int(num) for num in numbers_lst]
    
    def count(self):
        return [num for num in self.column if num != 0].__len__()
    
    def unique(self):
        return set(self.column).__len__()
        
df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)# [4, 4, 3, 0, 2, 0, 4]
print(df.count())# 5
print(df.unique())# 4

# Представим, вы делаете обработку данных и в конце каждого дня сохраняете результат в архив. 
# Вы хотите, чтобы данные каждого дня лежали в отдельном файле для этого дня, при этом можно 
# было бы получить данные за произвольный день.
# Перед запуском кода создайте папку с названием archive там же, где находится ноутбук:

print('_' * 40)
import pickle as pic
from datetime import datetime
from os import path

class Dumper():
    def __init__(self, acrhive_dir='Archive/'):
        self.archive_dir = acrhive_dir

    def dump(self, data):
        # Библиотека pickle позволяет доставать и класть объекты в файл
        with open(file=self.get_file_name(), mode='wb') as file:
            pic.dump(data, file)
    
    def load_for_day(self, day):
        file_name = path.join(self.archive_dir, day + '.pkl')
        # Оператор with это аналог using {} в C# где гарантируется, что контекст будет потом удален (для оптимизации памяти)
        with open(file_name, 'rb') as file:
            sets = pic.load(file)
        return sets
    
    # возвращает корректное имя для файла (делаем нейминг файла [название]+[сегодняшняя дата].pkl)
    def get_file_name(self):
        today = datetime.now().strftime("%y-%m-%d")
        return path.join(self.archive_dir, today + '.pkl')

# Пример использования  
data = {
    'perfomance': [10, 20, 10],  
    'clients': {"Romashka": 10, "Vector": 34}  
}

# Создаем класс
dumper = Dumper()
# Сохраним данные
dumper.dump(data)  

# Восстановим для сегодняшней даты  
file_name = datetime.now().strftime("%y-%m-%d")
restored_data = dumper.load_for_day(file_name)
print(restored_data)  
# => {'perfomance': [10, 20, 10], 'clients': {'Romashka': 10, 'Vector': 34}} 

# Сохранение и восстановление работает в пару строк. В результате мы можем приводить достаточно сложные операции к простому виду.

print('_' * 40)
import pickle as pic
from datetime import datetime
from os import path
# Задание 5.3

# Напишите класс сборщика технических сообщений OwnLogger.
# У него должен быть:
# атрибут logs, содержащий {"info": None, "warning": None, "error": None, "all": None}.
# метод log(message, level), который записывает сообщения. Здесь сообщение message может быть любым, 
# а level — один из "info", "warning", "error".
# метод show_last(level), где level может быть "info", "warning", "error", "all".
# Для "all" он просто возвращает последнее добавленное сообщение, а для остальных — последнее поступившее сообщение 
# соответствующего уровня. При этом по умолчанию значение именно "all".
# Если подходящего сообщения нет, возвращает None.

class OwnLogger():
    def __init__(self, logs = {"info": None, "warning": None, "error": None, "all": None}):
        self.logs = logs
        
    def log(self, message, level):
        self.logs['all'] = []
        if level in self.logs.keys():
            is_empty = True if self.logs[level] is None else False
            if is_empty:
                self.logs[level] = []
            self.logs[level].append(message)
            self.logs['all'].append(message)
        print(self.logs)

    def show_last(self, level='all'):
        try:
            if level == 'all':
                return [last_all for last_all in self.logs['all'] or None][-1]
            else:
                return [last_level for last_level in self.logs[level] or None][-1]
        except:
            return None

# logger = OwnLogger()
# logger.log("System started", "info")
# logger.log("System started_2", "info")
# logger.log("System started_3", "info")
# # logger.show_last("error")
# # None
# # Некоторые интерпретаторы Python могут не выводить None, тогда в этой проверке у вас будет пустая строка

# logger.log("Connection instable", "warning")
# logger.log("Connection lost", "error")

# logger.show_last() # Connection lost
# logger.show_last("info") # System started

# logger.show_last(level='error')

res = OwnLogger()
res.log(message='System started', level='info')
res.log(message='System started 2', level='info')
res.log(message='Warning message', level='warning')

print(res.show_last(level='error'))

print('_' * 40)
# Чтобы работать с путями операционной системы, нужно импортировать модуль os
import os

# Функция os.chdir() позволяет нам изменить директорию

# Чтобы узнать какой вы сейчас путь используете
start_path = os.getcwd()
print(start_path) # /Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20

# Далее попробуем подняться на директорию выше:
os.chdir("..") # подняться на один уровень выше
dir_up = os.getcwd() 
print(dir_up) # /Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/

# Теперь вернемся в ту директорию, из которой стартовали. Изначально мы сохраняли её в переменной start_path.
os.chdir(start_path)
start_path = os.getcwd()
print(start_path) # /Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20

# С помощью функции os.listdir() можно получить весь список файлов, находящихся в директории. 
# Если не указать никаких аргументов, то будет взята текущая директория.
list_dir = os.listdir()
print(list_dir) 
# ['.DS_Store', 'Archive', 'PY_15_Принципы_ООП_в_Python_и_отладка_кода.py', 
# 'PY_15_Принципы_ООП_в_Python_и_отладка_кода.ipynb', 'Data', 'helpers']

if 'tmp.py' not in os.listdir():
    print('Файл отсутствует в данной директории')
    
print('_' * 40)
# Задание 7.3
# Задание на самопроверку.
# Сделайте функцию, которая принимает от пользователя путь и выводит всю информацию о содержимом этой папки. 
# Для реализации используйте функцию встроенного модуля os.walk(). Если путь не указан, то сравнение начинается 
# с текущей директории.

def get_path(path=''):
    if path == '':
        os.chdir(os.getcwd())
        files_info = os.listdir()
        print(files_info)
    else:
        os.chdir(path)
        files_info = os.listdir()
        print(files_info)

get_path(os.getcwd())
get_path('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python')
get_path()

print('_' * 40)

def get_path_v2(path=None):
    start_path = path if path is not None else os.getcwd()
    
    for root, dirs, files in os.walk(start_path):
        print('Текущая директория', root)
        print('------')
        
        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")
        
        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")
        
        if files and dirs:
            print("Все пути:")
        for file in files:
            print("Файл: ", os.path.join(root, file))
        for dir in dirs:
            print("Папка: ", os.path.join(root, dir))
        print('=======')
        
get_path_v2(os.getcwd())
get_path_v2('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python')
get_path_v2()

print('_' * 40)
import os
# Задание 7.4
# Задание на самопроверку.
# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.

# # 1. Создаем файл
# with open('Data/input.txt', 'w') as f:
#     strings = ['1__test', '2__test', '3__test', '4__test', '5__test']
#     print(f.writelines(strings))
    
# # Читаем файл input
# with open('Data/output.txt', 'r') as f:
#     print(f.readlines())
    
# # 2. Перезаписываем файл построчно в другой файл
# with open('Data/output.txt', 'w') as output:
#     input = open('Data/input.txt')
#     output.writelines(input)
    
# # Читаем файл
# with open('Data/input.txt', 'r') as f:
#     print(f.readlines())

# или такой вариант 
# with open("Data/input.txt", "r") as input_file:
#     with open("Data/output.txt", "w") as output_file:
#         for line in input_file:
#             output_file.write(line)

print('_' * 40)
# Задание 7.5
# Задание на самопроверку.
# Дан файл numbers.txt, компоненты которого являются действительными числами (файл создайте самостоятельно и 
# заполните любыми числам, в одной строке одно число). Найдите сумму наибольшего и наименьшего из значений и 
# запишите результат в файл output.txt.

# Создание файла
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/numbers.txt', 'w') as numbers:
    numbers_list = ['1\n','2\n','3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n','11\n','12\n','13\n','14\n','15\n']
    numbers.writelines(numbers_list)

# Чтение файла
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/numbers.txt', 'r') as numbers:
    num_list = numbers.readlines()
    for i, num in enumerate(num_list):
        int_num = num.replace('\n', '')
        num_list[i] = int(int_num)
    with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/output.txt', 'w') as output:
        # Запись наибольшего числа
        output.writelines(f'{max(num_list)}\n')
        output.flush()
        # Запись наименьшего числа
        output.writelines(f'{min(num_list)}\n')

# Или такой вариант
# filename = 'numbers.txt'
# output = 'output.txt'

# with open(filename) as f:
#     min_ = max_ = float(f.readline())  # считали первое число
#     for line in f:
#         num =  float(line)
#         if num > max_:
#             max_ = num
#         elif num < min_:
#             min_ = num

#     sum_ = min_ + max_

# with open(output, 'w') as f:
#     f.write(str(sum_))
#     f.write('\n')

print('_' * 40)
# Задание 7.6
# Задание на самопроверку.
# В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную. 
# Подсчитайте количество учащихся, чья оценка меньше 3 баллов. Cодержание файла:

# Не будем создавать файл в коде, будет считывать уже готовый. Файл назову students.txt
import re
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/students.txt', 'r') as students:
    stud_lst = students.readlines()
    count = 0
    for el in stud_lst: 
        mark = re.findall('[0-9]+', el) # Распарсить строку можно с помощью регулярного выражения
        if int(mark[0]) < 3: count += 1
    print(f'Количество учащихся с оценкой меньше 3 баллов составляет: {count} человек')
    
# или такой вариант
# count = 0
# for line in open("input.txt"):
#     points = int(line.split()[-1])
#     if points < 3:
#         count += 1

print('_' * 40)
# Задание 7.7
# Задание на самопроверку.
# Выполните реверсирование строк файла (перестановку строк файла в обратном порядке).

# Читаем файл numbers.txt (числа с 1 -15)
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/numbers.txt', 'r') as reader:
    content = reader.readlines()
reversed_content = []
for line in content:
    line = line.strip('\n')
    reversed_line = line[::-1]
    reversed_content.append(reversed_line)
print(reversed_content)

# или такой вариант
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/numbers.txt', "r") as reader:
    with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/reversed_numbers.txt', "w") as writer:
        for line in reversed(reader.readlines()):
            writer.write(line)
with open('/Users/alexander/Desktop/SKILLFACTORY/Введение в язык Python/Lesson-20/Data/reversed_numbers.txt', 'r') as reader:
    print(reader.readlines())


# Исключения
print('_' * 40)

# Задание 8.7
# Задание на самопроверку.
# Создать скрипт, который будет в input() принимать строки, и их необходимо будет конвертировать в числа, 
# добавить try-except на то, чтобы строки могли быть сконвертированы в числа.
# В случае удачного выполнения скрипта написать: «Вы ввели <введённое число>».
# В конце скрипта обязательно написать: «Выход из программы».
# ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.

# try:
#     user_input = input('Введите строку или число: ')
#     result = int(user_input)
# except Exception as ex:
#     print('Вы ввели неправильное число!')
# else:
#     print(f'Вы ввели {result}')
# finally:
#     print('Выход из программы')
    
# или такой вариант

# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')

print('_' * 40)
# Задание 9.5
# Задание на самопроверку.
# Создайте класс Square. Добавьте в конструктор класса Square собственное исключение NonPositiveDigitException, 
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.

# Исключения 
class NonPositiveDigitException(ValueError):
    pass

# Сам класс
class Square(NonPositiveDigitException):
    def __init__(self, square_side):
        try:
            if square_side <= 0:
                raise NonPositiveDigitException('Сторона квадрата не должна быть 0 или отрицательным числом')
            else:
                print(f'Сторона квадрата: {square_side}')
        except ValueError as ex:
            print(ex)
            
Square(1)

Square(0)

# или другой, эталонный вариант
# class NonPositiveDigitException(ValueError):
#     pass
 
# class Square:
#     def __init__(self, a):
#         if a <= 0:
#             raise NonPositiveDigitException('Неправильно указана сторона квадрата')