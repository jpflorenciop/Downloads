# Questão 01
# numero = int(input("Digite um número positivo: "))

# for i in range(numero + 1):
#     if i %2 ==0:
#         print(i)

#Questão 2
# numero = int(input("Digite um número de 1 a 10: "))
# for i in range(1, 11):
#     multiplicacao = numero*i
#     print(f"{numero} x {i} = {multiplicacao}")

#Questão 3
# n1 = int(input('Digite o numero inicial: '))
# n2 = int(input('Digite o numero final: '))
# conta = range(n1,n2+1)
# soma = 0

# for i in conta:
#     soma += i
# print(soma)

#Questão4
# for i in range(10,-1,-1):
#     print(i)

# print("Fogo!") 

#QUestão5

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 ==0:
#         print('fizbuzz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 ==0:
#         print('buzz')
#     else:
#         print(i)

#QUestao6

# for i in range(1,11):
#     print(f"Número: {i} - Quadrado: {i**2}")

#QUestão 7

# qnt_notas = int(input("Quantas notas deseja digitar? "))
# soma = 0
# for i in range(qnt_notas):
#     nota = float(input(f"Digite sua nota {i +1}: "))
#     soma += nota
# media = soma/qnt_notas
# print(f"A média é {media}")

#QUestão 8

# for temperatura in range(20, 41):
#     if temperatura >=35:
#         print(f"Temperatura {temperatura}°C: Alerta de calor!")
#     else:
#         print(f"Temperatura {temperatura}°C: Normal")

#Questao 9

# palavra = input("Digite uma palavra: ")

# print(len("samara"))
# for letra in range(len(palavra)-1, -1, -1):
#     print(palavra[letra])
