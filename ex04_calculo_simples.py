# Beecrowd - Cálculo Simples
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
# o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2
# e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

lista_peca1 = []
lista_peca2 = []

# dados peça 1
dados_peca1 = input("").split()
lista_peca1 = [float(numero) for numero in dados_peca1]

# dados peça 2
dados_peca2 = input("").split()
lista_peca2 = [float(numero) for numero in dados_peca2]

# separando os dados
código_peca1 = lista_peca1[0]
numero_peca1 = lista_peca1[1]
valor_unitario_peca1 = lista_peca1[2]

código_peca2 = lista_peca2[0]
numero_peca2 = lista_peca2[1]
valor_unitario_peca2 = lista_peca2[2]

# somando o valor total das duas peças
soma_peca1 = numero_peca1 * valor_unitario_peca1
soma_peca2 = numero_peca2 * valor_unitario_peca2
soma_total = soma_peca1 + soma_peca2

# printando o total a ser pago
print(f"VALOR A PAGAR: R$ {soma_total:.2f}")
