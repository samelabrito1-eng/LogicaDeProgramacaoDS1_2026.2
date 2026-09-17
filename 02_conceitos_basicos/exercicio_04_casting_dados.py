"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("bem-vindo ao programa de calculo de idade em 2026")
ano_nascimento = input("digite o ano de nascimento (em formato de texto):")
ano_nascimento = int(ano_nascimento) 
idade_em_2026 = 2026 - ano_nascimento
print("a idade que a pessoa completara ate o final de 2026 e de {} anos".format(idade_em_2026))
