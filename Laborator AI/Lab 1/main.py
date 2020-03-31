import math


def ex1():
    text = "Ana are mere rosii si galbene"
    print("Ultimul cuvant este: " + str(ex1solver(text)))

def ex1solver(text):
    l = text.split(" ")
    l.sort()
    return l[len(l) - 1]


def ex2():
    xa = 1
    ya = 5
    xb = 4
    yb = 1
    print("Distanta euclidiana este: " + str(ex2solver(xa, ya, xb, yb)))

def ex2solver(xa, ya, xb, yb):
    return math.sqrt((xa-xb)**2 + (ya-yb)**2)


def ex3():
    v = [1,0,2,0,3]
    w = [1,2,0,3,1]
    print("Produsul vectorilor este: "+ str(ex3solver(v, w)))

def ex3solver(v, w):
    produs = 0
    for i in range(len(v)):
        produs += v[i] * w[i]
    return produs


def ex4():
    text = "ana are ana are mere rosii ana"
    print("Cuvintele care apar o singura data in text sunt:")
    ex4solver(text)

def ex4solver(text):
    list = text.split(" ")
    for i in list:
        word = list.count(i)
        if word == 1:
            print(i)


def ex5():
    arr = [1,2,3,4,2]
    print("Numarul care se repeta de 2 ori este: " + str(ex5solver(arr)))

def ex5solver(list):
    return sum(list) - (len(list) * (len(list) - 1) / 2)
    """
    for i in arr:
        cont = arr.count(i)
        if cont == 2:
            return i
    """


def ex6():
    n = 11
    arr = [2,8,7,2,2,5,2,3,1,2,2]
    print("Elementul majoritar este: " + str(ex6solver(arr, n)))

def ex6solver(arr, n):
    def getMajorityElement(list):
        candidate = None
        count = 0
        for element in list:
            if element != candidate:
                if count == 0:
                    candidate = element
                    count = 1
                else:
                    count -= 1
            else:
                count += 1

        count = 0
        for element in list:
            count += 1 if element == candidate else 0

        return candidate if count >= len(list) // 2 + 1 else None
    '''
    for i in arr:
        cont = arr.count(i)
        if cont > n // 2:
            return i
    '''


def ex7():
    k = 2
    n = 6
    arr = [7,4,6,3,9,1]
    print("Al k-lea cel mai mare numar este: " + str(ex7solver(arr, k)))

def ex7solver(arr, k):
    sarr = sorted(arr, reverse=True)
    return sarr[k - 1]


def ex8():
    n = 16
    print(ex8solver(n))

def ex8solver(n):
    q = []
    binary = []
    q.append("1")

    i = 1
    while i <= n:
        q.append(q[0] + "0")
        q.append(q[0] + "1")

        binary.append(q[0])
        q.pop(0)
        i+=1

    return binary


def ex9():
    matrix = [[0, 2, 5, 4, 1],
              [4, 8, 2, 3, 7],
              [6, 3, 4, 6, 2],
              [7, 3, 1, 8, 3],
              [1, 5, 7, 9, 4]]
    print("Suma este: " + str(ex9solver(matrix, 1, 1, 3, 3)))

def ex9solver(matrix, p, q, r, s):
    sum = 0
    i = p
    while i <= r:
        j = q
        while j <= s:
            sum += matrix[i][j]
            j+=1
        i+=1

    return sum


def ex10():
    n = 3
    m = 5
    matrix = [[0,0,0,1,1],
              [0,1,1,1,1],
              [0,0,1,1,1]]
    print("Linia este: " + str(ex10solver(matrix, n, m)))

def ex10solver(matrix, n, m):
    maxi = 0
    line = 0
    for i in range(n):
        j = 0
        while matrix[i][j] == 0:
            j += 1
        if maxi < m - j:
            maxi = m - j
            line = i

    return line + 1



def getNumberOfOnes(arr):
    left = 0
    n = right = len(arr)

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0)):
            return n - mid
        elif (arr[mid] == 1):
            right = mid - 1
        else:
            left = mid + 1

'''
    Returneaza linia din matrice care contine cele mai multe valori de 1
    Input: matrix - Array of arrays
    Ouput: lineIndex - integer
'''
def getMaxLineIndex(matrix):
    lineIndex = -1
    maxOnes = -1

    for index, line in enumerate(matrix):
        sum = getNumberOfOnes(line)
        if sum > maxOnes:
            maxOnes = sum
            lineIndex = index

    return lineIndex

def exe10():
    matrix = [[0, 0, 0, 1, 1],
              [0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1]]

    lineIndex = getMaxLineIndex(matrix)

    print(lineIndex + 1)




def ex11solver(matrix, n, m):

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and minimumSteps(matrix, i, j, n, m) == -1:
                matrix[i][j] = 1

    return matrix


def minimumSteps(mat, x, y, n, m):

    # init matrice valori rute cu -1
    dp = [[-1 for i in range(m)] for i in range(n)]

    # init matrice vizitata cu flase
    vis = [[False for i in range(m)] for i in range(n)]

    # apelam functia pentru pasii minimi
    res = findMinSteps(mat, x, y, dp, vis, n, m)

    # daca nu exista
    if (res >= 99999):
        return -1
    else:
        return res


def findMinSteps(mat, n, m, dp, vis, row, col):

    # am ajuns la margine
    if (n == 0 or m == 0 or n == (row - 1) or m == (col - 1)):
        return 0

    # exista deja ruta pe aici
    if (dp[n][m] != -1):
        return dp[n][m]

    # vizitam pozitia
    vis[n][m] = True

    # rutele
    ans1, ans2, ans3, ans4 = 99999, 99999, 99999, 99999

    # vertical sus
    if (mat[n - 1][m] == 0):
        if (vis[n - 1][m] == False):
            ans1 = 1 + findMinSteps(mat, n - 1, m, dp, vis, row, col)

    # orizontal dreapta
    if (mat[n][m + 1] == 0):
        if (vis[n][m + 1] == False):
            ans2 = 1 + findMinSteps(mat, n, m + 1, dp, vis, row, col)

    # orizontal stanga
    if (mat[n][m - 1] == 0):
        if (vis[n][m - 1] == False):
            ans3 = 1 + findMinSteps(mat, n, m - 1, dp, vis, row, col)

    # vertical jos
    if (mat[n + 1][m] == 0):
        if (vis[n + 1][m] == False):
            ans4 = 1 + findMinSteps(mat, n + 1, m, dp, vis, row, col)

    # calea minima rezultata din toate rutele
    dp[n][m] = min(ans1, min(ans2, min(ans3, ans4)))
    return dp[n][m]



def ex11():
    matrix = [[1,1,1,1,0,0,1,1,0,1],
              [1,0,0,1,1,0,1,1,1,1],
              [1,0,0,1,1,1,1,1,1,1],
              [1,1,1,1,0,0,1,1,0,1],
              [1,0,0,1,1,0,1,1,0,0],
              [1,1,0,1,1,0,0,1,0,1],
              [1,1,1,0,1,0,1,0,0,1],
              [1,1,1,0,1,1,1,1,1,1]]

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in ex11solver(matrix, 8, 10)]))



if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
    ex8()
    ex9()
    exe10()
    ex11()




