#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal 
# e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome 
# e informando o valor do salário em comparação com o bônus recebido
CONSTANTE_BONUS = 1000
nome = input("digite seu nome: ")
salario = input("digite seu salario: ")
bonus = input("digite seu bonus: ")

bonuskpi = CONSTANTE_BONUS + (float(salario) * float(bonus))

print(f"Bom dia,{nome},! O cálculo do KPI do bônus de 2024 é de: {bonuskpi} reais.")