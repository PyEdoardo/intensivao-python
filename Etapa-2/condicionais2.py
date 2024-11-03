peso = 70
altura = 1.80

imc = peso / (altura **2) #Podemos usar os () para criar uma prioridade matemática no cálculo, onde o bloco dos () será executado antes
                          #O Símbolo ** é a expressão de potência, onde elevamos a altura ao quadrado para depois ser dividido!

if imc < 18.5: #Se o IMC for menor que 18.5
    print(f"Abaixo do Peso!\nIMC: {imc}")

elif imc < 24.9: #O Elif significa "Ou" ou "Se então", podendo ter vários desses elifs dependendo do programa!
    print(f"Peso Normal!\nIMC: {imc}")

elif imc < 29.9: #Se o IMC for menor que 29.9
    print(f"Sobrepeso!\nIMC: {imc}")

else:
    print(f"Obesidade!\nIMC: {imc}") #Caso nenhuma condição acima seja verdadeira, esse else será rodado!
