#!/usr/bin/env python3

###
## https://www.youtube.com/watch?v=kqtD5dpn9C8
###

# Ler o nome e idade, depois imprimir de volta
#first_name = input("Qual o seu nome? ")
#ano_nascimento = input("Em que ano nasceu? ")
#idade = 2024 - int(ano_nascimento)
#print("Hello " + first_name)
#print("Você tem "+ str(idade) + " anos")

## Fazer uma pequena calculadora
#num1 = float(input("First number: "))
#num2 = float(input("Second number: "))
#sum = num1 + num2
#print("A soma dos dois numeros é: " + str(sum))

# Conversor de pesos
#peso_atual = float(input("Qual o seu peso atual? "))
#
#medida = input("(K)g ou (L)bs: ")
#converter = medida.lower()
#if converter == "l" :
#	peso_convertido = peso_atual / 2.2046
#	medida = " Kg"
#elif converter == "k" :
#	peso_convertido = peso_atual * 2.2046
#	medida = " Lbs"
#else :
#	print("Unidade de medida desconhecida")
#	exit()
#
#print("Seu peso convertio " + str(peso_convertido) + medida)

#numbers = [1, 2, 3, 4, 5]
#print(numbers)
#numbers.append(6)
#numbers.insert(-1, 8)
#print(numbers)

#numbers = [1, 2, 3, 4, 5]
#print(numbers)
#for item in numbers:
#	print(item)

#print("")

#i = 0
#while i < len(numbers):
#	print(numbers[i])
#	i += 1

for number in range(5,10,2):
	print(number)
