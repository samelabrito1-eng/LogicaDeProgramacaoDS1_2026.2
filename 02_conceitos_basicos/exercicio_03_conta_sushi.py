"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("bem-vindo ao programa de calculo da conta do nagoya sushi house")
valor_total = float(input("digite o valor total consumido no restaurante (em R$):"))
taxa_servico = valor_total * 0.10
valor_final = valor_total + taxa_servico
print("o valor final da conta a pagar e de R$ {: .2f}".format(valor_final))
