# Canibais e Missionários

## Problema

Em uma margem de um rio, estão três missionários e três canibais. Há um barco disponível que pode acomodar até duas pessoas e que eles gostariam de usar para atravessar o rio. Se número dos canibais superar o dos missionários em qualquer uma das margens do rio, os missionários serão comidos. Assim que, como pode o barco ser usado para transportar com segurança todos os missionários e canibais para a outra margem do rio?

## Solução

Dado o problema, temos as seguintes restrições:

1. O barco pode levar no máximo 2 pessoas
2. Sempre devem ter mais missionários do que canibais em uma dada margem do rio.

Para resolver o problema, foi utilizado o algoritmo de busca em largura/amplitude e a linguagem de programação Python.
O algoritmo consiste em, a partir de um estado inicial, gerar todos os estados possíveis a partir dele e, para cada um desses estados, gerar todos os estados possíveis a partir dele e assim por diante até que o estado final seja encontrado.

Os estados serão representados com `[#M, #C, #B]`.
Onde M representa os missionários, C os canibais e B se o barco está, ou não, na margem do rio podendo assim, ser 1 (está na margem) ou 0 (está do outro lado).

Ou seja:

- **Estado Inicial**: [3,3,1] -> Todos os missionários e canibais de um lado do rio
- **Estado Final**: [0,0,0] -> Todos os missionários e canibais do outro lado do rio

## Execução

Para executar o programa, basta executar o ficheiro `canibais_missionarios.py` com o comando `python canibais_missionarios.py`. O número de missionários e canibais é 3 por padrão, mas pode ser alterado no ficheiro `canibais_missionarios.py`. Após a execução, será mostrado no terminal o caminho percorrido para chegar ao estado final.

## Exemplo

Exte exemplo mostra a execução do programa com 3 missionários e 3 canibais.

 <details>
      <summary>Abrir o exemplo...</summary>
      <br>


```
------------
Movimento # 0

[3, 3, 1]
Missionários: 3
Canibais: 3
Posição do barco: 1
------------

------------
Movimento # 1

[3, 1, 0]
Missionários: 3
Canibais: 1
Posição do barco: 0
------------

------------
Movimento # 2

[3, 2, 1]
Missionários: 3
Canibais: 2
Posição do barco: 1
------------

------------
Movimento # 3

[3, 0, 0]
Missionários: 3
Canibais: 0
Posição do barco: 0
------------

------------
Movimento # 4

[3, 1, 1]
Missionários: 3
Canibais: 1
Posição do barco: 1
------------

------------
Movimento # 5

[1, 1, 0]
Missionários: 1
Canibais: 1
Posição do barco: 0
------------

------------
Movimento # 6

[2, 2, 1]
Missionários: 2
Canibais: 2
Posição do barco: 1
------------

------------
Movimento # 7

[0, 2, 0]
Missionários: 0
Canibais: 2
Posição do barco: 0
------------

------------
Movimento # 8

[0, 3, 1]
Missionários: 0
Canibais: 3
Posição do barco: 1
------------

------------
Movimento # 9

[0, 1, 0]
Missionários: 0
Canibais: 1
Posição do barco: 0
------------

------------
Movimento # 10

[0, 2, 1]
Missionários: 0
Canibais: 2
Posição do barco: 1
------------

------------
Movimento # 11

[0, 0, 0]
Missionários: 0
Canibais: 0
Posição do barco: 0
------------
Total de Movimentos: 11
Trajecto percorrido: [[3, 3, 1], [3, 1, 0], [3, 2, 1], [3, 0, 0], [3, 1, 1], [1, 1, 0], [2, 2, 1], [0, 2, 0], [0, 3, 1], [0, 1, 0], [0, 2, 1], [0, 0, 0]]
```

</details>
