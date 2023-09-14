# --Исключения и обработка исключений--
from datetime import datetime

# Вот некоторые - исключение при делении на 0 (ноль), ZeroDevisionError т.к. на ноль по правилам математики делить нельзя и т.д.
# Пример явный
#print("Before exceprion")
#i = 1 / 0
#print("After exception")

# Пример неявный (сработает ошибка только при наступлении события деления на ноль)
#a = input("a: ")
#b = input("b: ")
#c = a / b
#print(f"Result: {c}")

# Однако, есть конструкции для отлова исключений, как и в C# try/catch/finally
print("Before ex...")
try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(f"c: {c}")
except ZeroDivisionError as ex:
    print(f"Exception: {ex}")

print("After ex...")

# Вся конструкция по обработки ошибок выглядит так:
print("---")
try:
    # --Ваш код--
    print("Some code...")
except Exception as ex: # Класс ошибки
    # --Отлов самой ошибки--
    print(ex)
else:
    # --Код, который выполнится, если все прошло хорошо в блоке try--
    print("Some code after try block...")
finally:
    # --Этот блок кода будет выполняться в любом случае в самом конце цепочки--
    print("This code will be execute finally from here!")

# Как это будет выглядеть в коде
try:
    print(f"Application starts... {datetime.now()}")
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = a / b
except Exception as ex:
    print(f"Everything goes wrong! - Exception: {ex}")
else:
    print("Everything goes fine!")
    print(f"result c: {c}")
finally:
    print(f"Application stops... {datetime.now()}")

# Ошибки бывают двух видов:
# отлавливаемые — всё, что наследуются от класса Exception;
# неотлавливаемые — SystemExit, KeyboardInterrupt и т.д.

# Задача 1
# Пусть есть некий список с id изображений
#  index = 10
#  images_db = [101252, 521929, 215251]
# Пользователь вводит номер (индекс) элемента, который он хочет получить, а мы выводим на экран сам элемент.
# Индекс, который ввёл пользователь, находится в переменной index.
#  img_id = images_db[index]
#  print(f'Image id: {img_id}')
# Есть вероятность, что в переменной index содержится такое число, что при обращении к списку возникнет ошибка выхода
# за его пределы. Например, если значение переменной index будет равно 10, а длина списка будет равна 3, мы увидим на
# экране следующее:
# IndexError: list index out of range
# Чтобы обработать исключение необходимо обернуть код в конструкцию try/except
index = 10
images_db = [101252, 521929, 215251]
try:
    img_id = images_db[index]
    print(f'Image id: {img_id}')
except: # В результате выполнения такого кода на экран выведется последний элемент в списке images_db.
    img_id = images_db[-1]
    print(f'Image id: {img_id}')

# Задача 2
# Часто перед разработчиком по стоит задача обезопасить его приложение от падения
# Следующая проблема — попытка преобразования значений value_1 и value_2 к типу данных float.
# Попытка привести один тип данных к другому может обернуться ошибкой ValueError

my_dict = {'a': 10, 'b': '5.214', 'c': 'simple_string'}
key_1, key_2 = 'a', 'c'
try:
    value_1 = my_dict[key_1]
    value_2 = my_dict[key_2]
    value_1, value_2 = float(value_1), float(value_2)
    new_value = value_1 + value_2
except KeyError as ex:
    print(f"Введен неверный ключ: {ex}")
except ValueError as ex: # Таких дополнительных блоков с ошибками может быть множество
    print(f"Неверное преобразование типов")

# Если есть необходимость обработать все исключения можно написать except Exception as ex:
# Исключение Exception — это специальный тип исключения, который является родительским для всех видов исключений.
# Блок except отлавливает исключения в порядке их наследования — от родительского до дочерних.

# Задание 6.5
medicines = {'Ибупрофен': 99, 'Эспумизан': 279, 'Пенталгин': 119}
name = 'Визин'
# Такого ключа в словаре нет

#medicines = {'Ибупрофен': 99, 'Эспумизан': 279, 'Пенталгин': 119}
#name = 'Ибупрофен'
# 99

try:
    print(medicines[name])
except Exception:
    name = "Такого ключа в словаре нет"
    print(name)

# Ошибки можно вызывать самому, как и в других языках например C# throw (в python raise)
#age = int(input("How old are you?"))
# Проверяем, что возраст пользователя корректный
#if age > 100 or age <= 0:
    # Намеренно вызываем ошибку, указывая ее в тексте
#    raise ValueError("You are to old or don't exist")
    # Возраст выводится только в том случае если он введен корректно
#print(f"You are {age} years old")

# Но следует все организовать через блоки try-except...
try:
    print("App start...")
    age = int(input("How old are you?"))
    # Проверяем, что возраст пользователя корректный
    if age > 100 or age <= 0:
        # Намеренно вызываем ошибку, указывая ее в тексте
        raise ValueError("You are to old or don't exist")
        # Возраст выводится только в том случае если он введен корректно
except ValueError as ex:
    print("Incorrect age")
    print(f"{ex}")
else:
    print(f"You are {age} years old")
finally:
    print("App stops...")

# Задание 6.7
number = 20
# result = 0.5

#number = 7
# result = 1.429

#number = 0
# ZeroDivisionError: Вы собираетесь делить на 0

if number != 0:
    result = number / 10
    print(round(result, 3))
else:
    raise ZeroDivisionError("Вы собираетесь делить на 0")

x = 8
res = "greater than 10" if x > 10 else "less than 10"
print(res)

sentences = 'East or West home is best'
print(sentences[:10])