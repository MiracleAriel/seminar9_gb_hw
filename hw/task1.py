# Функция для нахождения корней квадратного уравнения

import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        return None


# Функция для генерации CSV файла с тремя случайными числами в каждой строке

import csv
import random

def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(row)


# Декоратор, который запускает функцию нахождения корней квадратного уравнения с каждой тройкой чисел из CSV файла:


def process_quadratic_roots(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                print(f"Equation: {a}x^2 + {b}x + {c} = 0")
                if roots is not None:
                    print(f"Roots: {roots[0]}, {roots[1]}")
                else:
                    print("No real roots")
                print()
    return wrapper
