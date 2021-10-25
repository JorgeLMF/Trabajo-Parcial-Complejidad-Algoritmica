import pandas as pd
url = "https://raw.githubusercontent.com/JorgeLMF/cc42_tf_202014828_201915747_201921559_201811355_201714378/main/DATASET/almacenesXyY.csv"
url2 = "https://raw.githubusercontent.com/JorgeLMF/cc42_tf_202014828_201915747_201921559_201811355_201714378/main/DATASET/puntosentregaXyY.csv"
file_almacenes = pd.read_csv(url).to_numpy()
pts_entrega = pd.read_csv(url2).to_numpy()

la_matrix = []
for i in range(1000):
    l = [0]*1000
    la_matrix.append(l)

for line in file_almacenes:
    la_matrix[line[0]][line[1]] = 1

for line in pts_entrega:
    if la_matrix[line[0]][line[1]] != 1:
       la_matrix[line[0]][line[1]] = 2

for line in la_matrix:
  print(line)
