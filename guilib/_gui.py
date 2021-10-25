# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(2560, 1600)
        self.image_x = QLabel(Form)
        self.image_x.setObjectName(u"image_x")
        self.image_x.setGeometry(QRect(0, 0, 800, 500))
        self.image_x.setFrameShape(QFrame.Box)
        self.image_x.setFrameShadow(QFrame.Plain)
        self.image_x.setLineWidth(2)
        self.startBtn = QPushButton(Form)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(1700, 0, 100, 50))
        self.stopBtn = QPushButton(Form)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(1700, 160, 100, 50))
        self.Exit = QPushButton(Form)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(1700, 210, 100, 50))
        self.image_y = QLabel(Form)
        self.image_y.setObjectName(u"image_y")
        self.image_y.setGeometry(QRect(800, 0, 800, 500))
        self.image_y.setFrameShape(QFrame.Box)
        self.image_y.setFrameShadow(QFrame.Plain)
        self.image_y.setLineWidth(2)
        self.image_z = QLabel(Form)
        self.image_z.setObjectName(u"image_z")
        self.image_z.setGeometry(QRect(0, 500, 800, 500))
        self.image_z.setFrameShape(QFrame.Box)
        self.image_z.setFrameShadow(QFrame.Plain)
        self.image_z.setLineWidth(2)
        self.image_label_4 = QLabel(Form)
        self.image_label_4.setObjectName(u"image_label_4")
        self.image_label_4.setGeometry(QRect(800, 500, 800, 500))
        self.image_label_4.setFrameShape(QFrame.Box)
        self.image_label_4.setFrameShadow(QFrame.Plain)
        self.image_label_4.setLineWidth(2)
        self.position = QCheckBox(Form)
        self.position.setObjectName(u"position")
        self.position.setGeometry(QRect(1700, 60, 121, 23))
        self.depth = QCheckBox(Form)
        self.depth.setObjectName(u"depth")
        self.depth.setGeometry(QRect(1700, 90, 121, 23))
        self.qualification = QCheckBox(Form)
        self.qualification.setObjectName(u"qualification")
        self.qualification.setGeometry(QRect(1700, 120, 141, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image_x.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.startBtn.setText(QCoreApplication.translate("Form", u"\u958b\u59cb\u9304\u5f71", None))
        self.stopBtn.setText(QCoreApplication.translate("Form", u" \u7d50\u675f\u9304\u5f71", None))
        self.Exit.setText(QCoreApplication.translate("Form", u"\u7d50\u675f\u7a0b\u5f0f", None))
        self.image_y.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.image_z.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.image_label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.position.setText(QCoreApplication.translate("Form", u"\u624b\u8ef8\u59ff\u52e2\u7570\u5e38", None))
        self.depth.setText(QCoreApplication.translate("Form", u"\u6309\u58d3\u6df1\u5ea6\u4e0d\u8db3", None))
        self.qualification.setText(QCoreApplication.translate("Form", u"\u6574\u9ad4\u8a55\u5206\u4e0d\u53ca\u683c", None))
    # retranslateUi

