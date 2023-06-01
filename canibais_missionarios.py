"""
As regras são de que o barco pode levar no máximo 2 pessoas e que sempre devem ter mais missionários do que canibais em uma dada margem do rio.
Para o barco: 1 (está na margem) ou 0 (está do outro lado).
[Missionarios, Canibais, Barco]
Estado Inicial = [3,3,1] -> Todos os missionários e canibais + o barco
Estado Final = [0,0,0] -> Todos passaram
"""


# Constantes para representar as margens do rio
POSICAO_ESQUERDA = 1
POSICAO_DIREITA = 0

# Constantes para o número inicial de missionários e canibais
NUM_MISSIONARIOS = 3
NUM_CANIBAIS = 3


def movimentos(estado):
    """
    Retorna uma lista dos movimentos possíveis (viagens permitidas)
    em um dado estado do problema
    """
    possibilidades = []
    missionarios, canibais, posicao_barco = estado

    print("Estado: ", estado)
    if posicao_barco == POSICAO_ESQUERDA:
        # Se o barco está na margem esquerda
        for i in range(1, 3):
            for j in range(0, i + 1):
                missionarios_novos = missionarios - j
                canibais_novos = canibais - (i - j)

                if is_estado_valido(missionarios_novos, canibais_novos):
                    possibilidades.append(
                        [missionarios_novos, canibais_novos, POSICAO_DIREITA])
    else:
        # Se o barco está na margem direita
        for i in range(1, 3):
            for j in range(0, i + 1):
                missionarios_novos = missionarios + j
                canibais_novos = canibais + (i - j)

                if is_estado_valido(missionarios_novos, canibais_novos):
                    possibilidades.append(
                        [missionarios_novos, canibais_novos, POSICAO_ESQUERDA])

    print(len(possibilidades), 'possibilidade(s):')
    for p in possibilidades:
        print(p)
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
    O front é a nossa fila de estados a serem explorados
    O front é inicializado com o estado inicial
    O explorado é uma lista de estados já visitados
    """
    fila = [[estado_inicial]]
    explorado = []
    # Enquanto houver estados a serem explorados na fila
    while fila:
        caminho = fila[0]
        fila = fila[1:]
        fim = caminho[-1]

        # print("Iteração", len(explorado) + 1)
        print("Explorados até agora:", explorado)

        if fim in explorado:
            continue
        for movimento in movimentos(fim):
            # Se o estado já foi explorado, não o adiciona à fila e continua a busca pelo próximo estado
            if movimento in explorado:
                continue
            fila.append(caminho + [movimento])
        explorado.append(fim)
        # Se o estado final for encontrado, retorna o caminho e termina a busca
        if fim == estado_final:
            break

    return caminho


estado_inicial = [NUM_MISSIONARIOS, NUM_CANIBAIS, POSICAO_ESQUERDA]
estado_final = [0, 0, POSICAO_DIREITA]

resposta = bfs(estado_inicial, estado_final)
# O total de movimentos é igual ao tamanho da resposta menos o estado inicial
total_movimentos = len(resposta) - 1
contador = 0

for estado in resposta:
    print('')
    print('------------')
    print('\033[1;36mMovimento\033[0m', contador)
    print('Missionários:', estado[0])
    print('Canibais:', estado[1])
    print('Posição do barco:', estado[2])
    print('------------')
    contador += 1

print('Total de Movimentos:', total_movimentos)
