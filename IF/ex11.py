from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(1, 3) - 1
print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
print()
jogador = int(input('Qual é a sua jogada? ')) - 1
print()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print()
print('=-' * 12)
print()
print('Jogador jogou: {}'.format(itens[jogador]))
print('Computador jogou: {}'.format(itens[computador]))
print()
print('=-' * 12)
if computador == 1:
  if jogador == 1:
      print('EMPATE!')
  elif jogador == 2:
      print('JOGADOR VENCEU!')
  elif jogador == 3:
      print('COMPUTADOR VENCEU!')
  else:
      print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 1:
      print('COMPUTADOR VENCEU!')
    elif jogador == 2:
      print('EMPATE!')
    elif jogador == 3:
      print('JOGADOR VENCEU!')
    else:
      print('JOGADA INVÁLIDA!')
elif computador == 3:
    if jogador == 1:
      print('JOGADOR VENCEU!')
    elif jogador == 2:
      print('COMPUTADOR VENCEU!')
    elif jogador == 3:
      print('EMPATE!')
    else:
      print('JOGADA INVÁLIDA!')
