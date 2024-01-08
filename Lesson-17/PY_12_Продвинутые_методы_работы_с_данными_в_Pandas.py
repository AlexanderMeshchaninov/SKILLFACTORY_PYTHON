import pandas as pd
melb_df = pd.read_csv('data/melb_data_fe.csv', sep=',')
print(melb_df.info())

# В прошлый раз было множество преобразований данной таблицы и если обратить внимание, то наше преобразование 
# столбцов к типам datetime и category «слетело».
# Почему это произошло?
# Ответ на самом деле очень прост: csv-файл не хранит в себе информацию о типах данных столбцов, 
# поэтому при чтении Pandas автоматически определяет тип данных столбца. Не забывайте об этом, 
# обмениваясь преобразованными данными с вашими коллегами

print('_' * 40)
# Задание 1.1
# Преобразуйте столбец Date в формат datetime и выделите квартал (quarter) продажи объектов недвижимости. 
# Найдите второй по популярности квартал продажи. В качестве ответа запишите число объектов, проданных в этом квартале.
melb_df['Date'] = pd.to_datetime(melb_df['Date'])
quarter = melb_df['Date'].dt.quarter
print(quarter.value_counts())

print('_' * 40)
# Задание 1.2
# Преобразуйте все столбцы, в которых меньше 150 уникальных значений, в тип данных category, 
# исключив из преобразования столбцы Date, Rooms, Bedroom, Bathroom, Car.
# В качестве ответа запишите результирующее количество столбцов, которые имеют тип данных category.

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
unique_count = 150
for col in melb_df.columns:
    if melb_df[col].nunique() < unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')
        
print(melb_df.info())

print('_' * 40)
# СОРТИРОВКА ПО ЗНАЧЕНИЯМ ОДНОГО СТОЛБЦА
# Приведём несколько примеров сортировки нашей таблицы с недвижимостью.
# Отсортируем таблицу по возрастанию цены объектов недвижимости (Price):
print(melb_df.sort_values(by='Price').head(10))

# Мы вывели десять строк таблицы, чтобы убедиться в верном порядке сортировки. 
# Также обратите внимание на индексы таблицы — их значения сохранились из исходной таблицы.

print('_' * 40)
# А теперь отсортируем таблицу по убыванию (от самой последней до самой первой) даты продажи 
# объекта (Date). Для этого выставим параметр ascending на False:
print(melb_df.sort_values(by='Date', ascending=False))

print('_' * 40)
# СОРТИРОВКА ПО ЗНАЧЕНИЯМ НЕСКОЛЬКИХ СТОЛБЦОВ
# Для сортировки по значениям нескольких столбцов необходимо передать названия этих столбцов в 
# параметр by в виде списка. При этом важно обращать внимание на порядок следования столбцов.

# Так, например, отсортируем таблицу сначала по возрастанию расстояния от центра города (Distance), 
# а затем — по возрастанию цены объекта (Price). Для того чтобы вывод был более наглядным, выделим 
# каждую десятую строку из столбцов Distance и Price результирующей таблицы:
print(melb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])

# Мы получили таблицу, отсортированную по возрастанию расстояния до центра города. Если встречаются объекты 
# недвижимости, у которых расстояние оказывается одинаковым, то внутри такой группы производится сортировка по цене объекта.

print(melb_df.sort_values(by=['Price', 'Distance']).loc[::10, ['Price', 'Distance']])

print('_' * 40)
# КОМБИНИРОВАНИЕ СОРТИРОВКИ С ФИЛЬТРАЦИЕЙ
# Найдём информацию о таунхаусах (Type), проданных компанией (SellerG) McGrath, у которых коэффициент соотношения 
# площадей здания и участка (AreaRatio) меньше -0.8. Результат отсортируем по дате продажи (Date) в порядке возрастания, 
# а после проведём сортировку по убыванию коэффициента соотношения площадей. Также обновим старые индексы на новые, установив 
# параметр ignore_index на True. Для наглядности результата выберем из таблицы только столбцы Data и AreaRatio
mask1 = melb_df['AreaRatio'] < -0.8 # коэффициент соотношения 
mask2 = melb_df['Type'] == 'townhouse' # ищем таунхаусы
mask3 = melb_df['SellerG'] == 'McGrath' # компания

result = melb_df[mask1 & mask2 & mask3].sort_values(
    by=['Date', 'AreaRatio'], 
    ascending=[True, False], 
    ignore_index=True).loc[:, ['Date', 'AreaRatio']]
print(result)

print('_' * 40)
# Задание 2.2
# Произведите сортировку столбца AreaRatio по убыванию. При этом индексы полученной 
# таблицы замените на новые. Какое значение площади здания находится в строке 1558? Ответ округлите до целого числа.
result = melb_df.sort_values(by=['AreaRatio'], ascending=False, ignore_index=True).loc[1558:, ['BuildingArea']]
print(result)

print('_' * 40)
# Задание 2.3
# Найдите таунхаусы (Type) с количеством жилых комнат (Rooms) больше 2. Отсортируйте полученную таблицу сначала по 
# возрастанию числа комнат, а затем по убыванию средней площади комнат (MeanRoomsSquare). Индексы таблицы замените 
# на новые. Какая цена будет у объекта в строке 18? Ответ запишите в виде целого числа.
mask1 = melb_df['Type'] == 'townhouse'
mask2 = melb_df['Rooms'] > 2
result = melb_df[mask1 & mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True).loc[18:18, ['Price']]
print(round(result))

print('_' * 40)
# ГРУППИРОВКА ДАННЫХ ПО ОДНОМУ КРИТЕРИЮ С ОДНОЙ АГРЕГАЦИЕЙ
# В качестве столбца для группировки возьмём столбец типа объекта недвижимости (Type):
print(melb_df.groupby(by=['Type']).mean(numeric_only=True))

print('_' * 40)
# Если необходимо видеть тип объекта в качестве отдельного столбца таблицы, мы можем выставить параметр as_index на False:
print(melb_df.groupby(by=['Type'], as_index=False).mean(numeric_only=True))

print('_' * 40)
# Как правило, нам не нужна информация обо всех столбцах, поэтому агрегирующие методы можно применять только 
# к интересующему нас столбцу. Например, давайте сравним средние цены на объекты в зависимости от их типа:
print(melb_df.groupby(by=['Type'])['Price'].mean())

print('_' * 40)
# Теперь давайте выясним, какие регионы (Regionname) наиболее удалены от центра Мельбурна.
# Для этого найдём минимальное значение расстояния от центра города до объекта в зависимости от его региона. 
# Результат отсортируем по убыванию расстояния:
print(melb_df.groupby(by=['Regionname'])['Distance'].min().sort_values(ascending=False))

print('_' * 40)
# Давайте построим таблицу для анализа продаж по месяцам. Для этого найдём количество продаж, а также среднее и 
# максимальное значения цен объектов недвижимости (Price), сгруппированных по номеру месяца продажи (MonthSale). 
# Результат отсортируем по количеству продаж в порядке убывания:
print(melb_df.groupby(by=['MonthSale'])['Price'].agg(['count', 'mean', 'max']).sort_values(by='count', ascending=False))

# В результате применения метода agg(), в который мы передали список с названиями интересующих нас агрегирующих функций, 
# мы получаем DataFrame со столбцами count, mean и max, где для каждого месяца рассчитаны соответствующие параметры. 
# Результат сортируем по столбцу count.

print('_' * 40)
# Если вам нужна полная информация обо всех основных статистических характеристиках внутри каждой группы, 
# вы можете воспользоваться методом agg(), передав в качестве его параметра строку 'describe':
print(melb_df.groupby('MonthSale')['Price'].agg('describe'))

print('_' * 40)
# После базовых математических функций наиболее частым агрегированием является подсчёт числа уникальных значений. 
# Так, например, мы можем вычислить число уникальных риелторских компаний в зависимости от региона, чтобы понять, 
# в каких регионах конкуренция на рынке недвижимости меньше. Это можно сделать, передав в параметр метода agg() строку 'nunique'.
# Более того, метод agg() поддерживает использование и других функций. Передадим дополнительно встроенную функцию set, 
# чтобы получить множество из агентств недвижимости, которые работают в каждом из регионов:
print(melb_df.groupby(by=['Regionname'])['SellerG'].agg(['nunique', set]))

print('_' * 40)
# Задание 3.1
# Сгруппируйте данные по признаку количества комнат и найдите среднюю цену объектов недвижимости в каждой группе. 
# В качестве ответа запишите количество комнат, для которых средняя цена наибольшая.
print(melb_df.groupby(['Rooms'])['Price'].agg(['mean']).sort_values(by='mean')) # 7 в конце

print('_' * 40)
# Задание 3.2
# Какой регион имеет наименьшее стандартное отклонение по географической широте (Lattitude)?
# В качестве ответа запишите название этого региона.
print(melb_df.groupby('Regionname')['Lattitude'].std())

print('_' * 40)
# Задание 3.3
# Какая риелторская компания (SellerG) имеет наименьшую общую выручку за период с 1 мая по 1 сентября (включительно) 2017 года?
# Для ответа на этот вопрос рассчитайте сумму продаж (Price) каждой компании в заданный период.
# Не забудьте перевести даты в формат datetime.
import datetime as dt
# Создадим диапазон дат
start_date = pd.to_datetime('2017-05-01')
end_date = pd.to_datetime('2017-09-01')
melb_filtered = melb_df[(melb_df['Date'] > start_date) & (melb_df['Date'] <= end_date)]
print(melb_filtered.groupby('SellerG')['Price'].agg(['sum', 'min']).sort_values(by='sum')) # LITTLE

print('_' * 40)
# --- Свобдные таблицы ---
# Например, мы уже умеем строить таблицу, которая показывает зависимость медианной цены и площади здания от числа комнат:
print(melb_df.groupby('Rooms')[['Price', 'BuildingArea']].median())

print('_' * 40)
# Также можно построить таблицу, в которой мы будем учитывать не только число комнат, но и тип здания (Type). 
# Для этого в параметрах метода groupby() укажем список из нескольких интересующих нас столбцов
print(melb_df.groupby(['Rooms', 'Type'])[['Price']].mean())
# В результате выполнения такого кода мы получаем Series, которая обладает несколькими уровнями индексов: 
# первый уровень — число комнат, второй уровень — тип здания. Такая организация индексов называется иерархической. 
# Вычисление параметра (средней цены) происходит во всех возможных комбинациях признаков.

print('_' * 40)
# Для того, чтобы финальный результат был представлен в виде сводной таблицы (первый группировочный признак по строкам, 
# а второй — по столбцам), а не в виде Series с иерархическими индексами, к результату чаще всего применяют метод unstack(), 
# который позволяет переопределить вложенный индекс в виде столбцов таблицы:
print(melb_df.groupby(['Rooms', 'Type'])['Price'].mean().unstack())

print('_' * 40)
# Давайте построим ту же самую таблицу, но уже с использованием метода pivot_table. В качестве параметра values укажем 
# столбец Price, в качестве индексов сводной таблицы возьмём Rooms, а в качестве столбцов — Type. Агрегирующую функцию 
# оставим по умолчанию (среднее). Дополнительно заменим пропуски в таблице на значение 0. Финальный результат для наглядности 
# вывода округлим с помощью метода round() до целых.
print(melb_df.pivot_table(
    values='Price',
    index='Rooms',
    columns='Type',
    aggfunc='mean',
    fill_value=0
).round())

print('_' * 40)
# А теперь давайте проанализируем продажи в каждом из регионов в зависимости от того, будний был день или выходной. 
# Для этого построим сводную таблицу, в которой строками будут являться названия регионов (Regionname), а в столбцах 
# будет располагаться наш «признак-мигалка» выходного дня (Weekend), который равен 1, если день был выходным, и 0 — в противном случае. 
# В качестве значений сводной таблицы возьмём количество продаж.
print(melb_df.pivot_table(
    values='Price',
    index='Regionname',
    columns='Weekend',
    aggfunc='count'
))

print('_' * 40)
# Разберём ещё один пример: найдём, как зависит средняя и медианная площадь участка (Landsize) от типа объекта (Type) 
# и его региона (Regionname). Чтобы посмотреть несколько статистических параметров, нужно передать в аргумент aggfunc 
# список из агрегирующих функций. Построим такую сводную таблицу, где пропущенные значения заменим на 0:
print(melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['mean', 'median'],
    fill_value=0
))

print('_' * 40)
# Давайте построим таблицу, в которой по индексам будут располагаться признаки метода продажи (Method) и типа объекта (Type), 
# по столбцам — наименование региона (Regionname), а на пересечении строк и столбцов будет стоять медианная цена объекта (Price):
print(melb_df.pivot_table(
    values='Price',
    index=['Method', 'Type'],
    columns='Regionname',
    aggfunc='median',
    fill_value=0
))

# Первым индексом в таблице идёт метод продажи здания, далее для метода указывается тип недвижимости. 
# По столбцам расположены регионы. В ячейках таблицы указана медианная цена для каждой такой комбинации.
# Такие таблицы уже сложнее читать, однако с помощью них можно более глубоко исследовать закономерности. 
# Например, можно видеть, что вне зависимости от метода продажи и региона цена на объекты типа house практически 
# всегда выше, чем на объекты другого типа.

print('_' * 40)
# ДОСТУП К ДАННЫМ В СВОДНОЙ ТАБЛИЦЕ

# Как получить доступ к данным или произвести фильтрацию в сложной сводной таблице, где есть дополнительные индексы?
# Давайте рассмотрим, что собой представляют столбцы сложной сводной таблицы.
# Запишем сводную таблицу, которую мы создавали ранее в переменную pivot:
pivot = melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['median','mean'],
    fill_value=0
)
print(pivot.columns)

# В результате мы получаем объект MultiIndex. Этот объект хранит в себе шесть комбинаций пар столбцов 
# (два статистических параметра и три типа здания), то есть есть шесть возможных вариантов обращения к столбцам таблицы.
# Мультииндексы раскрываются подобно вложенным словарям — по очереди, как матрёшка. Чтобы получить 
# доступ к определённому столбцу, вы должны сначала обратиться к столбцу, который находится уровнем выше.

print('_' * 40)
# Так, из таблицы pivot мы можем получить средние значения площадей участков для типа здания unit, 
# просто последовательно обратившись по имени столбцов:
print(pivot['mean']['unit'])

print('_' * 40)
# Аналогично производится и фильтрация данных. Например, если нам нужны регионы, в которых средняя площадь 
# здания для домов типа house меньше их медианной площади, то мы можем найти их следующим образом:
mask = pivot['mean']['house'] < pivot['median']['house']
filtered_pivot = pivot[mask]
print(filtered_pivot)

print('_' * 40)
# Чтобы получить индексы отфильтрованной таблицы, можно воспользоваться атрибутом index и обернуть результат в список:
print(list(filtered_pivot.index))

print('_' * 40)
# Задание 4.2
# Составьте сводную таблицу, которая показывает зависимость медианной площади (BuildingArea) здания от 
# типа объекта недвижимости (Type) и количества жилых комнат в доме (Rooms). Для какой комбинации признаков 
# площадь здания наибольшая?
# В качестве ответа запишите эту комбинацию (тип здания, число комнат) через запятую, без пробелов.
print(melb_df.pivot_table(
    values='BuildingArea',
    index='Rooms',
    columns='Type',
    aggfunc='median',
    fill_value=0
))

print('_' * 40)
# Задание 4.3
# Составьте сводную таблицу, которая показывает зависимость медианной цены объекта недвижимости (Price) 
# от риелторского агентства (SellerG) и типа здания (Type).
# Во вновь созданной таблице найдите агентство, у которого медианная цена для зданий типа unit максимальна. 
# В качестве ответа запишите название этого агентства.
print(melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='median',
    fill_value=0
))

print('_' * 40)
# --- Data set MOVIELENS ---
import pandas as pd

# ratings1 и ratings2 — таблицы с данными о выставленных пользователями оценках фильмов. 
# Они имеют одинаковую структуру и типы данных — на самом деле это две части одной таблицы с оценками фильмов.

# userId — уникальный идентификатор пользователя, который выставил оценку;
# movieId — уникальный идентификатор фильма;
# rating — рейтинг фильма.

ratings1 = pd.read_csv('data/ratings1.csv', sep=',')
print(ratings1.head())

print('_' * 40)
ratings2 = pd.read_csv('data/ratings2.csv', sep=',')
print(ratings2.head())

print('_' * 40)
# dates — таблица с датами выставления всех оценок.

# date — дата и время выставления оценки фильму.
dates = pd.read_csv('data/dates.csv', sep=',')
print(dates.head())

print('_' * 40)
# movies — таблица с информацией о фильмах.

# movieId — уникальный идентификатор фильма;
# title — название фильма и год его выхода;
# genres — жанры фильма.
movies = pd.read_csv('data/movies.csv', sep=',')
print(movies.head())

# Итак, представим, что нам надо получить единую таблицу, в которой будут собраны рейтинги, даты выставления рейтингов, 
# а также информация о фильмах. Вот как мы будем действовать:

# 1. Склеим таблицы ratings1 и ratings2 в единую структуру.
# 2. К полученной таблице с рейтингами подсоединим столбец с датой проставления рейтинга, склеив столбцы таблиц между собой.
# 3. Присоединим к нашей таблице информацию о названиях и жанрах фильмов.

dates['date'] = pd.to_datetime(dates['date'])
print(dates['date'].dt.year.value_counts())

print('_' * 40)
# --- Объединение DataFrame (CONCAT) ---

# На первый взгляд может показаться, что всё прошло успешно, однако если мы посмотрим на индексы 
# последних строк таблицы, то увидим, что их нумерация не совпадает с количеством строк. 
# Это может привести к некорректному объединению таблиц по ключевым столбцам на следующем этапе решения нашей задачи.
# Это связано с тем, что по умолчанию concat сохраняет первоначальные индексы объединяемых таблиц, 
# а обе наши таблицы индексировались, начиная от 0. Чтобы создать новые индексы, нужно выставить параметр ignore_index на True:
ratings = pd.concat([ratings1, ratings2], ignore_index=True)
print(ratings)

print('_' * 40)
# Посмотрим количество строк в ratings и dates т.к. впоследствии придется склеивать их
print(f"Количество строк в ratings {ratings.shape[0]}")
print(f"Количество строк в dates {dates.shape[0]}")
print(dates.shape[0] == ratings.shape[0])

print('_' * 40)
# Размерность таблиц разная — как такое могло произойти?
# На самом деле очень просто: при выгрузке данных информация об оценках какого-то 
# пользователя попала в обе таблицы (ratings1 и ratings2). В результате конкатенации случилось 
# дублирование строк. В данном примере их легко найти — выведем последнюю строку таблицы ratings1 
# и первую строку таблицы ratings2:
print(ratings2.head(1))
print(ratings1.tail(1))

print('_' * 40)
# Чтобы очистить таблицу от дублей, мы можем воспользоваться методом DataFrame drop_duplicates(), 
# который удаляет повторяющиеся строки в таблице. Не забываем обновить индексы после удаления дублей, 
# выставив параметр ignore_index в методе drop_duplicates() на значение True:
ratings = ratings.drop_duplicates(ignore_index=True)
print(ratings)
print('Число строк в таблице ratings: ', ratings.shape[0])

print('_' * 40)
# Теперь, после всех манипуляций мы можем конкатенировать таблицы ratings и dates по столбцам (выставив axis=1)
ratings_dates = pd.concat([ratings, dates], axis=1)
print(ratings_dates.tail(7))

print('_' * 40)
# Задание 6.2
# Заданы две таблицы — df1 и df2. В первой содержатся имена и фамилии сотрудников, во второй — их должности.
df1 = pd.DataFrame({"Name": ["Pankaj", "Lisa"], "Surname": ["Sobolev", "Krasnova"]})
df2 = pd.DataFrame({"Role": ["Admin", "Editor"]})
unite_table = pd.concat([df1, df2], ignore_index=True, axis=1)
print(unite_table)

# Задание 6.3
# В ваше распоряжение предоставлена директория users. В данной директории содержатся csv-файлы, 
# в каждом из которых хранится информация об идентификаторах пользователей (user_id) и ссылки на их 
# фотографии (image_url). Файлов в директории может быть сколько угодно.
# Вам необходимо написать функцию concat_user_files(path), параметром которой является path — путь до директории. 
# Функция должна объединить информацию из предоставленных вам файлов в один DataFrame и вернуть его.
# Список названий всех файлов, находящихся в директории, вы можете получить с помощью функции os.listdir(path) 
# из модуля os. Отсортируйте полученный список, прежде чем производить объединение файлов.
# Обратите внимание, что метод os.listdir() возвращает только названия файлов в указанной директории, 
# а при чтении файла необходимо указывать полный путь до него.
# Не забудьте обновить индексы результирующей таблицы после объединения.
# Примечание. Учтите, что на тестовом наборе файлов в результате объединения могут возникнуть дубликаты, 
# от которых необходимо будет избавиться.
# Например, для директории users/ результирующая таблица должна иметь следующий вид:

# import pandas as pd
# import os as os

# def concat_user_files(path):
#     lst_dir = os.listdir(path)
#     lst_dir.sort()
#     table_list = []
#     for index, elem in enumerate(lst_dir):
#         current_table = pd.read_csv(f'./Root/users/{elem}', sep=',')
#         table_list.append(current_table)
    
#     united_table = pd.concat(table_list, ignore_index=True)
#     united_table = united_table.drop_duplicates(ignore_index=True)
#     return united_table

# table = concat_user_files('./Root/users')
# print(table)

print('_' * 40)
# --- Типы объединения JOIN, MERGE ---

print('_' * 40)
# Left (ratings_dates + movies)
joined_left = ratings_dates.join(
    movies,
    rsuffix='_right',
    how='left'
)
print(joined_left)

print('_' * 40)
# Right (movies + ratings_dates)
joined_right = ratings_dates.join(
    movies,
    rsuffix='_left',
    how='right'
)
print(joined_right)

print('_' * 40)
# Однако это не тот результат, который мы хотели, ведь мы не получили соответствия фильмов и их рейтингов. 
# Чтобы совместить таблицы по ключевому столбцу с помощью метода join(), необходимо использовать ключевой 
# столбец в «правой» таблице в качестве индекса. Это можно сделать с помощью метода set_index(). 
# Также необходимо указать название ключа в параметре on.

joined = ratings_dates.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)
print(joined)

# В результате такого объединения для каждого идентификатора фильма movieId в таблице ratings_dates найден 
# совпадающий с ним идентификатор movieId в таблице movies и присоединена информация о самом фильме (title и genres). 
# Это как раз то, что нам нужно.

print('_' * 40)
# Merge
merged = ratings_dates.merge(
    movies,
    on='movieId',
    how='left'
)
print(merged.head())
print(f'Число строк в ratings_dates: {ratings_dates.shape[0]}')
print(f'Число строк в merged: {merged.shape[0]}')
print(ratings_dates.shape[0] == merged.shape[0])

print('_' * 40)
# ОСОБЕННОСТИ ИСПОЛЬЗОВАНИЯ MERGE()
# Возникает вопрос: почему мы выбрали тип объединения left, а не full, например?
# Найти ответ нам поможет пример. Объединим ratings_dates с movies по ключевому 
# столбцу movieId, но с параметром how='outer' (full outer) и выведем размер таблицы, 
# а также её «хвост».
merged_2 = ratings_dates.merge(
    movies,
    on='movieId',
    how='outer'
)
print(merged_2)

print('_' * 40)
# В качестве примера объединим ratings1 и ratings2 с помощью merge
ratings_merged = ratings1.merge(
    ratings2,
    how='outer'
)
print(ratings_merged)

# Стоит отметить, что метод merge автоматически удаляет дубликаты

print('_' * 40)
# Задание 7.3
# Даны две исходных таблицы:
data_1 = pd.DataFrame({'Value': [100, 45, 80],
                       'Group': [1, 4, 5]},
                      index = ['I0', 'I1', 'I2']
                     )
data_2 = pd.DataFrame({'Company': ['Google', 'Amazon', 'Facebook'],
                       'Add': ['S0', 'S1', 'S7']},
                      index = ['I0', 'I1', 'I3']
                     )
data_merged = data_1.join(
    data_2,
    how='inner'
    )
print(data_merged)

print('_' * 40)
# Задание 7.4
# Даны две исходные таблицы:
a = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [103, 214, 124], 'C': [1, 4, 2]})
b = pd.DataFrame({'V': ['d', 'b', 'c'], 'U': [1393.7, 9382.2, 1904.5], 'C': [1, 3, 2]})
a_b_merged = a.merge(
    b,
    how='right',
    on='C'
)
print(a_b_merged)

print('_' * 40)
# Задание 7.5
# Даны две таблицы: items_df, в которой содержится информация о наличии товаров на складе, и purchase_df с данными о покупках товаров.
# Информация в таблицах представлена в виде следующих столбцов:
# item_id — идентификатор модели;
# vendor — производитель модели;
# stock_count — имеющееся на складе количество данных моделей (в штуках);
# purchase_id — идентификатор покупки;
# price — стоимость модели в покупке.

items_df = pd.DataFrame({
            'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
            'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
            'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
        })

purchase_df = pd.DataFrame({
            'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
            'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
            'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
        })
merged = items_df.merge(
    purchase_df.set_index('item_id'),
    on='item_id',
    how='inner',
)

income = (merged['price'] * merged['stock_count']).sum() # 19729490
print(income)

print('_' * 40)
# --- Продвинутые методы работы с Pandas (!повторение!) ---

import pandas as pd

melb_df = pd.read_csv('data/melb_data_fe.csv', sep=',')
print(melb_df.head())

print('_' * 40)
# Сортировка данных по определенному столбцу
print(melb_df.sort_values(by='Price').head(10))

print('_' * 40)
# Или другой вариант - сортировка по нескольким столбцам
print(melb_df.sort_values(
    by=['Date', 'Regionname', 'Rooms'],
    ascending=[True, True, False], # [Возрастание, Возрастание, Убывание]
    ignore_index=True
    ).loc[::10, ['Date', 'Regionname', 'Rooms']].head(10))

print('_' * 40)
# Группировка данных (по типу здания выводя среднюю цену)
print(melb_df.groupby(by='Type')['Price'].mean())

print('_' * 40)
# Или другой вариант - выборка по регионам, считаем минимальное расстояние регионов от центра
print(melb_df.groupby(by='Regionname', as_index=False)['Distance'].min().sort_values(by=['Distance'], ascending=False))

print('_' * 40)
# Использование выборки и нескольких агреггирующих функций agg
print(melb_df.groupby(by='MonthSale')['Price'].agg(['count', 'mean', 'max']).sort_values(by='count', ascending=False))

print('_' * 40)
# Более того, метод agg поддерживает использование других функций (количество уникальных категорий, сами компании)
print(melb_df.groupby('Regionname')['SellerG'].agg(['nunique', set]))

print('_' * 40)
# Сводные таблицы pivot_table
print(melb_df.pivot_table(
    values='Price',
    index='Rooms',
    columns='Type',
    fill_value=0
).round(2))

print('_' * 40)
# Для того, чтобы посмотреть несколько статистических параметров 
# (медианное и среднее значение для площади прилегающей территории в зависимости от региона и типа здания)
print(melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    fill_value=0,
    aggfunc=['median', 'mean']
))

print('_' * 40)
# Сводные таблицы позволяют рассматривать данные по нескольким признакам (методу и типу)
print(melb_df.pivot_table(
    values='Price',
    index=['Method', 'Type'],
    columns='Regionname',
    fill_value=0,
    aggfunc='median'
))

print('_' * 40)
# Объединение таблиц с помощью concat (поумолчанию объединение происходит по строкам)
ratings1 = pd.read_csv('data/ratings1.csv', sep=',')
ratings2 = pd.read_csv('data/ratings2.csv', sep=',')
ratings = pd.concat([ratings1, ratings2], 
                    ignore_index=True)

print(ratings)

print('_' * 40)
# Объединение по столбцам axis=1
ratings = pd.concat([ratings1, ratings2], 
                    ignore_index=True,
                    axis=1)

print(ratings)

print('_' * 40)
print('_' * 40)
# Для решения задач нам понадобится выделить из признака title год выпуска фильма. Для этого напишем функцию get_year_release(arg).
import re # библиотека для регулярных выражений
import pandas as pd
import numpy as np
ratings_movies = pd.read_csv('data/ratings_movies.csv', sep=',')

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем 0
        return 0
    
ratings_movies['year_release'] = ratings_movies['title'].apply(get_year_release)
print(ratings_movies)

print('_' * 40)
# Задание 8.1
# Создайте в таблице новый признак year_release, который соответствует году выпуска фильма.
# У скольких фильмов не указан год их выпуска?
mask1 = ratings_movies['year_release'] == 0
print(ratings_movies[mask1].shape[0])

print('_' * 40)
# Задание 8.2
# Какой фильм, выпущенный в 1999 году, получил наименьшую среднюю оценку зрителей?
# В качестве ответа запишите название этого фильма без указания года его выпуска.
mask1 = ratings_movies['year_release'] == 1999
print(ratings_movies[mask1].groupby(by='title')['rating'].mean().sort_values())

print('_' * 40)
# Задание 8.3
# Какое сочетание жанров фильмов (genres), выпущенных в 2010 году, получило наименьшую среднюю оценку (rating)?
# Запишите сочетание так же, как оно указано в таблице (через разделитель |, без пробелов).
mask1 = ratings_movies['year_release'] == 2010
print(ratings_movies[mask1].groupby('genres')['rating'].mean().sort_values())

print('_' * 40)
# Задание 8.4
# Какой пользователь (userId) посмотрел наибольшее количество различных (уникальных) комбинаций жанров (genres) фильмов? 
# В качестве ответа запишите идентификатор этого пользователя.
print(ratings_movies.groupby('userId')['genres'].nunique().sort_values(ascending=False))

print('_' * 40)
# Задание 8.5
# Найдите пользователя, который выставил наименьшее количество оценок, но его средняя оценка фильмам наибольшая.
# В качестве ответа укажите идентификатор этого пользователя.
# Чтобы рассчитать несколько параметров для каждого пользователя (количество оценок и среднюю оценку), можно воспользоваться методом agg() 
# на сгруппированных данных.
print(ratings_movies.groupby(by='userId')['rating'].agg(
    ['count', 'mean'])
      .sort_values(by=['count', 'mean'], 
                   ascending=[True, False]))

print('_' * 40)
# Задание 8.6
# Найдите сочетание жанров (genres) за 2018 год, которое имеет наибольший средний рейтинг (среднее по столбцу rating), 
# и при этом число выставленных ему оценок (количество значений в столбце rating) больше 10.
# Запишите сочетание так же, как оно указано в таблице (через разделитель |, без пробелов).
mask1 = ratings_movies['year_release'] == 2018
count_table = ratings_movies[mask1].groupby('genres')['rating'].agg(
    ['mean', 'count'])
mask2 = count_table['count'] > 10
print(count_table[mask2].sort_values(by='mean', ascending=False))

print('_' * 40)
# Задание 8.7
# Добавьте в таблицу новый признак year_rating — год выставления оценки. Создайте сводную таблицу, которая иллюстрирует 
# зависимость среднего рейтинга фильма от года выставления оценки и жанра. 
# Выберите верные варианты ответа, исходя из построенной таблицы:
ratings_movies['date'] = pd.to_datetime(ratings_movies['date'])
ratings_movies['year_rating'] = ratings_movies['date'].dt.year

pivot= ratings_movies.pivot_table(
    index = 'year_rating',
    columns = 'genres',
    values = 'rating',
    aggfunc= np.mean
).round(2)
print(pivot)

print('_' * 40)
# Задание 8.8
orders_df = pd.read_csv('data/orders.csv', sep=';')
print(orders_df)

print('_' * 40)
products_df = pd.read_csv('data/products.csv', sep=';')
print(products_df)

orders_products = orders_df.merge(
    products_df,
    left_on='ID товара',
    right_on='Product_ID',
    how='left'
)
print(orders_products[orders_products['Name'].isna()])

print('_' * 40)
# Задание 8.9
mask1 = orders_products['Отменен'] == 'Да'
print(orders_products[mask1]['Name'])

print('_' * 40)
# Задание 8.10
orders_products['Profit'] = orders_products['Количество'] * orders_products['Price']
mask1 = orders_products['Оплачен'] == 'Да'
print(orders_products[mask1].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False))