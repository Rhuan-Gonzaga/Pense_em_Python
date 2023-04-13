"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.5
Escreve uma função chamada is_sorted que tome uma lista como parâmetro e
retorne TRUE se a lista estiver classificada em ordem ascendente, e FALSE
se não for o caso
"""
def is_sorted(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))


t = [1,2,2]
t2 = ['b','a']
print(is_sorted(t))