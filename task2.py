# import random

# equel = int(input('Количество решении: '))

# for i in range(equel):
#     a = random.randint(1, 10)
#     num = random.randint(1, 50)
#     print(num,'*',a,'= ?')
#     answer = int(input('Введите ответ: '))
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def number_of_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

n = int(input("Введите число: "))
sum = sum_of_digits(n)
count = number_of_digits(n)
difference = sum - count
print("Сумма чисел:", sum)
print("Количество цифр в числе:", count)
print("Разность суммы и количества цифр:", difference)

 

