class Dumper():
    def __init__(self, acrhive_dir='Archive/'):
        self.archive_dir = acrhive_dir

    def dump(self, data):
        # Библиотека pickle позволяет доставать и класть объекты в файл
        with open(file=self.get_file_name(), mode='wb') as file:
            pic.dump(data, file)
    
    def load_for_day(self, day):
        file_name = path.join(self.archive_dir, day + '.pkl')
        # Оператор with это аналог using {} в C# где гарантируется, что контекст будет потом удален (для оптимизации памяти)
        with open(file_name, 'rb') as file:
            sets = pic.load(file)
        return sets
    
    # возвращает корректное имя для файла (делаем нейминг файла [название]+[сегодняшняя дата].pkl)
    def get_file_name(self):
        today = datetime.now().strftime("%y-%m-%d")
        return path.join(self.archive_dir, today + '.pkl')

# Пример использования  
data = {
    'perfomance': [10, 20, 10],  
    'clients': {"Romashka": 10, "Vector": 34}  
}