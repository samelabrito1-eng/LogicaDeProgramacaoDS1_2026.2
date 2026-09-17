"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("bem-vindo ao programa de calculo de consumo da motocicleta kawasaki versys 300")
distancia_pecorrida = float(input("digite a distancia total percorrida (em km):"))
combustivel_gasto = float(input("digite o total de combustiveis gastos (em litros):"))
consumo_medio = distancia_pecorrida / combustivel_gasto
print("o consumo medio da motocicleta kawaski versys 300 e de {: .2f} km/l".format(consumo_medio))
