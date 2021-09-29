# Backtracking
Backtracking: El Backtracking es una técnica de algoritmos utilizada para solucionar problemas, en la cual intenta construir recursivamente e ingrementalmente la solución para dicho problema. 
En donde se eliminan las soluciones que sean de utilidad para resolver el problema.   

1) Tener puntos de acopio con capacidad

2) Tener el punto de salida para los carros y la maxima capacidad de cada carro (X)

3) Backtracking : respuesta nos de X configuraciones de las rutas - {x1, x2 .. xn} no puden tener elementos iguales mas que el comienzo porque todos salen del mismo punto de partida

Limite: cuando ya no haya posiciones que tomar (coordenas de los puntos de acopio {x,y} . Para esto tendremos un arreglo de booleanos donde sera
True: cuando ese punto de acopio ya este tomado por alguna de las configuraciones
False: no esta tomado por ninguna hasta ahora
Y tambien procurar que la suma del tamaño de las configuraciones sea mayor a |N| - |X|

Ejemplo:

Si tenemos 3 carros todos salen del mismo punto y tenemos 7 puntos de acopio entonces iremos construyendo las posibles rutas de la siguiente manera:

Al comienzo a cada punto de acopio le asignados un ID este entre el [0,6] y en el backtracking se iran construyendo recursivamente las 3 configuraciones (1 configuracion por cada carro). Al comienzo las configuraciones estaran vacias: represtadas como un arreglo de tamaño 0. Ademas de un contador que nos diga cuanto ya va cargando cada carro para no sobrepasar el limite de este. Ademas tendrmos un arreglo de booleanos el cual nos indicara si es que los puntos de acopio ya han sido visitados (con sus respectivos IDs)

En el backtracking se iran marcando como visitados a los IDs de los puntos de acopio mientras vayan siendo visitados. Se tendra un loop el cual no indicara a cual ruta/configuracion de los 3 carros agregarla y la iremos añaniendo o no al arreglo de la ruta respectiva. Esto significaria que tendremos un funcion llamada "solve" con 1 parametro el cual es en que posicion de los puntos de acopio estas. Asi a cada posicion la intentaremos agregar a uno de los carros. Tenemos que procurar que este punto de acopio no sobrepase el limite que tiene el carro.

Al final cuando ya se llegue al limite tendrmos 3 configuraciones disjuntas ya que cada punto de acopio solo puede ser visitado por 1 solo carro. Por ejemplo si tenemos 3 carros y 7 puntos de acopio al final tendremos 3 rutas asi:

[0,1,2,3]

[4,5]

[6]

Esto significaria que como respuesta de esta primera parte tendremos todas las particiones disjuntas posibles de los puntos de acopio procurando que ninguna de estas se pase del limite de capacidad del carro.

Luego de ello pasaremos a cada particion permutarla y quedarnos con la permutacion en la cual se recorre menos distancia, tal como un TSP simple. Con un punto de vista greedy si tomamos la menor permutacion en tema de distancia para cada uno la suma de todas las distancias tambien deberia ser la minima. Asi al final de todo ello tendremos las configuraciones en un orden en el cual el carro debera recorrer la distancia minima posible. Ejemplo al final podremos tener de resultado:

[1,2,0,3]
[5,4]
[6]
Lo cual significaria que el carro 1 debe ir a estos puntos de acopio en el siguiente orden: [1,2,0,3] , el carro 2 a: [5,4] y el 3 al [6]

Complejidad deberia ser algo cercano a:

O( (n^x) * n! ) siendo n el numero de puntos de acopio y X el numero de configutaciones. ya que tenemos N posibles puntos de acopio y X posibles rutas. ademas luego de ello se pasa a ver todas las permutsaciones de cada rut a lo cual tiene una complejidad de n! en el peor de los casos
