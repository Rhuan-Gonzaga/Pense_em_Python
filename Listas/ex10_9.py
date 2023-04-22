"""
Livro Pense em Python Capitulo 10 - listas
Exercício 10.9
Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento
por palavra. Escreva duas versões desta função, uma usando o método append e
outra usando a expressão t = t + [x]. Qual leva mais tempo para ser executada? Por quê?

RESPOSTA:Confesso que achei que a fução usando o método append seria a que levaria mais tempo
mas pesquisando vi que a função append() adiciona cada plavra a lista existente. Enquanto a
função que usa a expressão t = t + [x]. cria uma nova lista cada vez que uma nova palavra é
adicionada
"""
import timeit

#Usando o método append
def mtd_app():
    arquivo = open(r"words.txt")
    linhas = arquivo.readlines()
    lista = []
    for i in linhas:
       for j in i:
            lista.append(j)
    return lista

#Usando a expressão t = t + [x].
def expre():
    arquivo = open(r"words.txt")
    linhas = arquivo.readlines()
    lista = []
    for i in linhas:
       for j in i:
            lista = lista + [j]
    return lista

inicio = timeit.default_timer()
mtd_app()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))

nicio = timeit.default_timer()
expre()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))