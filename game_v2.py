"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    pred_min = 1
    pred_max = 101
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    number = 0
    while True:
        count += 1
        number = (pred_min+pred_max)//2
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > number:
            pred_min = number
        else:
            pred_max = number
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости задачи
    values = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in values:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм '{predict.__name__}' угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
