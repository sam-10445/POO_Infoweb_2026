soma_pares = 0
soma_impar = 0
print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 == 0: #par
    soma_pares += a
else:
    soma_impar += a

if b % 2 == 0: #par
    soma_pares += b
else:
    soma_impar += b

if c % 2 == 0: #par
    soma_pares += c
else:
    soma_impar += c

if d % 2 == 0: #par
    soma_pares += d
else:
    soma_impar += d

print("Soma dos pares =",soma_pares)
print('Soma dos ímpares =',soma_impar)