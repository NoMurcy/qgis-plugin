# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj_2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BasicCalculationsDialogBase(object):
    def setupUi(self, BasicCalculationsDialogBase):
        BasicCalculationsDialogBase.setObjectName("BasicCalculationsDialogBase")
        BasicCalculationsDialogBase.resize(506, 350)
        self.button_box = QtWidgets.QDialogButtonBox(BasicCalculationsDialogBase)
        self.button_box.setGeometry(QtCore.QRect(130, 290, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mMapLayerComboBox = QgsMapLayerComboBox(BasicCalculationsDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(130, 90, 241, 41))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.teskt_wybor = QtWidgets.QLabel(BasicCalculationsDialogBase)
        self.teskt_wybor.setGeometry(QtCore.QRect(130, 50, 161, 31))
        self.teskt_wybor.setObjectName("teskt_wybor")
        self.przycisk_pole = QtWidgets.QPushButton(BasicCalculationsDialogBase)
        self.przycisk_pole.setGeometry(QtCore.QRect(280, 200, 93, 28))
        self.przycisk_pole.setObjectName("przycisk_pole")
        self.przycisk_przew = QtWidgets.QPushButton(BasicCalculationsDialogBase)
        self.przycisk_przew.setGeometry(QtCore.QRect(280, 160, 93, 28))
        self.przycisk_przew.setObjectName("przycisk_przew")
        self.tekst_przew = QtWidgets.QLabel(BasicCalculationsDialogBase)
        self.tekst_przew.setGeometry(QtCore.QRect(30, 170, 241, 16))
        self.tekst_przew.setObjectName("tekst_przew")
        self.tekst_pole = QtWidgets.QLabel(BasicCalculationsDialogBase)
        self.tekst_pole.setGeometry(QtCore.QRect(30, 210, 171, 16))
        self.tekst_pole.setObjectName("tekst_pole")
        self.label_pole = QtWidgets.QLabel(BasicCalculationsDialogBase)
        self.label_pole.setGeometry(QtCore.QRect(380, 200, 121, 21))
        self.label_pole.setText("")
        self.label_pole.setObjectName("label_pole")
        self.label_wys = QtWidgets.QLabel(BasicCalculationsDialogBase)
        self.label_wys.setGeometry(QtCore.QRect(390, 160, 111, 31))
        self.label_wys.setText("")
        self.label_wys.setObjectName("label_wys")

        self.retranslateUi(BasicCalculationsDialogBase)
        self.button_box.accepted.connect(BasicCalculationsDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(BasicCalculationsDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(BasicCalculationsDialogBase)

    def retranslateUi(self, BasicCalculationsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        BasicCalculationsDialogBase.setWindowTitle(_translate("BasicCalculationsDialogBase", "Basic Calculations"))
        self.teskt_wybor.setText(_translate("BasicCalculationsDialogBase", "Choose layer:"))
        self.przycisk_pole.setText(_translate("BasicCalculationsDialogBase", "LICZ"))
        self.przycisk_przew.setText(_translate("BasicCalculationsDialogBase", "LICZ"))
        self.tekst_przew.setText(_translate("BasicCalculationsDialogBase", "KLIKNIJ ABY POLICZYĆ PRZEWYŻSZENIE"))
        self.tekst_pole.setText(_translate("BasicCalculationsDialogBase", "KLIKNIJ ABY POLICZYĆ POLE"))
from qgsmaplayercombobox import QgsMapLayerComboBox
