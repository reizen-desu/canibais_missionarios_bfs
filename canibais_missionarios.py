"""
As regras são de que o barco pode levar no máximo 2 pessoas e que sempre devem ter mais missionários do que canibais em uma dada margem do rio.
Para o barco: 1 (está na margem) ou 0 (está do outro lado).
[Missionarios, Canibais, Barco]
Estado Inicial = [3,3,1] -> Todos os missionários e canibais + o barco
Estado Final = [0,0,0] -> Todos passaram
"""


# Constantes para representar as margens do rio
MARGEM_ESQUERDA = 0
MARGEM_DIREITA = 1

# Constantes para o número inicial de missionários e canibais
NUM_MISSIONARIOS = 3
NUM_CANIBAIS = 3


def movimentos(estado):
    """
    Retorna uma lista dos movimentos possíveis (viagens permitidas)
    em um dado estado do problema
    """
    possibilidades = []
    missionarios, canibais, margem_barco = estado

    if margem_barco == MARGEM_ESQUERDA:
        # Se o barco está na margem esquerda
        for i in range(1, 3):
            for j in range(0, i + 1):
                missionarios_novos = missionarios - j
                canibais_novos = canibais - (i - j)

                if is_estado_valido(missionarios_novos, canibais_novos):
                    possibilidades.append(
                        [missionarios_novos, canibais_novos, MARGEM_DIREITA])
    else:
        # Se o barco está na margem direita
        for i in range(1, 3):
            for j in range(0, i + 1):
                missionarios_novos = missionarios + j
                canibais_novos = canibais + (i - j)

                if is_estado_valido(missionarios_novos, canibais_novos):
                    possibilidades.append(
                        [missionarios_novos, canibais_novos, MARGEM_ESQUERDA])

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


def bfs(inicio, final):
    # O front é o nosso estado inicial
    # O explorado é uma lista de estados já visitados
    front = [[inicio]]
    explorado = []
    # Enquanto houver estados a serem explorados
    while front:
        path = front[0]
        front = front[1:]
        fim = path[-1]
        if fim in explorado:
            continue
        for movimento in movimentos(fim):
            if movimento in explorado:
                continue
            front.append(path + [movimento])
        explorado.append(fim)
        # Se o estado final for encontrado, retorna o caminho
        if fim == final:
            break

    return path


inicio = [NUM_MISSIONARIOS, NUM_CANIBAIS, MARGEM_ESQUERDA]
final = [0, 0, MARGEM_DIREITA]
resposta = bfs(inicio, final)
contador = 0

for estado in resposta:
    print('')
    print('------------')
    print('Movimento', contador)
    print('Missionários:', estado[0])
    print('Canibais:', estado[1])
    print('Barco na margem:', estado[2])
    print('------------')
    contador += 1
