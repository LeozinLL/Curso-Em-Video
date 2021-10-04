num = int(input('Digite um número para ver sua tabuada: '))
for x in range(1, 11):
  print('{} x {} = {}'.format(num, x, num * x))
  