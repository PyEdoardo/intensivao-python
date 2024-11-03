linguagem = input("Digite sua linguagem de programação favorita: ")

match linguagem: ##Estrutura mais moderna, pode ser uma ótima pedida pra manipular strings
    case "Javascript":
        print("Você pode virar desenvolvedor web!")
    case "Python":
        print("Você pode virar analista de dados!")
    case "PHP":
        print("Você pode virar desenvolvedor back end!")
    case "Java":
        print("Você pode criar aplicações multiplataforma e web!")
    case "C":
        print("Você pode virar desenvolvedor de baixo nível!")
    case "Assembly":
        print("Você pode desenvolver direto para o hardware!")
    
    case _: ##Esse _ significa default, ou seja, padrão, caso nenhum dos casos acima sejam atendidos, ele será o executado, parecido com o "Else"!
        print("Independente da linguagem você pode ser um ótimo dev!\nLembre-se que a linguagem é apenas uma ferramenta!")

        