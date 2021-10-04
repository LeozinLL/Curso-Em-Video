peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
  print('Você está ABAIXO do peso normal.')
elif 18.5 <= imc < 25:
  print('Você está com o peso ideal.')
elif 25 <= imc < 30:
  print('Você está ACIMA do peso.')
elif 30 <= imc < 40:
  print('Você está OBESO, cuidado.')
elif imc >= 40:
  print('Você está com OBESIDADE MÓRBIDA, MUITO CUIDADO!!!')
