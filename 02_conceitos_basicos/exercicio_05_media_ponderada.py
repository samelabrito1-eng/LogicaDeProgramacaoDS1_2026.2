"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("bem-vindo ao programa de calculo da media ponderada da avaliacao tecnica")
nota1 = float(input("digite a nota da primeira avaliacao (peso 2):"))
nota2 = float(input("digite a nota da segunda avaliacao (peso 3):"))
nota3 = float(input("digite a nota da terceira avaliacao (peso 5):"))
media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)
print("a media final ponderada das avaliacoes e de {: .2f}".format(media_ponderada))