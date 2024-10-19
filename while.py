import time
import random

#Apostador Ira entrar com o nome
name = str(input("Ola Apostador, Infome Seu Nome: "))
time.sleep(2)
print("Seja Bem Vindo", name)

#Aqui o usuario ira colocar o valor de inicio na banca
banca = float(input("Digite O Valor para adicionar ao seu saldo:R$ "))
aposta = float(input("Digite O valor de Sua Aposta:R$"))

#ira aparacer o saldo atual do usuario
time.sleep(3)
sobra = (banca - aposta)
print("Seu Saldo Atual é:R$", sobra)

while sobra > 0:
    #Numeros que serao sorteados
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    #Numero escolhido Pelo usuário
    n = int(input("Digite seu número da sorte entre 0 e 20: "))
    time.sleep(2)
    print("Seu Numero da Sorte É: ",n)

    #Numero Sorteado
    time.sleep(4)
    s = random.choice(numeros)
    print("O número Sorteado Foi: ",s)

    #ira verificar se o numero do usuario foi sorteado
    time.sleep(3)
    if n == s:
        print("Parabéns Apostador, Seu numero foi sorteado!")
        print("+R$", aposta)
    else:
        print("Infelizmente Seu número Nao foi sorteado!", "-R$", aposta)

    time.sleep(2)
    #ira perguntar se o usuario deseja continuar
    c = str(input("Deseja Continuar? :"))
    if c == "nao":
        break
