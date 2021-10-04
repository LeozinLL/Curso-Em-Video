print('{:=^40}'.format(' LOJAS LEONARDO '))
preço = float(input('Preço das compras: R$ '))
print()
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção de pagamento? '))
if opção == 1:
  total = preço - (preço * 0.1)
elif opção == 2:
  total = preço - (preço * 0.05)
elif opção == 3:
  total = preço
  parcela = total / 2
  print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
  total = preço + (preço * 0.2)
  totparc = int(input('Quantas parcelas? '))
  parcela = total / totparc
  print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
  total = preço
  print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
print('Sua compra de {:.2f} reais vai custar {:.2f} no final.'.format(preço, total))
