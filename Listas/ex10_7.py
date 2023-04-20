"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.7
Escreva uma função chamada has_duplicates que tome uma lista e retorne True
se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original
"""
def has_duplicates(lista):
    return len(lista) != len(set(lista))


lista = [7,8,9,2,9]
print(has_duplicates(lista))

33131031999