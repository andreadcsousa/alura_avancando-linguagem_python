# Lendo a primeira linha
Romário 37
Junior 32
Daniel 28
Izzy 38

arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)

# O código acima lê linha a linha do arquivo, uma por vez, então começará da primeira.


# Lendo um arquivo completo
frutas = ["Banana", "Maçã", "Pera", "Uva", "Jamelão"]

arquivo = open('frutas.txt', 'r')

linha = arquivo.readline()  # lê a primeira linha e retorna "Banana"
print(linha)
linha = arquivo.readline()  # lê a linha seguinte e retorna "Maçã"
print(linha)

arquivo = open('frutas.txt', 'r')

conteudo = arquivo.read()
print(conteudo)
conteudo = arquivo.read()
print(conteudo)

# Para ler um arquivo duas vezes, utilizando "read" é necessário fechar e abrir o arquivo novamente. Pois o segundo comando de leitura começará de onde o outro parou, ou seja, do final e no fim não tem nada.
