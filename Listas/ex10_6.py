"""
Livro Pense em Python Capitulo 10 - listas
Exercicio 10.6
DUas palavras são anagramas se você puder soletrar uma rearranjando as letras
da outra. Escreva uma função chamada is_anagram que tome duas strings e retorne
True se forem anagramas
"""
def is_anagram(p1,p2):
    if sorted(p1) == sorted(p2):
        return True
    else:
        return False

p1 = input("")
p2 = input("")
print(is_anagram(p1,p2))