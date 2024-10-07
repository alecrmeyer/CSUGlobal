import numpy as np

def gen_cost_matrix(a, b):
    xlen = len(a) + 1
    ylen = len(b) + 1

    ret = np.matrix(np.ones((xlen,ylen)) * np.inf)
    ret[0,0] = 0
    for i in range(1, xlen):
        for j in range(1, ylen):
            dist = (a[i-1] - b[j-1])**2

            deletion = ret[i-1, j]
            insertion = ret[i, j-1]
            match = ret[i-1, j-1]

            ret[i,j] = dist + min(deletion, insertion, match)
    return ret

def cheapest_alignment(cost_matrix):
    dimensions = cost_matrix.shape
    rows, columns = dimensions
    i = rows - 1
    j = columns - 1

    cost = cost_matrix[i, j]
    path = [[]]
    path.append([i, j])
    while(i > 0 and j > 0):
        a = cost_matrix[i-1, j]
        b = cost_matrix[i, j-1]
        c = cost_matrix[i-1, j-1]
        tmp = np.array([a, b, c])
        ind = np.argmin(tmp)

        if ind == 0:
            cost += cost_matrix[i-1, j]
            i -= 1
        elif ind == 1:
            cost += cost_matrix[i, j-1]
            j -= 1
        else:
            cost += cost_matrix[i-1, j-1]
            i-=1
            j-=1
        path.append([i, j])
    path = path[1:] # Remove empty entry
    return cost, path

def euclidean_cost(a, b):
    matrix = np.zeros((len(a), len(b)))
    for i in range(len(a)):
        for j in range(len(b)):
            matrix[i, j] = (a[i] - b[j])**2
    return matrix

def cost_euclid(a, b):
    cost_matrix = euclidean_cost(a, b)
    cost, path = cheapest_alignment(cost_matrix)
    return cost, path

def cost(a, b):
    cost_matrix = gen_cost_matrix(a, b)
    cost, path = cheapest_alignment(cost_matrix)
    return cost, path



            