alunos = {

}

while True: ##Quando você quiser deixar um loop realmente infinito e que não dependa de nenhuma condição, crie um loop assim!
            ##Se quiser quebrar o loop, use o "break".
    opcoes = print("Opções: (1) Mostra alunos, (2) Adiciona aluno, (3) Remove Aluno, (4) Procura um aluno, (0) Encerra o Programa.")
    opcao = int(input("\nDigite a opção: "))
    if opcao == 0:
        print("Encerrando Programa...")
        break
    elif opcao == 1:
        print(alunos)
    elif opcao == 2:
        nome = input("Qual o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        alunos[nome] = idade
        print(f'Aluno {nome} adicionado!')
    elif opcao == 3:
        chave_deletar = input("Escreva o aluno que seja deletar: ")
        alunos.pop(chave_deletar)
        print(f'Aluno Deletado!')
    elif opcao == 4:
        procurar_aluno = input("Digite o nome do aluno: ")
        print(f'Aluno: {alunos.get(procurar_aluno)}')
    else:
        print("Essa opção não existe!")


