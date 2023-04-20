"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.8
Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem anivesario
no mesmo dia? você pode estimar esta probabilidade gerando amostras aleatorias
de 23 dias de anivesarios e verificando as correspondências. Dica:
Você pode gerar anivesarios aleatorios com a função randit no modulo randon

"""
from random import randint

n_pessoas = int(input("Digite o numero de pessoas: "))
n_repe = int(input("Digite o numero de repetições: "))
repetidos = 1

for _ in range(n_repe):
    datas_anive ={randint(1, 366) for _ in range(n_pessoas)}
    if len(datas_anive) != n_pessoas:
        repetidos+=1

porcentagem = (repetidos/n_repe) * 100
print(f"{porcentagem}%")