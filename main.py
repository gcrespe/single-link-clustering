import singlelink as singlelink
import numpy as numpy
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import adjusted_rand_score 

def main():
    auxiliar = input(
        "Qual o arquivo que deseja inserir?\n 1 = c2ds1-2sp\n 2 = c2ds3-2g\n 3 = monkey\n 4 = m\n")
    if auxiliar == "1":
        p = "c2ds1-2sp"
    elif auxiliar == '2':
        p = "c2ds3-2g"
    elif auxiliar == '3':
        p = "monkey"
    elif auxiliar == '4':
        p = "m"    

    path = "bases/" + p + ".txt"

    data = path
  
    dataset = pd.read_csv(path, sep = '\t')
    
    kMin = int(input("Qual é o kmin?\n"))
    
    kMax = int(input("Qual é o kmax?\n"))
 
    singlelink.singleLinkClustering(kMin, kMax, data, p)

    pyplot.scatter(dataset['D1'].values, dataset['D2'].values) 
    pyplot.savefig(f'grafico_geral.jpg')

    file = open('clusterFiles/singleLink/' + p + "Resultado" + '.txt', 'w')

    for i in range(kMin, kMax+1):
        datasetSaida = pd.read_csv(f'clusterFiles/SingleLink/{p}{i}.clu', sep = '\t', names=["sample_label", "class"])
        resultadoSaida = pd.read_csv(f'clusterFiles/SingleLink/{p}Real.clu', sep = '\t', names=["sample_label", "class"])

        x = datasetSaida['class'].values
        y = resultadoSaida['class'].values

        print(adjusted_rand_score(x,y))

        rand = adjusted_rand_score(x,y)

        file.write("Indice Rand - " + ' ' + p + str(i) + ' = ' + str(round(rand, 3)) + '\n')

        print(datasetSaida['class'].values)

        pyplot.scatter(dataset['D1'].values, dataset['D2'].values, c = datasetSaida['class'].values) 
        pyplot.savefig(f'grafico_{i}.jpg')

main()
