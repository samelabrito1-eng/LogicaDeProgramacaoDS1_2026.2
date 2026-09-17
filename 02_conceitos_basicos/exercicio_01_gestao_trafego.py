"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("bem-vindo ao programa de gestao de trafego da loja casas paulino")
print("digite o valor total investido na campanha (em R$):")
valor_investido = float(input())
print("digite o numero total de cliques obtidos:")
numero_cliques = int (input())
cpc_medio = valor_investido / numero_cliques
print("o custo por clique medio da campanha e R$ {: .2f}".format(cpc_medio))