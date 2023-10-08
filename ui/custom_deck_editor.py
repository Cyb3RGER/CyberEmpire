import logging
import os.path
import random
from typing import Optional

from PySide6.QtCore import QTextStream
from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import QDialog, QFileDialog, QDialogButtonBox

import custom_decks
from cards import CardHelper
from settings import RandomizerSettings
from ui.CodeEditor import CodeEditor
from ui.TextEditLogHandler import TextEditLogHandler
from ui.ui_custom_deck_editor import Ui_Dialog
from utils import prog_name


class CustomDeckEditor(QDialog):
    def __init__(self):
        super().__init__()
        self.deck: Optional[custom_decks.CustomDeck] = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        mock_settings = RandomizerSettings()
        self.card_helper = CardHelper(mock_settings)
        self.setWindowTitle(f'{prog_name} - Custom Deck Editor')
        self.logger = logging.getLogger('custom_deck_validator')
        self.logger.setLevel(logging.DEBUG)
        self.parser = custom_decks.CustomDeckParser()
        self.handler = TextEditLogHandler(self.ui.txt_result)
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.handler.setLevel(logging.INFO)
        # replace parser log handlers
        self.parser.logger = self.logger
        self.parser.logger.addHandler(self.handler)
        self.current_file = None
        self.ui.txt_source = CodeEditor(self)
        self.ui.txt_source.setObjectName(u"txt_source")
        self.ui.txt_source.setStyleSheet(u"")
        self.ui.txt_source.setBackgroundVisible(False)
        self.ui.gridLayout.addWidget(self.ui.txt_source, 1, 0, 1, 1)

        self.ui.btn_file.clicked.connect(self.select_file)
        self.ui.txt_source.textChanged.connect(self.update_log)
        self.ui.btn_generate.clicked.connect(self.generate_deck)
        self.ui.btn_generate.setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save_file)

    def __del__(self):
        self.parser.logger.removeHandler(self.handler)

    def generate_deck(self):
        if self.deck is None:
            return
        result = self.card_helper.get_deck_from_custom_deck(self.deck, random.Random())
        self.ui.txt_example.setPlainText(str(result))

    def save_file(self):
        if not self.current_file:
            return
        with open(self.current_file, 'w') as f:
            f.write(self.ui.txt_source.toPlainText())

    def update_log(self):
        if not self.current_file:
            return
        self.reset_log()
        _, file_name = os.path.split(self.current_file)
        try:
            self.deck = self.parser.parse(self.ui.txt_source.toPlainText(), file_name)
            self.ui.btn_generate.setEnabled(True)
        except Exception:
            self.deck = None
            self.ui.btn_generate.setEnabled(False)

    def reset_log(self):
        self.ui.txt_result.clear()

    def reset_file(self):
        self.current_file = None
        self.setWindowTitle(f'{prog_name} - Custom Deck Editor')
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(False)
        self.ui.txt_source.clear()
        self.reset_log()

    def select_file(self):
        self.reset_file()
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Select game folder...")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setViewMode(QFileDialog.ViewMode.Detail)
        dialog.setDirectory(os.path.join(os.getcwd(), 'custom_decks'))
        dialog.setNameFilter('Custom Decks (*.txt)')
        if dialog.exec():
            file_path = dialog.selectedFiles()[0]
            if file_path and os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data = f.read()
                    self.ui.txt_source.setPlainText(data)
                self.current_file = file_path
                _,file_name = os.path.split(self.current_file)
                self.setWindowTitle(f'{prog_name} - Custom Deck Editor - {file_name}')
                self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Save).setEnabled(True)
                try:
                    self.deck = self.parser.load(file_path)
                    self.ui.btn_generate.setEnabled(True)
                except:
                    self.deck = None
                    self.ui.btn_generate.setEnabled(False)
