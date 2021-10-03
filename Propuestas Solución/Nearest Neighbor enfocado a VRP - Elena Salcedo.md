# Nearest Neighbor enfocado a VRP

## Descripción
<p align="justify">
Es un algoritmo heurístico que está enfocado en resolver problemas similares al TSP, mediante la búsqueda de un árbol de expansión mínima. Para ello, primero, selecciona un nodo al azar como punto de partida. Luego, desde el vértice elegido donde se encuentra el viajero, lo enlaza con el nodo con mayor proximidad a este, solamente si el viajero no ha transitado por este anteriormente. Este proceso se repite hasta que todos los vértices hayan sido recorridos. (Salazar, 2019)
	</p>
<p align="center">
 <img src="https://knuth.uca.es/moodle/pluginfile.php/9502/mod_page/content/12/vecino_mas_cercano.png" />
	</p>
<p align="center">
Figura 1: Selección del próximo nodo mediante el uso del algoritmo del vecino más cercano. 
Muñoz, M. (2015). El viajante de comercio. [Figura]. Recuperado de http://knuth.uca.es/moodle/mod/page/view.php?id=3417
</p>

## Análisis Asimptótico de posible algoritmo principal

```
def nearest_neighbor(grafo, nodo_del_cual_partir, nodo_final):						.	T(n):
	si nodo del cual partir igual a nodo final:							.		1
		terminar funcion									.		   1
	si no:
		la menor distancia es infinita								.		1
		para cada dato del grupo con el que trabajar:						.		2 + n(...)
			hallar distancia con punto inicial						.			6
			si la distancia es menor que la menor distancia anterior, reemplazarla		.			2
		unir nodo del que se partió con nodo a la menor distancia				.		1
		nearest_neighbor(grafo, nodo_a_la_menor_distancia, nodo_final)				.		O(n)
T(n) = O(n^2)

def nnalgorithm(grafo, nodo_del_cual_partir (i), nodo_final (f)):				.	T(n) =
	si la cantidad de datos con la cual trabajar es aceptable:				.		1
		nearest_neighbor(grafo, i, f)							.			O(n^2)
	si no:											
		mitad = (i + f) // 2								.			3
		a = nnalgorithm(grafo, i, mitad)						.			T(n/2)
		b = nnalgorithm(grafo, mitad + 1, f)						.			T(n/2)

T(n) = 2 T(n/2) + O(n^2)

log_2(2) = 1

1 < 2

T(n) = O(n^2)
```

## Referencia bibliográfica:

Salazar, B. (2019). *Problema del agente viajero – TSP*. Recuperado de:  https://www.ingenieriaindustrialonline.com/investigacion-de-operaciones/problema-del-agente-viajero-tsp/
