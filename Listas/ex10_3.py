"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.3
Escreva uma função chamada middle que receba uma lista e retorne uma nova
lista com todos os elementos originais, exceto os primeiros e os ultimos elementos
"""
def middle(t):
   return t[1:3]

t = [1,2,3,4]
print(middle(t))