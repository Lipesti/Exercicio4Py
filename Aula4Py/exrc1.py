#Exercicio 1 
#Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valor entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”

numero = int(input('Informe um numero para saber se é valido: '))

if numero <= 9:
    print('O numero está correto')
elif numero >9:
        print('O numero está incorreto')

