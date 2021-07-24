def mostrar(pontos, carta):
    if len(carta) > 1:
        print(f'Voce tirou as cartas {carta}\n')
    else:
        print(f'Voce tirou a carta {carta}\n')
    if pontos < 21:
        print(f'Esta com \033[33m{pontos}\033[m pontos.\n')
    elif pontos == 21:
        print(f'Esta com \033[32m{pontos}\033[m pontos.\n')
    else:
        print(f'Esta com \033[31m{pontos}\033[m pontos.\n')


def sortear_carta():
    from random import choice
    carta = choice(criar_baralho())
    if carta == 'A':
        return carta, 1
    elif carta in ['J', 'Q', 'K']:
        return carta, 10
    return carta, int(carta)


def jogada(jogador, numero):
    print('-'*40)
    print(f'Jogador {numero}: {jogador}\n')
    cartas_iniciais = [sortear_carta()for _ in range(2)]
    carta = [card[0] for card in cartas_iniciais]
    pontos = sum([ponto[1] for ponto in cartas_iniciais])
    mostrar(pontos, carta)
    while True:
        opt = ''
        while opt not in ['S', 'N']:
            opt = input('Pedir mais uma carta?\n'
                        '[S | N]: ').strip().upper()
        if opt == 'N':
            break
        else:
            carta, ponto = sortear_carta()
            pontos += ponto
            mostrar(pontos, carta)
    return pontos


def criar_baralho():
    baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               'J', 'Q', 'K']
    return baralho


def verificar_vencedor(jodadores):
    lista_sorteada = sorted(jodadores.items(),
                            key=lambda x: x[1], reverse=True)
    ranking = [jogador for jogador in lista_sorteada if jogador[1] > 21]
    lista_sorteada = sorted(jodadores.items(), key=lambda x: x[1])
    ranking.extend([jogador
                   for jogador in
                    lista_sorteada[:len(lista_sorteada)-len(ranking)]])
    return ranking[::-1]


def main():
    nomes_jogadores = [input(f'Nome Participante {i+1}: ').title().strip()
                       for i in range(int(input('Numero de participantes: ')))]
    jogadores = {}
    for n, nome in enumerate(nomes_jogadores):
        jogadores[nome] = jogada(nome, n+1)
    ranking = verificar_vencedor(jogadores)
    print('-'*31)
    print(f'{"|":<11}{"BlackJack":19}{"|"}')
    print('-' * 31)
    for pos, jogador in enumerate(ranking):
        print(f'{str(pos+1)+"º":<4}{jogador[0]:<10}{"-"} '
              f'{jogador[1]:>3} pontos')


if __name__ == '__main__':
    main()
