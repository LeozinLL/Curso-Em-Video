from datetime import date
atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
  print('A classificação é MIRIM')
elif idade <= 14:
  print('A classificação é INFANTIL')
elif idade <= 19:
  print('A classificação é JUNIOR')
elif idade <= 25:
  print('A classificação é SÊNIOR')
elif idade > 25:
  print('A classificação é MASTER')
  