#-------começo da função volume feijoada--------------
def volume():
    while True:
     try:
        porcao = float(input('Qual volume da poção(ml):'))
        if porcao < 300:
          print('Opção invalida, Tente novamente. Não aceitamos porções menores que 300ml ou maiores que 5l. tente novamnete!')
          continue

        elif porcao >= 300 and porcao <= 5000:
          porcao = porcao *0.08
          return porcao

        elif porcao > 5000:
            print('Opção invalida, Tente novamente. Não aceitamos porções menores que 300ml ou maiores que 5l. tente novamnete!')
            continue



     except ValueError:
         print('Pare de digitar valores não numericos!')
         continue

#-------fim da função volume feijoada-----------------
#-------começo da função opção feijoada---------------

def cardapio():
     while True:
        cardapi = input('Escolha a opção de feijoada:\nb -Básica(Feijão + paiol + costelinha) \np - Premium(Feijão + paiol + costelinha + partes do porco) \ns - Suprema(Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon\n>>)')
        if cardapi == 'b':
             return 1.00
        elif cardapi == 'p':
             return 1.25
        elif cardapi == 's':
             return 1.50
        else:
            print('opção invalida. tente novamente!')
            continue


#-------fim da função opção feijoada------------------
#-------começo da função acompanhamento feijoada------
def acom():
    while True:
       acomp = input('deseja mais algum acompanhmento:\ 0- Não desejo mais acompanhamentos (encerrar pedido) \ 1- 200g de arroz \ 2- 150g de farofa especial\ 3- 100g de couve cozida \ 4- 1 laranja descascada \n>>')
       subtotal = 0
       if  acomp == '0':
         return subtotal
       elif  acomp == '1':
        subtotal + subtotal + 5
        continue
       elif  acomp == '2':
        subtotal + subtotal + 6
        continue
       elif  acomp == '3':
        subtotal + subtotal + 7
        continue
       elif  acomp == '4':
        subtotal + subtotal + 3
        continue
       else:
        print('opção invalida. tente novamente!')
        continue

#-------fim da função acompanhemento feijoada---------
#-------começo da main--------------------------------
print('bem-vindo ao restaurante de Lucas Garcia Laurentino da Silva')

print ('O valor total a ser pago foi de: R$ {:.2f}'.format(volume() * cardapio() + acom()))

#-------fim da main-----------------------------------
