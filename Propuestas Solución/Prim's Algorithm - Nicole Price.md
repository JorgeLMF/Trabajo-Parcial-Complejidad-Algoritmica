# Algoritmo de Prim
## Introducción
Robert Prim ideó un algoritmo en 1957 para la resolución del problema del Árbol de coste total mínimo (MST).  Este consiste en encontrar un árbol de peso total mínimo conectando nodos o vértices con arcos de peso mínimo que sea conectados por nodos o vértices sin formar ciclos.

## ¿En qué consiste?
Consiste en dividir los nodos de un grafo en dos conjuntos: visitados y no visitados. Al principio, hay un vértice del conjunto visitado que corresponde al equipo central. En cada iteración se incrementa el grafo de visitados en un nodo, este grafo tiene que ser de coste mínimo. 

## ¿Cuál es su complejidad?
En un grafo denso, la complejidad tiende a ser **O(n^2)**, mas si se implementa en montículos, la complejidad es de **O(a logn)**.
