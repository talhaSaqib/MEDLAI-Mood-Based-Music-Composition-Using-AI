# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medlai2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.generateMelodyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.generateMelodyBtn.setObjectName("generateMelodyBtn")
        self.gridLayout.addWidget(self.generateMelodyBtn, 10, 1, 1, 1)
        # self.uploadImageBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.uploadImageBtn.sizePolicy().hasHeightForWidth())
        # self.uploadImageBtn.setSizePolicy(sizePolicy)
        # self.uploadImageBtn.setObjectName("uploadImageBtn")
        # self.gridLayout.addWidget(self.uploadImageBtn, 0, 1, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.moodLabel = QtWidgets.QLabel(self.verticalWidget)
        self.moodLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moodLabel.sizePolicy().hasHeightForWidth())
        self.moodLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.moodLabel.setFont(font)
        self.moodLabel.setObjectName("moodLabel")
        self.verticalLayout.addWidget(self.moodLabel)
        self.gridLayout.addWidget(self.verticalWidget, 1, 0, 1, 1)
        self.uploadSeedBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadSeedBtn.setObjectName("uploadSeedBtn")
        self.gridLayout.addWidget(self.uploadSeedBtn, 6, 1, 1, 1)
        self.orLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.orLabel.setFont(font)
        self.orLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.orLabel.setObjectName("orLabel")
        self.gridLayout.addWidget(self.orLabel, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.verticalLayout_2, 10, 3, 1, 1)
        self.s3label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.s3label.setFont(font)
        self.s3label.setObjectName("s3label")
        self.gridLayout.addWidget(self.s3label, 10, 0, 1, 1)
        self.moodCombo = QtWidgets.QComboBox(self.centralwidget)
        self.moodCombo.setObjectName("moodCombo")
        self.moodCombo.addItem("")
        self.moodCombo.addItem("")
        self.moodCombo.addItem("")
        self.moodCombo.addItem("")
        self.moodCombo.addItem("")
        self.moodCombo.addItem("")
        self.gridLayout.addWidget(self.moodCombo, 0, 3, 1, 1)
        self.s2label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.s2label.setFont(font)
        self.s2label.setObjectName("s2label")
        self.gridLayout.addWidget(self.s2label, 6, 0, 1, 1)
        self.s1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.s1Label.setFont(font)
        self.s1Label.setObjectName("s1Label")
        self.gridLayout.addWidget(self.s1Label, 0, 0, 1, 1)
        self.confirmlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.confirmlabel.setFont(font)
        self.confirmlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmlabel.setObjectName("confirmlabel")
        self.gridLayout.addWidget(self.confirmlabel, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFAQs = QtWidgets.QAction(MainWindow)
        self.actionFAQs.setObjectName("actionFAQs")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionFAQs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generate Melody"))
        self.generateMelodyBtn.setText(_translate("MainWindow", "Generate Melody"))
        # self.uploadImageBtn.setText(_translate("MainWindow", "Upload Image/Video"))
        self.moodLabel.setText(_translate("MainWindow", "Hide this"))
        self.uploadSeedBtn.setText(_translate("MainWindow", "Upload Seed Music"))
        self.orLabel.setText(_translate("MainWindow", "OR "))
        self.s3label.setText(_translate("MainWindow", "Step 3"))
        self.moodCombo.setItemText(0, _translate("MainWindow", "Select Your Mood"))
        self.moodCombo.setItemText(1, _translate("MainWindow", "Happy"))
        self.moodCombo.setItemText(2, _translate("MainWindow", "Sad"))
        self.moodCombo.setItemText(3, _translate("MainWindow", "Energetic"))
        self.moodCombo.setItemText(4, _translate("MainWindow", "Depressed"))
        self.moodCombo.setItemText(5, _translate("MainWindow", "Calm"))
        self.s2label.setText(_translate("MainWindow", "Step 2"))
        self.s1Label.setText(_translate("MainWindow", "Step 1"))
        self.confirmlabel.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFAQs.setText(_translate("MainWindow", "FAQs"))
        # self.uploadImageBtn.hide()
        self.orLabel.hide()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())