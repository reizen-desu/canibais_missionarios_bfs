"""
As regras são de que o barco pode levar no máximo 2 pessoas e que sempre devem ter mais missionários do que canibais em uma dada margem do rio.
Para o barco: 1 (está na margem) ou 0 (está do outro lado).
[Missionarios, Canibais, Barco]
Estado Inicial = [3,3,1] -> Todos os missionários e canibais + o barco
Estado Final = [0,0,0] -> Todos passaram
"""


def movimentos(estado):
    """
    Retorna uma lista dos movimentos possíveis (viagens permitidas)
    em um dado estado do problema
    """
    possibilidades = []
    missionarios = estado[0]
    canibais = estado[1]
    margem_barco = estado[2]

    if margem_barco == 1:
        # Se o barco está na margem esquerda
        for i in range(0, 3):
            for j in range(0, 3):
                missionarios_novos = missionarios - i
                canibais_novos = canibais - j
                if i + j <= 2 and i + j >= 1 and missionarios_novos >= 0 and canibais_novos >= 0 and missionarios_novos <= 3 and canibais_novos <= 3:
                    # Verifica se o número total de pessoas no barco é válido (1 a 2 pessoas)
                    # Verifica se o número de missionários e canibais não é negativo
                    # Verifica se a quantidade de missionários e canibais não excede a quantidade inicial
                    if missionarios_novos != 0:
                        if missionarios_novos >= canibais_novos:
                            if (3 - missionarios_novos) != 0:
                                # Verifica se há missionários na margem oposta
                                if (3 - canibais_novos + j) <= (3 - missionarios + i):
                                    # Verifica se a quantidade de missionários na margem oposta
                                    # não é menor do que a quantidade de canibais na margem oposta
                                    possibilidades.append(
                                        [missionarios_novos, canibais_novos, 0])
                            else:
                                # Se não há missionários na margem oposta, adiciona a possibilidade
                                possibilidades.append(
                                    [missionarios_novos, canibais_novos, 0])
                    else:
                        # Se não há missionários na viagem, adiciona a possibilidade
                        possibilidades.append(
                            [missionarios_novos, canibais_novos, 0])
    else:
        # Se o barco está na margem oposta, testa as possibilidades de travessia
        for i in range(0, 3):
            for j in range(0, 3):
                missionarios_novos = missionarios + i
                canibais_novos = canibais + j
                if i + j <= 2 and i + j >= 1 and missionarios_novos >= 0 and canibais_novos >= 0 and missionarios_novos <= 3 and canibais_novos <= 3:
                    # Verifica se o número total de pessoas no barco é válido (1 a 2 pessoas)
                    # Verifica se o número de missionários e canibais não é negativo
                    # Verifica se a quantidade de missionários e canibais não excede a quantidade inicial
                    if missionarios != 0:
                        if (3 - missionarios_novos) != 0:
                            # Verifica se há missionários na margem oposta
                            if (3 - canibais_novos - j) <= (3 - missionarios - i) and missionarios_novos >= canibais_novos:
                                # Verifica se a quantidade de missionários na margem oposta
                                # não é menor do que a quantidade de canibais na margem oposta
                                possibilidades.append(
                                    [missionarios_novos, canibais_novos, 1])
                        else:
                            # Se não há missionários na margem oposta, adiciona a possibilidade
                            possibilidades.append(
                                [missionarios_novos, canibais_novos, 1])
                    else:
                        # Se não há missionários na viagem, adiciona a possibilidade
                        possibilidades.append(
                            [missionarios_novos, canibais_novos, 1])

    return possibilidades


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


inicio = [3, 3, 1]
final = [0, 0, 0]

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
