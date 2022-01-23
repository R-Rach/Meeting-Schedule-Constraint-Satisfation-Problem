"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


def domainGraphGenerator(text,m):
    domainDict = {}

    temp = text.split('\n')
    for i in range(len(temp)):
        temp[i] = temp[i].split(':')
        temp[i] = temp[i][1].split(",")
        for j in range(len(temp[i])):
            temp[i][j] = int(temp[i][j])

    for i in range(m):
        domainDict["N"+str(i+1)] = temp[i]
    
    return domainDict