def euclidean_dist(x, y):
    result = 0
    for i in range(len(x)):
            result += pow( (x[i] - y[i]), 2)
    result = pow(result, 0.5)
    return result
    raise NotImplementedError()

def manhattan_dist(x, y):
    result = 0
    for i in range(len(x)):
            result += abs(x[i] - y[i])
    return result
    raise NotImplementedError()

def jaccard_dist(x, y):
    x = set(x)
    y = set(y)
    J = len(x.intersection(y)) /len(x.union(y))
    return 1-J
    raise NotImplementedError()

def cosine_sim(x, y):
    product = 0
    sqrtx = 0
    sqrty = 0
    for i in range(len(x)):
            product += x[i] * y[i]
            sqrtx += pow(x[i], 2)
            sqrty += pow(y[i], 2)
    return product / pow(sqrtx * sqrty, 0.5)
    raise NotImplementedError()

# Feel free to add more
