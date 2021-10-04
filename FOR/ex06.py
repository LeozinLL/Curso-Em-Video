first = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print()
dec = first + (10 - 1) * razão
for x in range(first, dec + razão, razão):
  print('{} '.format(x))
print()
print('ACABOU!')
