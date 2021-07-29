def mensagem(txt, cor='normal', pular_linha=1):
    cores = {'vermelho': '\033[31m', 'verde': '\033[32m',
             'azul': '\033[34m', 'amarelo': '\033[33m', 'grifar': '\033[43m',
             'magenta': '\033[35m', 'normal': '\033[0m', 'limpa': '\033[m'}
    if pular_linha == 1:
        print(f'{cores[cor]}{txt}{cores["limpa"]}')
    else:
        print(f'{cores[cor]}{txt}{cores["limpa"]}', end=' ')


def mostrarForca(erros):
    if erros == 0:
        print(f'''
    +-+-+-+     \033[32mERROS: {erros}/6\033[m
    |
    |
    |
    |
    ''')

    elif erros == 1:
        print(f'''
    +-+-+-+     \033[32mERROS: {erros}/6\033[m
    |     O
    |
    |
    |
    ''')

    elif erros == 2:
        print(f'''
    +-+-+-+     \033[33mERROS: {erros}/6\033[m
    |     O
    |     |
    |
    |
    ''')

    elif erros == 3:
        print(f'''
    +-+-+-+     \033[33mERROS: {erros}/6\033[m
    |     O
    |    /|
    |
    |
    ''')

    elif erros == 4:
        print(f'''
    +-+-+-+     \033[33mERROS: {erros}/6\033[m
    |     O
    |    /|\\
    |
    |
    ''')

    elif erros == 5:
        print(f'''
     +-+-+-+     \033[31mERROS: {erros}/6\033[m
    |     O
    |    /|\\
    |    /
    |
    ''')

    elif erros == 6:
        print(f'''
    +-+-+-+     \033[31mERROS: {erros}/6\033[m
    |     O
    |    /|\\
    |    / \\
    |
    ''')


def mostrarRegras():
    mensagem('''
                        REGRAS
1- Palavra escolhida não poderá conter números;
2- Palavra escolhida deverá contêr ao menos 2 letras;
3- Sempre deverá ser chutado uma letra por vez e nunca uma palavra;
4- "Tema" não é obrigatório se a palavra for digitada manualmente;
5- Jogue sem moderacão!!!
    ''', 'amarelo')


def mostrarNomeDoJogo():
    mensagem(f'{"-------------------------":>29}')
    mensagem(f'{"|     JOGO DA FORCA     |":>29}')
    mensagem(f'{"-------------------------":>29}')


def mostrarSituacaoDaRodada():
    global erros, tema, palavra, palavra_escondida, letras_digitadas
    mostrarForca(erros)
    mensagem(f'TEMA: {tema}')
    mensagem(
        f'LETRAS: {sum([1 for el in palavra if el not in ["-", " "]])}')
    mensagem('Palavra:', 'azul', 0)
    for el in palavra_escondida:
        mensagem(el, 'azul', 0)
    print()
    letras_digitadas.sort()
    mensagem('Letras digitadas: ', 'normal', 0)
    mensagem(letras_digitadas, 'magenta')
    print()


def modoDeJogo():
    modo = ''
    while modo not in ['1', '2']:
        modo = input(
            'Criar tema e paralavra aleatória ou\n'
            'deseja escrever tema e palavra?\n\n'
            '[ 1 - ALEATÓRIA | 2 - ESCREVER ]: ')
        print('-' * 43)
    return modo


def continuarJogo():
    jogar_novamente = input('DESEJA JOGAR NOVAMENTE? [1 - SIM | 2 - NAO]\n'
                            'OPCAO: ')

    while jogar_novamente not in ['1', '2']:
        mensagem('Por favor, digite uma opcao válida!', 'vermelho')
        jogar_novamente = input('DESEJA JOGAR NOVAMENTE? [1 - SIM | 2 - NAO]\n'
                                'OPCAO: ')
    if jogar_novamente == '1':
        return True
    return False


def definirTemaPalavra():
    if modoDeJogo() == '1':
        tema, palavra = gerarTemaPalavraAleatoria()
    else:
        tema = input('DIGITE O TEMA: ').strip().upper()
        palavra = input('DIGITE A PALAVRA: ')
        # Impedindo que seja digitado apenas uma letra ou números na palavra;
        # Sendo assim as duas condições precisam ser False para sair do while.
        while len(palavra) < 2 or bool([True for el in palavra if el.isdigit()]):
            mensagem('*POR FAVOR, DIGITE UMA PALAVRA VÁLIDA*', 'vermelho')
            palavra = input('DIGITE A PALAVRA: ')
        palavra = tratarString(palavra)
    return tema, palavra


def gerarTemaPalavraAleatoria():
    from random import choice
    banco_de_palavras = {
        'FRUTA': [
            'ABACATE', 'ABACAXI', 'ACEROLA', 'BANANA', 'MACA', 'CAJU',
            'CEREJA', 'FIGO', 'FRAMBOESA', 'GOIABA', 'KIWI', 'LARANJA',
            'LIMAO', 'MAMAO', 'MELAO', 'PESSEGO', 'TANGERINA'
        ],
        'ANIMAL': [
            'ABELHA', 'BALEIA', 'CACHORRO', 'CAMALEAO', 'DRAGAO-DE-KOMODO',
            'DROMEDARIO', 'EMA', 'ELEFANTE', 'FOCA', 'FLAMINGO', 'GOLFINHO',
            'HIPOPOTAMO', 'JACARE', 'LEAO', 'LAGARTO', 'MACACO', 'OVELHA',
            'PAPAGAIO', 'RAPOSA', 'RATO', 'TARTARUGA', 'TAMANDUA-BANDEIRA',
            'URSO-POLAR', 'VACA', 'ZEBRA'
        ],
        'COR': [
            'AMARELO', 'AZUL', 'BRANCO', 'LARANJA', 'VERDE', 'ROXO',
            'VERMELHO', 'CINZA', 'PRETO', 'VIOLETA', 'ROSA', 'LILAS', 'MARROM'
        ],
        'MARCA DE CARRO': [
            'ASTON MARTIN', 'AUDI', 'BENTLEY', 'BMW', 'CHEVROLET', 'CHRYSLER',
            'CITROEN', 'DODGE', 'FERRARI', 'FIAT', 'FORD', 'HONDA', 'HYUNDAI',
            'JAC', 'JAGUAR', 'JEEP', 'LAMBORGHINI', 'LAND ROVER', 'LEXUS',
            'MASERATI', 'MCLAREN', 'MERCEDEZ-BENZ', 'MINI', 'MITSUBISHI,',
            'NISSAN', 'PEUGEOT', 'PORSCHE', 'RENAULT', 'SUBARU', 'SUZUKI',
            'TOYOTA', 'TROLLER', 'VOLKSWAGEN', 'VOLVO', 'YAMAHA'
        ],
        'ESTADO DO BRASIL': [
            'ACRE', 'ALAGOAS', 'AMAPA', 'AMAZONAS', 'BAHIA', 'CEARA', 'GOIAS',
            'ESPIRITO SANTO', 'MARANHAO', 'MATO GROSSO', 'MATO GROSSO DO SUL',
            'MINAS GERAIS', 'PARA', 'PARAIBA', 'PARANA', 'PERNAMBUCO', 'PIAUI',
            'RIO DE JANEIRO', 'RIO GRANDE DO SUL', 'RONDONIA', 'RORAIMA',
            'SANTA CATARINA', 'SAO PAULO', 'SERGIPE', 'TOCANTINS',
            'DISTRITO FEDERAL'
        ]
    }

    tema = choice(list(banco_de_palavras))
    palavra = choice(banco_de_palavras[tema])
    return tema, palavra


def tratarString(elemento):
    import unicodedata
    # Removendo espacos adicionais no meio e no fim da palavra(ou letra).
    elemento = elemento.split()
    # Juntando palavras e adicionando um espaco entre elas.(Ou na letra)
    elemento = ' '.join(elemento)
    # Removendo caracteres especiais / padronizando no modelo 'UTF-8'
    return unicodedata.normalize('NFD', elemento).encode('ascii', 'ignore') \
        .decode('utf-8').upper()


def validarChute(letra):
    global letras_digitadas, palavra
    # Verificando se o usuario digitou apenas uma letra e tambem se a
    # letra digitada é um caractere nao necessario para adivinhar a palavra.
    if len(letra) == 1 and letra not in [' ', '-']:
        if letra not in letras_digitadas:
            # Se a letra ainda nao foi digitada e esta presente na
            # palavra secreta, retorna True para considerar um chute válido.
            if letra in palavra:
                return 'Chute valido'
    return 'Chute invalido'


def adicionarLetraChutada(letra):
    global letras_digitadas
    letras_digitadas.append(letra)
    return letras_digitadas


def marcarAcerto():
    global letra, palavra, palavra_escondida
    mensagem('Acertou!!!', 'verde')
    # Adiciona a letra digitada em palavra_escondida, se a variavel percorrida
    # (palavra), letra por letra for igual a letra digitada, senao coloca o
    # mesmo elemento novamente no lugar para nao alterar os demais itens.
    palavra_escondida = [letra
                         if letra == list(palavra)[idx] else el
                         for idx, el in enumerate(palavra_escondida)
                         ]
    # Retorna palavra_escondida atualizada
    return palavra_escondida


def marcarErro():
    global erros, letras_digitadas, letra
    codigo_erro = checarTipoDeErro()
    if codigo_erro in [1, 2, 3]:
        erros += 1
        if codigo_erro == 3:
            letras_digitadas = adicionarLetraChutada(letra)
    return erros, letras_digitadas


def checarTipoDeErro():
    global letra, letras_digitadas
    # Verifica se o usuario apena digitou "Enter" sem ter escrito nada.
    if len(letra) == 0:
        codigo_de_erro = 0
    # Verifica se o conteudo é uma palavra ou um número.
    elif len(letra) > 1 or letra.isdigit():
        codigo_de_erro = 1
    elif letra in letras_digitadas:
        codigo_de_erro = 2
    else:
        codigo_de_erro = 3
    return codigo_de_erro


def mostrarTipoErro():
    tipos_erros = ['Por favor, experimente chutar alguma letra.\n'
                   'Nenhum ponto será descontado.',
                   'Por favor, chute apenas letras!\n'
                   'Você está perdendo pontos.',
                   f'Você já chutou a letra "{letra}", cuidado. Errou.',
                   f'Não possui a letra "{letra}". Errou.'
                   ]
    tipo_erro = checarTipoDeErro()
    mensagem(tipos_erros[tipo_erro], 'vermelho')


def checarVitoria(qnt_erros, palavra):
    if qnt_erros < 6:
        mensagem(f'Parabens! Voce acertou a palavra {palavra}!!!', 'verde')
        print('-' * 43)
        return
    mensagem(f'Voce perdeu, a palavra era {palavra}', 'vermelho')
    print('-' * 43)


continuar = True
mostrarRegras()
while continuar:
    mostrarNomeDoJogo()
    erros = 0
    tema, palavra = definirTemaPalavra()
    print()
    # Listando letra a letra para usar como gabarito
    gabarito = list(palavra)
    # Recebe "_" se a palavra não conter espaços ou hífens
    palavra_escondida = ['_' if el not in ['-', ' '] else el
                         for el in gabarito]
    letras_digitadas = []
    # Finaliza a rodada se o usuario errar 6 vezes ou
    # acertar todas as letras
    while erros < 6 and palavra_escondida != gabarito:
        mostrarSituacaoDaRodada()
        letra = tratarString(input('Digite uma letra: '))
        if validarChute(letra) == 'Chute valido':
            palavra_escondida = marcarAcerto()
            letras_digitadas = adicionarLetraChutada(letra)
        else:
            mostrarTipoErro()
            erros, letras_digitadas = marcarErro()
            if checarTipoDeErro() == 3:
                letras_digitadas = adicionarLetraChutada(letra)
        print('-' * 43)
    mostrarSituacaoDaRodada()
    checarVitoria(erros, palavra)
    continuar = continuarJogo()

mensagem('Obrigado por jogar O Jogo da Forca!', 'grifar')
