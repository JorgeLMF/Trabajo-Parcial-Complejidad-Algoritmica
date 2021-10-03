# Espacio de Búsqueda

El problema de enrutamiento de vehículos propone un mapa con una gran cantidad de puntos de reparto y puntos de entrega que deberán ser conectados por uno o más vehículos
con la intención de encontrar la ruta más eficiente para conectar dichos puntos. Se sabe entonces que los vehículos partiran de uno o más puntos, que servirán de nodo/nodos
iniciales. 

En un estado inicial, el mapa de puntos no tiene conexiones entre sus puntos pues los almacenes aún no envían los productos a los puntos de entrega.

<p align="center">
  <img src="https://user-images.githubusercontent.com/35857164/135735219-cac9e0a3-2478-4fb9-9086-6496e47ced23.png" />
</p>

Conforme los múltiples algoritmos recorren el grafo a partir de un nodo inicial, estos van calculando las posibles rutas entre los diversos nodos del grafo, tratando de encontrar 
las rutas que permitan recorrer la totalidad de los nodos en el camino más corto posible, lo que da como resultado un campo de búsqueda con las siguientes características: 

<p align="center">
  <img src="https://user-images.githubusercontent.com/35857164/135735610-8f207336-05cc-49b9-9559-84b880d18968.png" />
</p>

Es probable que durante las muchas iteraciones del algoritmo, los caminos trazados inicialmente sean reemplazados en eficiencia por nuevas conexiones producto de una variación
en el orden de los nodos que componen un camino, generando variaciones en los posibles resultados de cada algoritmo. Dicho esto, el resultado final podria terminar viéndose así:

<p align="center">
  <img src="https://user-images.githubusercontent.com/35857164/135735723-20c3df9e-fe7b-45b8-bade-35e961a86dd3.png" />
</p>

Este estado final todos los puntos de entrega estarán conectados mediante caminos de distintas longitudes con un punto de distribución y todos los puntos habrán sido visitados una sola vez.

Cabe resaltar que este tipo de problemas no suelen tener soluciones únicas, por lo que en la gran mayoría de los casos, los resultados obtenidos por los algoritmos serán solamente
respuestas muy cercanas a la respuesta definitiva, más no necesariamente la respuesta 100% correcta.

Unas restricciones que tomaremos en cuenta son:
- Los puntos no podrán ser visitados más de una sola vez
- Si un punto de entrega coincide con un punto de distribución, este no se tomará en cuenta pues el producto ya habría llegado a su destino.
