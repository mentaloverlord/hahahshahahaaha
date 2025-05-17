import random


def generate_random_number(min_value: int, max_value: int) -> int:
    """
    Генерирует случайное число в указанном диапазоне.

    :param min_value: Минимальное значение (включительно).
    :param max_value: Максимальное значение (включительно).
    :return: Случайное число.
    """
    if min_value > max_value:
        raise ValueError("Минимальное значение не может быть больше максимального.")

    return random.randint(min_value, max_value)