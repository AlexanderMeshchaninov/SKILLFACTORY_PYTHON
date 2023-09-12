# --Простой условный оператор--
# Для формализации и визуализации алгоритмов ветвления существуют "блок-схемы"
from datetime import datetime

# Простой алгоритм брать зонт или нет в зависимости от погоды
is_rainy = True # Дождь будет

if is_rainy:
    print("Take an umbrella")
else:
    print("Don't take un umbrella")

# еще пример
a = 2 ** 10
b = 3 ** 5

if a > b:
    print('Value of variable a > value of variable b')
else:
    print('Value of variable a <= value of variable b')

# еще пример
target_word = 'and'
words = ['and', 'or', 'not']
if target_word in words:
    print('String "{}" is in list'.format(target_word))
    # или так
    print(f'String "{target_word}" is in list')
print(f"Target word '{target_word}'")
print(f"List of words: {words}")

a = 16
b = 14 + a
print("b=", b)

a = 7
b = 9 + a
print("a=F(,'b, ')")

mx = 0
s = 0
x = -5
if x < 0:
    s = x
if x > mx:
    mx = x
print(s)
print(mx)

people_count = 5
if people_count < 10:
    print("Добро пожаловать!")
else:
    print("Всё занято. Подождите!")

password = '879f2aabS'
answer = '879f2aabS'
if answer == password:
    print("Добро пожаловать!")
else:
    print("Вы ввели неверный пароль!")

name = 'Андрей'
age = 21
if age >= 18:
    print(f"Добрый вечер, {name}!")
else:
    print(f"Привет, {name}! Приносим свои извинения, но вы не можете гулять после 22:00")

# --Вложенные условные операторы--
is_rainy = True
is_heavy_rain = False

if is_rainy:
    # Здесь вписывается еще одно условие if (вложенный оператор)
    if is_heavy_rain:
        print("Take un umbrella")
    else:
        print("Take on a raincoat")
else:
    print("Don't take an umbrella")

# Пример выдавать ли кредит
is_credit_history_good = True # Хорошая ли кредитная история?
is_there_a_deposit = True # Есть ли залог?
is_there_a_debt = 500.0 # Если ли долг (более 1_000 $)?
is_there_a_guarantors = False # Есть ли поручители?
positive_response = "выдать кредит"
negative_response = "не выдавать кредит"

def check_credit_history():
    if is_credit_history_good:
        if is_there_a_debt > 1000:
            print(negative_response)
        else:
            print(positive_response)
    else:
        if is_there_a_deposit:
            if is_there_a_guarantors:
                print(positive_response)
            else:
                print(negative_response)
        else:
            print(negative_response)

check_credit_history()

#number = 200
# 200 делится на 2 и на 5

#number = 8
# 8 делится на 2, но не делится на 5

#number = 15
# 15 не делится на 2, но делится на 5

number = 27
# 27 не делится ни на 2, ни на 5

if (number % 2 != 0) and (number % 5 != 0):
    print(f"{number} не делится ни на 2, ни на 5")
else:
    if (number % 2 == 0) and (number % 5 != 0):
        print(f"{number} делится на 2, но не делится на 5")
    if (number % 2 != 0) and (number % 5 == 0):
        print(f"{number} не делится на 2, но делится на 5")
    if (number % 2 == 0) and (number % 5 == 0):
        print(f"{number} делится на 2 и на 5")

# Если не использовать никакой логический оператор или оператор сравнения в условном операторе,
# то интерпретатор за вас производит неявное приведение типов. То есть переводит переменную к bool и проверяет её значение.
# Примерная таблица:
#TRUE	                                                                FALSE
#int	-5, 10                                                          0
#(Любое целое число, отличное от нуля)

#float	-0.6, 45.5                                                      0.0
#(Любое число с плавающей точкой, отличное от нуля)

#str	"String"                                                        ""
#(Любая непустая строка)

#list	[1, 2, 3]                                                       []
#(Любой непустой список)

#dict	{"one": 1, "two": 2}                                            {}
#(Любой непустой словарь)

#NoneType	                                                            None

# Это можно проверить с помощью метода bool()
print(bool(3.4), bool(0.0)) # True False
print(bool("Hello"), bool("")) # True False

# Проверка на пустую строку (хорошие и плохие практики)
password = "Hello Alexander!"
# Правильно
if not password:
    print("You forgot to enter your password")
else:
    print("Password entered")

# Плохо
if password == "":
    print("You forgot to enter your password")
else:
    print("Password entered")

# Очень плохо!
if len(password) == 0:
    print("You forgot to enter your password")
else:
    print("Password entered")

# Примеры вверху так же применимы и к коллекция, спискам, словарям

result = 10
my_dict = {'key_1': 10}
item = my_dict.pop('key_1')
if my_dict:
    result = result + item
else:
    result = result + 1

print(result) #11

# --Тернарный условный оператор--
# Шаблон синтаксиса:
# variable = <значение при выполнении условия> if <условие> else <значение при невыполнении условия>

a = 42
b = 41
# Выведем с помощью "тернарника" результат (большее число)
result = a if a > b else b
print(result)

# Без использования тернарного оператора
cust_age = 40
# Проверяем условие: возраст больше 60
if cust_age >= 60:
    # условие выполняется
    print("Eligible for discount")
else:
    # условие не выполняется
    print("Not eligible for discount")
## Not eligible for discount

# C тернарным оператором
cust_discount = "Eligible for discount" if cust_age >= 60 else "Not eligible for discount"
print(cust_discount)

# Кстати говоря, подобные простейшие задачи можно решать и вовсе без условных операторов.
# Когда у нас есть задача с двумя исходами, можно создать словарь с ключами True и False,
# значения этого словаря будут соответствовать тем значениям, которые должны вернуться по результатам исходов:

answer_dict = {
    True: "Eligible for discount",
    False: "Not eligible for discount"
}

# Тогда для того, чтобы вывести соответствующую фразу на экран, достаточно передать условие cust_age >= 60
# в качестве индекса словаря. Когда это условие будет равно True, мы получим из словаря строку "Eligible for discount",
# в противном случае — строку "Not eligible for discount":

cust_age = 40
print(answer_dict[cust_age >= 60])
## Not eligible for discount

lst = ['a', 'b', 'c']
x = 5 if 'f' in lst else None
print(x)

cust_age = 60
cust_discount = 20 if cust_age >= 60 else 10
print(cust_discount)

# Задание 1 (определить является ли текущее время утром и вывести соответствующее сообщение.
# Утром считается временной промежуток с 6 (включительно) и до 12 часов (невключительно).
now = "11:11:23"
# Разделим компоненты на час, минута, секунда
hours, minutes, seconds = now.split(":")
# Далее конвертация строк в целочисленные значения
hours, minutes, seconds = int(hours), int(minutes), int(seconds)

if(hours >= 6) and (hours < 12):
    print("Morning!")

# Но python, такой python. Можно то же самое выражение записать лаконичнее.
if 6 <= hours < 12:
    print("Morning!")

# Есть еще третий (немного экзотический) способ решить данную задачу. С помощью метода range
if hours in range(6, 12): # От 6 включительно, до 12 невключительно
    print("Morning!")

# Задача 2 (В математике координатную плоскость условно разделяют на 4 четверти (обычно они обозначаются римскими цифрами).
# Нам необходимо написать программу, которая определяет, к какой четверти принадлежит точка.
# Координаты точки хранятся в переменных x и y. Так, точка со следующими координатами:)

# x, y = (6.3, 7.2) # I
# x, y = (-3, 3) # II
# x, y = (-6.3, -5.3) # III
x, y = (6.3, -5.3) # IV

# Но у записанной конструкции есть один существенный, хотя и неочевидный недостаток. Обратим внимание, что условия будут
# проверяться последовательно друг за другом. Независимо от того, что одно из условий уже выполнилось
# (например, x > 0 and y > 0), другие условные операторы всё равно будут отрабатывать.
# И это несмотря на то, что если точка попала в одну из четвертей координатной плоскости, то в другую она никак
# попасть не может! То есть в программе происходит 4 проверки, вне зависимости от того, чему равны значения переменных x и y.

# I
if (x > 0) and (y > 0):
    print("I четверть")
# II
if (x < 0) and (y > 0):
    print("II четверть")
# III
if (x < 0) and (y < 0):
    print("III четверть")
# IV
if (x > 0) and (y < 0):
    print("IV четверть")

# Либо через вложенные операторы
if x > 0:
    if y > 0:                # x > 0, y > 0
        print("I quarter")  # Первая четверть
    else:                    # x > 0, y < 0
        print("IV quarter")  # Четвёртая четверть
else:
    if y > 0:                # x < 0, y > 0
        print("II quarter")  # Вторая четверть
    else:                    # x < 0, y < 0
        print("III quarter") # Третья четверть

# Условия, которые никогда не могут быть выполнены одновременно, называются взаимоисключающими.
# И для обработки таких условий лучше всего подойдёт не множественный if, а конструкция if-elif-else.

# Задание 5.1
time = 8
if 7 <= time < 10:
    print("Пора вставать!")
else:
    print("Ты проспал!")

# Задание 5.2
# target_word = "quantity"
target_word = "apply"
lst_str = list(target_word)
if ('q' in lst_str) or ('z' in lst_str):
    print("Ух ты! Вы ввели редкое слово!") # Если есть q или z
else:
    print("Это не очень редкое слово...") # Если нет q и z

# Задание 5.3

# height = 183
# weight = 78
# zodiac_sign = 'козерог' # Ваша половинка нашлась!

height = 171
weight = 75
zodiac_sign = 'весы' # "Попробуем поискать еще!"

if (height > 180 and weight < 80) and (zodiac_sign in {'весы', 'дева', 'овен','козерог'}):
    print("Ваша половинка нашлась!")
else:
    print("Попробуем поискать еще!")

# --if-elif-else--

# Пример
a = 10
if a == 10:
    print("a == 10")
elif a > 10:
    print("a > 10")
else:
    print("a < 10")

# Можно переписать пример выше с координатами, для более корректной работы ветки

# I
if (x > 0) and (y > 0):
    print("I четверть")
# II
elif (x < 0) and (y > 0):
    print("II четверть")
# III
elif (x < 0) and (y < 0):
    print("III четверть")
# IV
elif (x > 0) and (y < 0):
    print("IV четверть")

# Еще пример
current_month = 12

if (current_month > 12):
    print("Incorrect!")
elif (3 <= current_month <= 5):
    print("Spring")
elif (6 <= current_month <= 8):
    print("Summer")
elif (9 <= current_month <= 11):
    print("Autumn")
else:
    print("Winter")

# Тот же пример по другому
if (current_month > 12):
    print("Incorrect!")
elif (current_month in [3, 4, 5]):
    print("Spring")
elif (current_month in [6, 7, 8]):
    print("Summer")
elif (current_month in [9, 10, 11]):
    print("Autumn")
else:
    print("Winter")

# Задание 5.4
speed = 4 # Скорость ветра

if (speed in [1, 4]):
    print("weak [1]")
elif (speed in [5, 10]):
    print("moderate [2]")
elif (speed in [11, 18]):
    print("strong [3]")
else:
    print("hurricane [4]")

# Задание 5.5 («Камень, ножницы, бумага»)
# Правила игры всем известны:
# камень побеждает ножницы;
# ножницы — бумагу;
# бумага — камень.

# player_1 = 'камень'
# player_2 = 'камень'
# Ничья!

#player_1 = 'ножницы'
#player_2 = 'бумага'
# Первый игрок — победитель!

player_1 = 'камень'
player_2 = 'бумага'
# Второй игрок — победитель!

if (player_1 in ['камень'] and player_2 in ['ножницы']):
    print("Первый игрок — победитель!")
elif (player_1 in ['ножницы'] and player_2 in ['бумага']):
    print("Первый игрок — победитель!")
elif (player_1 in ['бумага'] and player_2 in ['камень']):
    print("Первый игрок — победитель!")
elif (player_2 in ['камень'] and player_1 in ['ножницы']):
    print("Второй игрок — победитель!")
elif (player_2 in ['ножницы'] and player_1 in ['бумага']):
    print("Второй игрок — победитель!")
elif (player_2 in ['бумага'] and player_1 in ['камень']):
    print("Второй игрок — победитель!")
else:
    print("Ничья!")

# --Комплексные задачи--
# Задача 4

# В словаре dish_time_dict представлены блюда, которые в данный момент ресторан может приготовить и среднее время их
# приготовления (в минутах).
dish_time_dict = {
    'Рамен с говядиной': 15,
    'Суши': 18,
    'Лагман с курицей': 20,
    'Лагман с говядиной': 24,
    'Плов с курицей': 28
}

# В словаре street_time_dict указаны районы города и среднее время доставки в эти районы (в минутах).
street_time_dict  = {
    'Дзержинский': 39,
    'Солнечный': 40,
    'Заводской': 27,
    'Гагаринский': 43,
    'Кировский': 37,
    'Октябрьский': 34
}

# Блюдо, заказанное пользователем, и район, в котором он живёт, хранятся в переменных dish и street соответственно.
dish, street = 'Рамен с говядиной', 'Заводской'
## Заказ будет доставлен вовремя

#dish, street = 'Плов с курицей', 'Солнечный'
## "Курьер задержится на 8 минут"

#dish, street = 'Бургер с говядиной', 'Солнечный'
## "Блюдо недоступно, закажите что-то другое"

# Необходимо реализовать программу, которая проверяет, успеет курьер доставить заказ за 60 (включительно) минут с момента
# его принятия или нет.
# Также необходимо реализовать проверку, что блюдо, заказанное клиентом, в данный момент доступно в ресторане, а район,
# в котором находится клиент, доступен для доставки.

# Проверяем делаем ли мы вообще такие заказы и есть ли такой район доставки
if street not in street_time_dict:
    print("Доставка в ваш район недоступна")
elif dish not in dish_time_dict:
    print("Блюдо недоступно, закажите что-то другое")
else: # если оба блока выше не сработают, то означает, что мы осуществляем и заказ и доставку, далее расчеты
    # получаем время доставки заказа
    street_time = street_time_dict[street]
    print(f"street time: {street_time}")
    # получаем время приготовления заказа
    dish_time = dish_time_dict[dish]
    print(f"dish time: {dish_time}")
    # расчитываем на сколько опоздает курьер или нет
    full_time = street_time + dish_time # общее время приготовления и доставки
    print(f"full time: {full_time}")
    # получаем время опоздания
    delay_time = full_time - 60
    print(f"delay time: {delay_time}")
    if delay_time <= 0:
        print("Заказ будет доставлен вовремя")
    else:
        print(f"Курьер задержится на {delay_time} минут")

# Задача 6

# Представим ситуацию. В последний месяц удача перестала вам улыбаться. У вас 3 раза взломали пароль от вашего профиля
# в соцсетях.
# Вы задумались над тем, что неправильно подходите к вопросу безопасности. И решаете написать программу на Python, которая
# будет проверять ваш пароль на надёжность. Немного погуглив, вы смогли составить список рекомендаций к паролю:

# Длина – 8 символов (если меньше – то проще взломать, а если длиннее – то сложно запомнить).
# Пароль не должен состоять только из цифр.
# Пароль не должен состоять только из букв.
# В пароле должны быть заглавные буквы.
# В пароле должны быть строчные символы.
# В пароле должен быть хотя бы один из специальных символов ('*', '-', '#'), но каждый из символов должен входить
# в пароль не более 1 раза.
# Другие спецсимволы недопустимы, так как вы их не можете запомнить. Вот список «плохих» символов:
# '!', '@', '$', '%', '^', '`', '&', '(', ')', '+', '=', '_', '~'.
# В случае надёжного пароля программа должна выводить фразу «Пароль идеален!», а в остальных случаях будут перечислены
# все ошибки, которые вы допустили.

# Можно составить словарь ошибок и внести необходимые данные
errors_dict = {
    'length': 'Длина пароля не равна 8 символам',
    'digits': 'Пароль состоит только из цифр',
    'letters': 'Пароль состоит только из букв',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Отсутствуют строчные буквы',
    'spec': 'Отсутствуют спецсимволы в пароле',
    'bad_symbols': 'В пароле использованы непредусмотренные символы'
}

# Далее создаем список "плохих" символов
bad_symbols = ['!', '@', '$', '%', '^', '`', '&', '(', ')', '+', '=', '_', '~']

# сам пароль хранится в переменной
password = 'Aafaf*al'

# Тут всё довольно просто: по условию нам нужно выводить весь перечень ошибок. Причём совершенно ясно, что наш пароль
# может содержать сразу несколько ошибок. Так, он может быть слишком коротким и одновременно содержать недопустимые символы.
# Отсюда мы делаем вывод, что условия для пароля не являются взаимоисключающими, поэтому нам нужно воспользоваться множественным if.

# Наша программа будет последовательно проверять каждое из ограничений, наложенных на пароль, и если это ограничение
# соблюдено, мы будем удалять из словаря соответствующий ключ и значение, соответствующее ему.
# В конце работы программы мы проверим, сколько ошибок осталось в словаре. Если ни одной — значит, всё получилось.
# В противном случае мы просто выведем на экран все оставшиеся ошибки.

# Сам код проверки пароля
if len(password) == 8:
    errors_dict.pop('length')
if not password.isdigit():
    errors_dict.pop('digits')
if not password.isalpha():
    errors_dict.pop('letters')
if password.lower() != password:
    errors_dict.pop('upper')
if password.upper() != password:
    errors_dict.pop('lower')
if '*' in password or '_' in password or '#' in password:
    errors_dict.pop('spec')
    if password.count('*') > 1 or password.count('_') > 1 or password.count('#') > 1:
        errors_dict['spec_count'] = 'Какой-то из спецсимволов в пароле использован более одного раза'
# Для проверки списка запрещенных символом можно было бы использовать циклы, НО есть более элегантное решение - множества
print(set(password))
print(set(bad_symbols))
print(set(password).intersection(set(bad_symbols))) # set()
# Если в результирующем множестве не останется элементов, это значит, что множества не пересекаются между собой, и
# исходный пароль не содержит запрещённых символов.

if not set(password).intersection(set(bad_symbols)):
    errors_dict.pop('bad_symbols')
if len(errors_dict) > 0:
    print(list(errors_dict.values()))
else:
    print("Ваш пароль идеален!")

# Задание 5.6
# Покупка
#purchases = ["Adidas", "Nike"]
# Стоимость заказа составила: 10848. С учетом скидки в 5% — 10305.6

#purchases = ["Nike", "Nike"]
# Стоимость заказа составила: 13100. С учетом скидки в 10% — 11790.0

#purchases = []
# Ваша корзина пуста

purchases = ["Nike"]
# Стоимость заказа составила: <стоимость>

# Расценки товаров
prices = {'Adidas': 4298, 'Nike': 6550, 'Puma': 4490, 'Asics': 3879}

if not purchases:
    print('Ваша корзина пуста')
else:
    if len(purchases) == 1:
        price = prices[purchases[0]]
        print(f'Стоимость заказа составила: {price}')
    elif len(purchases) == 2:
        total_price = prices[purchases[0]] + prices[purchases[1]]
        if len(set(purchases).intersection(prices.keys())) == 2:
            discount_5 = total_price / 100 * 5
            print(f'Стоимость заказа составила: {total_price}. С учетом скидки в 5% — {total_price - discount_5}')
        elif len(set(purchases).intersection(prices.keys())) == 1:
            discount_10 = total_price / 100 * 10
            print(f'Стоимость заказа составила: {total_price}. С учетом скидки в 10% — {total_price - discount_10}')


#date = '16.04.2019 15:59'
# category = 2

#date = '12.05.2019 08:42'
# category = 1

date = '05.07.2018 20:15'
# category = 3
category = None
day, month, year = date.split(" ")[0].split('.')

if year == '2019':
    if month == '05':
        category = 1
    else:
        category = 2
else:
    category = 3
print(category)

# Задача 5.8

#city_info = "Москва , не готов к переезду , готов к командировкам"
#city_info = "Москва , м. Беломорская , не готов к переезду, не готов к командировкам"
#city_info = "Санкт-Петербург , готов к переезду (Сочи, Москва) , готов к командировкам"
city_info = "Новосибирск , готов к переезду, не готов к командировкам"

city = None

million_cities = [
    'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань',
    'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону', 'Уфа',
    'Красноярск', 'Пермь', 'Воронеж', 'Волгоград']

curr_city = city_info.split(' ,')[0]

if curr_city == 'Москва' or curr_city == 'Санкт-Петербург':
    city = curr_city
    print(city)
elif curr_city in million_cities:
    city = "Город миллионник"
    print(city)
else:
    city = "Другое"
    print(city)
