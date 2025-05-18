# Beecrowd - Média 2
# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2,
# a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0,
# sempre com uma casa decimal.

notaA = float(input("Digite a Primeira Nota: "))
notaB = float(input("Digite a Segunda Nota: "))
notaC = float(input("Digite a Terceira Nota: "))

# calculando média e pesos
soma_notas = (notaA * 2) + (notaB * 3) + (notaC * 5)
divisao_notas = soma_notas / 10

# printando média
print(f"MEDIA = {divisao_notas:.1f}")
