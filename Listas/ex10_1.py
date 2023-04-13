"""
Capitulo 10 - listas
Exercicio 10.1
Escreva uma função chmada nested_sum que receba uma lista de listas
de numero inteiros e adicione os elementos de todas as listas aninhadas.
"""
def nested_sum(lista):
    soma = 0
    for i in lista:
        for j in i:
            soma = soma + j
    return soma


t = [[1,2], [3], [4,5,6]]
print(nested_sum(t))
