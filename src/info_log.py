import json
import logging

logger = logging.getLogger('info_logs')  # Создаем логгер с именем 'masks'
logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования INFO
# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('logs/info_logs.log', encoding="utf-8")
# Настраиваем формат записей в логе
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
file_handler.setFormatter(file_formatter)  # Применяем форматтер к обработчику
logger.addHandler(file_handler)  # Добавляем обработчик к логгеру


def logs_info_ti_file(data, file_patch):
    try:
        logger.info(f'Записываем данные в файл {file_patch}')
        with open(file_patch, "w") as data_file:
            json.dump(data, data_file)
    except Exception as ex:
        logger.error((f'Произошла ошибка: {ex}'))
