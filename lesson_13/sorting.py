"""
Здравствуйте, Сергей Игоревич!

1 курс я не проходил, поэтому, просто написал пузырьковую сортировку.
"""


# Пузырьковая сортировка
def bubble_sort(x):
    N = len(x)
    for i in range(0, N - 1):
        for j in range(0, N - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
