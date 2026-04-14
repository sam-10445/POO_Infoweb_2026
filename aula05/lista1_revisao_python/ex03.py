print('Digite uma frase: ')
x = input()
soma = 0
for letra in x:
    if letra >= '0' and letra <= '9':
        soma = soma + int(letra)
print(soma)