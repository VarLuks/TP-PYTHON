# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_organigrama.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormOrganigrama(object):
    def setupUi(self, FormOrganigrama):
        FormOrganigrama.setObjectName("FormOrganigrama")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormOrganigrama)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.titulo_label = QtWidgets.QLabel(FormOrganigrama)
        self.titulo_label.setObjectName("titulo_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titulo_label)
        self.titulo_lineEdit = QtWidgets.QLineEdit(FormOrganigrama)
        self.titulo_lineEdit.setObjectName("titulo_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titulo_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.enviar_button = QtWidgets.QPushButton(FormOrganigrama)
        self.enviar_button.setObjectName("enviar_button")
        self.verticalLayout.addWidget(self.enviar_button)

        self.retranslateUi(FormOrganigrama)
        QtCore.QMetaObject.connectSlotsByName(FormOrganigrama)

    def retranslateUi(self, FormOrganigrama):
        _translate = QtCore.QCoreApplication.translate
        FormOrganigrama.setWindowTitle(_translate("FormOrganigrama", "Formulario Organigrama"))
        self.titulo_label.setText(_translate("FormOrganigrama", "Título:"))
        self.enviar_button.setText(_translate("FormOrganigrama", "Enviar"))