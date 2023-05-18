a = int(input('Введите число: '))

def smallest_divisor(a):
    divisor = 2
    while divisor <= a:
        if a % divisor == 0:
            return divisor
        divisor += 1

res = smallest_divisor(a)
print('\nНаименьший делитель, больше 1:',res)