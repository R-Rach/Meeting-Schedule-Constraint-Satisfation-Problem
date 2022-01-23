"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


def mrv(domaindict, constraintdict):
    domainlist = list(domaindict.items())

    for i in range(len(domainlist)):
        for j in range(i + 1, len(domainlist)):
            if len(domainlist[j][1]) < len(domainlist[i][1]):
                temp = domainlist[i]
                domainlist[i] = domainlist[j]
                domainlist[j] = temp
            if len(domainlist[j][1]) == len(domainlist[i][1]):
                if len(constraintdict[domainlist[j][0]]) > len(constraintdict[domainlist[i][0]]):
                    temp = domainlist[i]
                    domainlist[i] = domainlist[j]
                    domainlist[j] = temp

    return dict(domainlist)