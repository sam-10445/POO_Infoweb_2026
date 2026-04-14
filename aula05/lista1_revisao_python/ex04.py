print('Digite uma sequência de números separados por vírgula: ')
x = input()
soma = 0
numeros = x.split(',')
for y in numeros:
    soma = soma + int(y)
print(f'Soma = {soma}')