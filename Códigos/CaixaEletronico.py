#-*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
data = datetime
saldo = 100.0
banco = 's'
while banco.lower() == 's':
	hora = int(data.now().strftime("%H"))
	if hora < 12:
		cumprimento = 'Olá, bom dia!'
	elif (hora > 11 and hora < 18):
		cumprimento = 'Olá, boa tarde!'
	else:
		cumprimento = 'Olá, boa noite!'

	try:
		if confirma_deposito.lower() == 's':
			if data.now() > liberar_deposito:
				saldo += deposito
				del processando_deposito
			else:
				processando_deposito = '*Saldo a liberar: ' + deposito_formatado
	except:
		None

	print()
	print(cumprimento + '\nBem vindo(a) ao banco.')
	saldo_formatado = "R$ {:,.2f}".format(saldo)
	print()
	print('Seu saldo é de ' + saldo_formatado)
	try:
		print(processando_deposito)
	except:
		None

	opcao = None
	while opcao == None:
		print()
		acoes = ["1- Sacar","2- Transferir","3- Depositar","4- Atualizar","5- Sair"]
		for a in acoes:
			print(a)
		print()	
		opcao = int(input('Escolha a opção desejada: '))

		if opcao < 1 or opcao > len(acoes):
			print()
			print('Opção inválida. Selecione uma opção entre 1 e ' + str(len(acoes)))
			opcao = None
	print()

	if opcao == 1:		
		saque = float(input('Saque ($RS): '))
		check_saldo = saldo - saque
		if check_saldo < 0:
			print('Você não possui saldo suficiente para esta operação')
		else:
			saldo -= saque
			saque_formatado = "R$ {:,.2f}".format(saque)
			print('Você sacou: ' + saque_formatado)

	if opcao == 2:		
		transferencia = float(input('Transferência ($RS): '))
		check_saldo = saldo - transferencia
		if check_saldo < 0:
			print('Você não possui saldo suficiente para esta operação')
		else:
			agencia = input('Agência: ')
			conta = input('Conta: ')
			transferencia_formatado = "R$ {:,.2f}".format(transferencia)
			print('Valor: ' + transferencia_formatado)
			print('Enviar para: ' + agencia + " " + conta)
			print()
			confirma_transferencia = input('Confirma a transferência? [S/N]: ')
			if confirma_transferencia.lower() == 's':
				saldo -= transferencia
				print('Operação realizada com sucesso!')
			else:
				print('Operação cancelada')

	if opcao == 3:		
		deposito = float(input('Depósito ($RS): '))
		confirma_deposito = input('Confirma o depósito? [S/N]: ')
		if confirma_deposito.lower() == 's':
			liberar_deposito = data.now() + timedelta(minutes=3)
			liberar_deposito_formatado = liberar_deposito.strftime("%d/%m/%Y %H:%M")
			deposito_formatado = "R$ {:,.2f}".format(deposito)
			print()
			print('Operação realizada com sucesso!')
			print('Estamos processando seu depósito de ' + deposito_formatado + '\nPrazo para liberação: ' + liberar_deposito_formatado)
		else:
			print()
			print('Operação cancelada')

	if opcao == 4:
		print('Atualizado!')

	if opcao == 5:
		print('Obrigado por usar o nosso banco!')
		input()
		exit()	

	print()		
	banco = input('Voltar ao menu principal? [S/N]: ')

print('Obrigado por usar o nosso banco!')
input()	