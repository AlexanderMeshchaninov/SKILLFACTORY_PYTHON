print('-' * 40)
# Правильное оформление функции (пример)
# BAD
# def func(x):
#     s_1=0
#     s_2=0
#     for i in x:
#         s_1=s_1+i
#     m_1=s_1/len(x)
#     for i in x:
#         s_2=s_2+i**2
#     m_2=s_2/len(x)
#     return m_2-m_1**2

# GOOD
def calculate_variance(number_list):
    '''ENG: Function to calculate variance of a list. RU: Функция для расчета дисперсии.'''
    
    sum_numbers = 0
    for number in number_list:
        sum_numbers += number
    mean = sum_numbers / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares += number**2 # Тут пробел не ставится ** т.к. имеет приоритет над +
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2 # Тут пробел не ставится ** т.к. имеет приоритет над +

number_list = [1, 2, 15, -12, 3, 6, 9]
print(calculate_variance(number_list))

print('-' * 40)
# --- Инструменты для DataScience ---
# --- Угадай число игра для примера ---
import numpy as np

def predict_number_game():
    """Функция (игра) угадай число от 1 до 100
    """
    # Генерируем число от 1 до 100
    number = np.random.randint(1, 101)
    # Количество попыток
    count = 0
    while True:
        count+=1
        # Цикл будет продолжаться пока мы не угадаем число
        predict_number = int(input(f"Угадайте число от 1 до 100 : "))
        
        # Основная логика игры
        if predict_number < number:
            print('Число должно быть больше')
        elif predict_number > number:
            print('Число должно быть меньше')
        else:
            print(f"Ура! Вы угадали число! {number}.\nВаши попытки {count}")
            break
    
# predict_number_game()

print('-' * 40)
# в аргументах указываем какой тип данных у нас на вход по умолчанию и -> int какой тип данных возвращает функция
def predict_number_game_self(number:int=1) -> int:
    """Функция (игра) угадай число где сам пк загадывает число и сам отгадывает

    Args:
        number (int, optional): заданное число. Defaults to 1.

    Returns:
        int: число попыток и угаданное число
    """
    count = 0
    while True:
        # Количество попыток
        count+=1
        # Предлагаемое число
        predict_number = np.random.randint(1, 100)
        # Условие выхода из цикла, когда число угадано
        if predict_number == number:
            break
        
    return(count)
        
count = predict_number_game_self(50)
print(f"число попыток: {count}")

def score_game(predict_number_game_self) -> int:
    """Вывод среднего значения угаданного числа список из 1000 подходов

    Args:
        predict_number_game_self (_type_): функция по угадыванию чисел

    Returns:
        int: среднее значение угаданных попыток
    """
    # Количество попыток
    count_lst = []
    np.random.seed(1) # фиксирует сид чисел 
    random_arr = np.random.randint(1, 100, size=1000) # задаем список чисел
    
    for number in random_arr:
        count = predict_number_game_self(number)
        count_lst.append(count)
    
    # среднее значение
    score = int(np.mean(count_lst))
    print(f"Ваш алгоритм угадывает число в среднем: {score} попыток")
    return(score)
    
# score_game(predict_number_game_self)
    
# --- Jupiter Notebook ---
# После запуска тут же увидим результат вывода. Это происходит из-за того, что в нашем файле game_v2.py прописан вызов функции score_game(). 
# Это не совсем корректно — библиотека не должна запускать свои функции, пока мы сами их не вызовем в главном файле.
# Это можно исправить. Чтобы отделить вызовы функций от импорта, необходимо в файле game_v2.py перенести вызовы функций в следующую конструкцию:

if __name__ == '__main__':
    # RUN
    score_game(predict_number_game_self)
    predict_number_game()