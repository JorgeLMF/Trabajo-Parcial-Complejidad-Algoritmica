# Algoritmo de Prim
## Introducción
Robert Prim ideó un algoritmo en 1957 para la resolución del problema del Árbol de coste total mínimo (MST).  Este consiste en encontrar un árbol de peso total mínimo conectando nodos o vértices con arcos de peso mínimo que sea conectados por nodos o vértices sin formar ciclos.

## ¿En qué consiste?
Consiste en dividir los nodos de un grafo en dos conjuntos: visitados y no visitados. Al principio, hay un vértice del conjunto visitado que corresponde al equipo central. En cada iteración se incrementa el grafo de visitados en un nodo, este grafo tiene que ser de coste mínimo. 

## ¿Cuál es su complejidad?

*a: número de arcos del grafo
n: número de vértices del grafo

En un grafo denso, la complejidad computacional tmeporal tiende a ser **O(n^2)** cuando a ≈ n^2.

## Pseudocódigo 
En las siguientes líneas se presentará un pseudocódigo del Algoritmo de Prim hacia un grafo con matriz de adyacencia que, posteriormente se adaptará para implementarse en un grafo con lista de adyacencia para solucionar el problema en estudio: VRP. 

```
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
```
 En este, se usan arreglos para almacenar los nodos VISITADOS, VECINOS y COSTE MÍNIMO para los vértices seleccionados durante la ejecución del algoritmo.
 
## Diagrama de flujo
En la siguiente imagen se podrá observar el Diagrama de Flujo con respecto a este Algoritmo
<p align=center>
    ![PRIM](https://user-images.githubusercontent.com/54080805/135726278-c5a156d0-d22d-43a4-920d-827a8283a77a.png)
    <div align="center"> Figura 1: Diagrama de Flujo del Algoritmo de Prim. Elaboración propia
</p>

    

## Referencias bibliográficas
- Cuesta, J. (11 de abril de 2013). Algoritmo de Prim. *Complejidad Algorítmica*. Recuperado de https://sites.google.com/site/complejidadalgoritmicaes/prim \[Consulta: 2 de octubre de 2021].
- Grafos Soft (2012). *Grafos - software para la construcción, edición y análisis de grafos*. Recuperado de https://arodrigu.webs.upv.es/grafos/doku.php?id=algoritmo_prim \[Consulta: 25 de setiembre de 2021].
