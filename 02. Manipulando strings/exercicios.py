# Buscando um caractere em uma string
palavra = "aluracursos"

palavra.find('s')  # resultado é 9   FALSE
palavra.find('l')  # resultado é 1   TRUE
palavra.find('a')  # resultado é 4   FALSE
palavra.find('b')  # resultado é -1  TRUE

# começando da posição 1, ele encontra a próxima letra a na palavra
palavra.find('a', 1)
palavra.find('a', 1)    # resultado é 4 agora sim é TRUE

# Para encontrar a posição de uma letra, pode-se usar "find()". A posição começa em 0 e não retorna letras repetidas na ocorrência. Find também aceita um parâmetro que define em que posição começar.


# Iterando em uma palavra
palavra = "Alura"
for letra in palavra:
    if (letra == "l"):
    print("Achou!")

palavra = "Alura"
for letra in palavra:
    if (letra == "l"):
        print("Achou!")

palavra = "Alura"
for palavra in letra:
    if (letra == "l"):
        print("Achou!")

# Na opção A, faltou indentação no print.
# A opção B retorna ACHOU.
# A opção C está buscando palavra em letra, não letra em palavra.


# Recordando...
a = "Cavalo"
b = "Calopsita"
print("{} e {}".format(b, a))   # resultado "Calopsita e Cavalo"

# No format é possível escolher qual valor será mostrado e em que ordem.


# Grandes poderes trazem grandes responsabilidades
nome = "clarice"
nome.capitalize()
print(nome)

# Precisa definir que "nome" irá receber a nova formatação

nome = "clarice"
nome = nome.capitalize()
print(nome)
