print('PROGRESSAO ARITMETICA COM WHILE')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
limite = 10

termo_atual = primeiro_termo
contador = 1

while contador <= limite:
    print(termo_atual)
    termo_atual += razao
    contador += 1

