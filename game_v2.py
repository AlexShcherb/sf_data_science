import numpy as np


def random_predict(number: int = 1) -> int:
    """Try to guess a number

    Args:
        number (int, optional): Number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return (count)


def score_game(random_predict) -> int:
    """What is the avr number of attempts needed to guess a number (1000 runs)

    Args:
        random_predict (_type_): guess function

    Returns:
        int: avr number of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(
        f"Algorithm in average guess the correct number in range of 1 to 100 in {score} attempts")


if __name__ == '__main__':
    score_game(random_predict)