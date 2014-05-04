def possible_mean(L):
    return float(sum(L))/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return float(temp) / len(L)

def test():
    A = [0,1,2,3,4,5,6,7,8]

    B = [5,10,10,10,15]

    C = [0,1,2,4,6,8]

    D = [6,7,11,12,13,15]

    E = [9,0,0,3,3,3,6,6]

    all = [A,B,C,D,E]
    for L in all:
        print(possible_mean(L))
        print(possible_variance(L))
        print("\n")

test()