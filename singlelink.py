import math as math
from scipy.spatial import distance


colors = 10*["g", "r", "c", "b", "m", "y", "tab:purple","tab:pink","tab:orange","tab:gray","tab:brown", "aquamarine", "darkblue"]

class dataset:
    def __init__(self, nome, data, cluster):
        self.nome = nome
        self.data = data
        self.closest = self
        self.cluster = cluster


class obj:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def sorting(elem):
    return elem.dist

#calcula a menor distancia entre os clusters
def minDist(i, j):
    if(i == j):
        return 0
    distancia = math.inf
    for a in i:
        for b in j:
            x = distance.euclidean(a.data, b.data)
            if (distancia > x):
                distancia = x
    return round(distancia, 4)

def readDataSet(name):
    path = name
    file = open(path)
    element = []
    dataSet = []
    nome = ''
    c = 0
    for line in file:
        for word in line.split():
            if(word == 'sample_label'):
                break
            else:
                if(line.split().index(word) == 0):
                    nome = word
                else:
                    element.append(float(word))
        if(element):
            datasetObject = dataset(nome, element, c)
            dataSet.append(datasetObject)
            c += 1
        element = []
    file.close()
    return dataSet

#realiza o agrupamento utilizando single-link, e salva o clustering como imagens
def singleLinkClustering(min, max, path, name):
    data = readDataSet(path)
    clusterSize = len(data)
    clusters = [[i] for i in data]

    count = 0

    #loop para fazer o agrupamento de todas as quantidades de clusters entre min e max
    while(clusterSize > min):
        list = []
        x = 0
        for i in clusters:
            print("X: ", x, "Cluster: ", i, "Iteração: ", count, "Clustersize:", clusterSize)   
            y = 0
            for j in clusters:
                if(x > y):
                    dist = minDist(i, j)
                    aux = obj(x, y, dist)
                    list.append(aux)
                y = y+1
            x = x+1
        list.sort(key=sorting)
        clusters[list[0].x] += clusters[list[0].y]
        del(clusters[list[0].y])
        clusterSize = clusterSize - 1
        if(clusterSize <= max):
            file = open('clusterFiles/singleLink/' + name + str(clusterSize) + '.clu', 'w')
            n = 0

            for i in clusters:
                for l in i:
                    for k in data:
                        if l.nome == k.nome:
                            k.cluster = n
                            break
                n += 1

            for each in data:
                file.write(str(each.nome) + '\t' + str(each.cluster)+'\n')
        count += 1