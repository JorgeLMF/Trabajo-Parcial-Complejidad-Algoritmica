import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import time
import math

url = "https://raw.githubusercontent.com/JorgeLMF/cc42_tf_202014828_201915747_201921559_201811355_201714378/main/DATASET/almacenesXyY.csv"
url2 = "https://raw.githubusercontent.com/JorgeLMF/cc42_tf_202014828_201915747_201921559_201811355_201714378/main/DATASET/puntosentregaXyY.csv"
file_almacenes = pd.read_csv(url).to_numpy()
pts_entrega = pd.read_csv(url2).to_numpy()

long_per_side=1000

warehouse_points=[]
for line in file_almacenes:
  m=long_per_side*(int(line[0]))+int(line[1])
  warehouse_points.append(m)

delivery_points=[]
for line in pts_entrega:
  m=long_per_side*(int(line[0]))+int(line[1])
  delivery_points.append(m)
  

def Mark_Visited(visited):
  for w_point in warehouse_points:
    visited[w_point] = True

def dijkstra(G, long_per_side, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  Mark_Visited(visited)
  visited[s]=False
  while queue:
    if all(visited[p] for p in delivery_points): break
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v] and not visited[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost

def Get_Path_by_delivery_point(lis,node):
  l=[]
  def _get_Path(node):
    if node==None: return
    else:
      l.append(node)
      _get_Path(lis[node])
  
  _get_Path(node)
  l.reverse()
  return l
def GenerarMalla(n):
  def NodeAdj(dir,i,j):
      if dir=='U':
        return n*(i-1)+j
      elif dir =='D':
        return n*(i+1)+(j)
      elif dir=='L':
        return n*(i)+(j-1)
      elif dir =='R':
        return n*(i)+(j+1)

  G=[]
  for i in range(n):
    for j in range(n):
      l=[]
      if i==0 or i==n-1 or j==n-1 or j==0:
        if i==0:
          if j==0:
            l.append(NodeAdj('R',i,j))
            l.append(NodeAdj('D',i,j))
          elif j==n-1:
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('D',i,j))
          else:
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('R',i,j))
            l.append(NodeAdj('D',i,j))
        elif i==n-1:
          if j==0:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('R',i,j))
          elif j==n-1:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('L',i,j))
          else:
            l.append(NodeAdj('U',i,j))
            l.append(NodeAdj('L',i,j))
            l.append(NodeAdj('R',i,j))
        elif j==0:
          l.append(NodeAdj('U',i,j))
          l.append(NodeAdj('R',i,j))
          l.append(NodeAdj('D',i,j))
        elif j==n-1:
          l.append(NodeAdj('U',i,j))
          l.append(NodeAdj('L',i,j))
          l.append(NodeAdj('D',i,j))
      else:
        l.append(NodeAdj('U',i,j))
        l.append(NodeAdj('L',i,j))
        l.append(NodeAdj('R',i,j))
        l.append(NodeAdj('D',i,j))
      m=[]
      for node in l:
        m.append(tuple([node,1]))
      G.append(m)
  return G

G=GenerarMalla(long_per_side)
for i in warehouse_points:
  inicio=time.time()
  path, cost = dijkstra(G,long_per_side, i)
  fin=time.time()
  print("Para el punto de almacen -> N: ",i," - ",round((fin-inicio),5),"s")
  print(cost[811965]) #costo de un delivery point
  print(cost[8687]) #costo de otro waherhouse point (inf: No lo toma en cuenta -> funciona)
  print(cost[0]) #(inf: no llego hasta ese nodo, pues ya todos los puntos de entregas estaban visitados)
  # for j in delivery_points:
  #   listita=Get_Path_by_delivery_point(path,j)
  #   print(listita,"-",len(listita))
  # mostrar el path funciona, pero explota por maximum recursion depth exceeded in comparison

  #al comprobar Djikstra con la mejora de parar la ejecución cuando se compruebe que todos los puntos de entrega están visitados,
  #se consume mayor tiempo computacional. Esto se debe a que va a estar comprobando constantemente si los 3500 puntos de entrega estan visitados.
print("listo")
