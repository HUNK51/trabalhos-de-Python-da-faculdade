print('seja bem vindo a pizzaria de Lucas Garcia l. da Silva')
print('+++++++++++++Cardapio+++++++++++++')
print('| Código | Descrição  |Pizza Média - M | Pizza Grande - G (30 % mais cara) |')
print('| 21     | Napolitana | R$ 20,00       |                          R$ 26,00 |')
print('| 22     | Margherita | R$ 20,00       |                          R$ 26,00 |')
print('| 23     | Calabresa  | R$ 25,00       |                          R$ 32,50 |')
print('| 24     | Toscana    | R$ 30,00       |                          R$ 39,00 |')
print('| 25     | portuguesa | R$ 30,00       |                          R$ 39,00 |\n')
subtotal = 0
while True:
    tamanho = input('Digite o tamanho da pizza desejada: ')
    if tamanho != 'm' and tamanho != 'g':
        print('tamanho invalido!')
        continue



    codigo = input('Insira o código da sua pizza: ')
    if tamanho =='m' and codigo == '21':
        subtotal = subtotal + 20
        print('Voce pediu uma pizza Napolitana - M: R$20.00')
    elif tamanho =='g' and codigo == '21':
        subtotal = subtotal + 26
        print('Voce pediu uma pizza Napolitana - G: R$26.00')
    elif tamanho == 'm' and codigo == '22':
        subtotal = subtotal + 20
        print('Voce pediu uma pizza Margherita - M: R$20.00')
    elif tamanho == 'g' and codigo == '22':
        subtotal = subtotal + 26
        print('Voce pediu uma pizza Margherita - G: R$26.00')
    elif tamanho == 'm' and codigo == '23':
        subtotal = subtotal + 25
        print('Voce pediu uma pizza Calabresa - M: R$25.00')
    elif tamanho == 'g' and codigo == '23':
        subtotal = subtotal + 32.50
        print('Voce pediu uma pizza Calabresa - G: R$32.50')
    elif tamanho == 'm' and codigo == '24':
        subtotal = subtotal + 30
        print('Voce pediu uma pizza Toscana - M: R$30.00')
    elif tamanho == 'g' and codigo == '24':
        subtotal = subtotal + 39
        print('Voce pediu uma pizza Toscana - G: R$39.00')
    elif tamanho == 'm' and codigo == '25':
        subtotal = subtotal + 30
        print('Voce pediu uma pizza Portuguesa - M: R$30.00')
    elif tamanho == 'g' and codigo == '25':
        subtotal = subtotal + 39
        print('Voce pediu uma pizza Portuguesa - G: R$39.00')

    else:
     print('pare de digitar caracteres errados')
     continue
    resposta = input('deseja mais algum serviços?(s/n)')
    if resposta == 's':
        continue
    else:
        print('o valor final da conta é:R${:.2f}' .format(subtotal))
        break
