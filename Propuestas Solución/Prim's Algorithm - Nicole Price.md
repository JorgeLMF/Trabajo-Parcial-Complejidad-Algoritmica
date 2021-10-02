# Algoritmo de Prim
## Introducción
Robert Prim ideó un algoritmo en 1957 para la resolución del problema del Árbol de coste total mínimo (MST).  Este consiste en encontrar un árbol de peso total mínimo conectando nodos o vértices con arcos de peso mínimo que sea conectados por nodos o vértices sin formar ciclos.

## ¿En qué consiste?
Consiste en dividir los nodos de un grafo en dos conjuntos: visitados y no visitados. Al principio, hay un vértice del conjunto visitado que corresponde al equipo central. En cada iteración se incrementa el grafo de visitados en un nodo, este grafo tiene que ser de coste mínimo. 

## ¿Cuál es su complejidad?
En un grafo denso, la complejidad tiende a ser **O(n^2)**, mas si se implementa en montículos, la complejidad es de **O(a logn)**.

'''
    Algoritmo_Prim(G grafo, A conjunto_aristas)
            A:= conjunto_vacío;
            VISTOS:= añadir (conjunto_vacio, {1});
            Para i=2 hasta n hacer
                        VECINO[i]:= 1;
                        COSTE_MÍNIMO [i]:= M [i, 1];
            FinPara

            Mientras (|VISTOS| < n) hacer           
                        min:= infinito;
                        Para j=2 hasta n hacer
                                   si (0 <= COSTE_MÍNIMO [j] < min) entonces
                                               min:= COSTE_MÍNIMO [j]; k:= j;
                                   FinSi
                        FinPara
                        A:= A U {(k, VECINO[k])};
                        VISTOS:= VISTOS U {k};
                        COSTE_MÍNIMO [k]:= -1;
                        para j=2 hasta n hacer
                                   si (M[k,j] < COSTE_MÍNIMO [j]) entonces                   
                                           COSTE_MÍNIMO [j]:= M [k,j]                                          
                                           VECINO[j]:= k;
                                   FinSi
                        FinPara
            FinMientras
    FinAlgoritmo_Prim
'''
