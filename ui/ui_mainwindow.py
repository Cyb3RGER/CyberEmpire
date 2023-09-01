# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 687)
        self.action_copy_game_files = QAction(MainWindow)
        self.action_copy_game_files.setObjectName(u"action_copy_game_files")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.grp_opt_decks = QGroupBox(self.centralwidget)
        self.grp_opt_decks.setObjectName(u"grp_opt_decks")
        self.gridLayout_6 = QGridLayout(self.grp_opt_decks)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.grp_opt_decks)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cmb_decks = QComboBox(self.grp_opt_decks)
        self.cmb_decks.setObjectName(u"cmb_decks")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmb_decks)

        self.label_5 = QLabel(self.grp_opt_decks)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.chb_no_xyz = QCheckBox(self.grp_opt_decks)
        self.chb_no_xyz.setObjectName(u"chb_no_xyz")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chb_no_xyz)

        self.label_6 = QLabel(self.grp_opt_decks)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.chb_no_pendulum = QCheckBox(self.grp_opt_decks)
        self.chb_no_pendulum.setObjectName(u"chb_no_pendulum")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.chb_no_pendulum)

        self.label_7 = QLabel(self.grp_opt_decks)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.chb_no_synchro = QCheckBox(self.grp_opt_decks)
        self.chb_no_synchro.setObjectName(u"chb_no_synchro")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.chb_no_synchro)

        self.label_16 = QLabel(self.grp_opt_decks)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.chb_include_custom = QCheckBox(self.grp_opt_decks)
        self.chb_include_custom.setObjectName(u"chb_include_custom")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chb_include_custom)

        self.chb_only_starter_decks = QCheckBox(self.grp_opt_decks)
        self.chb_only_starter_decks.setObjectName(u"chb_only_starter_decks")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.chb_only_starter_decks)

        self.label_13 = QLabel(self.grp_opt_decks)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_13)


        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_decks, 1, 0, 1, 1)

        self.grp_opt_shop = QGroupBox(self.centralwidget)
        self.grp_opt_shop.setObjectName(u"grp_opt_shop")
        self.gridLayout_5 = QGridLayout(self.grp_opt_shop)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_12 = QLabel(self.grp_opt_shop)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.label_15 = QLabel(self.grp_opt_shop)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.chb_shop_portraits = QCheckBox(self.grp_opt_shop)
        self.chb_shop_portraits.setObjectName(u"chb_shop_portraits")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.chb_shop_portraits)

        self.label_8 = QLabel(self.grp_opt_shop)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.chb_shop_prices = QCheckBox(self.grp_opt_shop)
        self.chb_shop_prices.setObjectName(u"chb_shop_prices")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.chb_shop_prices)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_9 = QLabel(self.grp_opt_shop)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.spb_min_price = QSpinBox(self.grp_opt_shop)
        self.spb_min_price.setObjectName(u"spb_min_price")
        self.spb_min_price.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spb_min_price.setMaximum(65530)
        self.spb_min_price.setSingleStep(10)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.spb_min_price)

        self.label_10 = QLabel(self.grp_opt_shop)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.spb_max_price = QSpinBox(self.grp_opt_shop)
        self.spb_max_price.setObjectName(u"spb_max_price")
        self.spb_max_price.setMaximum(65530)
        self.spb_max_price.setSingleStep(10)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.spb_max_price)


        self.formLayout_4.setLayout(3, QFormLayout.FieldRole, self.formLayout_5)

        self.cmb_shop_packs = QComboBox(self.grp_opt_shop)
        self.cmb_shop_packs.setObjectName(u"cmb_shop_packs")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.cmb_shop_packs)


        self.gridLayout_5.addLayout(self.formLayout_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_shop, 2, 0, 1, 1)

        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setFlat(False)

        self.gridLayout.addWidget(self.btn_run, 3, 0, 1, 2)

        self.grp_opt_arenas = QGroupBox(self.centralwidget)
        self.grp_opt_arenas.setObjectName(u"grp_opt_arenas")
        self.gridLayout_8 = QGridLayout(self.grp_opt_arenas)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.grp_opt_arenas)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.chb_shuffle_arenas = QCheckBox(self.grp_opt_arenas)
        self.chb_shuffle_arenas.setObjectName(u"chb_shuffle_arenas")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.chb_shuffle_arenas)


        self.gridLayout_8.addLayout(self.formLayout_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_arenas, 2, 1, 1, 1)

        self.grp_opt_duelists = QGroupBox(self.centralwidget)
        self.grp_opt_duelists.setObjectName(u"grp_opt_duelists")
        self.gridLayout_2 = QGridLayout(self.grp_opt_duelists)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_11 = QLabel(self.grp_opt_duelists)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.chb_duelist_portrais = QCheckBox(self.grp_opt_duelists)
        self.chb_duelist_portrais.setObjectName(u"chb_duelist_portrais")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.chb_duelist_portrais)

        self.label_3 = QLabel(self.grp_opt_duelists)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.chb_link_duelists_decks = QCheckBox(self.grp_opt_duelists)
        self.chb_link_duelists_decks.setObjectName(u"chb_link_duelists_decks")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.chb_link_duelists_decks)

        self.label_2 = QLabel(self.grp_opt_duelists)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.chb_random_sig_cards = QCheckBox(self.grp_opt_duelists)
        self.chb_random_sig_cards.setObjectName(u"chb_random_sig_cards")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.chb_random_sig_cards)


        self.gridLayout_2.addLayout(self.formLayout_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_duelists, 1, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.txt_seed = QLineEdit(self.widget)
        self.txt_seed.setObjectName(u"txt_seed")

        self.gridLayout_7.addWidget(self.txt_seed, 0, 1, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 22))
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetup.menuAction())
        self.menuSetup.addAction(self.action_copy_game_files)

        self.retranslateUi(MainWindow)

        self.btn_run.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_copy_game_files.setText(QCoreApplication.translate("MainWindow", u"Copy game files", None))
        self.grp_opt_decks.setTitle(QCoreApplication.translate("MainWindow", u"Decks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Randomize Decks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Exclude XYZ Cards", None))
        self.chb_no_xyz.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Exclude Pendulum Cards", None))
        self.chb_no_pendulum.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Exclude Synchro Cards", None))
        self.chb_no_synchro.setText("")
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"Load Custom decks from the 'custom_decks' folder. Decks have to be in the .ydc format.", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Include Custom Decks", None))
        self.chb_include_custom.setText("")
        self.chb_only_starter_decks.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Only randomize Starter Decks", None))
        self.grp_opt_shop.setTitle(QCoreApplication.translate("MainWindow", u"Shop", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Randomize Shop Packs", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Shuffle Shop Portraits", None))
        self.chb_shop_portraits.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Randomize Shop Prices", None))
        self.chb_shop_prices.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Minimum Price", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Maximum Price", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.grp_opt_arenas.setTitle(QCoreApplication.translate("MainWindow", u"Arenas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Shuffle Arenas:", None))
        self.chb_shuffle_arenas.setText("")
        self.grp_opt_duelists.setTitle(QCoreApplication.translate("MainWindow", u"Duelists", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Randomize Duelist Portraits", None))
        self.chb_duelist_portrais.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Randomize Portraits with Decks", None))
        self.chb_link_duelists_decks.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Randomize Signature Cards", None))
        self.chb_random_sig_cards.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.txt_seed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for random seed", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
    # retranslateUi

