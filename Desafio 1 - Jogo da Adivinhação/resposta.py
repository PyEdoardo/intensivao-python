import random

numero_secreto = random.randint(1, 20) ##Gera um número secreto entre 1 e 20
tentativas = 5
tentativa_atual = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 20. Você tem 5 tentativas.")

while tentativa_atual < tentativas: ##Laço enquanto o usuário ainda tiver tentativas restantes
    tentativa_atual += 1 ##Equivalente ao "tentatida_atual = tentatida_atual + 1"
    palpite = int(input(f"Tentativa {tentativa_atual}: Digite seu palpite: "))

    if palpite < numero_secreto:
        print("O número é maior que seu palpite.")
    elif palpite > numero_secreto:
        print("O número é menor que seu palpite.")
    else:
        print("Parabéns! Você adivinhou o número!")
        break  ##Sai do laço se o número for adivinhado
else:
    print(f"Você perdeu! O número secreto era {numero_secreto}.") ##Executa se o laço terminar sem um break (número não foi adivinhado)

    