# Beecrowd - Média 1
# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um
# aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a
# nota B tem peso 7.5 (A soma dos pesos portanto é 11).
# Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

notaA = float(input("Digite a Primeira Nota: "))
notaB = float(input("Digite a Segunda Nota: "))

# calculando média
soma_notas = (notaA * 3.5) + (notaB * 7.5)
divisao_notas = soma_notas / 11

# printando nota
print(f"MEDIA = {divisao_notas:.5f}")
