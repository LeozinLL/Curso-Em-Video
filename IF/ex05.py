n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é: {:.1f}'.format(n1, n2, m))
if m >= 7:
  print('Aluno está APROVADO!')
elif 5 <= m <= 6.9:
  print('Aluno está de RECUPERAÇÃO!') 
elif m < 5:
  print('Aluno está REPROVADO!')
