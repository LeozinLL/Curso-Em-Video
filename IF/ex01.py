casa = float(input('Qual é o valor da casa?: '))
s = float(input('Quanto é o salário do comprador?: '))
anos = int(input('Em quantos anos deseja pagar o imóvel?: '))
prest = casa / (anos * 12)
min = s * 0.3 
print('Para pagar uma casa de {:.2f}R$ em {} anos, a prestação será de {:.2f}R$'.format(casa, anos, prest))
if prest <= min:
  print('Empréstimo pode ser CONCEDIDO!')
else:
  print('Empréstimo NEGADO!')
