"""Guess the number"""
import numpy as np
number = np.random.randint(1, 101)   # Come up with a number

# number of attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100: "))

    if predict_number > number:
        print("The number should be smaller")
    elif predict_number < number:
        print("The number should be bigger")
    else:
        print(
            f"You were right! The number is {number}. You have spent {count} attempts!")
        break
