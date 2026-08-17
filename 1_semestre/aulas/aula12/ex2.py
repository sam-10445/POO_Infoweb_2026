'''from datetime import datetime
s = input("Informe sua data de nascimento (dd/mm/aaaa): ")
print(s)

d, m, a = s.split('/')
d = int(d)
m = int(m)
a = int(a)
print(d)
print(m)
print(a)
data = datetime(a, m, d)
print(data)
print(data.strftime("%d/%m/%Y")) #strftime - passa uma data para string'''

#FORMA MAIS EFICIENTE
from datetime import datetime
s = input("Informe sua data de nascimento (dd/mm/aaaa): ")
data = datetime.strptime(s, "%d/%m/%Y")
print(data)
print(data.strftime("%d/%m/%Y")) #strftime - passa uma data para string

# strptime - passa uma string para datetime
# strftime - passo uma datetime para string

x = int(input('Informe um número: ')) #pedi um número
# pedi uma data
d = datetime.strptime(input('Informe uma data: '), "%d/%m/%Y" )

hoje = datetime.now()
nasc = datetime.strptime(input(''), "%d/%m/%Y")

d = hoje - nasc
print(d)

anos = d.days // 365
meses = d.days % 365 // 30
print(anos, 'anos')
print(meses, 'meses')