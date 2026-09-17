# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
print("bem-vindo ao programa de divisão de conta do nagoya sushi house")
print("digite o valor total da conta (em R$):")
valor_conta = float(input())
print("digite o numero de pessoas para dividir a conta:") 
numero_pessoas =str(input())
print("o valor por pessoa e:R$ {: .2f}".format(valor_conta / int(numero_pessoas)))
print("fim do programa de divisao de conta do nagoya sushi house")

