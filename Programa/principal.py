from biblioteca.funções import *
from time import sleep

while True:
    itens(['Calcular Bhaskara', 'Sair do Programa'])

    resp = str(input('Opção: '))

    if resp == '1':
        linha()
        somar()

    elif resp == '2':
        linha2()
        print('Até Mais!')
        sleep(1)
        break

    else:
        print('============================'.center(100))
        print('| DIGITE UMA OPÇÃO VÁLIDA! |'.center(100))
        print('============================'.center(100))
        print('')