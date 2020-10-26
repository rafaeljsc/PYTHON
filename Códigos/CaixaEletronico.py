#-*- coding: utf-8 -*-
saldo = 100
while saldo >= 0:
	print()
	sacar = (input('Saldo: $RS ' + str(saldo) + '\nDeseja sacar? [S/N]: '))
	if sacar.lower() == 's':
		saque = int(input('Saque ($RS): '))
		check_saldo = saldo - saque
		if check_saldo < 0:
			print('Você não possui saldo suficiente para esta operação')
			input()
		else:
			saldo -= saque
			print('Você sacou: R$ ' + str(saque))
	else:
		print('Obrigado por usar nosso banco!')
		input()
		break