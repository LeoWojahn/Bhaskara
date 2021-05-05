def itens(lista):
    print('----------------------------------------------< MENU >----------------------------------------------')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-----------------------------------------< DIGITE A OPÇÃO >-----------------------------------------')
    

def linha():
    print('------------------------------------------< COEFICIENTES >------------------------------------------')
    
    
def linha2():
    print('----------------------------------------------------------------------------------------------------')


def somar():
    a = int(input('Coeficiente A: '))
    b = int(input('Coeficiente B: '))
    c = int(input('Coeficiente C: '))

    print('--------------------------------------------< RESPOSTA >--------------------------------------------')

    delta = (b ** 2) - 4 * a * c
    print(f'Δ = {delta}')

    if delta < 0:
        print('Número negativo, não há como continuar!')

    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        print(f'x1 = {int(x1)}')
        print(f'x2 = {int(x2)}')