import asyncio
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QProgressDialog, QMessageBox

from randomizer import Randomizer
from settings import RandomDeckSettings, RandomShopPackSettings
from ui.ui_mainwindow import Ui_MainWindow
from utils import prog_name


class MainWindow(QMainWindow):
    def __init__(self, args):
        super().__init__()
        self.rando = Randomizer()
        self.rando.setup_from_args(args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(prog_name)

        # setup widgets
        for v in RandomDeckSettings:
            self.ui.cmb_decks.addItem(v.name.replace('_', ' '))
        for v in RandomShopPackSettings:
            self.ui.cmb_shop_packs.addItem(v.name.replace('_', ' '))

        self.apply_settings()

        # connect slots
        self.ui.action_copy_game_files.triggered.connect(self.game_path_browse)
        self.ui.txt_seed.textChanged.connect(self.update_seed)
        self.ui.cmb_decks.currentIndexChanged.connect(self.update_setting)
        self.ui.cmb_decks.currentIndexChanged.connect(self.enable_balancing_options)
        self.ui.chb_no_xyz.stateChanged.connect(self.update_setting)
        self.ui.chb_no_pendulum.stateChanged.connect(self.update_setting)
        self.ui.chb_no_synchro.stateChanged.connect(self.update_setting)
        self.ui.chb_include_custom.stateChanged.connect(self.update_setting)
        self.ui.chb_only_starter_decks.stateChanged.connect(self.update_setting)
        self.ui.spb_mon_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.spb_low_level_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.spb_high_level_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.spb_spell_trap_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.spb_spell_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.spb_trap_percent.valueChanged.connect(self.validate_balance_percentage)
        self.ui.chb_duelist_portrais.stateChanged.connect(self.update_setting)
        self.ui.chb_link_duelists_decks.stateChanged.connect(self.update_setting)
        self.ui.chb_random_sig_cards.stateChanged.connect(self.update_setting)
        self.ui.cmb_shop_packs.currentIndexChanged.connect(self.update_setting)
        self.ui.chb_shop_portraits.stateChanged.connect(self.update_setting)
        self.ui.chb_shop_prices.stateChanged.connect(self.update_setting)
        self.ui.spb_min_price.valueChanged.connect(self.validate_shop_price)
        self.ui.spb_max_price.valueChanged.connect(self.validate_shop_price)
        self.ui.chb_shuffle_arenas.stateChanged.connect(self.update_setting)
        self.ui.btn_run.clicked.connect(self.run_rando)

        # self.apply_settings()

        self.enable_options(self.rando.has_game_files())

    def apply_settings(self):
        if self.rando.seed is None:
            self.ui.txt_seed.setText("")
        else:
            self.ui.txt_seed.setText(str(self.rando.seed))
        self.ui.cmb_decks.setCurrentIndex(self.rando.settings.random_decks)
        self.ui.chb_no_xyz.setChecked(self.rando.settings.exclude_xyz_cards)
        self.ui.chb_no_pendulum.setChecked(self.rando.settings.exclude_pendulum_cards)
        self.ui.chb_no_synchro.setChecked(self.rando.settings.exclude_synchro_cards)
        self.ui.chb_include_custom.setChecked(self.rando.settings.include_custom_decks)
        self.ui.chb_only_starter_decks.setChecked(self.rando.settings.only_starter_decks)
        self.ui.spb_mon_percent.setValue(self.rando.settings.mon_percent)
        self.ui.spb_low_level_percent.setValue(self.rando.settings.low_level_percent)
        self.ui.spb_high_level_percent.setValue(self.rando.settings.high_level_percent)
        self.ui.spb_spell_trap_percent.setValue(self.rando.settings.spell_trap_percent)
        self.ui.spb_spell_percent.setValue(self.rando.settings.spell_percent)
        self.ui.spb_trap_percent.setValue(self.rando.settings.trap_percent)
        self.ui.chb_duelist_portrais.setChecked(self.rando.settings.random_duelist_portraits)
        self.ui.chb_link_duelists_decks.setChecked(self.rando.settings.link_duelists_decks)
        self.ui.chb_random_sig_cards.setChecked(self.rando.settings.random_sig_cards)
        self.ui.cmb_shop_packs.setCurrentIndex(self.rando.settings.random_shop_packs)
        self.ui.chb_shop_portraits.setChecked(self.rando.settings.shuffle_shop_portraits)
        self.ui.chb_shop_prices.setChecked(self.rando.settings.random_shop_prices)
        self.ui.spb_min_price.setValue(self.rando.settings.shop_min_price)
        self.ui.spb_max_price.setValue(self.rando.settings.shop_max_price)
        self.ui.chb_shuffle_arenas.setChecked(self.rando.settings.shuffle_arenas)

    def enable_options(self, val: bool):
        self.ui.txt_seed.setEnabled(val)
        self.ui.btn_run.setEnabled(val)
        self.ui.grp_opt_decks.setEnabled(val)
        self.ui.grp_opt_arenas.setEnabled(val)
        self.ui.grp_opt_shop.setEnabled(val)
        self.ui.grp_opt_duelists.setEnabled(val)

    def enable_balancing_options(self, value):
        self.ui.grp_balance_opts.setEnabled(
            value in [RandomDeckSettings.Balanced, RandomDeckSettings.Full_Random, RandomDeckSettings.By_Type,
                      RandomDeckSettings.Archtype])

    def update_seed(self, value):
        if value == "":
            self.rando.seed = None
        else:
            self.rando.seed = value

    def update_setting(self, value):
        setting_attr_mapping = {
            "cmb_decks": "random_decks",
            "chb_no_xyz": "exclude_xyz",
            "chb_no_pendulum": "exclude_pendulum",
            "chb_no_synchro": "exclude_synchro",
            "chb_include_custom": "include_custom",
            "chb_only_starter_decks": "only_starter_decks",
            "spb_mon_percent": "mon_percent",
            "spb_low_level_percent": "low_level_percent",
            "spb_high_level_percent": "high_level_percent",
            "spb_spell_trap_percent": "spell_trap_percent",
            "spb_spell_percent": "spell_percent",
            "spb_trap_percent": "trap_percent",
            "chb_duelist_portrais": "random_duelist_portraits",
            "chb_link_duelists_decks": "link_duelists_decks",
            "chb_random_sig_cards": "random_sig_cards",
            "cmb_shop_packs": "random_shop_packs",
            "chb_shop_portraits": "shuffle_shop_portraits",
            "chb_shop_prices": "random_shop_prices",
            "spb_min_price": "shop_min_price",
            "spb_max_price": "shop_max_price",
            "chb_shuffle_arenas": "shuffle_arenas",
        }
        sender_name = self.sender().objectName()
        if sender_name in setting_attr_mapping:
            attr_name = setting_attr_mapping[sender_name]
            type_mapping = {
                "cmb": int,
                "chb": bool,
                "spb": int,
                "dsb": float,
                "txt": str,
            }
            name_split = sender_name.split('_')
            if len(name_split) >= 1 and name_split[0] in type_mapping:
                attr_value = type_mapping[name_split[0]](value)
                self.rando.settings.__setattr__(attr_name, attr_value)
                print(attr_name, value, attr_value)

    def game_path_browse(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Select game folder...")
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.Detail)
        if dialog.exec():
            self.rando.copy_game_files(dialog.selectedFiles()[0])
            self.enable_options(self.rando.has_game_files())

    def run_rando(self):
        progress = QProgressDialog()
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.forceShow()

        err = False
        gen = self.rando.run()
        for i in gen:
            if i[0] == -1:
                err = True
                err_box = QMessageBox()
                err_box.setText(f"An error occurred:\n{i[1]}\n{i[2]}")
                err_box.exec()
                gen.close()
                break
            value = i[0] / i[2] * 100
            text = i[1]
            if len(i) > 3:
                value += i[3] / i[5] / i[2] * 100
                text = i[4]
            progress.setLabelText(text)
            progress.setValue(value)
        progress.close()
        self.apply_settings()
        if not err:
            msg_box = QMessageBox()
            msg_box.setText(f"Done! You can find the result in {self.rando.get_out_path()}")
            msg_box.exec()

    def validate_shop_price(self):
        sender = self.sender()
        sender.setValue(round(sender.value() / sender.singleStep()) * sender.singleStep())
        if sender == self.ui.spb_min_price and self.ui.spb_min_price.value() > self.ui.spb_max_price.value():
            self.ui.spb_min_price.setValue(self.ui.spb_max_price.value())
        if sender == self.ui.spb_max_price and self.ui.spb_max_price.value() < self.ui.spb_min_price.value():
            self.ui.spb_max_price.setValue(self.ui.spb_min_price.value())
        self.update_setting(sender.value())

    def validate_balance_percentage(self):
        sender = self.sender()
        mapping = {
            "spb_mon_percent": self.ui.spb_spell_trap_percent,
            "spb_spell_trap_percent": self.ui.spb_mon_percent,
            "spb_low_level_percent": self.ui.spb_high_level_percent,
            "spb_high_level_percent": self.ui.spb_low_level_percent,
            "spb_spell_percent": self.ui.spb_trap_percent,
            "spb_trap_percent": self.ui.spb_spell_percent,
        }
        if sender.objectName() in mapping:
            second_box = mapping[sender.objectName()]
            second_box.setValue(100 - sender.value())
            self.update_setting(second_box.value())
        self.update_setting(sender.value())
