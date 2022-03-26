#Exercicio 2
#Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$ 37,50

turno1 = print('Digite 1 para o turno de Dia')
turno2 = print('Digite 2 para o turno de Noite')

turno = int(input('Digite seu turno: '))

horastrabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
salario = horastrabalhadas*37.50
salario = horastrabalhadas*45.00
if(turno == 1):
    salario = 37.50*horastrabalhadas
    print(f'O valor do salario para o turno Diurno é R$: {salario}')
else:
    turno == 2 == horastrabalhadas*45.00
    salario = 45.00*horastrabalhadas
    print(f'O valor do salario para o turno Noturno é R$: {salario} ')