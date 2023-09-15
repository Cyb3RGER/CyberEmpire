# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
        MainWindow.resize(1000, 627)
        self.action_copy_game_files = QAction(MainWindow)
        self.action_copy_game_files.setObjectName(u"action_copy_game_files")
        self.action_validate_custom = QAction(MainWindow)
        self.action_validate_custom.setObjectName(u"action_validate_custom")
        self.action_converter = QAction(MainWindow)
        self.action_converter.setObjectName(u"action_converter")
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
        self.grp_opt_duelists = QGroupBox(self.centralwidget)
        self.grp_opt_duelists.setObjectName(u"grp_opt_duelists")
        self.gridLayout_2 = QGridLayout(self.grp_opt_duelists)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lbl_random_duelist_portraits = QLabel(self.grp_opt_duelists)
        self.lbl_random_duelist_portraits.setObjectName(u"lbl_random_duelist_portraits")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lbl_random_duelist_portraits)

        self.lbl_link_duelists_decks = QLabel(self.grp_opt_duelists)
        self.lbl_link_duelists_decks.setObjectName(u"lbl_link_duelists_decks")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lbl_link_duelists_decks)

        self.chb_link_duelists_decks = QCheckBox(self.grp_opt_duelists)
        self.chb_link_duelists_decks.setObjectName(u"chb_link_duelists_decks")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.chb_link_duelists_decks)

        self.lbl_random_sig_cards = QLabel(self.grp_opt_duelists)
        self.lbl_random_sig_cards.setObjectName(u"lbl_random_sig_cards")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.lbl_random_sig_cards)

        self.chb_random_sig_cards = QCheckBox(self.grp_opt_duelists)
        self.chb_random_sig_cards.setObjectName(u"chb_random_sig_cards")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.chb_random_sig_cards)

        self.cmb_random_duelist_portraits = QComboBox(self.grp_opt_duelists)
        self.cmb_random_duelist_portraits.setObjectName(u"cmb_random_duelist_portraits")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.cmb_random_duelist_portraits)


        self.gridLayout_2.addLayout(self.formLayout_6, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_duelists, 2, 1, 1, 1)

        self.grp_opt_decks = QGroupBox(self.centralwidget)
        self.grp_opt_decks.setObjectName(u"grp_opt_decks")
        self.gridLayout_6 = QGridLayout(self.grp_opt_decks)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_decks = QLabel(self.grp_opt_decks)
        self.lbl_decks.setObjectName(u"lbl_decks")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_decks)

        self.cmb_decks = QComboBox(self.grp_opt_decks)
        self.cmb_decks.setObjectName(u"cmb_decks")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmb_decks)

        self.grp_opt_no = QGroupBox(self.grp_opt_decks)
        self.grp_opt_no.setObjectName(u"grp_opt_no")
        self.gridLayout_9 = QGridLayout(self.grp_opt_no)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbl_no_link = QLabel(self.grp_opt_no)
        self.lbl_no_link.setObjectName(u"lbl_no_link")

        self.gridLayout_7.addWidget(self.lbl_no_link, 3, 0, 1, 1)

        self.chb_no_gemini = QCheckBox(self.grp_opt_no)
        self.chb_no_gemini.setObjectName(u"chb_no_gemini")

        self.gridLayout_7.addWidget(self.chb_no_gemini, 1, 3, 1, 1)

        self.label_3 = QLabel(self.grp_opt_no)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.grp_opt_no)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 2, 2, 1, 1)

        self.lbl_no_xyz = QLabel(self.grp_opt_no)
        self.lbl_no_xyz.setObjectName(u"lbl_no_xyz")

        self.gridLayout_7.addWidget(self.lbl_no_xyz, 0, 0, 1, 1)

        self.chb_no_pendulum = QCheckBox(self.grp_opt_no)
        self.chb_no_pendulum.setObjectName(u"chb_no_pendulum")

        self.gridLayout_7.addWidget(self.chb_no_pendulum, 1, 1, 1, 1)

        self.label_2 = QLabel(self.grp_opt_no)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_5 = QLabel(self.grp_opt_no)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 3, 2, 1, 1)

        self.chb_no_xyz = QCheckBox(self.grp_opt_no)
        self.chb_no_xyz.setObjectName(u"chb_no_xyz")

        self.gridLayout_7.addWidget(self.chb_no_xyz, 0, 1, 1, 1)

        self.lbl_no_pendulum = QLabel(self.grp_opt_no)
        self.lbl_no_pendulum.setObjectName(u"lbl_no_pendulum")

        self.gridLayout_7.addWidget(self.lbl_no_pendulum, 1, 0, 1, 1)

        self.chb_no_tuner = QCheckBox(self.grp_opt_no)
        self.chb_no_tuner.setObjectName(u"chb_no_tuner")

        self.gridLayout_7.addWidget(self.chb_no_tuner, 2, 3, 1, 1)

        self.chb_no_link = QCheckBox(self.grp_opt_no)
        self.chb_no_link.setObjectName(u"chb_no_link")

        self.gridLayout_7.addWidget(self.chb_no_link, 3, 1, 1, 1)

        self.chb_no_spirit = QCheckBox(self.grp_opt_no)
        self.chb_no_spirit.setObjectName(u"chb_no_spirit")

        self.gridLayout_7.addWidget(self.chb_no_spirit, 3, 3, 1, 1)

        self.lbl_no_synchro = QLabel(self.grp_opt_no)
        self.lbl_no_synchro.setObjectName(u"lbl_no_synchro")

        self.gridLayout_7.addWidget(self.lbl_no_synchro, 2, 0, 1, 1)

        self.chb_no_synchro = QCheckBox(self.grp_opt_no)
        self.chb_no_synchro.setObjectName(u"chb_no_synchro")

        self.gridLayout_7.addWidget(self.chb_no_synchro, 2, 1, 1, 1)

        self.chb_no_union = QCheckBox(self.grp_opt_no)
        self.chb_no_union.setObjectName(u"chb_no_union")

        self.gridLayout_7.addWidget(self.chb_no_union, 0, 3, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.grp_opt_no)

        self.lbl_only_starter_decks = QLabel(self.grp_opt_decks)
        self.lbl_only_starter_decks.setObjectName(u"lbl_only_starter_decks")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_only_starter_decks)

        self.chb_only_starter_decks = QCheckBox(self.grp_opt_decks)
        self.chb_only_starter_decks.setObjectName(u"chb_only_starter_decks")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.chb_only_starter_decks)

        self.lbl_include_custom = QLabel(self.grp_opt_decks)
        self.lbl_include_custom.setObjectName(u"lbl_include_custom")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_include_custom)

        self.chb_include_custom = QCheckBox(self.grp_opt_decks)
        self.chb_include_custom.setObjectName(u"chb_include_custom")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.chb_include_custom)

        self.label_26 = QLabel(self.grp_opt_decks)
        self.label_26.setObjectName(u"label_26")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_26)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.lbl_custom_random = QLabel(self.grp_opt_decks)
        self.lbl_custom_random.setObjectName(u"lbl_custom_random")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.lbl_custom_random)

        self.chb_custom_random = QCheckBox(self.grp_opt_decks)
        self.chb_custom_random.setObjectName(u"chb_custom_random")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.chb_custom_random)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.formLayout_11)

        self.grp_balance_opts = QGroupBox(self.grp_opt_decks)
        self.grp_balance_opts.setObjectName(u"grp_balance_opts")
        self.formLayout_2 = QFormLayout(self.grp_balance_opts)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.lbl_mon_percent = QLabel(self.grp_balance_opts)
        self.lbl_mon_percent.setObjectName(u"lbl_mon_percent")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.lbl_mon_percent)

        self.spb_mon_percent = QSpinBox(self.grp_balance_opts)
        self.spb_mon_percent.setObjectName(u"spb_mon_percent")
        self.spb_mon_percent.setKeyboardTracking(False)
        self.spb_mon_percent.setMinimum(0)
        self.spb_mon_percent.setMaximum(100)
        self.spb_mon_percent.setSingleStep(1)
        self.spb_mon_percent.setValue(0)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.spb_mon_percent)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.lbl_low_level_percent = QLabel(self.grp_balance_opts)
        self.lbl_low_level_percent.setObjectName(u"lbl_low_level_percent")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.lbl_low_level_percent)

        self.lbl_high_level_percent = QLabel(self.grp_balance_opts)
        self.lbl_high_level_percent.setObjectName(u"lbl_high_level_percent")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.lbl_high_level_percent)

        self.spb_low_level_percent = QSpinBox(self.grp_balance_opts)
        self.spb_low_level_percent.setObjectName(u"spb_low_level_percent")
        self.spb_low_level_percent.setKeyboardTracking(False)
        self.spb_low_level_percent.setMaximum(100)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.spb_low_level_percent)

        self.spb_high_level_percent = QSpinBox(self.grp_balance_opts)
        self.spb_high_level_percent.setObjectName(u"spb_high_level_percent")
        self.spb_high_level_percent.setKeyboardTracking(False)
        self.spb_high_level_percent.setMaximum(100)
        self.spb_high_level_percent.setSingleStep(1)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.spb_high_level_percent)


        self.formLayout_7.setLayout(1, QFormLayout.FieldRole, self.formLayout_8)

        self.lbl_spell_trap_percent = QLabel(self.grp_balance_opts)
        self.lbl_spell_trap_percent.setObjectName(u"lbl_spell_trap_percent")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.lbl_spell_trap_percent)

        self.spb_spell_trap_percent = QSpinBox(self.grp_balance_opts)
        self.spb_spell_trap_percent.setObjectName(u"spb_spell_trap_percent")
        self.spb_spell_trap_percent.setKeyboardTracking(False)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.spb_spell_trap_percent)

        self.label_21 = QLabel(self.grp_balance_opts)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.grp_balance_opts)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.lbl_spell_percent = QLabel(self.grp_balance_opts)
        self.lbl_spell_percent.setObjectName(u"lbl_spell_percent")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.lbl_spell_percent)

        self.lbl_trap_percent = QLabel(self.grp_balance_opts)
        self.lbl_trap_percent.setObjectName(u"lbl_trap_percent")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.lbl_trap_percent)

        self.spb_spell_percent = QSpinBox(self.grp_balance_opts)
        self.spb_spell_percent.setObjectName(u"spb_spell_percent")
        self.spb_spell_percent.setKeyboardTracking(False)
        self.spb_spell_percent.setMaximum(100)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.spb_spell_percent)

        self.spb_trap_percent = QSpinBox(self.grp_balance_opts)
        self.spb_trap_percent.setObjectName(u"spb_trap_percent")
        self.spb_trap_percent.setKeyboardTracking(False)
        self.spb_trap_percent.setMaximum(100)

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.spb_trap_percent)


        self.formLayout_7.setLayout(3, QFormLayout.FieldRole, self.formLayout_9)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.formLayout_7)


        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.grp_balance_opts)


        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_decks, 2, 0, 3, 1)

        self.grp_opt_shop = QGroupBox(self.centralwidget)
        self.grp_opt_shop.setObjectName(u"grp_opt_shop")
        self.gridLayout_5 = QGridLayout(self.grp_opt_shop)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lbl_shop_packs = QLabel(self.grp_opt_shop)
        self.lbl_shop_packs.setObjectName(u"lbl_shop_packs")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_shop_packs)

        self.lbl_shop_portraits = QLabel(self.grp_opt_shop)
        self.lbl_shop_portraits.setObjectName(u"lbl_shop_portraits")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lbl_shop_portraits)

        self.chb_shop_portraits = QCheckBox(self.grp_opt_shop)
        self.chb_shop_portraits.setObjectName(u"chb_shop_portraits")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.chb_shop_portraits)

        self.lbl_shop_prices = QLabel(self.grp_opt_shop)
        self.lbl_shop_prices.setObjectName(u"lbl_shop_prices")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.lbl_shop_prices)

        self.chb_shop_prices = QCheckBox(self.grp_opt_shop)
        self.chb_shop_prices.setObjectName(u"chb_shop_prices")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.chb_shop_prices)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lbl_min_price = QLabel(self.grp_opt_shop)
        self.lbl_min_price.setObjectName(u"lbl_min_price")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.lbl_min_price)

        self.spb_min_price = QSpinBox(self.grp_opt_shop)
        self.spb_min_price.setObjectName(u"spb_min_price")
        self.spb_min_price.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spb_min_price.setKeyboardTracking(False)
        self.spb_min_price.setMaximum(65530)
        self.spb_min_price.setSingleStep(10)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.spb_min_price)

        self.lbl_max_price = QLabel(self.grp_opt_shop)
        self.lbl_max_price.setObjectName(u"lbl_max_price")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.lbl_max_price)

        self.spb_max_price = QSpinBox(self.grp_opt_shop)
        self.spb_max_price.setObjectName(u"spb_max_price")
        self.spb_max_price.setKeyboardTracking(False)
        self.spb_max_price.setMaximum(65530)
        self.spb_max_price.setSingleStep(10)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.spb_max_price)


        self.formLayout_4.setLayout(3, QFormLayout.FieldRole, self.formLayout_5)

        self.cmb_shop_packs = QComboBox(self.grp_opt_shop)
        self.cmb_shop_packs.setObjectName(u"cmb_shop_packs")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.cmb_shop_packs)

        self.label_25 = QLabel(self.grp_opt_shop)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_25)


        self.gridLayout_5.addLayout(self.formLayout_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_shop, 3, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.lbl_seed = QLabel(self.widget)
        self.lbl_seed.setObjectName(u"lbl_seed")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.lbl_seed)

        self.txt_seed = QLineEdit(self.widget)
        self.txt_seed.setObjectName(u"txt_seed")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.txt_seed)


        self.gridLayout_4.addLayout(self.formLayout_10, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setItalic(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setFlat(False)

        self.gridLayout.addWidget(self.btn_run, 5, 0, 1, 2)

        self.grp_opt_arenas = QGroupBox(self.centralwidget)
        self.grp_opt_arenas.setObjectName(u"grp_opt_arenas")
        self.gridLayout_8 = QGridLayout(self.grp_opt_arenas)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_shuffle_arenas = QLabel(self.grp_opt_arenas)
        self.lbl_shuffle_arenas.setObjectName(u"lbl_shuffle_arenas")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_shuffle_arenas)

        self.chb_shuffle_arenas = QCheckBox(self.grp_opt_arenas)
        self.chb_shuffle_arenas.setObjectName(u"chb_shuffle_arenas")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.chb_shuffle_arenas)

        self.lbl_random_battle_packs = QLabel(self.grp_opt_arenas)
        self.lbl_random_battle_packs.setObjectName(u"lbl_random_battle_packs")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_random_battle_packs)

        self.cmb_random_battle_packs = QComboBox(self.grp_opt_arenas)
        self.cmb_random_battle_packs.setObjectName(u"cmb_random_battle_packs")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.cmb_random_battle_packs)


        self.gridLayout_8.addLayout(self.formLayout_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grp_opt_arenas, 4, 1, 1, 1)

        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuSetup.addAction(self.action_copy_game_files)
        self.menuTools.addAction(self.action_validate_custom)
        self.menuTools.addAction(self.action_converter)

        self.retranslateUi(MainWindow)

        self.btn_run.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_copy_game_files.setText(QCoreApplication.translate("MainWindow", u"Copy game files", None))
        self.action_validate_custom.setText(QCoreApplication.translate("MainWindow", u"Edit custom deck", None))
        self.action_converter.setText(QCoreApplication.translate("MainWindow", u"Card ID Converter", None))
        self.grp_opt_duelists.setTitle(QCoreApplication.translate("MainWindow", u"Duelists", None))
        self.lbl_random_duelist_portraits.setText(QCoreApplication.translate("MainWindow", u"Randomize Duelist Portraits", None))
        self.lbl_link_duelists_decks.setText(QCoreApplication.translate("MainWindow", u"Randomize Portraits with Decks", None))
        self.chb_link_duelists_decks.setText("")
        self.lbl_random_sig_cards.setText(QCoreApplication.translate("MainWindow", u"Randomize Signature Cards", None))
        self.chb_random_sig_cards.setText("")
        self.grp_opt_decks.setTitle(QCoreApplication.translate("MainWindow", u"Decks", None))
        self.lbl_decks.setText(QCoreApplication.translate("MainWindow", u"Randomize Decks", None))
        self.grp_opt_no.setTitle(QCoreApplication.translate("MainWindow", u"Exclude ", None))
        self.lbl_no_link.setText(QCoreApplication.translate("MainWindow", u"Link Cards", None))
        self.chb_no_gemini.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gemini Cards", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tuner Cards", None))
        self.lbl_no_xyz.setText(QCoreApplication.translate("MainWindow", u"XYZ Cards", None))
        self.chb_no_pendulum.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Union Cards", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Spirit Cards", None))
        self.chb_no_xyz.setText("")
        self.lbl_no_pendulum.setText(QCoreApplication.translate("MainWindow", u"Pendulum Cards", None))
        self.chb_no_tuner.setText("")
        self.chb_no_link.setText("")
        self.chb_no_spirit.setText("")
        self.lbl_no_synchro.setText(QCoreApplication.translate("MainWindow", u"Synchro Cards", None))
        self.chb_no_synchro.setText("")
        self.chb_no_union.setText("")
        self.lbl_only_starter_decks.setText(QCoreApplication.translate("MainWindow", u"Only Starter Decks", None))
        self.chb_only_starter_decks.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_include_custom.setToolTip(QCoreApplication.translate("MainWindow", u"Load Custom decks from the 'custom_decks' folder. Decks have to be in the .ydc format.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_include_custom.setText(QCoreApplication.translate("MainWindow", u"Include Custom Decks", None))
        self.chb_include_custom.setText("")
        self.label_26.setText("")
        self.lbl_custom_random.setText(QCoreApplication.translate("MainWindow", u"Use random amount", None))
        self.chb_custom_random.setText("")
        self.grp_balance_opts.setTitle(QCoreApplication.translate("MainWindow", u"Balancing", None))
        self.lbl_mon_percent.setText(QCoreApplication.translate("MainWindow", u"Monster Precent", None))
        self.spb_mon_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.lbl_low_level_percent.setText(QCoreApplication.translate("MainWindow", u"1-4 stars", None))
        self.lbl_high_level_percent.setText(QCoreApplication.translate("MainWindow", u"5+ stars", None))
        self.spb_low_level_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.spb_high_level_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.lbl_spell_trap_percent.setText(QCoreApplication.translate("MainWindow", u"Spell/Trap Percent", None))
        self.spb_spell_trap_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_21.setText("")
        self.label_22.setText("")
        self.lbl_spell_percent.setText(QCoreApplication.translate("MainWindow", u"Spell Percent", None))
        self.lbl_trap_percent.setText(QCoreApplication.translate("MainWindow", u"Trap Percent", None))
        self.spb_spell_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.spb_trap_percent.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.grp_opt_shop.setTitle(QCoreApplication.translate("MainWindow", u"Shop", None))
        self.lbl_shop_packs.setText(QCoreApplication.translate("MainWindow", u"Randomize Shop Packs", None))
        self.lbl_shop_portraits.setText(QCoreApplication.translate("MainWindow", u"Shuffle Shop Portraits", None))
        self.chb_shop_portraits.setText("")
        self.lbl_shop_prices.setText(QCoreApplication.translate("MainWindow", u"Randomize Shop Prices", None))
        self.chb_shop_prices.setText("")
        self.lbl_min_price.setText(QCoreApplication.translate("MainWindow", u"Minimum Price", None))
        self.lbl_max_price.setText(QCoreApplication.translate("MainWindow", u"Maximum Price", None))
        self.label_25.setText("")
        self.lbl_seed.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
#if QT_CONFIG(tooltip)
        self.txt_seed.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.txt_seed.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.txt_seed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank for random seed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hover over an option for more info", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.grp_opt_arenas.setTitle(QCoreApplication.translate("MainWindow", u"Other", None))
        self.lbl_shuffle_arenas.setText(QCoreApplication.translate("MainWindow", u"Shuffle Arenas", None))
        self.chb_shuffle_arenas.setText("")
        self.lbl_random_battle_packs.setText(QCoreApplication.translate("MainWindow", u"Randomize Battle Packs", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

