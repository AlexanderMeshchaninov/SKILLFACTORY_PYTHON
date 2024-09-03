import os.path
import logging

# Функция для создания лог-файла и записи в него информации
def get_logger(path, file):
    """Создает лог-файл для логирования в него
    Args:
        path {string} -- путь к директории
        file {string} -- имя файла
    Returns:
        [obj] -- [логер]
    """
    # проверяем, существует ли файл
    log_file = os.path.join(path, file)
    
    #если  файла нет, создаем его
    if not os.path.isfile(log_file):
        open(log_file, 'w+', encoding='utf-8').close()

    # поменяем формат логирования
    logging_file_format = "%(levelname)s: %(asctime)s: %(message)s"
    
    # конфигурируем лог-файл
    logging.basicConfig(
        format=logging_file_format,
        level=logging.INFO
    )
    logger = logging.getLogger()
    
    # создадим хэнлдер для записи лога в файл
    handler = logging.FileHandler(log_file)
    
    # установим уровень логирования
    handler.setLevel(level=logging.INFO)
    
    # создадим формат логирования, используя file_logging_format
    formatter = logging.Formatter(logging_file_format)
    handler.setFormatter(formatter)
    
    # добавим хэндлер лог-файлу
    logger.addHandler(handler)
    return logger