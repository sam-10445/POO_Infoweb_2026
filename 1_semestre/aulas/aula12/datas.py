from datetime import datetime

x = datetime(2026, 5, 20, 15, 30, 10)
print(x)
y = datetime(2000, 1, 5)
print(y)

print(x.day) #pega o dia
print(x.month) #pega o mês
print(x.year) #pega o ano
print(x.hour) #pega o hora
print(x.minute) #pega o minutos
print(x.second) #pega o segundos
print(x.microsecond) #pega o milhonessimo segundo

#COM O FUSO HORÁRIO ZERO
z = datetime.now() #pega a hora atual
print(z)

#COM O FUSO HORÁRIO AJUSTADO (-3 - Brasil)
z = datetime.now(ZoneInfo("America/Sao_Paulo"))