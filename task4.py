def search(x, y, r):
  coinDistance = x ** 2 + y ** 2
  radius = r ** 2

  if coinDistance <= radius:
    print('Монета где-то здесь!')
  else:
    print('Монета не находится поблизости!')

  return 

  
x = float(input('Введите точку икс монеты: '))
y = float(input('Введите точку игрик монеты: '))
r = float(input('Введите радиус поиска: '))

search(x, y, r)