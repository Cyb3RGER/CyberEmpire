# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_deck_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QPlainTextEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1171, 659)
        Dialog.setStyleSheet(u"QTextEdit {\n"
"	background: rgb(30,31,34)\n"
"}")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.btn_file = QPushButton(Dialog)
        self.btn_file.setObjectName(u"btn_file")

        self.gridLayout.addWidget(self.btn_file, 0, 0, 1, 1)

        self.txt_result = QTextEdit(Dialog)
        self.txt_result.setObjectName(u"txt_result")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.txt_result.setFont(font)
        self.txt_result.setAutoFillBackground(False)
        self.txt_result.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result, 0, 1, 2, 1)

        self.txt_example = QPlainTextEdit(Dialog)
        self.txt_example.setObjectName(u"txt_example")

        self.gridLayout.addWidget(self.txt_example, 1, 2, 1, 1)

        self.btn_generate = QPushButton(Dialog)
        self.btn_generate.setObjectName(u"btn_generate")

        self.gridLayout.addWidget(self.btn_generate, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_file.setText(QCoreApplication.translate("Dialog", u"Open custom deck file...", None))
        self.btn_generate.setText(QCoreApplication.translate("Dialog", u"Generate Example Deck", None))
    # retranslateUi

