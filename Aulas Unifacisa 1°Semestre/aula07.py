# Questão 1
lista = [7.5, 8.0, 5.5, 9.0, 6.0]

# soma = 0
# for numero in lista:
#   # soma = soma + numero
#    soma += numero

# print("A soma é", soma)

# Questão 2
# for nota in lista:
#     if nota >= 7:
#         print("Aprovado")
#     else:
#         print("Reprovado")

#Questão3

# cidades = ["Campina", "Esperança", "Queimadas", "Lagoa Seca", "Areia"]

# for cidade in cidades:
#     print("Eu adoraria visitar " + cidade + "!")
#   # print(f"Eu adoraria visitar {cidade}!")

#Questão 4

# numeros = [1, 5, 10, 15, 20]
# dobros = []

# for numero in numeros:
#     dobro = numero *2
#     dobros.append(dobro)

# print(dobros)

# Questão 5
# frutas = ['banana', 'manga', 'uva', 'abacaxi']

# for fruta in frutas:
#     print(f"Nome da fruta: {fruta} = Qnt. de letras: {len(fruta)}")

#QUestão 6
# itens = ['ok', 'ok', 'erro', 'ok', 'erro', 'ok']

# contador = 0
# for palavra in itens:
#     if palavra == "erro":
#         contador +=1
      
# print(f"A palavra ERRO foi exibida {contador} vezes")

#Questão 7
# precos = [100, 250, 40, 500, 120]
# for preco in precos:
#     desconto = preco * 0.1
#     preco_final = preco - desconto 
#     print(f"O preço final do produto é: {preco_final}")

#Questão 8
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros:
#     if numero % 2 == 0:
#         print(f"Número {numero} é par")
#     else:
#         print(f"Número {numero} é ímpar")

#Questão 9
# valores = [10, -5, 20, -1, 30, -10]
# soma = 0

# for valor in valores:
#     if valor > 0:
#         soma += valor

# print(f"A soma dos valores positivos é: {soma}")

#Questão 10
# animais = ['gato', 'elefante', 'cão', 'girafa', 'boi', 'leão']

# for animal in animais:
#     if len(animal) <= 4:
#         print(animal)

#Questão 11
# usuarios_cadastrados = ["joão", "maria", "samara"]
# nome_digitado = input("Digite seu nome: ").lower()
# acesso = False
# for usuario in usuarios_cadastrados:
#     if(nome_digitado == usuario):
#         acesso = True
# if acesso:
#     print("Acesso Liberado")
# else:
#     print("Acesso Negado")

#Questão 12
# pontuacoes = [45, 89, 32, 102, 67]
# maior_valor = pontuacoes[0]

# for numero in pontuacoes:
#     if(numero > maior_valor):
#         maior_valor = numero
# print(f"O maior valor é {maior_valor}")

# Questão 13

# pedidos = ['P', 'E', 'P', 'C', 'E', "A"]
# for letra in pedidos:
#     if letra == "P":
#         print("Pendente")
#     elif letra == "E":
#         print("Enviado")
#     elif letra == "C":
#         print("Cancelado")
#     else:
#         print("Opção inexistente")

#Questão 14

# nomes = ['ana', 'carlos', 'beatriz']
# emails = []

# for nome in nomes:
#     email = nome+"@maisunifacisa.com.br"
#     emails.append(email)

# print(emails)