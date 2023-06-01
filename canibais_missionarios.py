"""
As regras são de que o barco pode levar no máximo 2 pessoas e que sempre devem ter mais missionários do que canibais em uma dada margem do rio.
Para o barco: 1 (está na margem) ou 0 (está do outro lado).
[Missionarios, Canibais, Barco]
Estado Inicial = [3,3,1] -> Todos os missionários e canibais + o barco
Estado Final = [0,0,0] -> Todos passaram
"""

# Retorna uma lista dos movimentos possíveis (viagens permitidas) em um dado estado do problema


def movimentos(estado):

    possibilidades = []
    miss = estado[0]
    cani = estado[1]
    barco = estado[2]

    # Barco na margem esquerda
    if barco == 1:
        for i in range(0, 3):
            for j in range(0, 3):
                miss2 = miss - i
                cani2 = cani - j
                if i+j <= 2 and i+j >= 1 and miss2 >= 0 and cani2 >= 0 and miss2 <= 3 and cani2 <= 3:
                    if miss2 != 0:
                        if miss2 >= cani2:
                            if (3-miss2) != 0:
                                if (3-cani+j) <= (3-miss+i):
                                    possibilidades.append([miss2, cani2, 0])
                            else:
                                possibilidades.append([miss2, cani2, 0])
                    else:
                        possibilidades.append([miss2, cani2, 0])
        # Barco na margem direita
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                miss2 = miss + i
                cani2 = cani + j
                if i+j <= 2 and i+j >= 1 and miss2 >= 0 and cani2 >= 0 and miss2 <= 3 and cani2 <= 3:
                    if miss != 0:
                        if (3-miss2) != 0:
                            if (3-cani-j) <= (3-miss-i) and miss2 >= cani2:
                                possibilidades.append([miss2, cani2, 1])
                        else:
                            possibilidades.append([miss2, cani2, 1])
                    else:
                        possibilidades.append([miss2, cani2, 1])

    return possibilidades


"""
Agora é feita uma simples implementação do BFS.
A fronteira é o estado inicial, a priori e nenhum nó foi explorado.
Então 'path' é o primeiro nó da fronteira, que em seguida é removido.
O fim do 'path' é o último nó explorado através daquela forma de solução.

Se um nó já foi explorado é ignorado.

Checa-se todas as possibilidades de movimento do último nó de um dado
caminho e, caso não tenha sido visitado antes, adiciona-se à fronteira
mais essa possível resposta. Se esse nó explorado for o estado desejado
o algoritmo se encerra.
"""


def bfs(inicio, final):
    front = [[inicio]]
    explored = []
    while front:
        path = front[0]
        front = front[1:]
        end = path[-1]
        if end in explored:
            continue
        for move in movimentos(end):
            if move in explored:
                continue
            front.append(path + [move])
        explored.append(end)
        if end == final:
            break

    return path


inicio = [3, 3, 1]
final = [0, 0, 0]

resposta = bfs(inicio, final)
contador = 0
for estado in resposta:
    print('Movimento', contador)
    print('Missionários:', estado[0])
    print('Canibais:', estado[1])
    print('Barco na margem:', estado[2])
    print('------------')
    contador += 1
