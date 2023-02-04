# Reforçando "len", "min" e "max"
lista = [2, 5, 2, 8, 5]

len(lista)  # retorna 5 números
min(lista)  # retorna 2 como menor número
max(lista)  # retorna 8 como maior número

palavra = "banana"

len(palavra)  # retorna 6 letras
min(palavra)  # retorna 'a'
max(palavra)  # retorna 'n'

# Mesmo com o alfabeto escrito de trás para frente, ele retorna A como primeira (min) e Z como segunda (max).
alfabeto = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

len(alfabeto)  # retorna 26 letras
min(alfabeto)  # retorna 'A'
max(alfabeto)  # retorna 'Z'


# Listas vs Tuplas
dias = ["D", "S", "T", "Q", "Q", "S", "S"]
dias.append("D")    # adiciona um domingo ao final da lista
dias                # verifica inserção do novo elemento
dias.pop()          # retorna o último valor da lista e o remove
dias                # verifica remoção do último elemento

dias = ("D", "S", "T", "Q", "Q", "S", "S")
dias.append("D")
dias.pop()


# Funções importantes
valores = ("a", "b", "c", "d", "e")
# AQUI

len(valores)        # retorna 5
max(valores)        # retorna 'e'
del (valores[0])     # retorna erro
min(valores)        # retorna 'a'

# O "min", o "max" e o "min" funcionam para qualquer sequência, inclusive tuplas.
# O "del" só funciona para sequências mutáveis com listas, mas não para tuplas.

valores = ["a", "b", "c", "d", "e"]

del (valores[0])


# Listas e tuplas juntas
p1 = (3, 5)
p2 = (4, 6)
p3 = (5, 7)

# retorna uma tupla com os valores de uma lista dentro
line = [p1, p2, p3]
line
[(3, 5), (4, 6), (5, 7)]


p1 = ("Nico", 39)
p2 = ("Flavio", 37)

# retorna uma tupla com os valores de uma lista dentro
instrutores = [p1, p2]
instrutores
[('Nico', 39), ('Flavio', 37)]

# retorna apenas o instrutor na posição 0
instrutores[0]
('Nico', 39)

# retorna apenas a idade do instrutor na posição 0
instrutores[0][1]
39


# Inserindo itens numa lista
palavras = []

palavras.append("banana")
palavras.append("abacaxi")
nova = tuple(palavras)

# resultado da tupla
nova
('banana', 'abacaxi')

outra = list(nova)

# resultado da lista
outra
['banana', 'abacaxi']


# Ajuda na conversão
nomes = ("Nico", "Douglas", "Flavio", "Daniel")
# AQUI
nomes.append("Fabio")

nomes = tuple(nomes)    # retorna erro
nomes = (nomes)         # retorna erro
nomes = nomes[0]        # retorna erro
nomes = []              # executa, pois nomes será uma lista vazia

# executa, pois usa a função "list" para criar uma lista baseada nos valores da tupla
nomes = list(nomes)
