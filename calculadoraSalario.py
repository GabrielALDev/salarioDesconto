import os

def opcoes () :
	print("Esse é um programa que calcula seu salario?")
	print("O que deseha fazer? ")
	print("1 - Iniciar programa")
	print("2 - Sair do programa")
	menu = input("Qual a opção desejada?\n")
	if menu == "1" :
		salario = float(input('Digite seu salario (sem desconto)R$:'))
		if salario <= 1320:
			desconto=salario*0.075
			salarioDesconto=salario-desconto
			print(f'Seu salário é R${salarioDesconto:.2f}')
			print("O calculo é feito pela tabela do INSS - 2023")
			reiniciar = input("Você deseja reiniciar S/N? ").upper()
			if reiniciar == "S" :
				os.system('cls') or None
				opcoes()
		elif (salario <= 1320.01) or (salario <= 2571.29):
			desconto=salario*0.09
			salarioDesconto=salario-desconto
			print(f'Seu salário é R${salarioDesconto:.2f}')
			print("O calculo é feito pela tabela do INSS - 2023")
			if reiniciar == "S" :
				os.system('cls') or None
				opcoes()
		elif (salario <= 2571.30) or (salario <= 3856.94):
			desconto=salario*0.12
			salarioDesconto=salario-desconto
			print(f'Seu salário é R${salarioDesconto:.2f}')
			print("O calculo é feito pela tabela do INSS - 2023")
			if reiniciar == "S" :
				os.system('cls') or None
				opcoes()
		elif (salario <= 3856.95) or (salario <= 7507.49) or (salario >= 7507.49):
			desconto=salario*0.14
			salarioDesconto=salario-desconto
			print(f'Seu salário é R${salarioDesconto:.2f}')
			print("O calculo é feito pela tabela do INSS - 2023")
			if reiniciar == "S" :
				os.system('cls') or None
				opcoes()
	elif menu == "2":
		print("Você saiu do programa")
		quit()
opcoes ()