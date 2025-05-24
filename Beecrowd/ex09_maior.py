"""
Beecrowd - O Maior

Faça um programa que leia três valores e apresente o maior dos três valores
lidos seguido da mensagem “eh o maior”. Utilize a fórmula abaixo

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

# entrada de dados
numeros = input("").split()

# separando dados
lista_numeros = [int(numero) for numero in numeros]
maior = 0

# checando o maior
for numero in lista_numeros:
    if numero > maior:
        maior = numero

# printando o maior
print(f"{maior} eh o maior")
