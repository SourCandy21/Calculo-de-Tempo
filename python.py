#Um programa que leia a quantidade de dias, horas, minutos e segudos do usuario. Calcule o total em segundos.

dias = 0
horas = 0
minutos = 0
segundos = 0

while dias == 0:
    dias = int(input("Digite a quantidade de dias: "))
    if dias == 0:
        print("Digite uma quantidade valida")
        dias = 0

while horas == 0:
    horas = int(input("Digite a quantidade de horas: "))
    if horas == 0:
        print("Digite uma quantidade valida")
        horas = 0

while minutos == 0:
    minutos = int(input("Digite a quantidade de minutos: "))
    if minutos == 0:
        print("Digite uma quantidade valida")

while segundos == 0:
    segundos = int(input("Digite a quantidade de segundos: "))
    if segundos == 0:
        print("Digite uma quantidade valida")


print("O total em segundos é: ", dias * 86400 + horas * 3600 + minutos * 60 + segundos)