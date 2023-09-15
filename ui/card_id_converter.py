from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QComboBox, QCompleter

from mappers import card_name_mapper
from ui.ui_card_id_converter import Ui_Dialog
from utils import prog_name


class CardIDConverter(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f'{prog_name} - Card ID Converter')

        completer = QCompleter(card_name_mapper.name_to_id.keys())
        completer.setCompletionRole(Qt.ItemDataRole.EditRole)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(Qt.MatchFlag.MatchWildcard)
        completer.setMaxVisibleItems(10)
        self.ui.txt_names.setCompleter(completer)

        self.ui.txt_id.textChanged.connect(self.on_id_changed)
        self.ui.txt_names.textChanged.connect(self.on_name_changed)

    def on_name_changed(self, value):
        self.ui.txt_id.blockSignals(True)
        id_ = card_name_mapper.get_id(value)
        if id_ == -1:
            pass
            self.ui.txt_id.setText("")
        else:
            self.ui.txt_id.setText(str(id_))
        self.ui.txt_id.blockSignals(False)

    def on_id_changed(self, value):
        self.ui.txt_names.blockSignals(True)
        try:
            id_ = int(value)
        except Exception:
            return
        self.ui.txt_names.setText(card_name_mapper.get_name(id_))
        self.ui.txt_names.blockSignals(False)
