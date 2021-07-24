def checar_disponibilidade_turno(tabuleiro):
    for linha in tabuleiro:
        for el in linha:
            if isinstance(el, int):
                return True
            else:
                pass
    return False


def traduzir_jogada_no_tabuleiro(jogada, tabuleiro):
    for i, linha in enumerate(tabuleiro):
        for j, el in enumerate(linha):
            if el == jogada:
                jogada = [i, j]
                break
    return jogada


def checar_disponibilidade_jogada(jogador_atual, jogada, tabuleiro):
    if isinstance(tabuleiro[jogada[0]][jogada[1]], int):
        tabuleiro[jogada[0]][jogada[1]] = jogador_atual
        print('Jogada efetuada!\033[m')
    return tabuleiro


def mostar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print()
        for el in linha:
            if el == 'X':
                print('\033[34mX\033[m', end=' | ')
            elif el == 'O':
                print('\033[35mO\033[m', end=' | ')
            else:
                print(el, end=' | ')
    print()
    print()


def checar_vitoria(jogador_atual, tabuleiro):
    vitoria = [
        jogador_atual == tabuleiro[0][0] and jogador_atual == tabuleiro[0][
            1] and jogador_atual == tabuleiro[0][2],
        jogador_atual == tabuleiro[1][0] and jogador_atual == tabuleiro[1][
            1] and jogador_atual == tabuleiro[1][2],
        jogador_atual == tabuleiro[2][0] and jogador_atual == tabuleiro[2][
            1] and jogador_atual == tabuleiro[2][2],
        jogador_atual == tabuleiro[0][0] and jogador_atual == tabuleiro[1][
            0] and jogador_atual == tabuleiro[2][0],
        jogador_atual == tabuleiro[0][1] and jogador_atual == tabuleiro[1][
            1] and jogador_atual == tabuleiro[2][1],
        jogador_atual == tabuleiro[0][2] and jogador_atual == tabuleiro[1][
            2] and jogador_atual == tabuleiro[2][2],
        jogador_atual == tabuleiro[0][0] and jogador_atual == tabuleiro[1][
            1] and jogador_atual == tabuleiro[2][2],
        jogador_atual == tabuleiro[0][2] and jogador_atual == tabuleiro[1][
            1] and jogador_atual == tabuleiro[2][0]
    ]
    if True in vitoria:
        return True
    return False


def jogada_realizada(jogador_atual, tabuleiro, jogada_invalida=True):
    while jogada_invalida:
        try:
            if jogador_atual == 'X':
                print('\033[34mPlayer 1(X):', end=' ')
            else:
                print('\033[35mPlayer 2(O):', end=' ')
            jogada = int(input())
            jogada = traduzir_jogada_no_tabuleiro(jogada, tabuleiro)
            tabuleiro = checar_disponibilidade_jogada(jogador_atual,
                                                      jogada, tabuleiro)
        except (ValueError, Exception):
            print('\033[31mPosição inválida! Tente novamente!\033[m')
            mostar_tabuleiro(tabuleiro)
        else:
            jogada_invalida = False
    return tabuleiro


def main():
    tabuleiro = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ]

    jogador1 = 'X'
    jogador2 = 'O'

    turno_disponivel = True

    while turno_disponivel:
        mostar_tabuleiro(tabuleiro)
        tabuleiro = jogada_realizada(jogador1, tabuleiro)
        mostar_tabuleiro(tabuleiro)
        ganhou = checar_vitoria(jogador1, tabuleiro)

        if ganhou:
            print('\033[34mJogador 1 venceu!\033[m')
            break

        turno_disponivel = checar_disponibilidade_turno(tabuleiro)

        if turno_disponivel:
            tabuleiro = jogada_realizada(jogador2, tabuleiro)
            ganhou = checar_vitoria(jogador2, tabuleiro)

            if ganhou:
                mostar_tabuleiro(tabuleiro)
                print('\033[35mJogador 2 venceu!\033[m')
                break
        else:
            print('\033[33mDeu velha!\033[m')


main()
