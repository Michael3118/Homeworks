import logging
import time
from logging import StreamHandler


def custom_decorator(log_file=None, log_level=logging.INFO, validate_args=None, do_before=None, do_after=None,
                     handle_error=None):
    def decorator(func):
        # Ініціалізація logging з використанням StreamHandler для виводу в консоль
        logging.basicConfig(level=log_level)
        console_handler = StreamHandler()
        logging.getLogger().addHandler(console_handler)

        if log_file:
            # Ініціалізація файлу для логування, якщо вказано log_file
            handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logging.getLogger().addHandler(handler)

        def wrapper(*args, **kwargs):
            # Валідація аргументів, якщо задано
            if validate_args:
                if not all(validate_args(arg) for arg in args):
                    logging.error("Invalid arguments.")
                    return None

            # Виконання дій до виклику функції, якщо задано
            if do_before:
                do_before()

            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                logging.info(f"Час виконання функції: {execution_time} секунд")

                # Виконання дій після виклику функції, якщо задано
                if do_after:
                    do_after()

                return result
            except Exception as e:
                # Обробка помилок, якщо задано
                logging.error(f"Помилка: {str(e)}")
                if handle_error:
                    handle_error(e)
                return None

        return wrapper

    return decorator

@custom_decorator(log_file="example.log")
def divide_and_log(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    result = a / b
    return result

# Виклик функції
result = divide_and_log(10, 2)
