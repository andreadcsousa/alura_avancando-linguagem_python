# Sistema para as frutas
# coding: utf-8
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar? ')

if (fruta_pedida in frutas):
    print('Sim, temos a fruta.')
else:
    print('Não temos a fruta.')

# Deve-se substituir o parâmetro do "if" por "fruta_pedida in frutas".


# Um bom jeito de economizar
precos = [
    1525, 1120, 1464, 1200, 1330, 1356, 1312, 1531, 1232, 1234, 1250, 1114, 1553, 1147, 1303, 1296, 1309, 1404, 1479, 1376, 1152, 1440, 1038, 1018, 1291, 1388, 1577, 1115, 1488, 1494, 1254, 1230, 1122, 1396, 1208, 1356, 1549, 1116, 1443, 1075, 1536, 1542, 1036, 1015, 1020, 1217, 1484, 1032, 1390, 1026
]

# Para verificar se "1025" é o menor que os preços registrados anteriormente, deve-se utilizar passar a lista como parâmetro e então utilizar "min()" para obter o menor valor da lista.

print(min(precos))


# Contando os funcionários
funcionarios = ['Astrid', 'Flavia', 'Talia', 'Mauricio', 'Waldemar', 'Marina']
print(funcionarios)

# Para saber o número de funcionários da lista acima, deve-se utilizar a função "len()", ela retorna a quantidade de itens de uma lista.

print(len(funcionarios))


# Um falso campeão
# Restante do código que gera a lista de colocação...

print(colocacao)
# Resultado: ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[1]

print(' O grande campeão do torneio é o time ' + campeao)
# Resultado: O grande campeão do torneio é o time Bruxos como Ronaldinho

# O problema é que ao definir o "campeao = colocacao[1]", ele acabou escolhendo o segundo da lista. Já que o índice de uma lista começa em 0 (zero), ele deveria definir "colocacao[0]".
