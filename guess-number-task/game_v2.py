"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int, interval: tuple) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число.
        interval (tuple): Интервал в котором происходит поиск числа
    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(
            interval[0], interval[1]+1)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def binary_search(number: int, interval: tuple) -> int:
    """Угадывание производится посредством бинарного поиска. На каждой итерации находим середину 
    сравниваем с загаданным числом, в случае несовпадения произвозводим поиск в новом диапазоне

    Args:
        number (int): Загаданое число 
        interval (tuple): Интервал в котором происходит поиск числа

    Returns:
        int: Число попыток
    """
    interval_middle = (interval[0]+interval[1])//2
    # выход из рекурсии -- равенство загаданого числа границам интервала или его середине
    if interval[0] == number or interval[1] == number or interval_middle == number:
        return 1
    else:
        # иначе выбираем ту половину интервала в которой находится число
        if interval_middle > number:
            return 1 + binary_search(number, (interval[0], interval_middle))
        else:
            return 1 + binary_search(number, (interval_middle, interval[1]))


def fibon_search(number: int, interval: tuple) -> int:
    """Угадывание производится посредством фибоначиева поиска.
    В интервале будем проходить по числам фибоначи

    Args:
        umber (int): Загаданое число 
        interval (tuple): Интервал в котором происходит поиск числа

    Returns:
        int: Число попыток
    """

    fib_numbers = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 99)
    count = 0

    previous = 0

    if interval[0] == number or interval[1] == number:
        return 1
    for i in fib_numbers:
        count += 1
        if interval[0] + i == number:
            return count
        elif interval[0] + i > number:
            # получаем новый интервал от предыщего числа фибоначи до текущего
            return count + fibon_search(number, (interval[0] + previous, interval[0] + i))
        previous = i


def score_game(func_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        func_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func_predict(number, (1, 100)))

    score = int(np.mean(count_ls))
    if 1 < score % 10 < 4:
        str_end = "ки"
    elif score % 10 == 1:
        str_end = "ку"
    else:
        str_end = "ок"
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыт{str_end}")
    return score


if __name__ == "__main__":

    # RUN
    score_game(binary_search)
