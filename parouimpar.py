#!/usr/bin/env python3
##
# Exercicio de fixação 2
# estruturas de decisão 
# if
##
# Par ou Impar

try:
	numero = int(input("Digite um número inteiro: "))
	
	resto = numero % 2
	
	if resto == 0:
		print("O numero digitado é par")
	else:
		print("O número digitado é ímpar")
except ValueError:
	print("Por favor, insira um número válido para testar")
