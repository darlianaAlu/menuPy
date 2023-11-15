import funcoes
opcao = 0

menu = "(1) Ler sequência\n(2) Exibir elementos da sequência\n(3) Soma dos elementos da sequência\n(4) Produto simples\n(5) Intercala\n(6) SAIR\n"
while opcao!=6:
    opcao = int(input(menu))
    if opcao == 1:
        N = int(input("Informe a quantidade de elementos do Vetor: "))
        S = funcoes.leSequencia(N)
    elif opcao == 2:
         print("(1) Exibir impares")
         print("(2) Exibir pares")
         print("(3) Exibir vetor")
         funcoes.exibeElementos(S, input())
    elif opcao == 3:
         print(funcoes.somaSequencia(S))
    elif opcao == 4:
         print(funcoes.produtoSimples(S))
    elif opcao ==5:
         print("Informe a quantidade de elementos do 2º Vetor:")
         T = funcoes.leSequencia(s.nextInt())
         funcoes.intercala(S, T)
    elif opcao == 6:
            print('Encerrando Programa...')
