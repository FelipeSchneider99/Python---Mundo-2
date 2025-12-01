from random import randint
from time import sleep
contador_palpite = 0
resposta = 0
numero_computador = randint(1, 10)
print('Vou pensar em um numero de 1 a 10, tente adivinhar!!')
print('-='*20)
while resposta != numero_computador:
    resposta = int(input('Digite um numero de 1 a 10: '))
    if resposta == numero_computador:
        print('!!!')
        sleep(0.3)
        print('O QUE?!?!')
        sleep(0.3)
        print('VOCE ACERTOU!!')
        sleep(0.3)
        contador_palpite += 1
    elif resposta == numero_computador + 1 or resposta == numero_computador -1:
        print('EHH... VOCE ERROU..!!! HAHA')
        contador_palpite += 1
    else:
        print('ERROU!! TENTE NOVAMENTE HAHAHA')
        contador_palpite += 1
    print('--' * 20)
print('-='*20)
print(f'Voce acertou em {contador_palpite} palpites')
