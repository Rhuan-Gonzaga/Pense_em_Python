"""
Livro Pense em Python Capitulo 10 - listas
Exercício 10.10
Para verificar se uma palavra está na lista de palavras, você pode usar o
operador in, mas isso seria lento porque pesquisaria as palavras em ordem.

Como as palavras/valores estão em ordem alfabética, podemos acelerar as coisas com
uma busca por bisseção (também conhecida como pesquisa binária), que é semelhante
ao que você faz quando procura uma palavra no dicionário. Você começa no meio e
verifica se a palavra que está procurando vem antes da palavra no meio da lista.
 Se for o caso, procura na primeira metade da lista. Se não, procura na segunda metade.

De qualquer forma, você corta o espaço de busca restante pela metade.
Se a lista de palavras tiver 113.809 palavras, o programa seguirá uns 17
 passos para encontrar a palavra ou concluir que não está lá.

Escreva uma função chamada in_bisect que receba uma lista ordenada,
um valor-alvo e devolva o índice do valor na lista se ele estiver lá,
ou None se não estiver.

Ou você pode ler a documentação do módulo bisect e usá-lo!
"""

#busca binaria
def in_bisect(lista, valor_alvo, inicio=0,fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor_alvo:
            return  meio
        #esquerda
        if valor_alvo < lista[meio]:
            return in_bisect(lista,valor_alvo,inicio, meio - 1)
        #Direita
        else:
            return in_bisect(lista,valor_alvo,meio +1, fim)

lista = [2,3,4,5,6]
print(in_bisect(lista, 6))