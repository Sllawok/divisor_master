import math

def div_master(a):         #  нахождение простого числа
    a = int(input("Введите число от 1 до 1000 : "))
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
            if (k <= 0):
                print("Число простое")
        else:
            print("Число не является простым")



def dividers(n):           #   выводит список всех делителей числа
    r=[1,n]
    i=2
    while(i*i<=n):
        if n%i==0:
            r=r+[i]
            k=n//i
            if k != i:
                 r=r+[k]
        i+=1
    return r

print(dividers(300))


def issimple(a):               #  выводит самый большой простой делитель числа
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(600851475143)
print(max(r))
