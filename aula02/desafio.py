#Inteiros (int)
##1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero1 = int(input("digite um valor: "))
numero2 = int(input("digite outro valor: "))
print(f"A soma de {numero1} e {numero2} é: {numero1 + numero2}")

##2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero1 = int(input("digite um valor: "))
print(f"O resto da divisão de {numero1} por 5 é: {numero1 % 5}")

##3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("digite um valor: "))
numero2 = int(input("digite outro valor: "))
print(f"O resultado da multiplicação entre {numero1} e {numero2} é: {numero1 * numero2}")

##4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero1 = int(input("digite um valor: "))
numero2 = int(input("digite outro valor: "))
resultado = numero1 // numero2
print(f"O resultado da divisão inteira entre {numero1} e {numero2} é: {resultado}")

##5.Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero1 = int(input("digite um valor: "))
print(f"O quadrado de {numero1} é: {numero1 ** 2}")

#Números de Ponto Flutuante (float)
##1.Escreva um programa que receba dois números flutuantes e realize sua adição.
numero1 = float(input("digite um valor: "))
numero2 = float(input("digite outro valor: "))
print(f"A soma de {numero1} e {numero2} é: {numero1 + numero2}")

##2.Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero1 = float(input("digite um valor: "))
numero2 = float(input("digite outro valor: "))
print(f"A média entre {numero1} e {numero2} é: {(numero1 + numero2) / 2}")

##3.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero1 = float(input("digite um valor: "))
numero2 = float(input("digite outro valor: "))
print(f"A potência entre {numero1} e {numero2} é: {numero1 ** numero2}")

##4.Faça um programa que converta a temperatura de Celsius para Fahrenheit.
numero1 = float(input("digite um valor: ")) 
print(f"A temperatura em Fahrenheit é: {(numero1 * 1.8) + 32}")

##5.Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
numero1 = float(input("digite um valor: "))
print(f"A área do círculo de raio {numero1} é: {3.14 * (numero1 ** 2)}")


#Strings (str)
##1.Escreva um programa que receba uma string do usuário e a converta para maiúsculas. 
nome = input("digite seu nome: ")
print(nome.upper()) 


##2.Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas. 
nome = input("digite seu nome: ")
print(nome.lower())

##3.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("digite uma frase: ")
print(frase.strip())

##4.Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("digite uma data no formato dd/mm/aaaa: ")
print(data[0:2])
print(data[3:5])
print(data[6:10])

##5.Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome = input("digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")
print(f"{nome} {sobrenome}")

#Booleanos (bool)
##1.Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
boleano1 = bool(input("digite um valor: "))
boleano2 = bool(input("digite outro valor: "))
print(f"O resultado da operação AND entre {boleano1} e {boleano2} é: {boleano1 and boleano2}")

##2.Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
boleano1 = bool(input("digite um valor: "))
boleano2 = bool(input("digite outro valor: "))
print(f"O resultado da operação OR entre {boleano1} e {boleano2} é: {boleano1 or boleano2}")

##3.Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
boleano = bool(input("digite um valor: "))
print(f"O valor invertido de {boleano} é: {not boleano}")

##4.Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = int(input("digite um valor: "))
numero2 = int(input("digite outro valor: "))
print(f"O resultado da operação OR entre {numero1} e {numero2} é: {numero1 == numero2}")

##5.Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = int(input("digite um valor: "))
numero2 = int(input("digite outro valor: "))
print(f"O resultado da operação OR entre {numero1} e {numero2} é: {numero1 != numero2}")

