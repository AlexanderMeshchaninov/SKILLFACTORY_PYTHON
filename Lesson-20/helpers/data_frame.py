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