import math


def read_number(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Ошибка: введите число.")


def fmt(x):
    x = round(x, 10) + 0.0
    return str(int(x)) if x.is_integer() else str(x)


print("Решение уравнения a*x^2 + b*x + c = 0")
a = read_number("Введите a: ")
b = read_number("Введите b: ")
c = read_number("Введите c: ")

if a == 0:
  
    if b == 0:
        if c == 0:
            print("Бесконечно много решений (x — любое число).")
        else:
            print("Решений нет.")
    else:
        print("Уравнение линейное. Корень: x =", fmt(-c / b))
else:
    d = b * b - 4 * a * c
    print("Дискриминант D =", fmt(d))
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Два действительных корня: x1 =", fmt(x1), ", x2 =", fmt(x2))
    elif d == 0:
        print("Один корень (два совпадающих): x =", fmt(-b / (2 * a)))
    else:
        re = -b / (2 * a)
        im = math.sqrt(-d) / (2 * abs(a))
        print("Действительных корней нет. Комплексные корни:")
        print("x1 =", fmt(re), "+", fmt(im), "i")
        print("x2 =", fmt(re), "-", fmt(im), "i")
