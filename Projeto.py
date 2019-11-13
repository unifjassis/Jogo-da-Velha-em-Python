import os

def fimJogo():
    print("O JOGO ACABOU!\n")
    exit()

def main():
    global matriz                                                   # *********DEIXEI A MATRIZ GLOBAL PQ EU N SOUBE USAR RETURN NELA**********
    global matriz2

    matriz = [["A1", "A2", "A3", "A4", "A5"],
              ["B1", "B2", "B3", "B4", "B5"],
              ["C1", "C2", "C3", "C4", "C5"],                       # MATRIZ ORIGINAL
              ["D1", "D2", "D3", "D4", "D5"],
              ["E1", "E2", "E3", "E4", "E5"]]

    matriz2 = [["A1", "A2", "A3", "A4", "A5"],
              ["B1", "B2", "B3", "B4", "B5"],
              ["C1", "C2", "C3", "C4", "C5"],                       # MATRIZ COPIA PARA MANIPULAR DEPOIS
              ["D1", "D2", "D3", "D4", "D5"],
              ["E1", "E2", "E3", "E4", "E5"]]

    introdução()                                                    # CHAMA INTRODUÇÃO E IDENTIFICA JOGADORES
    Amatriz()                                                       # CHAMA A FUNÇÃO QUE LE A MATRIZ
    rodada()                                                        # CHAMA A FUNÇÃO QUE PEDE A JOGADA

def introdução():
    print("\nBem vindo ao jogo da velha 5x5!\n")                    # EXIBE BOAS VINDAS

    global jogador1, jogador2

    jogador1 = input("Digite o 1 jogador: ")                        # PERGUNTA O NOME DOS JOGADORES
    jogador2 = input("Digite o 2 jogador: ")
    print("\nATENÇÃO, CASO JOGUE EM UMA POSIÇÃO ERRADA, PERDERA A VEZ!\n")

def Amatriz():                                                      # FUNÇÃO QUE PRINTA A MATRIZ

    print()
    for linha in range(0, 5):                                       # PERCORRE A MATRIZ EM LINHA
        for coluna in range(0, 5):                                  # PERCORRE A MATRIZ EM COLUNA
            print(f"[{matriz[linha][coluna]:^5}]", end='')          # EXIBE CADA ELEMENTO DA MATRIZ
        print()

def rodada():
    jogada = 1                                                      # CONTADOR DE RODADAS
    l = 0                                                           # CONTADOR DE INDICE LINHA
    c = 0                                                           # CONTADOR DE INDICE COLUNA

    while jogada <= 25:                                             # LIMITE MAXIMO DE JOGADAS

        global desenho                                              # VARIAVEIS GLOBAIS PARA USAR EM OUTRAS FUNÇOES
        global letra
        global posição
        global jogador

        if jogada % 2 == 0:                                         # EXIBE O JOGADOR QUE DEVE JOGAR
            jogador = "\nVez de %s" %jogador1
            print(jogador)
            desenho = "O"                                           # DESENHO JOGADOR 1 = BOLINHA

        if jogada % 2 != 0:
            jogador = "\nVez de %s" %jogador2
            print(jogador)
            desenho = "X"                                           # DESENHO JOGADOR 2 = XIS

        posição = input("Onde deseja jogar: ")                      # QUAL LETRA O USUARIO QUER JOGAR

        for linha in matriz:                                        # PERCORRE A MATRIZ
            for letra in linha:                                     # PERCORRE AS LETRAS DA MATRIZ

                if letra == posição:                                # VERIFICA SE A ENTRADA ESTA CORRETA
                    if posição == "X" or posição == "O":
                        print("Jogada incorreta!\n")                # CASO NAO SEJA, IMPRIME ERRO
                        print("Perdeu a Vez!\n")

                    else:
                        matriz[l][c] = desenho                      # CASO ESTEJA É TROCADA PELO DESENHO DO JOGADOR

                c += 1                                              # INCREMENTA COLUNA
            l += 1                                                  # INCREMENTA LINHA
            c = 0                                                   # REINICIA A COLUNA
        l = 0                                                       # REINICIA A LINHA
        jogada += 1

        Amatriz()                                                   # PRINTA A MATRIZ DE NOVO, JA SUBSTITUIDA
        vitoria()                                                   # CHAMA A FUNÇÃO QUE VERIFICA VITORIA NO JOGO

    if jogada > 25:
        print("Empate!\n")                                          # QUANDO ATINGE O MAXIMO DE JOGADAS SEM VENCEDOR
        fimJogo()

def vitoria():                                                      # VERIFICA CONDIÇÃO DE VITORIA

    #********************** CONDIÇÃO EM LINHA *********************

    l = 0                                                           # CONTADOR DE LINHA
    c = 0                                                           # CONTADOR DE COLUNA

    xis = ["X", "X", "X", "X"]                                      # PRE CONDIÇÃO DE VITORIA DE LINHA EM X E EM BOLINHA
    bolinha = ["O", "O", "O", "O"]

    for linha in matriz:                                            # PERCORRE LINHA POR LINHA DA MATRIZ

        xis.append(matriz2[l][4])                                   # ADICIONA O ULTIMO ELEMENTO DA LINHA EM XIS
        bolinha.append(matriz2[l][4])                               # ADICIONA O ULTIMO ELEMENTO DA LINHA EM BOLINHA

        #print("Xis ", xis)
        #print("Bolinha ", bolinha)                                 # TESTES
        #print("Linha ", linha)

        if set(linha) == set(xis):                                  # COMPARA A LINHA ATUAL COM XIS E BOLINHA
            print("Vitoria em linha!\n")                            # CASO SEJA, CHAMA VITORIA
            print("Vitoria de: %s\n" % jogador2)
            fimJogo()

        elif set(linha) == set(bolinha):
            print("Vitoria em linha!\n")                            # CASO SEJA, CHAMA VITORIA
            print("Vitoria de: %s\n" % jogador1)
            fimJogo()

        del(xis[4])                                                 # REMOVE O ULTIMO ELEMENTO DE XIS
        del(bolinha[4])                                             # REMOVE O ULTIMO ELEMENTO DE BOLINHA

        xis.insert(0, matriz2[l][0])                                # ADICIONA O PRIMEIRO ELEMENTO DA LINHA EM XIS
        bolinha.insert(0, matriz2[l][0])                            # ADICIONA O PRIMEIRO ELEMENTO DA LINHA EM BOLINHA

        #print("Xis ", xis)
        #print("Bolinha ", bolinha)                                 # TESTES
        #print("Linha ", linha)

        if set(linha) == set(xis):                                  # COMPARA A LINHA ATUAL COM XIS E BOLINHA
            print("Vitoria em linha!\n")                            # CASO SEJA, CHAMA VITORIA
            print("Vitoria de: %s\n" % jogador2)                    # EXIBE O JOGADOR VITORIOSO
            fimJogo()

        elif set(linha) == set(bolinha):
            print("Vitoria em linha!\n")                            # CASO SEJA, CHAMA VITORIA
            print("Vitoria de: %s\n" % jogador1)                    # EXIBE O JOGADOR VITORIOSO
            fimJogo()

        del (xis[0])                                                # REMOVE O PRIMEIRO ELEMENTO DE XIS
        del (bolinha[0])                                            # REMOVE O PRIMEIRO ELEMENTO DE BOLINHA

        l+=1                                                        # INCREMENTA L E MUDA PRA PROXIMA LINHA
    l = 0                                                           # ZERA L PARA SER USADO EM OUTRAS VERIFICAÇOES

    #**************************** CONDIÇÃO EM COLUNA **************************

    i = 0                                                           # CONTADOR DE LINHA NA CONDIÇÃO COLUNA
    j = 0                                                           # CONTADOR DE ELEMENTONA CONDIÇÃO COLUNA

    trueX = []                                                      # CASO TENHA 4 TRUE É VITORIA
    trueO = []                                                      # CASO TENHA 4 TRUE É VITORIA

    while j < 5:                                                    # CONTADOR DE LINHAS
        while i < 5:                                                # CONTADOR DE COLUNAS

            if matriz[l][c] == "X":                                 # COMPARA SE É X
                trueX.append("True")                                # CASO SEJA ADICIONA TRUE EM TRUEX

                if len(trueX) == 4:                                 # COM 4 ITENS EM TRUX CHAMA FUNÇÃO VITORIA
                    print("Vitoria em coluna!\n")
                    print("Vitoria de: %s\n" %jogador2)
                    fimJogo()

            elif matriz[l][c] != "X":                               # CASO NAO SEJA LIMPA TRUEX
                trueX.clear()                                       # É IMPORTANTE LIMPAR PQ SAO 5 ELEMENTOS NA COLUNA
                                                                    # E COM 4 ELEMENTOS JA É VITORIA
            elif matriz[l][c] == "O":
                trueO.append("True")

                if len(trueO) == 4:                                 # COM 4 ELEMENTOS EM TRUEO CHAMA FUNÇÃO VITORIA
                    print("Vitoria em coluna!\n")
                    print("Vitoria de: %s\n" % jogador1)            # EXIBE O JOGADOR VITORIOSO
                    fimJogo()

            elif matriz[l][c] != "O":                               # CASO NAO SEJA LIMPA TRUEO
                trueO.clear()                                       # É IMPORTANTE LIMPAR PQ COM APENAS 4 JA GANHA

            l+= 1                                                   # INCREMENTA L PARA BUSCAR NA MATRIZ
            i+= 1                                                   # INCREMENTA I PARA AVANÇAR COLUNA
        c+= 1                                                       # INCREMENTA C PARA BUSCAR NA MATRIZ
        l = 0                                                       # ZERA L PARA REINICIAR A BUSCA EM UMA NOVA LINHA
        i = 0                                                       # ZERA I PARA REINICIAR BUSCA EM UMA NOVA COLUNA
        j+= 1                                                       # INCREMENTA J PARA AVANÇAR LINHAS
    j = 0                                                           # ZERA J PARA REINICIAR A CONTAGEM DE LINHAS CASO NECESSARIO

    # ************************CONDIÇÃO EM TRANSVERSAL***********************

    # **************** CONDIÇÃO DE VITORIA COMPARA TODOS OS ELEMENTOS DA TRANSVERSAL JA DEFINIDOS **************

    # ********************* ESQUERDA PRA DIREITA ********************

    l = 0                                                           # CONTADOR DE LINHA
    c = 0                                                           # CONTADOR DE COLUNA CRESCENTE
    o = 4                                                           # CONTADOR DE COLUNA DECRESCENTE

    # PRIMEIRA VERIFICAÇÃO NA TRANSVERSAL XIS DE BAIXO
    if matriz[l + 1][c] == "X" \
         and matriz[l + 2][c + 1] == "X" \
         and matriz[l + 3][c + 2] == "X" \
         and matriz[l + 4][c + 3] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL XIS DE BAIXO
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

    # SEGUNDA VERIFICAÇÃO NA TRANSVERSAL XIS DO MEIO, QUE VARIA ENTRE OS 4 PRIMEIROS ELEMENTOS OU OS 4 ULTIMOS
    elif matriz[l][c] == "X" \
         and matriz[l + 1][c + 1] == "X" \
         and matriz[l + 2][c + 2] == "X" \
         and matriz[l + 3][c + 3] == "X"\
            or matriz[l + 1][c + 1] == "X"\
            and matriz[l + 2][c + 2] == "X"\
            and matriz[l + 3][c + 3] == "X"\
            and matriz[l + 4][c + 4] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL XIS DO MEIO
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

    # TERCEIRA VERIFICAÇÃO NA TRANSVERSAL XIS DE CIMA
    elif matriz[l][c+1] == "X" \
         and matriz[l + 1][c + 2] == "X" \
         and matriz[l + 2][c + 3] == "X" \
         and matriz[l + 3][c + 4] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL XIS DE CIMA
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

    # PRIMEIRA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DE BAIXO
    elif matriz[l + 1][c] == "O" \
         and matriz[l + 2][c + 1] == "O" \
         and matriz[l + 3][c + 2] == "O" \
         and matriz[l + 4][c + 3] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL BOLINHA DE BAIXO
        print("Vitoria de: %s\n" %jogador1)
        fimJogo()

    # SEGUNDA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DO MEIO QUE VARIA ENTRE OS 4 PRIMEIROS ELEMENTOS OU OS 4 ULTIMOS
    elif matriz[l][c] == "O" \
         and matriz[l + 1][c + 1] == "O" \
         and matriz[l + 2][c + 2] == "O" \
         and matriz[l + 3][c + 3] == "O"\
            or matriz[l + 1][c + 1] == "O"\
            and matriz[l + 2][c + 2] == "O"\
            and matriz[l + 3][c + 3] == "O"\
            and matriz[l + 4][c + 4] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL BOLINHA DO MEIO
        print("Vitoria de: %s\n" % jogador1)
        fimJogo()


    # TERCEIRA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DE CIMA
    elif matriz[l][c+1] == "O" \
         and matriz[l + 1][c + 2] == "O" \
         and matriz[l + 2][c + 3] == "O" \
         and matriz[l + 3][c + 4] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL BOLINHA DE CIMA
        print("Vitoria de: %s\n" % jogador1)
        fimJogo()


    #******************************** DA DIREITA PRA ESQUERDA ****************************

    # PRIMEIRA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DE CIMA
    elif matriz[l][o - 1] == "O" \
         and matriz[l + 1][o - 2] == "O" \
         and matriz[l + 2][o - 3] == "O" \
         and matriz[l + 3][o - 4] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DE CIMA
        print("Vitoria de: %s\n" % jogador1)
        fimJogo()

    # SEGUNDA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DO MEIO QUE VARIA ENTRE OS 4 PRIMEIROS E OS 4 ULTIMOS
    elif matriz[l][o] == "O" \
         and matriz[l + 1][o - 1] == "O" \
         and matriz[l + 2][o - 2] == "O" \
         and matriz[l + 3][o - 3] == "O"\
            or matriz[l + 1][o - 1] == "O"\
            and matriz[l + 2][o - 2] == "O"\
            and matriz[l + 3][o - 3] == "O"\
            and matriz[l + 4][o - 3] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DO MEIO
        print("Vitoria de: %s\n" % jogador1)
        fimJogo()

    # TERCEIRA VERIFICAÇÃO NA TRANSVERSAL BOLINHA DE BAIXO
    elif matriz[l+1][o] == "O" \
         and matriz[l + 2][o - 1] == "O" \
         and matriz[l + 3][o - 2] == "O" \
         and matriz[l + 4][o - 3] == "O":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DE BAIXO
        print("Vitoria de: %s\n" % jogador1)
        fimJogo()

    # PRIMEIRA VERIFICAÇÃO NA TRANSVERSAL XIS DE CIMA
    elif matriz[l][o - 1] == "X" \
         and matriz[l + 1][o - 2] == "X" \
         and matriz[l + 2][o - 3] == "X" \
         and matriz[l + 3][o - 4] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DE CIMA
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

    # SEGUNDA VERIFICAÇÃO NA TRANSVERSAL XIS DO MEIO QUE VARIA ENTRE OS 4 PRIMEIROS ELEMENTOS E OS ULTIMOS 4
    elif matriz[l][o] == "X" \
         and matriz[l + 1][o - 1] == "X" \
         and matriz[l + 2][o - 2] == "X" \
         and matriz[l + 3][o - 3] == "X"\
            or matriz[l + 1][o - 1] == "X"\
            and matriz[l + 2][o - 2] == "X"\
            and matriz[l + 3][o - 3] == "X"\
            and matriz[l + 4][o - 4] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DO MEIO
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

    # TERCEIRA VERIFICAÇÃO NA TRANSVERSAL XIS DE BAIXO
    elif matriz[l+1][o] == "X" \
         and matriz[l + 2][o - 1] == "X" \
         and matriz[l + 3][o - 2] == "X" \
         and matriz[l + 4][o - 3] == "X":
        print("\nVitoria transversal!\n")                                 # DIAGONAL DE BAIXO
        print("Vitoria de: %s\n" % jogador2)
        fimJogo()

main()