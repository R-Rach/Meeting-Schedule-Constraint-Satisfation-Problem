"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


import sys
import GlobalVariables
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ConstraintGraphGenrator import constraintGraphGenerator
from DFS_BT import dfs_bt
from DFS_BT_AC3 import dfs_bt_ac3
from DomainGraphGenerator import domainGraphGenerator
from MRV import mrv


class GUIDriver(QMainWindow):

    def __init__(self):
        super(GUIDriver, self).__init__()
        self.setGeometry(0, 30, 1450, 810)
        self.setWindowTitle("AI Assignment 4")
        self.nLabel = []
        self.nAnsLabel = []
        for i in range(30):
            self.nLabel.append(QtWidgets.QLabel(self))
            self.nAnsLabel.append(QtWidgets.QLabel(self))
        self.initGUI()

    def initGUI(self):

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("GROUPS")
        self.label1.move(120, 0)

        self.textbox1 = QTextEdit(self)
        self.textbox1.move(5, 45)
        self.textbox1.resize(300, 200)
        self.textbox1.setText(
            "G1:N3,N5,N8,N9,N12,N18,N19\nG2:N8,N9,N12,N19,N2\nG3:N3,N5,N4,N16,N8,N9,N19\nG4:N8,N9,N12,N15\nG5:N15,N16,N17,N18,N19,N20\nG6:N3,N5,N7,N11,N14,N20\nG7:N3,N5,N12,N2,N18,N19,N20,N1\nG8:N3,N5,N8,N9,N10,N18,N19,N20\nG9:N3,N13,N8,N9,N7,N19,N20\nG10:N1,N8,N9,N13,N20\nG11:N18,N19,N20\nG12:N3,N11,N8,N18,N19,N20\nG13:N3,N8,N10,N12,N4,N20\nG14:N3,N5,N11,N9,N10,N17,N19,N20\nG15:N2,N8,N12,N18,N19,N20")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PERSONS")
        self.label2.move(450, 0)

        self.textbox2 = QTextEdit(self)
        self.textbox2.move(324, 45)
        self.textbox2.resize(300, 200)
        self.textbox2.setText(
            "N1:2,5,7\nN2:1,4,6,2\nN3:2,5,6,1\nN4:2,4,6,8\nN5:2,6,5\nN6:1,5,3\nN7:2,4,6,1,8\nN8:1,3,4\nN9:4,1,5,8,6\nN10:8\nN11:2,3\nN12:1,2,3,4,7\nN13:7,1,8\nN14:5,3,6,1\nN15:2,5\nN16:2,5,1,4\nN17:1,4,5,6\nN18:5,4\nN19:1,3,6,8\nN20:6")

        self.resetB = QtWidgets.QPushButton(self)
        self.resetB.setText("RESET ALL")
        self.resetB.resize(200, 30)
        self.resetB.move(700, 10)
        self.resetB.clicked.connect(self.resetBclicked)

        self.setMtextbox = QLineEdit(self)
        self.setMtextbox.resize(180, 30)
        self.setMtextbox.move(650, 60)

        self.setValuemB = QtWidgets.QPushButton(self)
        self.setValuemB.resize(100, 30)
        self.setValuemB.move(850, 60)
        self.setValuemB.setText("SET 'm'")
        self.setValuemB.clicked.connect(self.setValueMClicked)

        self.heuristicTextbox = QLineEdit(self)
        self.heuristicTextbox.resize(200, 30)
        self.heuristicTextbox.move(710, 110)
        self.heuristicTextbox.setEnabled(False)

        self.heuristicLabel = QtWidgets.QLabel(self)
        self.heuristicLabel.setText("ENTER above the desired heuristic\n\r\r\r\r\r\r\r\r\r\r\r\r\r\r(DEFAULT/MRV)")
        self.heuristicLabel.adjustSize()
        self.heuristicLabel.move(706, 145)

        self.dfsB = QtWidgets.QPushButton(self)
        self.dfsB.resize(100, 60)
        self.dfsB.move(670, 190)
        self.dfsB.setText("DFS\nBacktracking")
        self.dfsB.setEnabled(False)
        self.dfsB.clicked.connect(self.dfsBclicked)

        self.ac3B = QtWidgets.QPushButton(self)
        self.ac3B.resize(100, 60)
        self.ac3B.move(850, 190)
        self.ac3B.setText("DFS\nBacktracking\nAC3")
        self.ac3B.setEnabled(False)
        self.ac3B.clicked.connect(self.ac3Bclicked)

        # 12 alalysis label
        self.r1L = QtWidgets.QLabel(self)
        self.r1L.setText("R1-> No of nodes till end (DFS+BT)-default ordering: 26635")
        self.r1L.move(1000, 10)
        self.r1L.adjustSize()

        self.r2L = QtWidgets.QLabel(self)
        self.r2L.setText("R2-> Memory allocated to one node: 216 Bytes")
        self.r2L.move(1000, 40)
        self.r2L.adjustSize()

        self.r3L = QtWidgets.QLabel(self)
        self.r3L.setText("R3-> Max length of implicit stack generated-default ordering: 18\n\r\r\r\r\r\r\r\r\r[cause max possible partial assignment is 17 in this case]")
        self.r3L.move(1000, 70)
        self.r3L.adjustSize()

        self.r4L = QtWidgets.QLabel(self)
        self.r4L.setText("R4-> Total time (DFS+BT)-default ordering: 2.912 sec")
        self.r4L.move(1000, 108)
        self.r4L.adjustSize()

        self.r5L = QtWidgets.QLabel(self)
        self.r5L.setText("R5 -> No of nodes till end (DFS+BT)-MRV: 772")
        self.r5L.move(1000, 130)
        self.r5L.adjustSize()

        self.r6L = QtWidgets.QLabel(self)
        self.r6L.setText("R6-> No of nodes till end (DFS+BT+AC3)-default ordering: 8545")
        self.r6L.move(1000, 160)
        self.r6L.adjustSize()

        self.r7L = QtWidgets.QLabel(self)
        self.r7L.setText("R7-> (R1 - R6)/R1: 0.6791")
        self.r7L.move(1000, 190)
        self.r7L.adjustSize()

        self.r8L = QtWidgets.QLabel(self)
        self.r8L.setText("R8-> Total time to compute (DFS+BT+AC3)-default ordering: 0.7312 sec")
        self.r8L.move(1000, 220)
        self.r8L.adjustSize()

        self.r9L = QtWidgets.QLabel(self)
        self.r9L.setText(
            "R4 vs R8-default ordering: With AC3 it takes 75% less time to compute\n\nGIVEN PROBLEM HAS NO COMPLETE ASSIGNMENT\n[so no. of nodes and timings are till complete tree is traversed]\n\nMAX possible Partial Assignments ----\n1) DFS+BT with default ordering- N1 to N17\n2) DFS+BT with MRV- N10,N20,N11,N15,N18,N1,N5,N6,N8,N13,\n\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\r\rN2,N3,N4,N14,N16\n3) DFS+BT+AC3 with default ordering- N1 to N17\n4) DFS+BT+AC3 with MRV- N10,N20,N11,N5,N18,N3")
        self.r9L.move(1000, 250)
        self.r9L.adjustSize()

        # 100node
        self.showtextbox = QTextEdit(self)
        self.showtextbox.move(5, 450)
        self.showtextbox.resize(700, 345)
        self.showtextbox.setLineWrapMode(QTextEdit.NoWrap)

        # noofnodes
        self.noofnodestb = QtWidgets.QLabel(self)
        self.noofnodestb.move(400, 425)
        self.noofnodestb.setText("No. of Nodes Generated -->")
        self.noofnodestb.adjustSize()

        self.noofnodestb2 = QtWidgets.QLabel(self)
        self.noofnodestb2.move(580, 425)
        self.noofnodestb2.setText("")
        self.noofnodestb2.adjustSize()
        # assignment
        self.assignL = QtWidgets.QLabel(self)
        self.assignL.setText("<-- MAX POSSIBLE PARTIAL ASSIGNMENT")
        self.assignL.setStyleSheet("QLabel {color:red;}")
        self.assignL.move(620, 321)
        self.assignL.adjustSize()
        # show
        self.showL = QtWidgets.QLabel(self)
        self.showL.setText("SOME NODES IN BETWEEN WILL BE SHOWN BELOW:\n(with node no. in front)")
        self.showL.move(5, 419)
        self.showL.adjustSize()
        # instruction
        self.instrtL = QtWidgets.QLabel(self)
        self.instrtL.setText("**** INSTRUCTIONS ****\n\n"
                             "1.) In the GROUPS and PERSONS textbox, default configurations are already present.\n"
                             "\r\r\r\r\rIf required, enter desired groups and personalities configuration in the same format as default.\n"
                             "\r\r\r\r\r(NO WHITE_SPACES or EMPTY_LINES anywhere || USE COMMA, COLON and variable names as default)\n\n"
                             "2.) Enter the value of 'm' -> same as number of variables specified in PERSONS textbox and click on \" SET 'm' \" button.\n\n"
                             "3.) Enter the desired heuristics- DEFAULT/MRV (in caps only) and Click on desired technique- DFS+BT or DFS+BT+AC3.\n\n"
                             "--> 4 POSSIBILITIES:- DEFAULT with DFS+BT||DEFAULT with DFS+BT+AC3||MRV with DFS+BT||MRV with DFS+BT+AC3\n"
                             "--> Every 500th/50th/200th node (depending upon total amount of node generated) \n\r\r\r\r\r\r\rand total no of nodes generated will be shown in textbox.\n"
                             "--> If given configuration does not have any solution, then maximum possible partial assignment will be shown in table,\n"
                             "\r\r\r\r\r\r\relse if solution exists, full assignment will be shown.\n"
                             "--> The ordering shown in table will be same as provided by heuristic (default or mrv).\n"
                             "--> There's a file name 'output.txt' that will have data of every node generated in sequence by the current technique.\n"
                             "--> After clicking on desired technique, open output.txt for data checking and close it afterwards.\n\n"
                             "5.) CLICK ON 'RESET ALL' button, it'll reset all data on GUI and output.txt file.\n"
                             "\r\r\r\r\rThen repeat step 1 to 3 with different heuristic and technique.")
        self.instrtL.move(715, 420)
        self.instrtL.adjustSize()

        self.extraL = QtWidgets.QLabel(self)
        self.extraL.setText("IT WAS NOT POSSIBLE to show every 100th node in given table and keep on updating it after a delay,\n"
                            "because PyQt5 was not supporting the sleep() method and such updating graphics in between recursion calls.\n"
                            "Hence I have displayed in the textbox which can be scrolled.")
        self.extraL.setStyleSheet("QLabel {color:red;}")
        self.extraL.move(715, 760)
        self.extraL.adjustSize()

    def paintEvent(self, event):
        line = QPainter()
        line.begin(self)
        line.setPen(Qt.red)
        line.drawLine(0, 255, 632, 255)
        line.drawLine(314, 0, 314, 255)
        line.drawLine(632, 0, 632, 255)
        line.setPen(Qt.black)
        line.drawLine(632, 50, 990, 50)
        line.drawLine(632, 100, 990, 100)
        line.drawLine(990, 0, 990, 450)
        line.drawLine(990, 450, 1450, 450)
        line.drawLine(632, 184, 990, 184)
        line.drawLine(811, 184, 811, 255)
        line.drawLine(632, 255, 990, 255)
        line.drawLine(0, 420, 990, 420)
        line.drawLine(710, 420, 710, 800)
        line.drawLine(390, 420, 390, 450)

    def setValueMClicked(self):

        if self.setMtextbox.text() == '':
            GlobalVariables.m = 20
        else:
            GlobalVariables.m = int(self.setMtextbox.text())

        if GlobalVariables.m < 6 or GlobalVariables.m > 30:
            self.setMtextbox.setText("ERASE & ENTER b/w 6-30")
            return

        self.setValuemB.setEnabled(False)
        self.setMtextbox.setEnabled(False)
        self.heuristicTextbox.setEnabled(True)
        self.dfsB.setEnabled(True)
        self.ac3B.setEnabled(True)
        for i in range(GlobalVariables.m):
            if i < 15:
                self.nLabel[i].resize(40, 30)
                self.nLabel[i].setStyleSheet("border: 1px solid black")
                self.nLabel[i].move(10 + i * 40, 265)

                self.nAnsLabel[i].resize(40, 30)
                self.nAnsLabel[i].setStyleSheet("border: 1px solid black")
                self.nAnsLabel[i].move(10 + i * 40, 295)

            elif i >= 15 and i < 30:
                self.nLabel[i].resize(40, 30)
                self.nLabel[i].setStyleSheet("border: 1px solid black")
                self.nLabel[i].move(10 + ((i - 15) * 40), 335)

                self.nAnsLabel[i].resize(40, 30)
                self.nAnsLabel[i].setStyleSheet("border: 1px solid black")
                self.nAnsLabel[i].move(10 + ((i - 15) * 40), 365)

    def resetBclicked(self):
        self.textbox1.setEnabled(True)
        self.textbox2.setEnabled(True)
        self.setMtextbox.setEnabled(True)
        self.setValuemB.setEnabled(True)
        self.heuristicTextbox.setEnabled(False)
        self.dfsB.setEnabled(False)
        self.ac3B.setEnabled(False)
        self.showtextbox.setText("")
        self.noofnodestb2.setText("")
        GlobalVariables.nodeCount = 0
        GlobalVariables.maxcount = 0
        GlobalVariables.maxassign = {}
        GlobalVariables.constraintgraph = {}
        GlobalVariables.domainGraph = {}
        os.remove('output.txt')
        GlobalVariables.f = open('output.txt', 'w')
        for i in range(GlobalVariables.m):
            self.nLabel[i].setText("")
            self.nLabel[i].resize(0, 0)
            self.nAnsLabel[i].setText("")
            self.nAnsLabel[i].resize(0, 0)
        GlobalVariables.m = 0

    def dfsBclicked(self):
        h = self.heuristicTextbox.text()

        if h == "DEFAULT":
            self.heuristicTextbox.setEnabled(False)
            self.dfsB.setEnabled(False)
            self.ac3B.setEnabled(False)
            GlobalVariables.constraintgraph = constraintGraphGenerator(self.textbox1.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = domainGraphGenerator(self.textbox2.toPlainText(), GlobalVariables.m)

            result = dfs_bt(GlobalVariables.constraintgraph, GlobalVariables.domainGraph, {}, GlobalVariables.m,
                            GlobalVariables.f, h, self)
            if result is None:
                i = 0
                for v, a in GlobalVariables.maxassign.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            if result is not None:
                i = 0
                for v, a in result.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            GlobalVariables.f.close()
            self.noofnodestb2.setText(str(GlobalVariables.nodeCount))
            self.noofnodestb2.setStyleSheet("QLabel {color:red;}")
            self.noofnodestb2.adjustSize()
            return

        if h == "MRV":
            self.heuristicTextbox.setEnabled(False)
            self.dfsB.setEnabled(False)
            self.ac3B.setEnabled(False)
            GlobalVariables.constraintgraph = constraintGraphGenerator(self.textbox1.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = domainGraphGenerator(self.textbox2.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = mrv(GlobalVariables.domainGraph,GlobalVariables.constraintgraph)

            result = dfs_bt(GlobalVariables.constraintgraph, GlobalVariables.domainGraph, {}, GlobalVariables.m,
                            GlobalVariables.f, h, self)
            if result is None:
                i = 0
                for v, a in GlobalVariables.maxassign.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            if result is not None:
                i = 0
                for v, a in result.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            GlobalVariables.f.close()
            self.noofnodestb2.setText(str(GlobalVariables.nodeCount))
            self.noofnodestb2.setStyleSheet("QLabel {color:red;}")
            self.noofnodestb2.adjustSize()
            return

        else:
            self.heuristicTextbox.setText("ERASE and ENTER correctly")
            return

    def ac3Bclicked(self):
        h = self.heuristicTextbox.text()

        if h == "DEFAULT":
            self.heuristicTextbox.setEnabled(False)
            self.dfsB.setEnabled(False)
            self.ac3B.setEnabled(False)
            GlobalVariables.constraintgraph = constraintGraphGenerator(self.textbox1.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = domainGraphGenerator(self.textbox2.toPlainText(), GlobalVariables.m)

            result = dfs_bt_ac3(GlobalVariables.constraintgraph, GlobalVariables.domainGraph, {}, GlobalVariables.m,
                                GlobalVariables.f, "DEFAULT", self)
            if result is None:
                i = 0
                for v, a in GlobalVariables.maxassign.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            if result is not None:
                i = 0
                for v, a in result.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            GlobalVariables.f.close()
            self.noofnodestb2.setText(str(GlobalVariables.nodeCount))
            self.noofnodestb2.setStyleSheet("QLabel {color:red;}")
            self.noofnodestb2.adjustSize()
            return

        if h == "MRV":
            self.heuristicTextbox.setEnabled(False)
            self.dfsB.setEnabled(False)
            self.ac3B.setEnabled(False)
            GlobalVariables.constraintgraph = constraintGraphGenerator(self.textbox1.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = domainGraphGenerator(self.textbox2.toPlainText(), GlobalVariables.m)
            GlobalVariables.domainGraph = mrv(GlobalVariables.domainGraph, GlobalVariables.constraintgraph)

            result = dfs_bt_ac3(GlobalVariables.constraintgraph, GlobalVariables.domainGraph, {}, GlobalVariables.m,
                                GlobalVariables.f, "MRV", self)
            if result is None:
                i = 0
                for v, a in GlobalVariables.maxassign.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            if result is not None:
                i = 0
                for v, a in result.items():
                    self.nLabel[i].setText(str(v))
                    self.nAnsLabel[i].setText(str(a))
                    i = i + 1
            GlobalVariables.f.close()
            self.noofnodestb2.setText(str(GlobalVariables.nodeCount))
            self.noofnodestb2.setStyleSheet("QLabel {color:red;}")
            self.noofnodestb2.adjustSize()
            return

        else:
            self.heuristicTextbox.setText("ERASE and ENTER correctly")
            return


def window():
    app = QApplication(sys.argv)
    window = GUIDriver()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
