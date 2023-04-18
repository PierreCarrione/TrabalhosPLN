import numpy as np

def distEdicao(target, source):
    matSolu = np.empty((len(target) + 1,len(source) + 1))

    for i in range(len(target) + 1):
        matSolu[i][0] = i
    for i in range(len(source) + 1):
        matSolu[0][i] = i

    for i in range(len(target) + 1):
        for j in range(len(source) + 1):

            if target[i - 1] == source[j - 1]:
                matSolu[i][j] = matSolu[i - 1][j - 1]
            else:
                matSolu[i][j] = 1 + min(matSolu[i][j - 1],  # Insert
                                   matSolu[i - 1][j],  # Remove
                                   matSolu[i - 1][j - 1])  # Replace

    return matSolu[len(target)][len(source)]


str1 = "sunday"
str2 = "saturday"

print(distEdicao(str1, str2))