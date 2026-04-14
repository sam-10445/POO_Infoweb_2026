#s = input("Digite uma frase:")
print("Digite uma frase:")
s = input()
palavras = s.split()
for x in palavras:
    x = x[::-1]
    print(x) #print(x[::-1]) -> pra substituir