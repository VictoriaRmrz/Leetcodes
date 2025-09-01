def findFairDistribution(points, values):
    hash = {}
    result = []
    #values.sort()
    values = list(set(values)) 
    aux = points.copy()
    #aux.sort()
    aux = list(set(aux)) # eliminar duplicados
    for i in range(len(aux)):
        hash[aux[i]] = values[i]

    for point in points:
        result.append(hash[point])

    return result

def main():
    points = [5, 2, 1, 2]
    values = [3, 2, 3, 4, 4, 2, 2]
    distribution = findFairDistribution(points, values) # [4,3,2,3]
    print(distribution)

if __name__ == "__main__":
    main()
