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