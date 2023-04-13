"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.2
Escreva uma função chamada cumsum que receba uma lista de numeros e retorne
a soma cumulativa; isto é, uma nova lista aonde o i-ésimo elemento é a soma dos
primeiros i+1 elementos da lista original

"""
def cumsum(lista):
    soma = 0
    nova_lista = []
    for i in lista:
       soma = i + soma
       nova_lista.append(soma)
    return nova_lista

t = [1,2,3]
print(cumsum(t))
