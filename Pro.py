
import math

def prime_factors(num):     #   функция выводит каноническое разложение числа на простые множители
    while num % 2 == 0:
        print(2,)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i,)
            num = num / i
    if num > 2:
        print(num)


def gsd_1(a,b):             #   функция выводит самый большой делитель
    print(math.gcd(a,b))