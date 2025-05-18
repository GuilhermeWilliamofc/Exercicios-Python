# Beecrowd - Diferença
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a
# diferença do produto de A e B pelo produto de C e D segundo a fórmula:
# DIFERENCA = (A * B - C * D).


A = int(input("Digite o 1º Número: "))
# o input tem q ficar vazio no beecrowd se n dá erro msm se a resposta estiver certa, só coloquei aqui pra ficar "bonito"
B = int(input("Digite o 2º Número: "))
C = int(input("Digite o 3º Número: "))
D = int(input("Digite o 4º Número: "))

soma1 = A * B
soma2 = C * D

print(f"DIFERENCA = {soma1 - soma2}")
