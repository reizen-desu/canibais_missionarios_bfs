# Canibais e Missionários

## Problema

Em uma margem de um rio, estão três missionários e três canibais. Há um barco disponível que pode acomodar até duas pessoas e que eles gostariam de usar para atravessar o rio. Se número dos canibais superar o dos missionários em qualquer uma das margens do rio, os missionários serão comidos. Assim que, como pode o barco ser usado para transportar com segurança todos os missionários e canibais para a outra margem do rio?

## Solução

Dado o problema, temos as seguintes restrições:

1. O barco pode levar no máximo 2 pessoas
2. Sempre devem ter mais missionários do que canibais em uma dada margem do rio.

Para resolver o problema, foi utilizado o algoritmo de busca em largura/amplitude e a linguagem de programação Python.
O algoritmo consiste em, a partir de um estado inicial, gerar todos os estados possíveis a partir dele e, para cada um desses estados, gerar todos os estados possíveis a partir dele e assim por diante até que o estado final seja encontrado.

Os estados serão representados com [#M, #C, #B]. Onde M representa os missionários, C os canibais e B se o barco está, ou não, na margem do rio podendo assim, ser 1 (está na margem) ou 0 (está do outro lado).

Ou seja:

**Estado Inicial**: [3,3,1] -> Todos os missionários e canibais de um lado do rio
**Estado Final**: [0,0,0] -> Todos os missionários e canibais do outro lado do rio
