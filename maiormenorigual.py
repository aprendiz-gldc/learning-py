#!/usr/bin/env python3
##
# Exercicio de fixação 3
# estruturas de decisão 
# if
# Recebe dois números inteiros e compara
##
# Maior Menor ou Igual

try:
	num1 = int(input("Digite um número inteiro: "))
	num2 = int(input("Digite outro número inteiro: "))
	
	if num1 == num2:
		print("Os numeros digitados são iguais")
	elif num1 < num2 :
		print(f"O número {num1} é menor que {num2}")
	else:
		print(f"O número {num1} é maior que {num2}")
except ValueError:
	print("Somente números inteiros. Tente novamente, por favor.")
