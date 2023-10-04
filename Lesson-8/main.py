# -- UNUMERATE --
print("-------")
# Cпособ 1 (цикл по элементам списка)
# Заданный список динамики пользователей
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# Задаем номер дня
number = 1
# Задаем цикл по элементам списка user_dynamics
for dynamic in user_dynamics:
    print(f"Day: {number}, {dynamic}")
    number += 1

print("-------")
# Способ 2 (цикл по индексам списка)
# Задаем цикл по индексам списка user_dynamics
N = len(user_dynamics)
for i in range(N):
    print(f"Day: {i + 1}, {user_dynamics[i]}")

print("-------")
# Способ 3
# Однако, можно объединить два подхода выше и организовать проход с помощью функции enumerate()
# Как можно обратить внимание, что enumerate выдает два параметра индекс элемента и его значение
for index, value in enumerate(user_dynamics):
    print(f"Day: {index + 1}, {value}")

print("--------")
# Задача 5.3 (переписать код под enumerate)
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
number_negative = None # объявляем переменную, в которой будем хранить номер последнего дня оттока, изначально она пустая (None)
# создаём цикл по элементам последовательности от 0 до N (не включая N)
for index, value in enumerate(user_dynamics): # index — индекс текущего элемента
    # проверяем условие оттока — текущий элемент отрицательный
    if value < 0: # если условие истинно,
        number_negative = index + 1  # перезаписываем значение номера дня
        print("Churn value: ", value) # выводим количество ушедших в этот день пользователей
        print("Number day: ", number_negative) # выводим номер дня

print("--------")
# Задача 5.4 (перезаписать в новый список элементы (первые три символа и индекс), если элемент содержит меньше трех то всю строку)
str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
## cut_str_list = [[0, 'Hel'], [1, 'my'], [2, 'nam'], [3, 'is'], [4, 'Eze'], [5, 'I'], [6, 'lik'], [7, 'kni']]
cut_str_list = []
for index, value in enumerate(str_list):
    cut_value = list(value)
    if len(cut_value) < 2:
        cut_value = cut_value
    else:
        cut_value = cut_value[:3]
    str_value = "".join([str(e) for e in cut_value])
    cut_str_list.append([index, str_value])
print(cut_str_list)

print("--------")
# -- Break --
# Оператор для прерывания цикла
# Задача 1
# Например у нас есть список to_inventory и нам из него нужно переложить 'вещи' в inventory. Однако, при достижении трех вещей цикл будет
# прерываться и появляться предупреждение:
to_inventory = ['Blood Moon Sword', 'Sunset-colored sword', 'Bow of Stars', 'Gain Stone']
inventory = []
for item in to_inventory:
    if len(inventory) == 3:
        print("Inventory is full!")
        break
    inventory.append(item)

print(inventory)

# Задача 2 (Например, изначально задано простое число 3, его возвели в степень 4 и получили число 81. Необходимо написать
# программу, которая проверяет, что число n является степенью числа 3.)

# Задаем некоторое число n
n = 27
# создаем бесконечный цикл
while True:
    if n % 3 == 0:
        # Если условие выполняется, новое число — результат целочисленного деления на 3.
        n = n // 3
        # Проверяем, что в результате деления получили 1
        if n == 1:
            # Выводим утвердительное сообщение
            print('n - is the power of the number 3!')
            # Выходим из цикла
            break
    else:
        # В противном случае выводим сообщение-опровержение
        print('n - is not the power of the number 3!')
        # Выходим из цикла
        break

# Задание 5.7 (Дописать программу, которая проверяет гипотезу Сиракуз.)
# Гипотеза Сиракуз заключается в том, что любое натуральное число n можно свести к 1, если повторять над ним следующие действия:
# если число чётное, разделить его нацело пополам, т. е. n = n // 2;
# если нечётное — умножить на 3, прибавить 1 и результат нацело разделить на 2, т. е. n = (n * 3 + 1) // 2.

# n = 19
## Syracuse hypothesis holds for number 19

n = 25921
## Syracuse hypothesis holds for number 25921

origin = n
# Создаём бесконечный цикл
while True:
    # Проверяем число на четность
    if n % 2 == 0: # Четное
        n = n // n
    else: # Нечетное
        n = (n * 3 + 1) // 2
    # Проверяем, что результат равен 1
    if n == 1:
        # Если условие выполняется, выводим утвердительное сообщение.
        print(f'Syracuse hypothesis holds for number {origin}')
        break

# -- CONTINUE -- (оператор перехода на новую итерацию цикла)
# Интерпретатор дойдя до оператора continue не прерывает цикл, как в случае с break, а переходит на новый итерационный цикл
# (пропускает весь код который стоит после continue)

# Например:
print("-------")
# Задание 1 (В честь Нового года магазин хочет отправить подарочные сертификаты всем, у кого активен статус программы скидок.)
# Необходимо написать программу, которая выводит идентификаторы клиентов, которым полагается подарочный сертификат
client_status = {
    103303: 'yes',
    103044: 'no',
    100423: 'yes',
    103032: 'no',
    103902: 'no'
}
# Создаём цикл по ключам словаря client_status
for user_id in client_status:
    # Далее перебираем ключи
        if client_status[user_id] == 'no':
            continue # Продолжаем итерацию далее
        else:
            print(f"Send present to user: {user_id}") # Дарим подарок

print("-------")
# Задание 5.10 (посчитать сколько в словаре элементов являются числами)
# mixture_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
## count_numbers = 4

mixture_dict = {'key1': 24, 'key2': '1.4', 'key3': 14, 'key4': 16.24, 'key6': 124.2414, 'key7': 12.2}
## count_numbers = 5
count_numbers = 0
for key in mixture_dict:

    if (type(mixture_dict[key]) != int and type(mixture_dict[key]) != float):
        continue
    else:
        count_numbers += 1
print(count_numbers)

print("-------")
# Помимо ключевых слов break и continue, существует ключевое слово pass. Заглушка pass означает «ничего не делать».
# Обычно мы используем её, потому что Python не позволяет создавать класс, функцию, цикл или оператор if без кода внутри.
# В приведённом ниже примере «вылетит» ошибка, если внутри i > 3 не будет кода, поэтому мы используем pass:
# Задан список
lst = [1,2,3,4,5]
# Создаём цикл по элементам списка
for i in lst:
    if i > 3:
        # Если i больше 3, ничего не делаем
        pass
    else:
        # В противном случае выводим элемент
        print(i)
print()

print("-------")
# Задача 1 (Подсчитать количество вхождений каждого символа в заданном тексте. В результате работы программы должен быть
# сформирован словарь, ключи которого — символы текста, а значения — количество вхождений символа в тексте.)
text = """
The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had 
not a moment to think about stopping herself before she found herself falling down a very deep well.Either the well was 
very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what 
was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see 
anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; 
here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it 
was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear 
of killing somebody, so managed to put it into one of the cupboards as she fell past it. `Well!' thought Alice to herself, 
`after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, 
I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
"""
# Для начала удаляем все пробелы, приводим текст к нижнему регистру и убираем символы переноса строки
text = text.replace(' ', '')
text = text.replace('\n', '')
text = text.lower()
print(text)

# Создаем пустой словарь для заполнения его значениями
count_dict = {}
# Для заполнения словаря используем следующий синтаксис
# Например
# count_dict['a'] = 1 # {'a': 1}
# Если мы встретем при переборе в тексте символ а, то посчитаем его вхождение таким образом:
# count_dict['a'] = count_dict['a'] + 1
# или сократив запись count_dict['a'] += 1

# Далее организовываем цикл
for symbol in text:
    if symbol not in count_dict:
        count_dict[symbol] = 1
    else:
        count_dict[symbol] += 1

# Можно дополнительно отсортировать словарь, для удобства
sorted_dict = dict(sorted(count_dict.items()))
print(sorted_dict)

print("-------")
# Задание 5.11 (похожее задание на вхождение, но на этот раз только символов пунктуации)
# text = """
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I am sure.
# So if she sells sea shells on the sea shore,
# I am sure that the shells are sea shore shells.
# """
## count_punctuation = {',': 1, '.': 2, '?': 0, '!': 0, ';': 1, '—': 0}

text = """
Иной раз казалось ему, что он уже с месяц лежит; в другой раз — что всё тот же день идет. Но об том — об том он совершенно забыл; зато ежеминутно помнил, что об чем-то забыл, чего нельзя забывать, — терзался, мучился, припоминая, стонал, впадал в бешенство или в ужасный, невыносимый страх.
Тогда он порывался с места, хотел бежать, но всегда кто-нибудь его останавливал силой, и он опять впадал в бессилие и беспамятство. Наконец он совсем пришел в себя!
"""
## count_punctuation = {',': 12, '.': 3, '?': 0, '!': 1, ';': 2, '—': 3}
text = text.lower()
text = text.replace(' ', '')
text = text.replace('\n', '')

count_punctuation = {',': 0, '.': 0, '?': 0, '!': 0, ';': 0, '—': 0}
for symbol in text:
    if symbol in count_punctuation.keys():
        if symbol in count_punctuation:
            count_punctuation[symbol] += 1
print(count_punctuation)

print("-------")
# Задача 2 (Подсчитать количество вхождений каждого слова в заданном тексте.
# В результате работы программы должен быть сформирован словарь, ключи которого — слова текста, а значения — количество
# вхождений слов в тексте.)
text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
text = text.lower()
text = text.replace('\n', '')

punctuation = {',', '.', '?', '!', ';', '—'}
for symbol in punctuation: text.replace(symbol, '')

text = list(text.split(' '))
words_count = {}
for word in text:
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word] += 1

print(words_count)

print("-------")
# Задача 5.12 (аналогичное задание выше)
sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm.'
## word_dict = {'a': 3, 'robot': 1, 'may': 1, 'not': 1, 'injure': 1, 'human': 2, 'being': 2, 'or': 1, 'through': 1, 'inaction': 1, 'allow': 1, 'to': 2, 'come': 1, 'harm': 1}

# sentence = "СчастьЕ нЕ в тоМ, чтобы делать всегда, что хочешь, а в Том, чтОБЫ всегдА хотеть того, ЧТО дЕлаешь."
## word_dict = {'счастье': 1, 'не': 1, 'в': 2, 'том': 2, 'чтобы': 2, 'делать': 1, 'всегда': 2, 'что': 2, 'хочешь': 1, 'а': 1, 'хотеть': 1, 'того': 1, 'делаешь': 1}

sentence = sentence.lower()
sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')
sentence = sentence.split(' ')
word_dict = {}
for word in sentence:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print(word_dict)

print("-------")
# Задача 5.13
# Версия 1 (долгая и не совсем правильная)
str_list = ["text", "morning", "notepad", "television", "ornament"]
symbol_to_check = 't'
## word_dict = {'text': 2, 'morning': 0, 'notepad': 1, 'television': 1, 'ornament': 1}

# str_list = ["text", "morning", "notepad", "television", "ornament"]
# symbol_to_check = 'n'
## word_dict = {'text': 0, 'morning': 2, 'notepad': 1, 'television': 1, 'ornament': 2}

word_dict = {}
for word in str_list:
    if word not in word_dict:
        word_dict[word] = 0
        elem_list = list(word)
        for symbol in elem_list:
            if symbol == symbol_to_check:
                word_dict[word] += 1
        elem_list = []
print(word_dict)

print("-------")
# Версия 2 (короткая и более оптимизированная)
for word in str_list:
    if word not in word_dict:
        word_dict[word] = 0
        word_dict[word] = word.count(symbol_to_check)
print(word_dict)

print("-------")
print("---Практика---")
# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']

# Выводим первые 100 слов из книги
# print(data[:100])
# Уникальные слова
word_set = set(data)
# Удаляем пометку новой главы
word_set.discard('[new chapter]')
# Выводим результаты
print(f'Общее количество слов: {len(data)}')
print(f'Общее количество уникальных слов: {len(word_set)}')

# Давайте напишем программу, которая посчитает частоту каждого слова. Для этого создадим словарь, ключами которого будут
# являться слова, а значения - количество вхождений этого слова в текст произведения. Заодно подсчитаем количество глав
# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
        # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
print(f'Количество глав: {count_chapter}')

# Создаем цикл по ключам и их порядковым номерам полученного словаря
for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    print(key, word_counts[key])

# Разделим все слова на главы. Для этого создадим список, в котором будем хранить списки - слова из определенной главы.
# Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []
# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)
# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
print(f'Вложенный список содержит {len(chapter_data)} внутренних списка')
# Выведем первые 100 слов 0-ой главы
print(chapter_data[0][:100])
print("-" * 30)
print(chapter_data[5][100]) # полная

# Подсчитаем, сколько раз каждое слово встречается в каждой из глав
# Инициализируем список, в котором будем хранить словари
chapter_words_count = []
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)

# Выводим результат
# print(chapter_words_count) # Огромный список, поэтому закомментировал
# Например
print(chapter_words_count[15]['князю']) # 2

# Делаем вывод результата:
# Создаем цикл по ключам словаря - спискам слов и их порядковым номерам
for chapter_number, chapter_dict in enumerate(chapter_words_count):
    if chapter_number == 10:
        break
    # Выводим номер главы
    print('-' * 40)
    print('Chapter: {}'.format(chapter_number))
    print('-' * 40)
    # Создаем цикл по ключам - словам и их порядковым номерам
    for i, word in enumerate(chapter_dict):
        # Выводим первые 10 слов из главы
        if i == 10:
            break
        print(word, chapter_dict[word])

# Задание 1
print('Задание 1')
print('-' * 100)
# Частота употребления отдельного слова в документе (term frequency)

# --------------------Входные параметры--------------------
target_word = 'гостья' # Слово для поиска
target_chapter = 15 # Номер главы для поиска
# --------------------Входные параметры--------------------

# RESULT---------------------------------------------------
term_frequency = 0 # Частота употребления слова
# RESULT---------------------------------------------------

# Количество вхождений искомого слова в главе
word_count = chapter_words_count[target_chapter].get(target_word)
# Проверка есть ли данное слово в главе
if word_count != None:
    # общее количество всех слов в главе (этот вариант предпочтительнее), суммирует частоту вхождения всех слов в главе
    # chapter_count = sum(chapter_words_count[target_chapter].values())
    chapter_count = len(chapter_data[target_chapter])
    # еще один вариант подсчета количества слов (не нравится)
    # for num in chapter_words_count[target_chapter].values():
    #     chapter_count += num
    # делим кол-во вхождений слова в главе на кол-во глав
    term_frequency = word_count / chapter_count
    # Получаем результат
    print(f"Частота употребления слова '{target_word}' в главе [{target_chapter}] составляет: {round(term_frequency, 6)}")
else:
    print(f"Искомого слова '{target_word}' в главе [{target_chapter}] нет")

print('Дополнительно')
print('-' * 40)

# RESULT---------------------------------------------------
all_words_tf = []
# RESULT---------------------------------------------------

temp = {}
# Дополнительно (рассчет частоты употребления для всех слов)
# Перебираем главы
for chapter_num, chapter_dict in enumerate(chapter_words_count):
    # Определяем количество слов в текущей главе
    chapter_count = len(chapter_data[chapter_num])
    # Перебираем слова в текущей главе
    for current_chapter, current_word in enumerate(chapter_dict):
        word_count = chapter_words_count[chapter_num].get(current_word)
        if word_count != None:
            # Записываем в словарь
            temp[current_word] = word_count / chapter_count
    all_words_tf.append(temp)
    temp = {}

print(round(all_words_tf[15]['гостья'], 6))

# Задание 2
print('Задание 2')
print('-' * 100)
# Доля документов, в которых встречается искомое слово (document frequency)

# --------------------Входные параметры--------------------
target_word = 'гостья' # Слово для поиска
number_of_chapters = count_chapter
chapters_word_count = 0
# --------------------Входные параметры--------------------

# RESULT---------------------------------------------------
document_frequency = 0
# RESULT---------------------------------------------------

# Рассчитываем число глав содержащих слово
for chapter_number, chapter_dict in enumerate(chapter_data):
    if target_word in chapter_dict:
        chapters_word_count += 1

document_frequency = chapters_word_count / number_of_chapters
print(f"Доля документов для слова ['{target_word}'] составляет {round(document_frequency, 6)}")

print('Дополнительно')
print('-' * 40)

# --------------------Входные параметры--------------------
chapters_word_count = 0
document_frequency = 0
number_of_chapters = count_chapter
# --------------------Входные параметры--------------------

# RESULT---------------------------------------------------
all_words_df = {}
# RESULT---------------------------------------------------

# Дополнительно (рассчет для всех уникальных слов)
for i, current_word in enumerate(word_set):

    for chapter_number, chapter_dict in enumerate(chapter_words_count):
        if current_word in chapter_dict:
            chapters_word_count += 1
    # Записываем в словарь
    all_words_df[current_word] = chapters_word_count / number_of_chapters
    chapters_word_count = 0
print(round(all_words_df['гостья'], 6))

# Задание 3
print('Задание 3')
print('-' * 100)
# Задача (отсеивание не важных слов от анализа) хорошо решается с помощью tf-idf — статистической метрики для оценки
# важности слова в тексте. Другими словами, tf-idf — это «контрастность» слова в документе (насколько оно выделяется среди других слов).
from math import log
# --------------------Входные параметры--------------------
target_word = 'анна'
target_chapter = 4

term_frequency = all_words_tf[target_chapter][target_word]
document_frequency = all_words_df[target_word]
inverse_document_frequency = 1 / document_frequency
# --------------------Входные параметры--------------------

# RESULT---------------------------------------------------
tf_idf = 0
# RESULT---------------------------------------------------

tf_idf = term_frequency * log(inverse_document_frequency)
print(f"Tf_idf для слова ['{target_word}'] в главе [{target_chapter}] составляет {round(tf_idf, 6)}")

print('Дополнительно')
print('-' * 40)

# RESULT---------------------------------------------------
all_words_tf_idf = []
# RESULT---------------------------------------------------

temp = {}
# Дополнительно (рассчет tf_idf для всех слов в каждой главе)
for chapter_number, chapter_dict in enumerate(chapter_words_count):
    for current_word in chapter_dict:
        term_frequency = all_words_tf[chapter_number][current_word]
        document_frequency = all_words_df[current_word]
        inverse_document_frequency = 1 / document_frequency
        temp[current_word] = term_frequency * log(inverse_document_frequency)
    all_words_tf_idf.append(temp)
    temp = {}
print(round(all_words_tf_idf[4]['анна'], 6))

# Задание 4
print('Задание 4')
print('-' * 100)
# Теперь, когда есть возможность вычислять tf-idf для каждого слова в главе, мы можем найти те слова, которые являются
# самыми «контрастными» для данной главы, то есть они могут являться в своём роде заголовком для главы.
# Задача вывести три слова, имеющие самое высокое значение tf-idf в заданной главе

# --------------------Входные параметры--------------------
target_chapter = 3
# --------------------Входные параметры--------------------

# RESULT---------------------------------------------------
# tf_idf_for_chapter = {}
# RESULT---------------------------------------------------
# Получаем нужный словарь с характеристиками
target_dict = all_words_tf_idf[target_chapter]
# Сортировка в порядке убывания с помощью метода sort()
sorted_target_dict_items = sorted(target_dict, key=target_dict.get, reverse=True)

for ite, current_word in enumerate(sorted_target_dict_items):
    if ite == 3:
        break
    print(f"{current_word} - {target_dict.get(current_word)}")
    # tf_idf_for_chapter[current_word] = target_dict.get(current_word)