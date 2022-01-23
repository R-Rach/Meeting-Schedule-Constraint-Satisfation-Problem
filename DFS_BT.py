"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import copy
import time

import GlobalVariables
from ConstraintCheck import constraintSatisfied
from MRV import mrv


def dfs_bt(constraintGraph, sortedDomainGraph, assignDict, m,f, heuristics, qtobj):

    if len(assignDict) == m:
        return assignDict

    for var,temp in sortedDomainGraph.items():
        if var in assignDict:
            continue
        else:
            break

    for value in sortedDomainGraph[var]:
        GlobalVariables.nodeCount = GlobalVariables.nodeCount + 1
        localAssign = copy.deepcopy(assignDict)
        localAssign[var] = value
        if heuristics == "DEFAULT":
            if GlobalVariables.nodeCount%500 == 0 or GlobalVariables.nodeCount == 1 or GlobalVariables.nodeCount == 2 or GlobalVariables.nodeCount ==3 or GlobalVariables.nodeCount ==4 or GlobalVariables.nodeCount ==5  or GlobalVariables.nodeCount ==6 or GlobalVariables.nodeCount ==7 or GlobalVariables.nodeCount ==8or GlobalVariables.nodeCount ==9 or GlobalVariables.nodeCount ==10:
                qtobj.showtextbox.append(str(GlobalVariables.nodeCount)+"-> "+str(localAssign)+"\n")
        if heuristics == "MRV":
            if GlobalVariables.nodeCount % 50 == 0 or GlobalVariables.nodeCount == 1 or GlobalVariables.nodeCount == 2 or GlobalVariables.nodeCount == 3 or GlobalVariables.nodeCount == 4 or GlobalVariables.nodeCount == 5:
                qtobj.showtextbox.append(str(GlobalVariables.nodeCount) + "-> " + str(localAssign) + "\n")
        f = open('output.txt', 'a')
        f.write(str(localAssign)+"\n")
        if constraintSatisfied(var, localAssign, constraintGraph):

            if len(localAssign) > GlobalVariables.maxcount:
                GlobalVariables.maxcount = len(localAssign)
                GlobalVariables.maxassign = localAssign

            result = dfs_bt(constraintGraph,sortedDomainGraph,localAssign,m,f,heuristics,qtobj)

            if result is not None:
                return result
    return None