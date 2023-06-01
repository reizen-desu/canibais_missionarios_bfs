"""
As regras são de que o barco pode levar no máximo 2 pessoas e que sempre devem ter mais missionários do que canibais em uma dada margem do rio.
Para o barco: 1 (está na margem) ou 0 (está do outro lado).
[Missionarios, Canibais, Barco]
Estado Inicial = [3,3,1] -> Todos os missionários e canibais + o barco
Estado Final = [0,0,0] -> Todos passaram para a outra margem
"""

# Declaração das margens do rio e do número inicial de missionários e canibais
MARGEM_ESQUERDA = 1
MARGEM_DIREITA = 0
NUM_MISSIONARIOS = 3
NUM_CANIBAIS = 3


def exibir_instrucoes():
    """
    Exibe as instruções para leitura dos estados com destaque adicional e negrito.
    """
    print("===================================================================")
    print("Instruções para leitura dos estados:")
    print("\033[1;34m\033[1mTexto em azul:\033[0m O barco está na margem esquerda")
    print("\033[1;33m\033[1mTexto em amarelo:\033[0m O barco está na margem direita")
    print(
        "\033[1;30m\033[1mTexto em cinza:\033[0m Possibilidades com estados já explorados")
    print("===================================================================")


def obter_movimentos_possiveis(estado, explorados):
    """
    Retorna uma lista dos movimentos possíveis (viagens permitidas)
    em um dado estado do problema.
    Os estados já explorados serão impressos em vermelho.
    """
    possibilidades = []
    missionarios, canibais, posicao_barco = estado

    print("Estado:", estado)
    margem_destino = MARGEM_DIREITA if posicao_barco == MARGEM_ESQUERDA else MARGEM_ESQUERDA

    for i in range(1, 3):
        for j in range(0, i + 1):
            if posicao_barco == MARGEM_ESQUERDA:
                missionarios_novos = missionarios - j
                canibais_novos = canibais - (i - j)
            else:
                missionarios_novos = missionarios + j
                canibais_novos = canibais + (i - j)

            if is_estado_valido(missionarios_novos, canibais_novos):
                novo_estado = [missionarios_novos,
                               canibais_novos, margem_destino]
                explorado = novo_estado in explorados
                possibilidades.append((novo_estado, explorado))

    print(len(possibilidades), 'possibilidade(s):')
    for p, explorado in possibilidades:
        cor = '\033[1;30m' if explorado else '\033[1;33m' if p[2] == MARGEM_ESQUERDA else '\033[1;34m'
        print(cor, p, '\033[0m')

    print('-------------------')
    return possibilidades


def is_estado_valido(missionarios, canibais):
    """
    Verifica se um estado é válido de acordo com as regras do problema.
    """
    if missionarios < 0 or canibais < 0 or missionarios > NUM_MISSIONARIOS or canibais > NUM_CANIBAIS:
        return False

    # Verifica se há mais canibais do que missionários em qualquer margem
    if (missionarios > 0 and canibais > missionarios) or (missionarios < NUM_MISSIONARIOS and canibais < missionarios):
        return False
        
    return True


# A busca em amplitude deve garantir que nenhum estado seja visitado mais de uma vez,
# portanto usamos uma lista de estados explorados para garantir isso.


def bfs(estado_inicial, estado_final):
    """
    A fila é a nossa lista de estados a serem explorados.
    A fila é inicializado com o estado inicial.
    O explorado é uma lista de estados já visitados.
    """

    fila = [[estado_inicial]]
    explorado = []
    # Enquanto houver estados a serem explorados na fila
    while fila:
        caminho = fila[0]
        fila = fila[1:]
        fim = caminho[-1]

        print("Explorados até agora:", explorado)

        if fim in explorado:
            continue
        for movimento, _ in obter_movimentos_possiveis(fim, explorado):
            # Se o estado já foi explorado, não o adiciona à fila e continua a busca pelo próximo estado
            if movimento in explorado:
                continue
            fila.append(caminho + [movimento])
        explorado.append(fim)
        # Se o estado final for encontrado, retorna o caminho e termina a busca
        if fim == estado_final:
            break

    return caminho


def encontrar_caminho(estado_inicial, estado_final):

    if not is_estado_valido(estado_inicial[0], estado_inicial[1]):
        print("===================================================================")
        print("O estado inicial fornecido não é válido.")
        print("===================================================================")
        return

    caminho = bfs(estado_inicial, estado_final)

    for estado in caminho:
        print('')
        print('------------')
        print('Movimento #', caminho.index(estado))
        print('')
        print(estado)
        print('Missionários:', estado[0])
        print('Canibais:', estado[1])
        print('Posição do barco:', estado[2])
        print('------------')

    print('Total de Movimentos:', len(caminho) - 1)

    exibir_instrucoes()


estado_inicial = [NUM_MISSIONARIOS, NUM_CANIBAIS, MARGEM_ESQUERDA]
estado_final = [0, 0, MARGEM_DIREITA]

encontrar_caminho(estado_inicial, estado_final)
