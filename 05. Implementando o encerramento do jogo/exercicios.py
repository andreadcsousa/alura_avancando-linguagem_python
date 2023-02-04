# Calculando o total de caracteres em um loop
total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    # AQUI
    total = total + 1
print(total - 1)

# Para encerrar o loop e imprimir o total de caracteres da variável "palavra", deve-se adicionar o código:
acabou = (total == len(palavra))
# Isso definirá "true" para a variável "acabou" apenas quando o total for igual ao tamanho da palavra "len".


# Saindo do loop
passos = 0
while (  # ):
  passos += 1
print(passos)

# Para sair do loop após 10 passos é necessário definir como parâmetro do "while":
passos < 10 ou passos <= 9
# Isso porque a contagem começa em 0 (zero), então "< 10" e "<= 9" tem o mesmo resultado.



# Forca com teste de erros alternativo
erros=6

# Para manter as 6 tentativas de erro, pode-se decrementar os "erros" e mudar o teste do "enforcou":
erros=erros - 1
enforcou=erros == 0

# Ou mudar o teste da variável enforcou, duplicando a quantidade de erros, para manter as tentativas em 6:
enforcou=erros == 12



# Loop relativo à list comprehension
frutas=["maçã", "banana", "laranja", "melancia"]

lista=[]
for fruta in frutas:
    lista.append(fruta.upper())

# Foi criada uma nova lista, que já adiciona as frutas com letra maiúscula
lista=[fruta.upper() for fruta in frutas]



# Preenchendo uma lista com os quadrados de números inteiros
inteiros=[1, 3, 4, 5, 7, 8]

quadrados=[n * n for n in inteiros]



# Para saber mais: inicializando uma lista de números pares
inteiros=[1, 3, 4, 5, 7, 8, 9]
pares=[]

for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

# Para reescrever o laço for em formato list comprehension, deve-se declarar na lista de pares a sintaxe:
pares=[numero for numero in inteiros if numero % 2 == 0]

# Um número da lista de inteiros será par
# Para cada número dentro nessa lista
# Se o módulo do número for igual a 0 (zero)
