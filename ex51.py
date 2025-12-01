primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = primeiro_termo + (10 - 1) * razao
for i in range (primeiro_termo, decimo + razao, razao):
    print(i)
