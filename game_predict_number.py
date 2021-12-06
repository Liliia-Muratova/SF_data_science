import numpy as np
from numpy import random

def game_predict_number(number: int = 1) -> int:
    print(number)
    # счетчик попыток
    count = 0   
    # нижняя граница поиска числа
    left_number = 1  
    # верхняя граница поиска числа
    right_number = 101  
    
    while True:
        count+=1
        
        mid_number = ((right_number + left_number) // 2)

        if mid_number == number:
            return count
        
        
        if number > mid_number:
            # смещение нижней границы поиска числа
            left_number = mid_number  

        elif number < mid_number:
            # смещение верхней границы поиска числа
            right_number = mid_number  

        else:
            break

    return count

game_predict_number()

def score_game(game_predict_number) -> int:

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(game_predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
score_game(game_predict_number)