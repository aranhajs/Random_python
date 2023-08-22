import random

def adivinhe(x):
    random_number= random.randint(1, x)
    adivinhe= 0
    while adivinhe !=random_number:
        adivinhe= int(input(f'Adivinhe o numero entre 1 e {x}: '))
        print('#'*40)
        if adivinhe < random_number:
            print('Desculpe, Você errou. Muito Baixo')
        elif adivinhe> random_number:
            print('Desculpe, Você errou. Muito Alto')
    print(f'Parabêns você acertou: {random_number}')

adivinhe(10)
