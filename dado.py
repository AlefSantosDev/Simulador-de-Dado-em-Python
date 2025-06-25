from random import randint

while True:
    input('Aperte qualquer tecla para rolar o dado: ')
    lado = randint(1, 6)

    if lado == 1:
        print('     ')
        print('  0  ')
        print('     ')
    elif lado == 2:
        print('0    ')
        print('     ')
        print('    0')
    elif lado == 3:
        print('0    ')
        print('  0  ')
        print('    0')
    elif lado == 4:
        print('0   0')
        print('     ')
        print('0   0')
    elif lado == 5:
        print('0   0')
        print('  0  ')
        print('0   0')
    elif lado == 6:
        print('0   0')
        print('0   0')
        print('0   0')

    denovo = input('Deseja jogar mais uma vez? (s/n): ').upper().strip()[0]
    if denovo.lower() not in 'sS':
        break
