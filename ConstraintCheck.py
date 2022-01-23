"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


def constraintSatisfied(var, localassignDict, cg):
    assign = localassignDict[var]
    neighboursList = cg[var]

    for neighbours in neighboursList:
        if neighbours in localassignDict:
            if localassignDict[neighbours] == assign:
                return False

    return True