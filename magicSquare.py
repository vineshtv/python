#!/bin/python3
'''
Solution for hackerrank problem - Forming a Magic Square.
Given a 3x3 matrix, find the cost of converting it to a magic square.
You will be given a  matrix  of integers in the inclusive range . We can
convert any digit  to any other digit  in the range  at cost of . Given ,
convert it into a magic square at minimal cost. Print this cost on a new line.

Note: For this particular case I could have hardcoded all the magic squares
of order 3(because the question had it hardcoded as 3). But this is scalable
for all indices(odd of course)
'''


# Create a magic square
def createms(n):
    m_s = [[0 for i in range(n)] for j in range(n)]

    #initialise the position of 1
    i = n//2
    j = n-1

    #Fill the magic square
    num = 1
    while num <= (n*n):
        if i == -1 and j == n: #case 3
            j = n - 2
            i = 0
            #j = n - 2
        else: # Check of out of bounds case from case 1
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        #print(i, j)
        if m_s[i][j] != 0: # Case 2
            j -= 2
            i += 1
            continue
        else:
            m_s[i][j] = num
            num += 1

        # Update the indices according to case 1
        i -= 1
        j += 1

    return m_s

def calcCost(s, ms, n):
    cost = 0
    for i in range(n):
        for j in range(n):
            cost += abs(s[i][j] - ms[i][j])

    return cost

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    min_cost = 0
    #Create the first magic square
    m1 = createms(3)
    m2 = list(zip(*m1[::-1]))
    m3 = list(zip(*m2[::-1]))
    m4 = list(zip(*m3[::-1]))
    m5 = list(zip(*m1))
    m6 = list(zip(*m2))
    m7 = list(zip(*m3))
    m8 = list(zip(*m4))

    min_cost = calcCost(s, m1, 3)
    ms = [m2, m3, m4, m5, m6 ,m7 ,m8]
    for x in ms:
        calc_cost = calcCost(s, x, 3)
        if calc_cost < min_cost:
            min_cost = calc_cost

    return(min_cost)

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

