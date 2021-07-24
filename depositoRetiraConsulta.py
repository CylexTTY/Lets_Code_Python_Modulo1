'''
Faça um programa para simular uma situação simples de depósito,
retirada e consulta em um banco. Exiba o seguinte menu com as opções:

1 - Depósito
2 - Retirada
3 - Saldo
4 - Sair do algoritmo
Se a escolha do usuário for depósito ou retirada, o algoritmo deverá pedir
o valor da operação e atualizar automaticamente o valor existente na conta.
O algoritmo deverá ser utilizado até que o usuário escolha a opção sair
do algoritmo.
'''
menu = {1: 'DEPOSITO', 2: 'RETIRADA', 3: 'SALDO', 4: 'SAIR'}
opt = 0
contaBancaria = 0
while opt != 4:
    for numero, nome in menu.items():
        print(f'{numero} - {nome}', end=' | ')
    try:
        opt = input('\nOpcao: ').upper().strip()
    except:
        print(f'Por favor escreva um numero de 1 a {len(menu)}')
    else:
        try:
            for k, v in menu.items():
                if str(k) == opt or v == opt:
                    opt = k
            print(menu[opt])
        except:
            print('Por favor, escolha um numero valido!')
        else:
            if opt == 4:
                print('Obrigado volte sempre')
            elif opt == 1:
                contaBancaria += float(input('Valor a depositar: R$'))
                print('Deposito efetuado com sucesso!')
            elif opt == 2:
                valorSacado = float(input('Valor a ser sacado: R$'))
                while valorSacado > contaBancaria or valorSacado < 0:
                    print(f'Desculpe, você pode sacar até R${contaBancaria}')
                    valorSacado = float(input('Valor a ser sacado: R$'))
                contaBancaria -= valorSacado
                print('Saque Realizado com sucesso!')
            else:
                print(f'Saldo em conta:\nR${contaBancaria:.2f}')

