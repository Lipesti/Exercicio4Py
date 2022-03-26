#Exercicio 4 
#Escreva um programa em Python que solicite ao usuário os valores de três
#contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique
#se o salário é suficiente para pagar as três contas, caso não seja apresente a
#mensagem “Salário insuficiente!”. Caso seja, apresente o valor que restou do
#salário após pagar as contas.

print('Verifique se o seu salario é o suficiente para efetuar o pagamento de suas contas')

luz = float(input('Informe o valor da conta de Luz R$: '))
agua = float(input('Informe o valor da conta sua de Agua R$: '))
internet = float(input('Informe o valor da sua conta de Internet R$: '))
salario = float(input('Informe o seu Salario R$: '))

valorContas = luz + agua + internet 

if (salario >= valorContas):
    print(f'O seu salario de R$: {salario} é o suficiente para efetuar o pagamento das contas {valorContas}')
elif (salario < valorContas):
    print('Desculpe seu saldo não é suficiente')