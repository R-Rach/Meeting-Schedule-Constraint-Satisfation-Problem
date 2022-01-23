"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import re

def constraintGraphGenerator(text, m):

    cgDict = {}

    temp = text.split('\n')

    for i in range(len(temp)):
        temp[i] = temp[i].split(':')
        temp[i] = temp[i][1].split(",")

    for i in range(m):
        cgDict["N"+str(i+1)] = []

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            x = temp[i][j]

            for k in range(len(temp[i])):
                if k == j:
                    continue
                if not cgDict[x].__contains__(temp[i][k]):
                    cgDict[x].append(temp[i][k])
    return cgDict