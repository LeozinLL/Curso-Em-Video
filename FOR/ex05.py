soma = 0
cont = 0
for x in range(1, 7):
  num = int(input('Digite o {} valor: '.format(x)))
  if num % 2 == 0:
    cont += 1
    soma += num
print()
print('Você informou {} número(s) PARES e a soma deles foi: {}'.format(cont, soma))
