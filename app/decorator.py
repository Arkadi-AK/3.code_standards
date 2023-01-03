"""Decorator with parameters"""
import time


def repeater(call_count, start_sleep_time, factor, border_sleep_time):
    """Decorator repeater"""

    def outer(fnc):
        def inner():
            if call_count == 0:
                return print("Запусков не будет")
            print(f"Кол-во запусков = {call_count}")
            print("Начало работы")
            for number in range(call_count):
                timer = start_sleep_time * factor ** number
                timer = min(timer, border_sleep_time)
                print(f"Запуск номер {number + 1}Ожидание: {timer} секунд.", end=" ")
                time.sleep(timer)
                func_result = fnc()
                print(f"Результат декорируемой функций = {func_result}.")
            print("Конец работы")
            return None

        return inner

    return outer


@repeater(call_count=4, start_sleep_time=1, factor=2, border_sleep_time=55)
def func():
    """The function that the decorator should use"""
    return "Hello, admin"


if __name__ == "__main__":
    func()
