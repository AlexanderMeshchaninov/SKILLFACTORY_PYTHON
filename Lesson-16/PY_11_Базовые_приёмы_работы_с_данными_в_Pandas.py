import pandas as pd

print('_' * 40)
melb_data_ps = pd.read_csv(filepath_or_buffer='data/melb_data_ps.csv', sep=',')
#print(melb_data_ps.head())

# Чтобы данные изначальной таблицы были консистентны, создаем копию для дальйшей работы
melb_df = melb_data_ps.copy()
print(melb_df.head())

print('_' * 40)
# Удалим столбцы index и Coordinates из таблицы с помощью метода drop(). Выведем первые пять строк таблицы и убедимся, что всё прошло успешно
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
print(melb_df.head())

# Альтернативный вариант:
# melb_df.drop(['index','Coordinates'],axis=1,inplace=True)
# melb_df.head()

# Математические операции над столбцами
# Например, давайте создадим переменную total_rooms, в которой будем хранить общее количество комнат в здании. 
# Для этого выполним сложение столбцов с количеством комнат, ванн и спален.

print('_' * 40)
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
print(total_rooms)

print('_' * 40)
# А теперь введём новый признак MeanRoomsSquare, который соответствует средней площади одной комнаты для каждого объекта. 
# Для этого разделим площадь здания на полученное ранее общее количество комнат
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
print(melb_df['MeanRoomsSquare'])

print('_' * 40)
# Можно ввести ещё один интересный признак — AreaRatio, коэффициент соотношения 
# площади здания (BuildingArea) и площади участка (Landsize). Для этого разницу двух площадей поделим на их сумму:
# Разница двух площадей
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
# Сумма всей площади
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
# Создаем новый признак (делим разницу и сумму всей площади)
melb_df['AreaRation'] = diff_area/sum_area
print(melb_df['AreaRation'])

# ! Таким образом, значение в столбце AreaRatio служит своеобразным указателем соотношения площадей объекта недвижимости. 
# ! Для пустырей — участков без строений — он будет равен -1, для домов без территории — 1, во всех остальных случаях мы 
# ! можем увидеть, какая площадь больше — здания или участка.

square = melb_df['Price'] **2
print(square)

print('_' * 40)
square = []
for p in melb_df['Price']:
    square.append(p ** 2)
square = pd.Series(square)
print(square)

print('_' * 40)
# Задание 2.3 (Напишите функцию delete_columns(df, col=[]), которая удаляет столбцы из DataFrame 
# и возвращает новую таблицу. Если одного из указанных столбцов не существует в таблице, то функция 
# должна возвращать None.)

def delete_columns(df, col=[]):
    # Проверка существует ли заданный столбец в таблице
    for t in col: 
        if t not in df.columns: return None
    
    df = df.drop(col, axis=1)
    return df
    

customer_df = pd.DataFrame({
            'number': [0, 1, 2, 3, 4],
            'cust_id': [128, 1201, 9832, 4392, 7472],
            'cust_age': [13, 21, 19, 21, 60],
            'cust_sale': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
            'cust_order': [1400, 14142, 900, 1240, 8430]
        })

print(customer_df)

new_customer_df = delete_columns(df=customer_df, col=['number', 'cust_age'])
print(new_customer_df)

# Задание 2.4 (Для каждой страны рассчитайте плотность населения (количество человек на квадратный километр). 
# Затем по полученным данным рассчитайте среднее по плотностям населения в указанных странах. 
# Ответ округлите до сотых. 
# * Плотность населения рассчитывается как количество человек, проживающих на территории отдельной страны, делённое на 
# площадь этой страны. Обратите внимание, что население в таблице представлено в миллионах.)

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

# Получаем плотность населения путем создания нового признака
countries_df['pop_density'] = (countries_df['population'] * 1_000_000)/countries_df['square']
mean_pop_density = countries_df['pop_density'].mean()

print(countries_df)
print(round(mean_pop_density, 2))

print('_' * 40)
print(melb_df['Date'].head())

# Для того чтобы преобразовывать столбцы с датами, записанными в распространённых форматах, 
# в формат datetime, можно воспользоваться функцией pandas.to_datetime(). В нашем случае в функции 
# нужно указать параметр dayfirst=True, который будет обозначать, что в первоначальном признаке первым идет день. 
# Преобразуем столбец Date в формат datetime, передав его в эту функцию:

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
print(melb_df['Date'])

print('_' * 40)
# Продажи за годы
years_sold = melb_df['Date'].dt.year
print(years_sold)
print('Min year sold:', years_sold.min())
print('Max year sold:', years_sold.max())
# Так как модальных значений в столбце может быть несколько, метод mode() возвращает объект Series, 
# даже если мода в данных только одна. Чтобы сохранить стилистику вывода информации о годе продажи 
# и выводить только число, а не Series, мы обращаемся к результату работы метода mode() по индексу 0
print('Mode year sold:', years_sold.mode()[0])

# Занесем результат пика продаж по месяцам
melb_df['MonthSale'] = melb_df['Date'].dt.month

print('_' * 40)
# Теперь попробуем понять, на какие месяцы приходится пик продаж объектов недвижимости. 
# Для этого выделим атрибут dt.month и на этот раз занесём результат в столбец MonthSale, 
# а затем найдём относительную частоту продаж для каждого месяца от общего количества продаж — 
# для этого используем метод value_counts() с параметром normalize (вывод в долях):
print(melb_df['MonthSale'].value_counts(normalize=True))

# Работа с интервалами
# В результате мы получаем Series, элементами которой является количество дней, которое прошло 
# с 1 января 2016 года. Обратите внимание, что данные такого формата относятся к типу timedelta.
# Чтобы превратить количество дней из формата интервала в формат целого числа дней, можно воспользоваться 
# аксессором dt для формата timedelta и извлечь из него атрибут days:
delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01')
print(delta_days)

print('_' * 40)
# Чтобы превратить количество дней из формата интервала в формат целого числа дней, можно 
# воспользоваться аксессором dt для формата timedelta и извлечь из него атрибут days
print(delta_days.dt.days)

print(melb_df.info())
print('_' * 40)
# Рассмотрим другой пример. Давайте создадим признак возраста объекта недвижимости в годах на момент продажи. 
# Для этого выделим из столбца с датой продажи год и вычтем из него год постройки здания. 
# Результат оформим в виде столбца AgeBuilding.
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
print(melb_df['AgeBuilding'])

# На самом деле столбец AgeBuilding дублирует информацию столбца YearBuilt, так как, зная год постройки 
# здания, мы автоматически знаем его возраст. Такие признаки не стоит оставлять вместе, поэтому оставим 
# возраст здания, так как он является более наглядным, а год постройки удалим из таблицы:
melb_df = melb_df.drop('YearBuilt', axis=1)
print(melb_df)

print('_' * 40)
# Задание 3.3
# Создайте в таблице melb_df признак WeekdaySale (день недели). Найдите, сколько объектов недвижимости 
# было продано в выходные (суббота и воскресенье), результат занесите в переменную weekend_count. 
# В качестве ответа введите результат вывода переменной weekend_count.
melb_df['WeekdaySale'] = melb_df['Date'].dt.day_of_week
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
print(weekend_count)

# Задание 3.4 - 3.5
# Вам представлены данные (в формате csv) об отчётах очевидцев НЛО в США за период с 1930 по 2020 год.
# В данных есть следующие признаки:
# "City" — город, где был замечен НЛО;
# "Colors Reported" — цвет объекта;
# "Shape Reported" — форма объекта;
# "State" — обозначение штата;
# "Time" — время, когда был замечен НЛО (данные отсортированы от старых наблюдений к новым). 
# Прочитайте данные, сделайте преобразование времени к формату datetime и выполните задания ниже.

ufo_data = pd.read_csv('data/ufo_data.csv', sep=',')
print(ufo_data.head())

ufo_data['Time'] = pd.to_datetime(ufo_data['Time'])
print(ufo_data)

print('_' * 40)
# Задание 3.4
# В каком году отмечается наибольшее количество случаев наблюдения НЛО в США?
print(ufo_data['Time'].dt.year.mode())

print('_' * 40)
# Задание 3.5
# Найдите средний интервал времени (в днях) между двумя последовательными случаями наблюдения НЛО в штате Невада (NV).
# Чтобы выделить дату из столбца Time, можно воспользоваться атрибутом datetime date.
# Чтобы вычислить разницу между двумя соседними датами в столбце, примените к нему метод diff().
# Чтобы перевести интервал времени в дни, воспользуйтесь атрибутом timedelta days.
dates = ufo_data[ufo_data['State'] == 'NV']['Time'].dt.date
diff_dates = dates.diff()
days = diff_dates.dt.days
print(round(days.mean()))

print('_' * 40)
# --- Реализация функций к столбцам ---
# Есть столбец Address с наличием большого количества уникальных функций nunique()
print(melb_df['Address'].nunique())

print('_' * 40)
# Поскольку данный столбец имеет можетсво уникальных категорий, то провести какую-либо статистическую выкладку не представляется возможным
# Обычно такие признаки удаляются, но можно поступить умнее. Выделить из данного признака характеристики подтипа
print(melb_df['Address'].loc[177])
print(melb_df['Address'].loc[1812])
print(melb_df['Address'].loc[9001])
# 2/119 Railway St N
# 9/400 Dandenong Rd
# 172 Danks St

# Итак, адрес строится следующим образом: сначала указывается номер дома и корпус, после указывается название улицы, 
# а в конце — подтип улицы, но в некоторых случаях к подтипу добавляется географическая отметка (N — север, S — юг и т. д.), 
# она нам не нужна . Для того чтобы выделить подтип улицы, на которой находится объект, можно использовать следующую функцию:

# На вход данной функции поступает строка с адресом.
def get_street_type(address):
    # Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
    # Метод split() разбивает строку на слова по пробелу.
    # В результате получаем список слов в строке и заносим его в переменную address_list.
    address_list = address.split(' ')
    # Обрезаем список, оставляя в нём только последний элемент,
    # потенциальный подтип улицы, и заносим в переменную street_type.
    street_type = address_list[-1]
    # Делаем проверку на то, что полученный подтип является географической пометкой.
    # Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
        # Если переменная street_type является географической пометкой,
        # переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
    # Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type

print('_' * 40)
# Теперь применим эту функцию к столбцу c адресом. Для этого передадим функцию get_street_type в аргумент метода столбца apply(). 
# В результате получим объект Series, который положим в переменную street_types:
street_types = melb_df['Address'].apply(get_street_type)
print(street_types)

print('_' * 40)
# Обратите внимание, что функция пишется для одного элемента столбца, а метод apply() применяется к каждому его элементу. 
# Используемая функция обязательно должна иметь возвращаемое значение.
# Итак мы выделили подтип улицы
print(street_types.nunique())

print('_' * 40)
# У нас есть 56 уникальных значений. Однако наш результат можно улучшить. 
# Давайте для начала посмотрим на частоту каждого подтипа улицы с помощью метода value_counts:
print(street_types.value_counts())

print('_' * 40)
# Из данного вывода можно увидеть, что есть группа наиболее популярных подтипов улиц, а дальше частота подтипов быстро падает.
# В таком случае давайте применим очень распространённый метод уменьшения количества уникальных категорий — 
# выделим n подтипов, которые встречаются чаще всего, а остальные обозначим как 'other' (другие).
# Для этого к результату метода value_counts применим метод nlargest(), который возвращает n наибольших значений из Series. 
# Зададим n=10, т. е. мы хотим отобрать десять наиболее популярных подтипов. Извлечём их названия с помощью атрибута index, 
# а результат занесём в переменную popular_stypes:

popular_stypes = street_types.value_counts().nlargest(10).index
print(popular_stypes)

# *** ======
def set_short_names(address):
    long_names = {'Avenue':'Av', 'Parade':'Prd', 'Boulevard':'Bvd', 
                  'Crescent':'Crc', 'Strand':'Std', 'Esplanade':'Esp', 
                  'Grove':'Grv', 'Fairway':'Fay', 'Crossway':'Crs', 
                  'Righi':'Rig', 'Victoria':'Vic', 'Ridge':'Rdg', 
                  'Crofts':'Crf', 'Glade':'Gld', 'Woodland':'Wod', 
                  'Outlook':'Out', 'Highway':'Hig', 'Athol':'Ath',
                  'Summit':'Sum', 'Grand':'Grd', 'Nook':'Nok', 
                  'Eyrie':'Eyr', 'Dell':'Dll', 'East':'Est',
                  'Loop':'Lop', 'Grange':'Gre', 'Terrace':'Ter', 
                  'Cove':'Cov', 'Corso':'Cro'}
    if address in long_names.keys():
        address = long_names[address]
    return address

melb_df['StreetType'] = street_types.apply(lambda x: set_short_names(x))
print(melb_df[melb_df['StreetType'] == 'Dll'])
# *** ======

print('_' * 40)
# Теперь, когда у нас есть список наиболее популярных подтипов улиц, введём lambda-функцию, которая будет проверять, 
# есть ли строка x в этом перечне, и, если это так, lambda-функция будет возвращать x, в противном случае она будет 
# возвращать строку 'other'. Наконец, применим такую функцию к Series street_types, полученной ранее, а результат 
# определим в новый столбец таблицы StreetType:
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
print(melb_df['StreetType'])

print('_' * 40)
# Посмотрим на результирующее число уникальных подтипов:
print(melb_df['StreetType'].nunique())

print('_' * 40)
# Теперь, у нас нет потребности хранить признак Address, так как, если конкретное местоположение объекта всё же и влияет 
# на его стоимость, то оно определяется столбцами Longitude и Lattitude. Удалим его из нашей таблицы:
melb_df = melb_df.drop('Address', axis=1)
print(melb_df)

# Таким образом, с помощью написания собственных функций и их комбинирования с методом apply() из библиотеки Pandas 
# мы смогли извлечь информацию из признака с адресом и заменить на признак подтипа улицы.

# ***Если присмотреться, то в списке подтипов улиц street_types можно заметить подтипы, которые именуются различным образом, 
# но при этом обозначают одинаковые вещи. Например, подтипы Av и Avenue, Bvd и Boulevard, Pde и Parade. Мы упустили данный 
# момент, хотя в реальных задачах стоит обращать пристальное внимание на результаты преобразований и исправлять неточности в данных.
# Такие ошибки в данных (обозначение идентичных категорий различными именами) являются одним из видов «грязных» данных.
# Порой отследить такие неточности бывает очень сложно, а при наличии большого количества категорий (например, более ста) — 
# практически невозможно.
# Мы предлагаем вам самостоятельно разобраться с этой ошибкой: попробуйте написать функцию-преобразование 
# (lambda-функцию-преобразование), которая возвращала бы вместо значений Avenue, Boulevard и Parade их топографические 
# сокращения, и примените её к данным о подтипах улиц.
# Обратите внимание, что данное преобразование необходимо применить до сокращения количества уникальных категорий.

print('_' * 40)
# Задание 4.2
# Ранее, в задании 3.3, мы создали признак WeekdaySale в таблице melb_df — день недели продажи. 
# Из полученных в задании результатов можно сделать вывод, что объекты недвижимости в Мельбурне продаются 
# преимущественно по выходным (суббота и воскресенье).
# Напишите функцию get_weekend(weekday), которая принимает на вход элемент столбца WeekdaySale и возвращает 1, 
# если день является выходным, и 0 — в противном случае, и создайте столбец Weekend в таблице melb_df с помощью неё.
# Примените эту функцию к столбцу и вычислите среднюю цену объекта недвижимости, проданного в выходные дни. 
# Результат округлите до целых.
def get_weekend(weekday):
    weekend = [5, 6]
    if weekday in weekend:
        return 1
    else:
        return 0
    
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
print(melb_df['Weekend'])

print(round(melb_df[melb_df['Weekend'] == 1]['Price'].mean()))

print('_' * 40)
# Задание 4.3
# Преобразуйте столбец SellerG с наименованиями риелторских компаний в таблице melb_df следующим образом: 
# оставьте в столбце только 49 самых популярных компаний, а остальные обозначьте как 'other'.
# Найдите, во сколько раз минимальная цена объектов недвижимости, проданных компанией 'Nelson', 
# больше минимальной цены объектов, проданных компаниями, обозначенными как 'other'. 
# Ответ округлите до десятых.
popular_companies = melb_df['SellerG'].value_counts().nlargest(49)
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_companies else 'other')

min_nelson_price = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
min_other_price = melb_df[melb_df['SellerG'] == 'other']['Price'].min()

result = min_nelson_price/min_other_price
print(round(result, 2))

print('_' * 40)
# Задание 4.4
# Представьте, что вы занимаетесь подготовкой данных о вакансиях с платформы hh.ru. 
# В вашем распоряжении имеется таблица, в которой с помощью парсинга собраны резюме кандидатов. 
# В этой таблице есть текстовый столбец «Опыт работы». Пример такого столбца представлен ниже в 
# виде объекта Series. Структура текста в столбце фиксирована и не может измениться.

# Напишите функцию get_experience(arg), аргументом которой является строка столбца с опытом работы. 
# Функция должна возвращать опыт работы в месяцах. Не забудьте привести результат к целому числу.

exp_data = pd.Series({
    0:'Опыт работы 8 лет 3 месяца',
    1:'Опыт работы 3 года 5 месяцев',
    2:'Опыт работы 1 год 9 месяцев',
    3:'Опыт работы 3 месяца',
    4:'Опыт работы 6 лет',
})

def get_experience(arg):
    # Возвращать опыт работы в месяцах
    # Split строки
    str_split = arg.split(' ')
    if len(str_split) == 4:
        last_word = str_split[-1]
        if last_word in ['месяцев', 'месяц', 'месяца']:
            month = int(str_split[2])
            return month
        else:
            year = int(str_split[2])
            return year*12
    else:
        year = int(str_split[2])
        month = int(str_split[4])
        return year*12 + month
    
ls = []
ls.append(exp_data.apply(get_experience))
res = pd.Series(ls)
print(res)

print('_' * 40)
# --- Категориальные и числовые данные ---
# Давайте определим число уникальных категорий в каждом столбце нашей таблицы melb_df. 
# Для этого создадим вспомогательную таблицу unique_counts:
# Создаем пустой список
unique_list = []
# пробегаемся по именам столбцов в таблице
for col in melb_df.columns:
    # создаём кортеж (имя столбца, число уникальных значений, тип столбца)
    item = (col, melb_df[col].nunique(), melb_df[col].dtypes)
    # добавляем кортеж в список
    unique_list.append(item)
# создаём вспомогательную таблицу и сортируем её
unique_counts = pd.DataFrame(
    unique_list,
    columns=['Column_Name', 'Num_Unique', 'Type']
).sort_values(by='Num_Unique', ignore_index=True)
# выводим её на экран
print(unique_counts)

print('_' * 40)
# --- Тип Category ---
# Преобразование столбца к типу category
# Для начала посмотрим сколько памяти занимает таблица
print(melb_df.info()) # 2.6 MB

# Сделаем преобразование столбцов к типу данных category:
# список столбцов, которые мы не берём во внимание
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
# задаём максимальное число уникальных категорий
max_unique_count = 150
# цикл по именам столбцов
for col in melb_df.columns:
    # проверяем условие
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        # преобразуем тип столбца в category
        melb_df[col] = melb_df[col].astype('category')

print(melb_df.info()) # 1.9 MB 
# Таким образом объем используемой памяти для табицы уменьшился почти в 1.5 раза!

# ПОЛУЧЕНИЕ АТРИБУТОВ CATEGORY
# У типа данных category есть свой специальный аксесcор cat, который позволяет получать информацию о 
# своих значениях и преобразовывать их. Например, с помощью атрибута этого аксессора categories мы можем 
# получить список уникальных категорий в столбце Regionname

print('_' * 40)
print(melb_df['Regionname'].cat.categories)

# А теперь посмотрим, каким образом столбец кодируется в виде чисел в памяти компьютера. 
# Для этого можно воспользоваться атрибутом codes:

print('_' * 40)
print(melb_df['Regionname'].cat.codes)

print(melb_df['Type'])
# С помощью метода аксессора rename_categories() можно легко переименовать текущие значения категорий. 
# Для этого в данный метод нужно передать словарь, ключи которого — старые имена категорий, а значения — новые.
# Рассмотрим на примере: переименуем категории признака типа постройки Type — заменим их на полные названия 
# (напомним, u — unit, h — house, t — townhouse).
melb_df['Type'] = melb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
})

print(melb_df['Type'])

# Подводные камни
# А теперь представим ситуацию, что появилась новая партия домов и теперь мы продаём и квартиры (flat). 
# Создадим объект Series new_houses_types, в котором будем хранить типы зданий новой партии домов. 
# Преобразуем тип new_houses_types в такой же тип, как и у столбца Type в таблице melb_data, и выведем результат на экран:
new_houses_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
new_houses_types = new_houses_types.astype(melb_df['Type'].dtype)

# С нашими новыми объектами недвижимости произошло нечто странное. 
# По какой-то причине вместо квартир мы получили пустые значения — NaN.
print(new_houses_types)

# На самом деле причина проста: тип данных category хранит только категории, которые были объявлены 
# при его инициализации. При встрече с новой, неизвестной ранее категорией, этот тип превратит её в 
# пустое значение, так как он просто не знает о существовании этой категории.

# Решить эту проблему на самом деле не сложно. Можно добавить категорию flat в столбец 
# Type с помощью метода акссесора cat add_categories(), в который достаточно просто передать имя новой категории
melb_df['Type'] = melb_df['Type'].cat.add_categories('flat')
new_houses_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
new_houses_types = new_houses_types.astype(melb_df['Type'].dtype)

print(new_houses_types) # Теперь все отлично

print('_' * 40)
# Задание 5.2
# При преобразовании столбцов таблицы о недвижимости к типу category мы оставили без внимания 
# столбец Suburb (пригород). Давайте исправим это.
# С помощью метода info() узнайте, сколько памяти занимает таблица melb_df.
# Преобразуйте признак Suburb следующим образом: оставьте в столбце только 119 наиболее популярных 
# пригородов, остальные замените на 'other'.
# Приведите данные в столбце Suburb к категориальному типу.
# В качестве ответа запишите разницу между объёмом занимаемой памяти до преобразования 
# (который мы получили ранее в модуле) и после него в Мб. Ответ округлите до десятых.

print(melb_df.info())
# Делим байты на количество мегабайт в байте
memory_before = melb_df.memory_usage(index=True).sum() / 1048576
# Преобразовать признак
popular_suburb = melb_df['Suburb'].value_counts().nlargest(119)
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_suburb else 'other')
# Привести к категориальному типу
melb_df['Suburb'] = melb_df['Suburb'].astype('category')

print(melb_df.info())
# Делим байты на количество мегабайт в байте
memory_after = melb_df.memory_usage(index=True).sum() / 1048576
memory_diff = memory_before - memory_after
print(round(memory_diff, 1))

print('_' * 40)
print('_' * 40)
# --- Базовые приемы работы в pandas (практика) ---
# Датасет представляет собой таблицу с информацией о 300 тысячах поездок за первые пять дней сентября 2018 года 
# и включает в себя следующую информацию:

# starttime — время начала поездки (дата, время);
# stoptime — время окончания поездки (дата, время);
# start station id — идентификатор стартовой стоянки;
# start station name — название стартовой стоянки;
# start station latitude, start station longitude — географическая широта и долгота стартовой стоянки;
# end station id — идентификатор конечной стоянки;
# end station name — название конечной стоянки;
# end station latitude, end station longitude — географическая широта и долгота конечной стоянки;
# bikeid — идентификатор велосипеда;
# usertype — тип пользователя (Customer — клиент с подпиской на 24 часа или на три дня, Subscriber — подписчик с годовой арендой велосипеда);
# birth year — год рождения клиента;
# gender — пол клиента (0 — неизвестный, 1 — мужчина, 2 — женщина).

import pandas as pd
# Изначальный импорт
citi_bike_data = pd.read_csv('data/citibike-tripdata.csv', sep=',')
# Копирую таблицу
citibike_df = citi_bike_data.copy()
print(citibike_df.head())

print('_' * 40)
# Задание 6.1
# Сколько пропусков в столбце start station id?
print(citibike_df['start station id'].isnull().sum())

print('_' * 40)
# Задание 6.2
# 1 point possible (graded)
# Какой тип данных имеют столбцы starttime и stoptime?
print(citibike_df['starttime'], citibike_df['stoptime'])

print('_' * 40)
# Задание 6.3
# Найдите идентификатор самой популярной стартовой стоянки. Запишите идентификатор в виде целого числа.
print(citibike_df['start station id'].mode())

print('_' * 40)
# Задание 6.4
# Велосипед с каким идентификатором является самым популярным?
print(citibike_df['bikeid'].mode())

print('_' * 40)
# Задание 6.5
# Какой тип клиентов (столбец usertype) является преобладающим — Subscriber или Customer?
# В качестве ответа запишите долю клиентов преобладающего типа среди общего количества клиентов. Ответ округлите до сотых.
subscriber = citibike_df[citibike_df['usertype'] == 'Subscriber']['usertype'].count()
customer = citibike_df[citibike_df['usertype'] == 'Customer']['usertype'].count()

user_type = subscriber if subscriber > customer else customer
print(round(user_type/len(citibike_df['usertype']), 2))

print('_' * 40)
# Задание 6.6
# Кто больше занимается велоспортом — мужчины или женщины? 
# В ответ запишите число поездок для той группы, у которой их больше.
men = citibike_df[citibike_df['gender'] == 1]['gender'].count()
woman = citibike_df[citibike_df['gender'] == 2]['gender'].count()
gender_count = men if men > woman else woman
print(gender_count)

print('_' * 40)
# Задание 6.7
print(citibike_df.describe())
print(citibike_df.describe(include=['object']))
print(citibike_df['start station name'].mode())

print('_' * 40)
# Задание 6.8
# В первую очередь удалим лишнюю информацию из данных.
# В наших данных присутствуют столбцы, которые дублируют информацию друг о друге: это столбцы с идентификатором и 
# названием стартовой и конечной стоянки. Удалите признаки идентификаторов стоянок. Сколько столбцов осталось?
#pd.set_option('display.max_columns', None)
print(citibike_df.head())
citibike_df = citibike_df.drop(['start station id', 'end station id'], axis=1)
print(citibike_df.head())

print('_' * 40)
# Задание 6.9
# Замените признак birth year на более понятный признак возраста клиента age. Годом отсчёта возраста выберите 2018 год. 
# Столбец birth year удалите из таблицы. Сколько поездок совершено клиентами старше 60 лет?
citibike_df['age'] = 2018 - citibike_df['birth year']
print(len(citibike_df[citibike_df['age'] > 60]))
citibike_df = citibike_df.drop(['birth year'], axis=1)

print('_' * 40)
# Задание 6.10
# Создайте признак длительности поездки trip duration. Для этого вычислите интервал времени между временем окончания 
# поездки (stoptime) и её началом (starttime). Сколько целых минут длилась поездка под индексом 3 в таблице?
citibike_df['starttime'] = pd.to_datetime(citibike_df['starttime'])
citibike_df['stoptime'] = pd.to_datetime(citibike_df['stoptime'])

print(citibike_df.info())
citibike_df['trip duration'] = citibike_df['stoptime']-citibike_df['starttime']
print(citibike_df['trip duration'].iloc[[3]])

print('_' * 40)
# Задание 6.11
# Создайте «признак-мигалку» weekend, который равен 1, если поездка начиналась в выходной день (суббота или воскресенье), 
# и 0 — в противном случае. Выясните, сколько поездок начиналось в выходные.
def get_weekend(weekday):
    weekend = [5, 6]
    if weekday in weekend:
        return 1
    else:
        return 0
day_of_week = citibike_df['starttime'].dt.day_of_week
print(day_of_week)
citibike_df['weekend'] = day_of_week.apply(get_weekend)
print(citibike_df[citibike_df['weekend'] == 1].shape[0])

print('_' * 40)
# Задание 6.12
# Создайте признак времени суток поездки time_of_day. Время суток будем определять из часа начала поездки. Условимся, что:
# поездка совершается ночью (night), если её час приходится на интервал от 0 (включительно) до 6 (включительно) часов;
# поездка совершается утром (morning), если её час приходится на интервал от 6 (не включительно) до 12 (включительно) часов;
# поездка совершается днём (day), если её час приходится на интервал от 12 (не включительно) до 18 (включительно) часов;
# поездка совершается вечером (evening), если её час приходится на интервал от 18 (не включительно) до 23 часов (включительно).
# Во сколько раз количество поездок, совершённых днём, больше, чем количество поездок, совёршенных ночью, за представленный в 
# данных период времени? Ответ округлите до целых.
def get_time_of_day(startime):
    if 0 <= startime <= 6: return 'night'
    if 6 < startime <= 12: return 'morning'
    if 12 < startime <= 18: return 'day'
    if 18 < startime <= 23: return 'evening'

starttime = citibike_df['starttime'].dt.hour
print(starttime)
citibike_df['time_of_day'] = starttime.apply(get_time_of_day)
print(citibike_df['time_of_day'])
day_rides = citibike_df[citibike_df['time_of_day'] == 'day']['time_of_day'].shape[0]
night_rides = citibike_df[citibike_df['time_of_day'] == 'night']['time_of_day'].shape[0]
print(round(day_rides/night_rides))