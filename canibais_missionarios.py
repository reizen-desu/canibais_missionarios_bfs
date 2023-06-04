"""
Regras do problema:
- O barco transporta no máximo 2 pessoas.
- Deve haver mais missionários do que canibais em uma margem.
[Missionarios, Canibais, Barco]
Estado Inicial: [3, 3, 1] (Todos missionários, canibais e o barco em uma margem)
Estado Final: [0, 0, 0] (Todos na outra margem)
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


def obter_estados_vizinhos(estado_atual, explorados):
    """
    Retorna uma lista dos movimentos possíveis (viagens permitidas)
    em um dado estado do problema.
    Os estados já explorados serão impressos em vermelho.
    """
    estados_vizinhos = []
    missionarios, canibais, posicao_barco = estado_atual

    print("Estado atual:", estado_atual)
    margem_destino = MARGEM_DIREITA if posicao_barco == MARGEM_ESQUERDA else MARGEM_ESQUERDA

    # Explora todas as combinações possíveis de movimentos de missionários e canibais a partir do estado_atual.
    # O primeiro loop determina o número de canibais que serão levados em uma viagem (1 a 2).
    for i in range(1, 3):
        # O segundo loop determina o número de missionários que serão levados em uma viagem
        # (variando de 0 a i (número de canibais escolhidos no primeiro loop))
        for j in range(0, i + 1):
            if posicao_barco == MARGEM_ESQUERDA:
                missionarios_novos = missionarios - j
                canibais_novos = canibais - (i - j)
            else:
                missionarios_novos = missionarios + j
                canibais_novos = canibais + (i - j)

            if is_estado_valido(missionarios_novos, canibais_novos):
                # Cria o estado vizinho se ele for válido
                estado_vizinho = [missionarios_novos,
                                  canibais_novos, margem_destino]
                # Verifica se o estado já foi explorado anteriormente
                estado_explorado = estado_vizinho in explorados
                # Se não foi, adiciona à lista de estados vizinhos
                estados_vizinhos.append((estado_vizinho, estado_explorado))

    print(len(estados_vizinhos), 'possibilidade(s):')
    for p, estado_explorado in estados_vizinhos:
        cor = '\033[1;30m' if estado_explorado else '\033[1;33m' if p[2] == MARGEM_ESQUERDA else '\033[1;34m'
        print(cor, p, '\033[0m')

    print('-------------------')
    return estados_vizinhos


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
    Busca em amplitude (BFS) para encontrar o caminho entre o estado inicial e o estado final.
    O lista (estados_a_explorar) é uma fila que recebe o primeiro caminho (estado inicial) e
    a lista (estados_explorados) é uma lista de estados visitados que é inicialmente vazia.
    """
    estados_a_explorar = [[estado_inicial]]
    estados_explorados = [] 

    # Enquanto houver estados a serem explorados na fila
    while estados_a_explorar:
        # Remove o primeiro caminho da lista
        caminho_atual = estados_a_explorar.pop(0)
        # Obtém o último estado do caminho atual
        estado_atual = caminho_atual[-1]

        if estado_atual in estados_explorados:
            continue  # Se o estado atual já foi explorado, pula para a próxima iteração

        # Adiciona o estado atual à lista de estados explorados
        estados_explorados.append(estado_atual)

        if estado_atual == estado_final:
            break  # Se o estado atual é o estado final, encerra o loop e retorna o caminho

        # Obtém os estados vizinhos do estado atual
        for estado_vizinho, _ in obter_estados_vizinhos(estado_atual, estados_explorados):
            if estado_vizinho not in estados_explorados:
                # Adiciona o caminho atualizado à lista de estados a explorar
                estados_a_explorar.append(caminho_atual + [estado_vizinho])

        print("Estados explorados até o momento:", estados_explorados)
    return caminho_atual


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
    print('Trajecto percorrido:', caminho)

    exibir_instrucoes()


estado_inicial = [NUM_MISSIONARIOS, NUM_CANIBAIS, MARGEM_ESQUERDA]
estado_final = [0, 0, MARGEM_DIREITA]

encontrar_caminho(estado_inicial, estado_final)
