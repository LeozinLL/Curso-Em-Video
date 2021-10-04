from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
option = 0
while option != 5:
    print()
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    print()
    option = int(input('Qual é a sua opção? '))
    if option == 1:
        soma = n1 + n2
        print()
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif option == 2:
        prod = n1 * n2
        print()
        print('O produto entre {} e {} é {}'.format(n1, n2, prod))
    elif option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print()
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
    elif option == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif option == 5:
        print()
        sleep(1)
        print('FInalizando...')
        sleep(2)
    else:
        print()
        print('Opção inválida. Tente novamente!')
print()
print('Fim do programa. Volte sempre!')