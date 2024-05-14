# Iasmin Evelin Santos

prova1 = 2
nota1 = float(input("Digite a nota da primeira prova: "))
prova2 = 3
nota2 = float(input("Digite a nota da segunda prova: "))
prova3 = 5
nota3 = float(input("Digite a nota da terceira prova: "))

calculo = (nota1*prova1) + (nota2*prova2) + (nota3*prova3)
peso = prova1 + prova2 + prova3
resultado = calculo / peso

print("A média final do aluno é: ", resultado)
