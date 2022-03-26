#Exercicio 3 
#- Faça um programa em Python que obtenha o valor de uma compra, calcular e
#mostrar o valor da compra considerando o desconto, conforme descrito abaixo:
#• para compras acima de R$ 200 a loja dá um desconto de 20%
#• para as abaixo disso não tem desconto, mostre o valor da compra.

print ('Verifique se possui desconto')
valorCompra = float(input('Informe o valor total da Compra R$: '))
desconto = valorCompra*0.2
valorDesconto = valorCompra - desconto

if(valorCompra >= 200):
    print(f'O valor da compra com o desconto aplicado é de R$: {valorDesconto}')
elif(valorCompra < 200):
    print('Desculpe não atingiu o valor minimo para obter o desconto')    