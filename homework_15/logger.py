import logging


def operation_log(param, command, requirement):
    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
             'в строке {lineno:03d} функция "{funcName}()" ' \
             'в {created} секунд записала сообщение: {msg}'
    logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
    if command == '40_is_type':
        return logging.error(f'параметра "{param}" не является типом данных')
    elif command == '40_type':
        return logging.error(f'Тип параметра "{param}" не соответствует требуемому типу данных: {requirement}')
    elif command == '40_value':
        return logging.error(f'параметр "{param}" не может быть нулевым или иметь отрицательное значение')
