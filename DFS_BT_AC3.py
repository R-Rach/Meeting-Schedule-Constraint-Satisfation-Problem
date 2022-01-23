"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import copy
import time

import GlobalVariables
from ConstraintCheck import constraintSatisfied
from MRV import mrv


def dfs_bt_ac3(constraintGraph, domainGraph, assignDict, m, f, heuristic, qtobj):

    if len(assignDict) == m:
        return assignDict

    for var,temp in domainGraph.items():
        if var in assignDict:
            continue
        else:
            break
    for value in domainGraph[var]:
        GlobalVariables.nodeCount = GlobalVariables.nodeCount + 1
        localAssign = copy.deepcopy(assignDict)
        localAssign[var] = value
        if heuristic == "DEFAULT":
            if GlobalVariables.nodeCount % 200 == 0 or GlobalVariables.nodeCount == 1 or GlobalVariables.nodeCount == 2 or GlobalVariables.nodeCount == 3 or GlobalVariables.nodeCount == 4 or GlobalVariables.nodeCount == 5 or GlobalVariables.nodeCount == 6 or GlobalVariables.nodeCount == 7 or GlobalVariables.nodeCount == 8 or GlobalVariables.nodeCount == 9 or GlobalVariables.nodeCount == 10:
                qtobj.showtextbox.append(str(GlobalVariables.nodeCount) + "-> " + str(localAssign) + "\n")
        if heuristic == "MRV":
            qtobj.showtextbox.append(str(GlobalVariables.nodeCount) + "-> " + str(localAssign) + "\n")

        f.write(str(localAssign)+"\n")
        if constraintSatisfied(var, localAssign, constraintGraph):

            if len(localAssign) > GlobalVariables.maxcount:
                GlobalVariables.maxcount = len(localAssign)
                GlobalVariables.maxassign = localAssign

            newlocalDomainGraph = ac3(var, domainGraph, localAssign, constraintGraph, heuristic)
            result = dfs_bt_ac3(constraintGraph, newlocalDomainGraph, localAssign, m, f, heuristic, qtobj)

            if result is not None:
                return result
    return None


def ac3(var, domainGraph, localAssignDict, constraintGraph, h):

    localDomainGraph = copy.deepcopy(domainGraph)
    localDomainGraph.pop(var)
    varAssign = localAssignDict[var]

    for neighbours in constraintGraph[var]:
        if localDomainGraph.__contains__(neighbours):
            if localDomainGraph[neighbours].__contains__(varAssign):
                localDomainGraph[neighbours].remove(varAssign)

    if h == "MRV":
        localDomainGraph = mrv(localDomainGraph, constraintGraph)
        return localDomainGraph
    else:
        return localDomainGraph