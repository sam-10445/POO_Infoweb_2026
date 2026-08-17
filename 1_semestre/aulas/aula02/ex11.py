import math

#função não deve ter print nem input
def Diagonal(b, h):
    diagonal = math.sqrt(b*b + h*h)
    return diagonal

print("Informe o valor da base")
b = float(input())
print("Informe o valor da altura")
h = float(input())
diagonal = Diagonal(b, h)
print(f"Diagonal = {diagonal:.2f}")