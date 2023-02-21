print('Bem vindo a Loja de Lucas garcia l. da silva')

valorproduto = float (input('por favor entre com o valor do produto: '))
print(valorproduto)

quantidadeproduto = int(input('entre com o valor da quantidade:'))

print(quantidadeproduto)
total = valorproduto * quantidadeproduto

if total < 4 :
    valorfinal = total

elif 5 <= total < 19:
    valorfinal = total - total * 0.03 #desconto de 3%
    print('O desconto  foi de 3%')


elif 20 <= total < 99:
    valorfinal = total - total * 0.06 #desconto de 6%
    print('O desconto foi de 6%')

else: #se o valor for acima de 99 entra nesse else
    valorfinal = total - total * 0.10
    print('O desconto foi de 10% ')

print("O valor sem desconto: R$ {:.2f}". format(total))
print("O valor com desconto: R$ {:.2f}". format(valorfinal))
