# print('-' * 40)
# # Задание 2.5 (посчитать кол-во символов в строке и возвести это число в 3 степень)
# python_string = 'Hello! My name is Python. I will help you to analyze some data.'
# result = python_string.__len__() ** 3
# print(result) # result = 250047
#
# print('-' * 40)
# # Задача 2.6
# predicted_time = 67.321
# real_time = 59.839
# absolute_error = round(predicted_time - real_time)
# print(absolute_error) # absolute_error = 7
#
# print('-' * 40)
# input_string = 'Hello! My name is Python. I will help you to analyze some data.'
# def preprosessing_str(input_str):
#     input_str = input_str.lower()
#     input_str = input_str.replace('!', '')
#     input_str = input_str.replace('.', '')
#     input_str = input_str.replace(',', '')
#     return len(input_str.split(' '))
#
# count_words = preprosessing_str(input_string)
# print(count_words)# count_words = 13
#
# input_string = 'There are many great articles about Artificial Intelligence and its benefits for business and society. However, many of these articles are too technical for the average reader.'
# ## count_words = 27
#
# print('-' * 40)
# # Задача 2.8
# file_path = 'data/images/train/10394.jpg'
# def preprosessing_file(path):
#     path_split = path.split('/')
#     file = path_split[-1]
#     file = file.split('.')
#     file_name = file[0]
#     file_extension = file[1]
#     return file_name, file_extension
# file_name, file_extension = preprosessing_file(file_path)
# print(file_name)
# print(file_extension)
# ## file_name = '10394'
# ## file_extension = 'jpg'
#
# file_path = 'data/images/validation/748923.gif'
# ## file_name = '748923'
# ## file_extension = 'gif'
#
# file_path = 'data/images/384300.png'
# ## file_name = '384300'
# ## file_extension = 'png'
#
# print('-' * 40)
# # Задача 2.9
# generated_text = "глаза нее на поднял он и она попросила что-нибудь скажи"
# def reversed_str(txt):
#     str_lst =  txt.split(' ')[::-1]
#     return str(' '.join(str_lst))
# updated_text = reversed_str(generated_text)
# print(updated_text) # updated_text = "скажи что-нибудь попросила она и он поднял на нее глаза"
#
# generated_text = "задачи своей решения способ или информацию ищет он поисковик в запрос вводит человек когда"
# ## updated_text = когда человек вводит запрос в поисковик он ищет информацию или способ решения своей задачи
#
# print('-' * 40)
# # Задача 2.10
# def change_password(user_name, new_password):
#     return f"Пользователь {user_name} сменил пароль на {new_password}"
#
# print(change_password('Andrey', '31andrey12QK'))
# # Пользователь Andrey сменил пароль на 31andrey12QK
#
# print(change_password('Vasilisk', 'uaf12laK'))
# # Пользователь Vasilisk сменил пароль на uaf12laK
#
# print('-' * 40)
# # Задача 3.5
# car_dict = {
#     'car_ID': [123, 117, 111, 82, 101, 96, 156, 2, 58, 49],
#     'fueltype': ['gas', 'diesel', 'diesel', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas'],
#     'horsepower': [68, 95, 95, 88, 97, 69, 62, 111, 101, 176],
#     'price': [7609.0, 17950.0, 13860.0, 8499.0, 9549.0, 7799.0, 8778.0, 16500.0, 13645.0, 35550.0]
# }
#
# def preprosessing_car_dict(car_dict):
#     # средняя стоимость авто
#     mean_price = round(sum(car_dict['price']) / len(car_dict['price']), 1)
#     # кол-во дизельных авто
#     count_diesel = car_dict['fueltype'].count('diesel')
#     # двигатель с минимальной мощностью
#     min_horsepower = min(car_dict['horsepower'])
#     return mean_price, count_diesel, min_horsepower
#
# mean_price, count_diesel, min_horsepower = preprosessing_car_dict(car_dict)
# print(mean_price, count_diesel, min_horsepower)
# # mean_price = 13973.9
# # count_diesel = 2
# # min_horsepower = 62
#
# print('-' * 40)
# # Задача 3.6
#
# def check_duplicates(ls):
#     unique_el = set(ls)
#     if len(unique_el) == len(ls):
#         return False
#     else:
#         return True
#
# lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
# print(check_duplicates(lst))
# # True
#
# lst = list(range(0, 15))
# print(check_duplicates(lst))
# # False
#
# print('-' * 40)
# # Задача 3.7
# def swap_places(ls):
#     first = ls[0]
#     last = ls[-1]
#     ls[-1] = first
#     ls[0] = last
#     return ls
# print(swap_places([1, 2, 3]))
# ## [3, 2, 1]
# print(swap_places([1, 2, 3, 4, 5]))
# ## [5, 2, 3, 4, 1]
# print(swap_places(['н', 'л', 'о', 'с']))
# ## ['с', 'л', 'о', 'н']
#
# print('-' * 40)
# # * Задача 3.8
# # Напишите функцию equalize_lengths(), которая принимает на вход список и возвращает новый список из строк одинаковой длины.
# def equalize_lengths(ls):
#     def preprosessing_el(input_string):
#         curr_len = len(input_string)
#         if curr_len < max_str:
#             # Добавляем нижнее подчеркивание, столько раз сколько должно хватить до максимальной длинны слова (разницу)
#             return input_string + '_' * (max_str - curr_len)
#         else:
#             return input_string
#     def elem_lenght(x):
#         return len(x)
#     max_str = max(map(elem_lenght, ls))
#     map_elem = map(preprosessing_el, ls)
#     return list(sorted(map_elem, key = lambda x: x.count('_')))
#
# print(equalize_lengths(['крот', 'белка', 'выхухоль']))
# # ['выхухоль', 'белка___', 'крот____']
#
# print(equalize_lengths(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
# # ['aaaaa', 'aaaa_', 'aaa__', 'aa___', 'a____']
#
# print(equalize_lengths(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
#
# # ['qweasdqweas', 'ewqqqqq____', 'rteww______', 'q__________']
#
# # Другое решение!
# def equalize_lengths(lst):
#     # Сортируем список по длине строк в нём в порядке убывания
#     sorted_lst = sorted(lst, key=lambda x: len(x), reverse=True)
#     # Находим максимальную длину строки
#     max_len = len(sorted_lst[0])
#     # Создаём цикл по индексам элементов списка
#     for i in range(1, len(sorted_lst)):
#         # Добавляем к i-ой строке n нижних подчёркиваний справа,
#         # где n — результат вычитания длины i-ой строки из максимальной длины строки.
#         sorted_lst[i] += '_' * (max_len - len(sorted_lst[i]))
#     # Возвращаем результат
#     return sorted_lst
#
# print('-' * 40)
# # * Задача 4.5
# # возвращает 1, если число положительное, -1 — если число отрицательное, и 0 — если число равно 0.
#
# def check_number_sign(num):
#     if num == 0: return 0
#     elif num > 0: return 1
#     else: return -1
#
# print(check_number_sign(5290))
# # 1
# print(check_number_sign(-983))
# # - 1
# print(check_number_sign(0))
# # 0
#
# print('-' * 40)
# # * Задача 4.6
# def find_min_number(a, b, c):
#     num_tulip = (a, b, c)
#     min = num_tulip[0]
#     for el in num_tulip:
#         if el < min:
#             min = el
#     return min
#
# print(find_min_number(130, 122, 19))
# # 19
# print(find_min_number(10.9, 12.2, 18.4))
# # 10.9
#
# print('-' * 40)
# # * Задача 4.7
#
# def sum_min_numbers(a, b, c):
#     num_lst = [a, b, c]
#     max_num = num_lst[0]
#     for el in num_lst:
#         if el > max_num:
#             max_num = el
#     num_lst.remove(max_num)
#     return sum(num_lst)
#
# print(sum_min_numbers(1, 2, 3))
# # 3
# print(sum_min_numbers(1, 2, -10))
# # -9
#
# print('-' * 40)
# # Задание 4.8
# def division(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Zero division error!")
#         return None
#
# print(division(189, 36))
# # 5.25
# print(division(1, 0))
# # Zero division error!
# # None
#
# print('-' * 40)
# # Задание 4.9
# def get_prediction(x1, x2):
#     if x1 < 20:
#         if x2 < 200:
#             return 300.5
#         else:
#             return 65.7
#     else:
#         if x2 < 170:
#             if x1 < 40:
#                 return -64.1
#             else:
#                 return 0.7
#         else:
#             return 1023
#
# print(get_prediction(x1=15, x2=150))
# # 300.5
# print(get_prediction(x1=15, x2=350))
# # 65.7
# print(get_prediction(x1=35, x2=100))
# # -64.1
# print(get_prediction(x1=175, x2=100))
# # 0.7
# print(get_prediction(x1=175, x2=200))
# # 1023
#
# print('-' * 40)
# # Задание 5.4
# def more_than_n(lst, n):
#     new_lst = []
#     if lst == []:
#         return []
#     else:
#         for num in lst:
#             if abs(num) > n:
#                 new_lst.append(num)
#     return new_lst
#
# print(more_than_n([-1, 4, 4.2, 42.2, -3.4, -5.2], 3))
# # [4, 4.2, 42.2, -3.4, -5.2]
# print(more_than_n([-1, 4, 4.2, 42.2, -3.4, -5.2], 10))
# # [42.2]
# print(more_than_n([], 10))
# # []
#
# print('-' * 40)
# # Задание 5.5
# def lucky_ticket(num):
#     num = str(num)
#     first_sum = 0
#     last_sum = 0
#     f_n = list(num[:3])
#     l_n = list(num[3:])
#     for i, v in enumerate(f_n): first_sum += int(f_n[i])
#     for i, v in enumerate(l_n): last_sum += int(l_n[i])
#     return True if first_sum == last_sum else False
#
# print(lucky_ticket(111111))
# # True
# print(lucky_ticket(123456))
# # False
# print(lucky_ticket(515740))
# # True
#
# print('-' * 40)
# # Задание 5.5
# def holes_count(num):
#     num = str(num)
#     num_lst = list(num)
#     result = 0
#     for n in num_lst:
#         n = int(n)
#         if n in [0,4,6,9]:
#             result += 1
#         if n == 8:
#             result += 2
#     return result
#
# print(holes_count(8))
# # 2
# print(holes_count(146))
# # 2
# print(holes_count(84628))
# # 6
#
# print('-' * 40)
# # Задание 5.7
# def even_numbers_in_matrix(matrix):
#     count = 0
#     for i, val in enumerate(matrix):
#         for k in val:
#             if k % 2 == 0:
#                 count += 1
#     return count
#
# matrix_example = [
#     [1, 5, 4],
#     [4, 2, -2],
#     [7, 65, 88]
# ]
#
# print(even_numbers_in_matrix(matrix=matrix_example)) # 5
#
# print('-' * 40)
# # * Задание 5.8 (операция сложения двух матриц)
# # Отдельная функция по проверке совпадения матриц
# def is_matrix_equals(matrix1, matrix2):
#     res_m1 = {'lines':0, 'col':0}
#     res_m2 = {'lines':0, 'col':0}
#     for m_1 in matrix1:
#         res_m1['lines'] += 1
#         res_m1['col'] += len(m_1)
#     for m_2 in matrix2:
#         res_m2['lines'] += 1
#         res_m2['col'] += len(m_2)
#     return True if res_m1 == res_m2 else False
#
# def matrix_sum(matrix1, matrix2):
#     # Обязательная проверка, что матрицы совпадают по размеру
#     if is_matrix_equals(matrix1, matrix2):
#         new_matrix = []
#         temp = []
#         for i in range(len(matrix1)):
#             for k in range(len(matrix2)):
#                 temp.append(matrix1[i][k] + matrix2[i][k])
#             new_matrix.append(temp)
#             temp = []
#         return new_matrix
#     else:
#         print("Error! Matrices dimensions are different!")
#         return None
#
# matrix_example = [
#           [1, 5, 4],
#           [4, 2, -2],
#           [7, 65, 88]
# ]
#
# print(matrix_sum(matrix1=matrix_example, matrix2=matrix_example))
# # [[2, 10, 8], [8, 4, -4], [14, 130, 176]]
#
# matrix1_example = [
#           [1, 5, 4],
#           [4, 2, -2]
# ]
#
# matrix2_example = [
#           [10, 15, 43],
#           [41, 2, -2],
#           [7, 5, 7]
# ]
#
# print(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# # Error! Matrices dimensions are different!
# # None
#
# matrix1_example = [
#           [1, 5, 4, 5],
#           [4, 2, -2, -5],
#           [4, 2, -2, -5]
# ]
#
# matrix2_example = [
#           [10, 15, 43],
#           [41, 2, -2],
#           [7, 5, 7]
# ]
#
# print(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# # Error! Matrices dimensions are different!
# # None
#
# print('-' * 40)
# # Задание 6.5
# def print_personal_data(**kwargs):
#     print()
#     for el in list(sorted(kwargs.items())):
#         print(f"{el[0]}:{el[1]}")
#
# print_personal_data(first_name='John', last_name='Doe', age=28, position='Python developer')
# # age: 28
# # first_name: John
# # last_name: Doe
# # position: Python developer
#
# print_personal_data(first_name='Jack', last_name='Smith', age=32, work_experience ='5 years', position='Project manager')
# # age: 32
# # first_name: Jack
# # last_name: Smith
# # position: Project manager
# # work_experience: 5 years
#
# print('-' * 40)
# # Задание 6.6
# def get_words_list(text):
#     punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#     for p in punctuation_list: text = text.replace(p, '')
#     text = text.lower()
#     return text.split(' ')
#
# text_example = "Arrakis, the planet known as Dune, is forever his place."
#
# print(get_words_list(text=text_example))
# # ['arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
#
# print('-' * 40)
# # Задание 6.7
# def get_unique_words(words_list):
#     unique_lst = set(words_list)
#     sorted_lst = sorted(unique_lst)
#     return sorted_lst
#
# words_list_example = ['and', 'take', 'the', 'most', 'special', 'care', 'that', 'you', 'locate', "muad'dib", 'in', 'his', 'place', 'the', 'planet', 'arrakis', 'do', 'not', 'be', 'deceived', 'by', 'the', 'fact', 'that', 'he', 'was', 'born', 'on', 'caladan', 'and', 'lived', 'his', 'first', 'fifteen', 'years', 'there', 'arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
#
# print(get_unique_words(words_list=words_list_example))
# ## ['and', 'arrakis', 'as', 'be', 'born', 'by', 'caladan', 'care', 'deceived', 'do', 'dune', 'fact', 'fifteen', 'first', 'forever', 'he', 'his', 'in', 'is', 'known', 'lived', 'locate', 'most', "muad'dib", 'not', 'on', 'place', 'planet', 'special', 'take', 'that', 'the', 'there', 'was', 'years', 'you']
#
# print('-' * 40)
# # Задание 6.8
# def get_most_frequent_word(text):
#     # Если пустая строка возвращаем пустую строку
#     if not text:
#         return text
#     else:
#         # Получаем только список слов
#         def get_words_list(text):
#             punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
#             for p in punctuation_list: text = text.replace(p, '')
#             text = text.lower()
#             return text.split(' ')
#         # Получаем списко уникальных слов (без повторений)
#         def get_unique_words(words_list):
#             unique_lst = set(words_list)
#             return unique_lst
#         words_list = get_words_list(text)
#         unique_words_set = get_unique_words(words_list)
#         words_frequency = map(lambda x: (x, round(words_list.count(x) / len(unique_words_set), 2)), unique_words_set)
#         filtered_words = filter(lambda x: x[1] >= 0.15, words_frequency)
#         return list(filtered_words)[0][0]
#
# text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
# print(get_most_frequent_word(text_example))
# # the
#
# text_example = "Есть урок, который идет не сорок пять минут, а всю жизнь. Этот урок проходит и в классе, и в поле, и дома, и в лесу. Я назвал этот урок седьмым потому, что в школе обычно бывает не больше шести уроков. Не удивляйтесь, если я скажу, что учителем на этом уроке может быть и береза возле вашего дома, и бабушка, и вы сами (В. Песков)"
# print(get_most_frequent_word(text_example))
# # и
#
# print('-' * 40)
# # Задание 6.9
# # В распоряжении есть список кортежей data. Каждый кортеж в нём состоит из четырёх элементов:
# # 0: имя человека,
# # 1: балл за экзамен по русскому языку,
# # 2: балл за экзамен по математике,
# # 3: балл за экзамен по информатике.
# data = [
#     ('Amanda', 37, 78, 67),
#     ('Patricia', 78, 93, 68),
#     ('Marcos', 79, 67, 89),
#     ('Dmitry', 67, 68, 100),
#     ('Andrey', 100, 78, 76),
#     ('Victoria', 93, 69, 96),
# ]
# def get_total_score(data):
#     updated_data = map(lambda x: (*x, (x[1] + x[2] + x[3])), data)
#     print(list(sorted(updated_data, key=lambda x: x[4])))
#
# print(get_total_score(data))
# # [('Amanda', 37, 78, 67, 182), ('Marcos', 79, 67, 89, 235), ('Dmitry', 67, 68, 100, 235), ('Patricia', 78, 93, 68, 239), ('Andrey', 100, 78, 76, 254), ('Victoria', 93, 69, 96, 258)]
#
# print('-' * 40)
# # Задание 6.10 (Рекурсивная функци для словаря, извлечь идентификатор)
# data = {
#     "type": "video",
#     "videoID": "vid001",
#     "links": [
#         {"type":"video", "videoID":"vid002", "links":[]},
#         {   "type":"video",
#             "videoID":"vid003",
#             "links": [
#             {"type": "video", "videoID":"vid004"},
#             {"type": "video", "videoID":"vid005"},
#             ]
#         },
#         {"type":"video", "videoID":"vid006"},
#         {   "type":"video",
#             "videoID":"vid007",
#             "links": [
#             {"type":"video", "videoID":"vid008", "links": [
#                 {   "type":"video",
#                     "videoID":"vid009",
#                     "links": [{"type":"video", "videoID":"vid010"}]
#                 }
#             ]}
#         ]},
#     ]
# }
#
# # Список для хранения результатов
# video_ids = []
# def find_video(data):
#     # Проверка, является ли текущий элемент словарем
#     if isinstance(data, dict):
#         # Итерируем ключи словаря
#         for key, value in data.items():
#             # Если ключ имеет название 'videoID'
#             if key == 'videoID':
#                 # Добавляем значение в новый словарь
#                 video_ids.append(value)
#             # Если ключ другой, то берем следующее значение
#             else:
#                 find_video(value)
#     # Так же проверяем яляется ли входные данные списком
#     elif isinstance(data, list):
#         # Обходим список
#         for item in data:
#             # Итерируем элементы списка
#             find_video(item)
#
# find_video(data)
# print(video_ids)
# # ['vid001', 'vid002', 'vid003', 'vid004', 'vid005', 'vid006', 'vid007', 'vid008', 'vid009', 'vid010']
#
# print('-' * 40)
# # Задание 7.1
# # Небольшая частная сыроварня, которая делает поставки в разные рестораны, просит вас проанализировать их производство
# # с целью его дальнейшего расширения.
# # Сыроварня предоставила данные о каждом из производимых ей сыров в виде словаря cheese_data.
# # Ключами словаря являются названия сыров, а значениями — списки, в которых последовательно
# # указываются следующие параметры сыра:
#
# # [0] название сыра;
# # [1] закупочная цена (рублей за 100 грамм);
# # [2] максимальный объём производства (килограммов в месяц);
# # [3] жирность (в процентах);
# # [4] тип (твёрдый, полутвёрдый, мягкий, полумягкий).
#
# cheese_data = {
#     'чеддер': [370, 5000, 33, 'твердый'],
#     'пармезан': [510, 4000, 29, 'твердый'],
#     'гауда': [250, 3700, 27, 'полутвердый'],
#     'эдам': [220, 10000, 30, 'полутвердый'],
#     'горгонзола': [320, 3000, 32, 'полумягкий'],
#     'рокфор': [340, 15000, 31, 'полумягкий'],
#     'стилтон': [360, 7000, 35, 'полумягкий'],
#     'камамбер': [250, 8000, 24, 'мягкий'],
#     'бри': [310, 6500, 28, 'мягкий'],
# }
#
# # 1 (отобрать сыры имеющие жирность не менее n %), написать функцию
# def filter_by_fat(cheese_data, n):
#     updated_dict = {}
#     for cheese in cheese_data.items():
#         cheese_name = cheese[0]
#         fat = cheese[1][2]
#         if fat < n:
#             updated_dict[cheese_name] = fat
#     return updated_dict
#
# print(filter_by_fat(cheese_data, n=30))
# # {'пармезан': 29, 'гауда': 27, 'камамбер': 24, 'бри': 28}
#
# print(filter_by_fat(cheese_data, n=25))
# # {'камамбер': 24}
#
# print('-' * 40)
# # Задание 7.2 (сколько денег (в рублях) сможет в месяц зарабатывать сыроварня, если будет производить
# # максимально возможное количество сыра.)
# def count_money(cheese_data):
#     result = 0
#     for cheese in cheese_data.items():
#         purchasing_price, max_prod, fat, type = cheese[1]
#         purchasing_price = purchasing_price * 10
#         result += purchasing_price * max_prod
#     return result
#
# print(count_money(cheese_data))
# ## 196100000
#
# print('-' * 40)
# # Задание 7.3
# def find_cheese_type(cheese_data, cheese_type):
#     result = []
#     for cheese in cheese_data.items():
#         name = cheese[0]
#         purchasing_price, max_prod, fat, type = cheese[1]
#         if type == cheese_type:
#             result.append(name)
#     return result
#
# print(find_cheese_type(cheese_data, cheese_type='мягкий'))
# # ['камамбер', 'бри']
#
# print(find_cheese_type(cheese_data, cheese_type='полумягкий'))
# # ['горгонзола', 'рокфор', 'стилтон']
#
# print('-' * 40)
# # Задание 7.4
# def sort_cheese(cheese_data):
#     result = []
#     for cheese in cheese_data.items():
#         name = cheese[0]
#         purchasing_price, max_prod, fat, type = cheese[1]
#         result.append((name, purchasing_price))
#     res_sorted = sorted(result, key=lambda x: x[1])
#     return list(map(lambda s: s[0], res_sorted))
#
# print(sort_cheese(cheese_data))
# # ['эдам', 'гауда', 'камамбер', 'бри', 'горгонзола', 'рокфор', 'стилтон', 'чеддер', 'пармезан']
#
# print('-' * 40)
# # Задание 7.5 (проверка на дубли)
# def purchase(ingredients):
#     counts = {}
#     is_unique = True
#     for ingr in ingredients:
#         if ingr in counts:
#             # Увеличиваем значение для существующего элемента
#             counts[ingr] += 1
#         else:
#             # Добавляем новый элемент в словарь с начальным значением 1
#             counts[ingr] = 1
#     for item, count in counts.items():
#         if count > 1:
#             # Если ингредиент дублируется, выводится строка
#             print(f"Вы продублировали ингредиент {item} в заказе {count} раз(а)")
#             is_unique = False
#     if is_unique:
#         # Если все ингредиенты разные
#         print("Ваш заказ оформлен верно")
#
# ingredients = ['кислота уксусная', 'кислота лимонная', 'закваска', 'кислота молочная', 'пряность', 'бактерии', 'аннато', 'кальций', 'калий', 'специя', 'молоко коровье', 'молоко овечье', 'фермент', 'соль', 'сливки', 'грибки', 'ароматизатор', 'молоко козье', 'дрожжи', 'каротин']
# purchase(ingredients)
# # Ваш заказ оформлен верно
#
# ingredients = ['молоко коровье', 'молоко овечье', 'бактерии', 'молоко козье', 'сливки', 'фермент', 'закваска', 'молоко коровье', 'соль', 'молоко коровье', 'бактерии', 'молоко овечье', 'кислота лимонная', 'грибки', 'соль', 'дрожжи', 'кислота уксусная', 'кальций', 'калий', 'каротин', 'аннато', 'специя', 'пряность', 'ароматизатор', 'соль', 'кислота молочная']
# purchase(ingredients)
# # Вы продублировали ингредиент бактерии в заказе 2 раз(а)
# # Вы продублировали ингредиент молоко коровье в заказе 3 раз(а)
# # Вы продублировали ингредиент молоко овечье в заказе 2 раз(а)
# # Вы продублировали ингредиент соль в заказе 3 раз(а)
#
# # ---Задачи с собеседования---
# # Задание 1
# print('Задание 1')
# print('-' * 100)
#
# # Функция ввода пользователем данных
# def user_input():
#     # Внутренняя функция для поиска пересечений в списке
#     def pure_intersection(numbers_a, numbers_b):
#         # Список А
#         list_a = set(numbers_a)
#         # Список Б
#         list_b = set(numbers_b)
#         # Получаем пересечение двух множеств
#         intersection_list = list(list_a.intersection(list_b))
#         return intersection_list
#
#     try:
#         # Временные переменные в которые получаем ввод данных от пользователя (последовательность А и Б)
#         temp_input_a = input(f'Введите 1-ую последовательность идентификаторов: ').split(', ')
#         temp_input_b = input(f'Введите 2-ую последовательность идентификаторов: ').split(', ')
#         # Преобразуем строковые данные в целочисленные значения
#         numbers_a = list(map(int, temp_input_a))
#         numbers_b = list(map(int, temp_input_b))
#         # Получаем пересечения
#         result = pure_intersection(numbers_a, numbers_b)
#         return result
#     except Exception:
#         print("Некорректный ввод")
#
# result = user_input()
# print(result)
#
# # Ввод:
# # 108, 138, 42, 52, 14
# # 109, 13, 52, 32, 42, 14, 109
# #
# # Вывод:
# # [42, 52, 14]
#
# # Задание 2
# print('Задание 2')
# print('-' * 100)
#
# # Функция ввода пользователем последовательности чисел
# def user_input():
#     # Внутрення функция для нахождения минимума и максимума
#     def find_min_max(num):
#         minimum = min(num)
#         maximum = max(num)
#         return minimum, maximum
#
#     input_string = input('Введите последовательность чисел: ')
#     if not input_string: return []
#     # Препроцессинг строки (замена запятой на точку)
#     input_string = input_string.replace(',', '.')
#     input_string = input_string.split(' ')
#     # Преобразовываем строковые данные в данные float или int
#     # Стоит отметить, что мне пришлось использовать вместо for цикл while т.к. в цикле for при удалении элемента был бы
#     # пропуск итерации. С циклом while проще вернуть итерацию на шаг назад
#     # переменная для итерации
#     ite = 0
#     while ite < len(input_string):
#         # просто меременная для элемента (для удобства)
#         current_element = input_string[ite]
#         # Удаляем из списка значения написанные прописью
#         if current_element.isalpha():
#             input_string.remove(current_element)
#             # возвращаемся на шаг назад, т.к. список сдвигается влево на один элемент после удаления
#             ite -= 1
#         # Можно было бы переопределить функцию isdigit(), чтобы работала как для int, так и для float, но решил сделать без
#         # переопределения
#         # Если элемент содержит точку, то мы приобразовываем элемент строки в тип float
#         elif '.' in current_element:
#             input_string[ite] = float(current_element)
#         # В противном случае преобразовываем в int
#         else:
#             input_string[ite] = int(current_element)
#         # Двигаем итератор на шаг вперед
#         ite += 1
#
#     # Просто для удобства записываем в другую переменную наш отредактированный список
#     numbers = input_string
#     # Используя внутренню функцию получаем минимум и максимум в списке
#     minimum, maximum = find_min_max(numbers)
#     # Распечатываем результат
#     print(f"Minimum: {minimum}")
#     print(f"Maximum: {maximum}")
#
# user_input()
# # Ввод:
# # -2,56 25,002 восемь 19,13 13 -37,5
# #
# # Вывод:
# # Minimum: -37.5
# # Maximim: 25.002
#
# # Задание 3
# print('Задание 3')
# print('-' * 100)
#
# # Функция ввода пользователем данных
# def user_input():
#     # Внутренняя функция для высчитывания медианы в списке
#     def find_median(num):
#         # Если длинна списка четная, то определяем медиану таким образом
#         if len(num) % 2 == 0:
#             # Получаем условную середину списка
#             mid_el = len(num) // 2
#             # Вычисляем среднее арифметическое между центральными элементами в последовательности
#             median = (num[mid_el - 1] + num[mid_el]) / 2
#         # Если список нечетный, то
#         else:
#             # Получаем середину списка (делим его нацело)
#             mid_el = len(num) // 2
#             # Медианой будет центральный элемент списка (среднее арифметическое искать не нужно)
#             median = num[mid_el]
#         # Возвращаем результат в типе float
#         return float(median)
#     try:
#         # Переменная в которую получаем последовательность чисел от пользователя
#         input_string = input('Введите последовательность чисел: ').split(', ')
#         # Если пользователь ничего не ввел, то выкидываем ошибку и сообщение
#         if not input_string: raise Exception
#         # Преобразуем строковые данные в целочисленные значения
#         numbers = list(map(int, input_string))
#         # Отсортировываем список (обязательно)
#         numbers.sort()
#         # Получаем медиану списка
#         median = find_median(numbers)
#         # Распечатываем результат
#         print(f"Median: {median}")
#     except Exception:
#         print("Некорректный ввод")
#
# user_input()
#
# # Ввод:
# # 1, 5, 2, 3, 6
# # Вывод:
# # Median: 3.0
#
# # Ввод:
# # 100, 5, 2, 4, 3, 6
# # Вывод:
# # Median: 4.5
#
# # Ввод:
# # Вывод:
# # Некорректный ввод
#
# # Ввод:
# # десять, 10, пять, 7, семь
# # Вывод:
# # Некорректный ввод
#
# # Задание 4
# print('Задание 4')
# print('-' * 100)
#
# # Функция ввода пользователем данных
# def user_input():
#     # Словари с десятками и сотнями (решил разбить большой словарь на несколько маленьких, плюс добавил окончания)
#     hundreds_dict = {"сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600, "семьсот": 700,
#                     "восемьсот": 800, "девятьсот": 900}
#     des_dict = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,
#                 "девять": 9, "десять": 10, "одинадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
#                 "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
#                 "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
#                 "восемьдесят": 80, "девяносто": 90}
#     # Внутренняя функция для преобразования строки в число
#     def transform_string_to_integer(input_string):
#         number_result = 0
#         for s in input_string:
#             # Если элемент содержит слово ноль
#             if s in ["ноль"]:
#                 number_result = 0
#             # Если элемент содержит слова в словаре сотней
#             elif s in hundreds_dict.keys():
#                 number_result += hundreds_dict[s]
#             # Если элемент содержит слова c тясячами
#             elif s in ["тысяча", "тысяч", "тысячи"]:
#                 number_result *= 1000
#             # Если элемент содержит слова c миллионами
#             elif s in ["миллион", "миллиона"]:
#                 number_result *= 1000000
#             # Если элемент содержит слова в словаре десяткой
#             elif s in des_dict.keys():
#                 number_result += des_dict[s]
#         return number_result
#
#     # Переменная в которую получаем число написанно словами
#     input_string = input('Введите число словами: ').split(' ')
#     # Получаем результат трансформации слова в число
#     result = transform_string_to_integer(input_string)
#     # Распечатываем результат
#     print(result)
#
# user_input()
#
# # Ввод:
# # один
# # Вывод:
# # 1
#
# # Пример №2:
# # Ввод:
# # двадцать
# # Вывод:
# # 20
#
# # Пример №3:
# # Ввод:
# # двести сорок шесть
# # Вывод:
# # 246
#
# # Пример №4:
# # Ввод:
# # семьсот восемьдесят три тысячи девятьсот девятнадцать
# # Вывод:
# # 783919
#
# # * Задание 5
# print('Задание 5')
# print('-' * 100)
# # Функция ввода пользователем данных
# def decompose_factorial():
#     # Внутренняя функция для вычисления факториала числа n и выполнения разложения факториала на простые множители
#     def factorial_func(n):
#         if n == 1 or n == 0:
#             return 1
#         return factorial_func(n-1) * n
#
#     # Внутренняя функция для вычисления множителя
#     def multiplier_func(n):
#         multi = []
#         d = 2
#         while d * d <= n:
#             if n % d == 0:
#                 multi.append(d)
#                 n //= d
#             else:
#                 d += 1
#         if n > 1:
#             multi.append(n)
#         return multi
#
#     # Переменная в которую получаем число от пользователя
#     n = int(input('Введите число: '))
#     # Получаем число факториала
#     num_fact = factorial_func(n)
#     # Получаем множитель
#     multi = multiplier_func(num_fact)
#     # Сортируем список
#     multi.sort()
#     # Получаем список без дублей
#     multi_set = set(multi)
#     # строка-результат
#     result_str = ''
#     for i, num in enumerate(multi_set):
#         # сам множитель
#         number = num
#         # получаем степень числа т.е. сколько раз данный множитель содержится в списке
#         degree = multi.count(number)
#         # Если степень множителя больше двух значит его нужно восвести в степень
#         if degree >= 2:
#             # составляем строку где {число} ^ {степень} *
#             result_str += str(number) + '^' + str(degree) + ' * '
#         # Тут примерно следующее, если мы перебираем последний элемент то строка уже будет без * (не идеально, да!)
#         elif i == len(multi_set) - 1:
#             result_str += str(number)
#         # если число без степень (представлено в списке в единственном числе), то добавляем его без знака ^
#         else:
#             result_str += str(number) + ' * '
#     # Распечатываем результат
#     return f'{n}! = {result_str}'
#
# print(decompose_factorial())
# #12! = 2^10 * 3^5 * 5^2 * 7 * 11
# # Ввод:
# # 5
# # Вывод:
# # 5! = 2^3 * 3 * 5
# # Пример №2:
# #
# # Ввод:
# # 22
# # Вывод:
# # 22! = 2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19
# # Пример №3:
# #
# # Ввод:
# # 25
# # Вывод:
# # 25! = 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23

import string
# * Задание 6
print('Задание 6')
print('-' * 100)
def user_input():
    # Библиотека с латинским алфавитом
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet)
    # Внутренняя функция замены двух одинаковых букв во введённой строке на следующую по алфавиту букву
    def replace_duplicates(s):
        step = 1
        while True:
            # Создаем список повторных букв (дубликатов)
            dublicates = []
            for char in s:
                if s.count(char) > 1:
                    dublicates.append(char)

            # Если не осталось дубликатов
            if not dublicates: break

            # Цикл нахождения дубликатов и удаление
            for char in set(dublicates):
                # Проверка если есть дубликаты
                if char in dublicates:
                    # Это дубликат
                    dub = char
                    if char == 'z':
                        s = s.replace(dub, '', 2)
                        s = s + alphabet_list[0]
                        print(f'step {step}: {s}')
                    else:
                        s = s.replace(dub, '', 2)
                        l_index = alphabet_list.index(char)
                        s = s + (alphabet_list[l_index + 1])
                        print(f'step {step}: {s}')
                step = step + 1
        print(f'output: {s}')
    # Строка от пользователя
    s = input('Введите строку латинскими буквами: ')
    if s.isalpha():
        # Функция замены дубликатов
        replace_duplicates(s.lower())
    else:
        print("Некорректный ввод")

user_input()
# input:
# zzzab
# step 1: zaba
# step 2: zbb
# step 3: zc
# output:
# cz

# input:
# hhakafh
#
# step 1: haakfi
# step 2: hkfib
# output:
# hkfib