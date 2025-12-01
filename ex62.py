print('PROGRESSÃO ARITMETICA COM ADIÇÃO DE LIMITE')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
limite = 10

termo_atual = primeiro_termo
cont = 1
while cont <= limite:
    print(termo_atual)
    termo_atual += razao
    cont += 1
    if cont == limite:
        adicional = int(input('Deseja adicionar mais quantos termos? Digite [0] para encerrar: '))
        if adicional == 0:
            print('Encerrando o programa...')
            break
        else:
            limite = limite + adicional
