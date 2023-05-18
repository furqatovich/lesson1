a = int(input("Введите первый год: "))
b = int(input("Введите второй год: "))

# Проверка каждого четырехзначного числа в интервале от a до b на наличие ровно трех одинаковых цифр
print("Годы от", a, "до", b, "с тремя одинаковыми цифрами:")
for year in range(a, b+1):
    digits = [int(digit) for digit in str(year)] # Разбиение числа на цифры
    if digits.count(digits[0]) == 3 or digits.count(digits[1]) == 3 or digits.count(digits[2]) == 3 or digits.count(digits[3]) == 3:
        print(year)