from biblioteca.funções import *
from time import sleep

while True:
    itens(['Calcular Bhaskara', 'Sair do Programa'])

    resp = str(input('Opção: '))

    if resp == '1':
        print('Hey')

    elif resp == '2':
        print('Até Mais!')
        sleep(1)
        break

    else:
        print('DIGITE UMA OPÇÃO VÁLIDA!')