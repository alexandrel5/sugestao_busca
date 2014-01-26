#!/usr/bin/env python
# -*- coding: utf-8 -*-

def porcentagem(s_recebida, valor=70): #valor da porcentagem a ser filtrada padrao 70% de igualdade
	lista = []
	tam = len(s_recebida)
	porcentagem = 100 / tam #tenho que arrumar para nao dar exceção da divisao por zero
	s_dicio = {'casa':[0], 'bola':[0], 'asa':[0], 'amor':[0], 'camila':[0], 'dora':[0], 'casamento':[0]}

	for letra in s_recebida: #percorre a string recebida
		for li in s_dicio: #percorre a lista de palavras armazenadas localmente 
			if letra in li : #letra de string recebida esta contida em palavra armazenada localmente
				s_dicio[li][0] = s_dicio[li][0] + porcentagem

	nova_lista_p = sorted(s_dicio.items(), key=lambda s: s[1])	# ordena pela porcentagem		
	
	for x in xrange(0, len(nova_lista_p)):
		if nova_lista_p[x][1][0] > valor:
			lista.append(nova_lista_p[x][0])

	return lista

def ordenar_Tamanho(lista):
	lista.sort(key=len)

	return lista


lista = porcentagem('casa')
lista = ordenar_Tamanho(lista)
print lista

