# --- Введение в Pandas ---
import pandas as pd
print(pd.__version__) # Версия

print('_' * 40)
print(pd.__name__)

# Создание Series пустой
series = pd.Series()

print('_' * 40)
# Способ 1 — из списка с использованием параметров функции pd.Series():

series = pd.Series(
    name='countries',
    index=['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'DK'],
    data=['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Дания'],
)
print(series)

print('_' * 40)
# Способ 2 — из списка с использованием параметров функции pd.Series():
countries = pd.Series({
    'UK': 'Англия',
    'CA': 'Канада',
    'US' : 'США',
    'RU': 'Россия',
    'UA': 'Украина',
    'BY': 'Беларусь',
    'DK': 'Дания'},
    name = 'countries'
)
print(countries)

print('_' * 40)
# Чтобы получить данные нужно написать расширения .loc или .iloc
print(countries.loc['DK'])

print('_' * 40)
# Или обернуть в список:
print(countries.loc[['UK', 'RU', 'DK']])

print('_' * 40)
# С .iloc работа с данными похожа на запросы по индексу в массивах
print(countries.iloc[4])
print('_' * 40)
# Или срез
print(countries.iloc[1:4])

print('_' * 40)
# Задание 2.4 (Напишите функцию create_medications(names, counts), которая создает Series medications, 
# индексами которой являются названия лекарств names, а значениями - их количество в поставке counts.)
# А также напишите функцию get_percent(medications, name), которая возвращает долю количества товара с 
# именем name от общего количества товаров в поставке в процентах.
def create_medications(names, counts):
    return pd.Series(index=names, data=counts)

def get_percent(medications, name):
    count = medications.loc[name]
    value = sum(medications)
    return count / value * 100

names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

medications = create_medications(names, counts)
print(medications)

print(get_percent(medications, "chlorhexidine")) #37.5

print('_' * 40)
# Dataframe как структура данных
# Два способа создания:
# Способ 1 - (простой)
countries_df = pd.DataFrame({
    'сountry': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Дания'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
print(countries_df)

# Поскольку мы не задали индексы, то сделаем это вручную
countries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
print(countries_df)

print('_' * 40)
# Способ 2 - (из вложенного списка)
countries_df = pd.DataFrame(
    data = [
        ['Англия', 56.29, 133396],
        ['Канада', 38.05, 9984670],
        ['США', 322.28, 9826630],
        ['Россия', 146.24, 17125191],
        ['Украина', 45.5, 603628],
        ['Беларусь', 9.5, 207600],
        ['Дания', 17.04, 2724902]
    ],
    columns= ['country', 'population', 'square'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'DK']
)
print(countries_df)
# К столбцу можно получить доступ таким образом (если в названии нет пробелов)
print(countries_df.population)
# или так
print(countries_df['population'])
print(type(countries_df.population))

print('_' * 40)
# Получить доступ к строкам
# Население Великобритании
uk_population = countries_df.loc['UK', ['population']]
print(uk_population)

print('_' * 40)
# Население и площадь по России
ru_population_square = countries_df.loc['RU', ['population', 'square']]
print(ru_population_square)

print('_' * 40)
# Украина, Белоруссия, Дания
ua_by_dk_info = countries_df.loc[['UA','BY','DK'], ['population', 'square']]
print(ua_by_dk_info)
# или
print(countries_df.iloc[4:8, 1:3])

print('_' * 40)
# Задание 3.5 (Создайте функцию create_companyDF(income, expenses, years), которая возвращает DataFrame, 
# составленный из входных данных со столбцами Income и Expenses и индексами, соответствующими годам рассматриваемого периода)
# Также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, записанными в таблице df, 
# за год year.
income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

def create_companyDF(income, expenses, years):
    result = pd.DataFrame({
        'Income': income,
        'Expenses': expenses
    })
    result.index = years
    return result
    
df = create_companyDF(income, expenses, years)
#     Income  Expenses
# 2018    478     156
# 2019    512     130
# 2020    196     270
print(df)

year = 2018
df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])

def get_profit(df, year):
    indexes = df.index
    if year not in indexes:
        return None
    else:
        data = df.loc[year, ['Income', 'Expenses']]
        income = data['Income']
        expenses = data['Expenses']
        df = income - expenses
        return df

print(get_profit(df, 2015)) # None
print(get_profit(df, year)) # 353

print('_' * 40)
# Разные источники данных в pandas
# Запишем наш DataFrame с информацией о странах в папку data
countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
countries_df.to_csv(path_or_buf='data/countries.csv', index=False, sep=';')

print('_' * 40)
# Чтение файла .csv из data
countries_source = pd.read_csv('data/countries.csv', sep=';')
print(countries_source)
# Также чтение по ссылке
# data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
# print(data)
# Чтение других форматов, например большого файла json из папки data
data_from_json = pd.read_json('data/melb_data.json')
print(data_from_json)

print('_' * 40)
# Данные представляют собой таблицу, в которой содержится 23 столбца:

# index — номер строки
# Suburb — наименование пригорода
# Address — адрес
# Rooms — количество комнат в помещении
# Type — тип здания (h — дом, коттедж, вилла, терраса; u — блочный, дуплексный дом; t — таунхаус)
# Price — цена помещения
# Method — метод продажи 
# SellerG — риэлторская компания
# Date — дата продажи (в формате день/месяц/год)
# Distance — расстояния до объекта от центра Мельбурна 
# Postcode — почтовый индекс
# Bedroom — количество спален
# Bathroom — количество ванных комнат
# Car — количество парковочных мест
# Landsize — площадь прилегающей территории
# BuildingArea — площадь здания
# YearBuilt — год постройки
# CouncilArea — региональное управление
# Lattitude — географическая широта
# Longitude — географическая долгота
# Regionname — наименование района Мельбурна
# Propertycount — количество объектов недвижимости в районе, выставленных на продажу
# Coordinates — широта и долгота, объединённые в кортеж
melb_data = pd.read_csv('data/melb_data.csv', sep=',')

print('_' * 40)
# Задание 5.1 (Найти цену под индексом 15)
print(melb_data.loc[15, ['Price']])

print('_' * 40)
# Задание 5.2 (Когда был продан объект под индексом 90?)
print(melb_data.loc[90, ['Date']])

print('_' * 40)
# Задание 5.3 (Во сколько раз площадь прилегающей территории, на которой 
# находится здание с индексом 3521, больше площади участка, на котором находится 
# здание с индексом 1690? Ответ округлите до целого числа.)
building_1 = float(melb_data.loc[3521, ['Landsize']])
building_2 = float(melb_data.loc[1690, ['Landsize']])
result = building_1 / building_2
print(round(result))

print('_' * 40)
# Вывод первых и последних строк
print(melb_data.head(5))
print('_' * 40)
print(melb_data.tail(7))

print('_' * 40)
# Размер таблицы
print(melb_data.shape)

print('_' * 40)
# Получение информации о столбцах
print(melb_data.info())

# Изменение типа данных в столбце
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
melb_data.info()

print('_' * 40)
# Получение описательной статистики
print(melb_data.describe())

print('_' * 40)
# Чтобы вывести ограниченную информацию можно воспользоваться следующим способом:
print(melb_data.describe().loc[:, ['Distance', 'BuildingArea', 'Price']])

print('_' * 40)
# Метод describe() можно применять не только к числовым признакам. С помощью параметра include 
# можно указать тип данных, для которого нужно вывести описательную информацию.
print(melb_data.describe(include=['object']))

print('_' * 40)
# Частота уникальных значений 
print(melb_data['Regionname'].value_counts())

# Чтобы сделать вывод более интерпретируемым и понятным, можно воспользоваться 
# параметром normalize. При установке значения этого параметра на True результат 
# будет представляться в виде доли (относительной частоты):
print('_' * 40)
print(melb_data['Regionname'].value_counts(normalize=True))

print('_' * 40)
# Задание 6.1 (Shape)
data = pd.DataFrame([[0,1], [1, 0], [1, 1]], columns=['А', 'B'])
print(data.shape)

print('_' * 40)
# Задание 6.3 (Coordinates. Какой тип данных?)
print(melb_data.dtypes['Coordinates'])

print('_' * 40)
# Задание 6.5 (Сколько пропущенных значений в столбце CouncilArea?)
print(melb_data.isnull().sum())

print('_' * 40)
# Задание 6.6 (Сколько столбцов после преобразования типов имеет целочисленный тип данных?)
print(melb_data.dtypes.value_counts())

print('_' * 40)
# Задание 6.9 (Сколько процентов от общего количества домов составляют таунхаусы (тип объекта — t)?)
print(melb_data['Type'].value_counts())
full_count = int(melb_data['Type'].count())
t_count = int(melb_data['Type'].value_counts()[2])
print(round(t_count * (100 / full_count)))

print('_' * 40)
# -- Агрегирующие методы --
# Например:

print('_' * 40)
# Cредние цены
print(melb_data['Price'].mean())

print('_' * 40)
# Максимальное число парковочных мест
print(melb_data['Car'].max())

print('_' * 40)
# А теперь представим, что риэлторская ставка для всех 
# компаний за продажу недвижимости составляет 12%. Найдём 
# общую прибыльность риэлторского бизнеса в Мельбурне. 
# Результат округлим до сотых:
rate = 0.12
income = melb_data['Price'].sum() * rate
print(round(income, 2))

print('_' * 40)
# Найдём, насколько медианная площадь территории отличается 
# от её среднего значения. Вычислим модуль разницы между 
# медианой и средним и разделим результат на среднее, чтобы 
# получить отклонение в долях:
landsize_mediana = melb_data['Landsize'].median()
landsize_mean = melb_data['Landsize'].mean()
print(abs(landsize_mediana - landsize_mean)/landsize_mean)

print('_' * 40)
# Какое количество комнат больше всего представлено на рынке
print(melb_data['Rooms'].mode())

print('_' * 40)
# Или например распространенное название районов
print(melb_data['Regionname'].mode())

print('_' * 40)
# Задание 7.4
# Чему равно отклонение (в процентах) медианного значения площади здания от его среднего значения?
# Ответ округлите до целого числа.
buildingarea_mediana = melb_data['BuildingArea'].median()
buildingarea_mean = melb_data['BuildingArea'].mean()
print(round(abs(buildingarea_mediana - buildingarea_mean)/buildingarea_mean * 100))

# Задание 7.6
# Сколько спален чаще всего встречается в домах в Мельбурне?
print(melb_data['Bedroom'].mode())

print('_' * 40)
# -- Фильтрация данных --
# Пример маски
mask = melb_data['Price'] > 200_000
print(mask)

print('_' * 40)
# далее применяем эту маску 
print(melb_data[mask].head())

print('_' * 40)
# или можно без переменной mask
print(melb_data[melb_data['Price'] > 2000000])

print('_' * 40)
# Найдём количество зданий с тремя комнатами. Для этого отфильтруем таблицу по условию: 
# обратимся к результирующей таблице по столбцу Rooms и найдём число строк в ней с помощью атрибута shape

# найти число строк в результирующей таблицы с помощью атрибута shape
print(melb_data[melb_data['Rooms'] == 3].shape[0])

print('_' * 40)
# Условия можно комбинировать, включая операторы & или || и т.д
print(melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300_000)])
print('_' * 40)
print(melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300_000)].shape[0])

print('_' * 40)
# Таких зданий оказалось всего три. Немного «ослабим» условие: теперь нас будут интересовать дома с ценой менее 
# 300 тысяч, у которых либо число комнат равно 3 либо площадь домов более 100 квадратных метров:
print(melb_data[(melb_data['Price'] < 300_000) & ((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100))].shape[0])

print('_' * 40)
# Фильтрацию часто сочетают со статистическими методами. Давайте найдём максимальное количество комнат в таунхаусах. 
# Так как в результате фильтрации получается DataFrame, то обратимся к нему по столбцу Rooms и найдём максимальное значение:
print(melb_data[melb_data['Type'] == 't']['Rooms'].max())

print('_' * 40)
# А теперь более сложный трюк: найдём медианную площадь здания у объектов, чья цена выше средней. 
# Для того чтобы оградить наш код от нагромождений, предварительно создадим переменную со средней ценой:
mean_price = melb_data['Price'].mean()
print(melb_data[melb_data['Price'] > mean_price]['BuildingArea'].median())

print('_' * 40)
# Задание 8.1
print(melb_data[melb_data['Bathroom'] == 0].shape[0])

print('_' * 40)
# Задание 8.2
print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3_000_000)].shape[0])

print('_' * 40)
# Задание 8.3
# Какова минимальная стоимость участка без здания (площадь здания равна 0) в таблице melb_data?
# Запишите ответ в виде целого числа.
result = melb_data[melb_data['BuildingArea'] == 0]['Price'].min()
print(round(result))

print('_' * 40)
# Задание 8.4
# Какова средняя цена объектов недвижимости в таблице melb_data с ценой менее одного миллиона, 
# в которых либо количество комнат больше пяти, либо здание моложе 2015 года?
print(round(melb_data[(melb_data['Price'] < 1_000_000) & ((melb_data['Rooms'] > 5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean()))

print('_' * 40)
# Задание 8.5
# В каком районе Мельбурна чаще всего продаются виллы и коттеджи (тип здания — h) с ценой меньше трёх миллионов?
print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3_000_000)]['Regionname'].mode())

print('_' * 40)
# -- Закрепление знаний --
import pandas as pd

# Читаем
melb_data = pd.read_csv(filepath_or_buffer='data/melb_data.csv', sep=',')

print('1._' * 40)
print(melb_data.head())
print('2._' * 40)
print(melb_data.tail())
print('3._' * 40)
print(melb_data.shape) # (строки - 13580, столбца - 23)
print('4._' * 40)
print(melb_data.info())
print('5._' * 40)
print(melb_data.describe())
print('5.1_' * 40)
print(melb_data.describe(include=['object'])) # выводим инф. для типа данных object
print('6_' * 40)
print(melb_data['Regionname'].value_counts()) # Частота определенного столбца
print('6.1_' * 40)
print(melb_data['Regionname'].value_counts(normalize=True)) # Частота определенного столбца (в процентном соотношении)

print('_' * 40)
print('_' * 40)
# Читаем
student_data = pd.read_csv(filepath_or_buffer='data/students_performance.csv', sep=',')

print('_' * 40)
print(student_data.head())

# gender — пол;
# race/ethnicity — раса/этническая принадлежность;
# parental level of education — уровень образования родителей;
# lunch — какие обеды получал студент во время обучения (standard — платный, free/reduced — бесплатный);
# test preparation course — посещал ли студент курсы подготовки к экзаменам (none — не посещал, completed — посещал);
# math score, reading score, writing score — баллы по математике, чтению и письму по сто балльной шкале.

print('_' * 40)
print(student_data.loc[155, ['writing score']])

print('_' * 40)
print(student_data.isnull().sum())

print('_' * 40)
print(student_data.info())

print('_' * 40)
print(round(student_data.memory_usage(index=True).sum()/1024))

print('_' * 40)
print(round(student_data['math score'].mean(axis=0)))

print('_' * 40)
print(student_data['race/ethnicity'].mode())

print('_' * 40)
result = student_data[student_data['test preparation course'] == 'completed']['reading score'].mean()
print(round(result))

print('_' * 40)
print(student_data[student_data['math score'] == 0].shape[0])

# Задание 9.10
# Проверьте гипотезу: у студентов с оплачиваемым питанием средний балл по математике выше, чем у студентов с льготным питанием.
# В качестве ответа напишите наибольший средний балл по математике среди этих групп студентов.
# Округлите ответ до целого числа.

print('_' * 40)
mask_1 = student_data[student_data['lunch'] == 'standard']['math score'].mean()
mask_2 = student_data[student_data['lunch'] == 'free/reduced']['math score'].mean()
result = (mask_1 > mask_2)
# Утверждение верно!
if result: print(round(mask_1))

# Задание 9.11
# Каков процент студентов, родители которых имеют высшее образование уровня бакалавриата (bachelor's degree)?
# Округлите ответ до целого числа.
print('_' * 40)
print(round(student_data[student_data['parental level of education'] == '''bachelor's degree'''].shape[0]*0.10))
# или
print(student_data["parental level of education"].value_counts(normalize=True))

# Задание 9.12
# Насколько медианный балл по письму у студентов в расовой группе А отличается от среднего балла по письму у студентов в расовой группе C?
# Округлите ответ до целого и запишите модуль этого числа.
print('_' * 40)
group_a = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
group_c = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean()
print(round(abs(group_c - group_a)))