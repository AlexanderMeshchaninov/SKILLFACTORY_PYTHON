import pandas as pd
import numpy as np

print('_' * 40)
# Данные о заболеваемости коронавирусной инфекцией
covid_data = pd.read_csv('data/covid_data.csv', sep=',')

# Мы будем работать со следующими столбцами:

# date — дата наблюдения;
# province/state — наименование провинции/штата;
# country — наименование страны;
# confirmed — общее число зафиксированных случаев на указанный день;
# deaths — общее число зафиксированных смертей на указанный день;
# recovered — общее число выздоровлений на указанный день.

mask = covid_data['country'] == 'United States'
#print(covid_data.head(100))
print(covid_data[mask])

print('_' * 40)
# Данные о процессе вакцинирования людей
vaccinations_data = pd.read_csv('data/country_vaccinations.csv', sep=',')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]

# Данная таблица содержит следующие столбцы:

# country — наименование страны;
# date — дата наблюдения;
# total_vaccinations — общее число введённых вакцин в стране на указанный день;
# people_vaccinated — общее число привитых первым компонентом в стране на указанный день;
# people_vaccinated_per_hundred — процент привитых первым компонентом в стране на указанный день (рассчитывается как );
# people_fully_vaccinated — общее число привитых вторым компонентом в стране на указанный день (первый компонент уже был введён им ранее);
# people_fully_vaccinated_per_hundred — процент привитых вторым компонентом в стране на указанный день (рассчитывается как );
# daily_vaccination — ежедневная вакцинация (число вакцинированных в указанный день);
# vaccines — комбинации вакцин, используемые в стране.

# print(vaccinations_data.head(10))

mask = vaccinations_data['country'] == 'United States'
#print(covid_data.head(100))
print(vaccinations_data[mask])

# Обратите внимание, что признаки confirmed, deaths, recovered, total_vaccination, people_vaccinated, people_fully_vaccinated 
# — это суммарные показатели по стране, то есть с каждым днём они должны расти. Такие признаки называют накопительными.

# Возникает большое желание объединить таблицы. Для этого необходимо учитывать следующие нюансы:
# 1. В таблице covid_data необходимо предварительно рассчитать суммарное ежедневное число 
# заболевших во всех провинциях/штатах в каждой стране.
# 2. В таблицах не совпадает число стран, а иногда и их названия. 
# При объединении таблиц по столбцу мы определённо теряем данные (в данной задаче потери незначительны). 
# Избежать этого можно ручными преобразованиями данных — искать различия в названиях стран в таблицах и преобразовывать их. 
# Однако это не является темой данного модуля.
# 3. Таблицы имеют разные периоды наблюдений (вакцины появились позже, чем сам вирус). 
# Объединив данные с типом inner, мы можем потерять большое количество наблюдений в таблице covid_data.

print('_' * 40)
# --- Предобработка данных ---
# Опираясь на замечания выше, выполним небольшую предобработку.
# В таблице covid_data:

# 1. Группируем таблицу по дате и названию страны и рассчитываем суммарные показатели по всем регионам. 
# Тем самым переходим от данных по регионам к данным по странам:
covid_data = covid_data.groupby(['date', 'country'], as_index=False)[['confirmed', 'deaths', 'recovered']].sum()

# 2. Преобразуем даты в формат datetime с помощью функции pd.to_datetime():
covid_data['date'] = pd.to_datetime(covid_data['date'])

# 3. Создадим признак больных на данный момент (active). Для этого вычтем из общего числа зафиксированных 
# случаев число смертей и число выздоровевших пациентов:
covid_data['active'] = covid_data['confirmed'] - covid_data['deaths']
print(covid_data)

# 4. Создадим признак ежедневного прироста числа заболевших, умерших и выздоровевших людей. 
# Для этого отсортируем данные по названиям стран, а затем по датам. После этого произведём 
# группировку по странам и рассчитаем разницу между «вчера и сегодня» с помощью метода diff():
covid_data = covid_data.sort_values(['country', 'date'])
covid_data['daily_confirmed'] = covid_data.groupby('country')[['confirmed']].diff()
covid_data['daily_deaths'] = covid_data.groupby('country')[['deaths']].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')[['recovered']].diff()

print(covid_data)

# В таблице vaccinations_data:

# 1. Преобразовать столбец date в формат datetime
vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])

print(covid_data.info())
print(vaccinations_data.info())

print('_' * 40)
# Задание 3.1
# За какой период представлены данные в таблице covid_data? В качестве ответа введите даты 
# в формате datetime (без указания времени).
print(covid_data['date'].min())
print(covid_data['date'].max())

print('_' * 40)
# Задание 3.2
# За какой период представлены данные в таблице vaccinations_data? В качестве ответа введите даты 
# в формате datetime без указания времени.
print(vaccinations_data['date'].min())
print(vaccinations_data['date'].max())

print('_' * 40)
# Задание 3.3
# С помощью метода merge() объедините таблицы covid_data и vaccinations_data по столбцам date и country.
# Тип объединения выставьте так, чтобы в результирующую таблицу попали только наблюдения за период, 
# вычисленный в задании 3.1. То есть в результирующую таблицу должны попасть все записи из таблицы 
# covid_data и из её пересечения с vaccinations_data, но не более. Результат объединения занесите в переменную covid_df.

# Сколько строк и столбцов в таблице covid_df?
# Введите ответ в виде двух чисел через дефис (например, 333-33): первое число — количество строк, второе число — количество столбцов.
# --- Объединение таблицы ---
covid_df = covid_data.merge(
    vaccinations_data,
    left_on=['date', 'country'],
    right_on=['date', 'country'],
    how='left'
)
mask = covid_df['country'] == 'United States'
print(covid_df)

covid_df.to_csv('data/covid_df.csv', sep=',')

# В получившейся в задании 3.3 таблице covid_df создайте признаки death_rate — общий процент смертей 
# среди зафиксированных случаев (летальность) и recover_rate — общий процент случаев выздоровления. 
# Данные характеристики рассчитайте как отношение числа смертей (deaths) и числа выздоровлений (recovered) 
# к числу зафиксированных случаев (confirmed) и умножьте результаты на 100%.
covid_df['death_rate'] = covid_df['deaths'] / covid_df['confirmed']*100
covid_df['recover_rate'] = covid_df['recovered'] / covid_df['confirmed']*100

print('_' * 40)
# Задание 3.4
# Какова максимальная летальность в США (United States) за весь период? Ответ округлите до второго знака после запятой.
mask_us = covid_df['country'] == 'United States'
max_death_rate_us = covid_df[mask_us][['death_rate']].max()
print(round(max_death_rate_us, 2))

print('_' * 40)
# Задание 3.5
# Чему равен средний процент выздоровевших в России (Russia)? Ответ округлите до второго знака после запятой.
mask_rus = covid_df['country'] == 'Russia'
mean_recover_rate_rus = covid_df[mask_rus][['recover_rate']].mean()
print(round(mean_recover_rate_rus, 2))

print('_' * 40)
import matplotlib.pyplot as plt
import pandas as pd

# # Используем объединенный дата-сет covid и vaccination - covid_df
# covid_data = pd.read_csv('data/covid_data.csv', sep=',')
# vaccinations_data = pd.read_csv('data/country_vaccinations.csv', sep=',')

# covid_df = covid_data.merge(
#     vaccinations_data,
#     left_on=['date', 'country'],
#     right_on=['date', 'country'],
#     how='left'
# )

grouped_cases = covid_df.groupby('date')[['daily_confirmed']].sum()
grouped_cases.plot(
    kind='line',
    figsize=(12, 4),
    title='Ежедневная заболеваемость по всем странам',
    grid=True,
    lw=3
)

print('_' * 40)