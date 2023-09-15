import logging
from logging import StreamHandler, LogRecord, FileHandler, Handler

from PySide6.QtCore import QIODevice
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTextEdit


class TextEditLogHandler(Handler):
    ErrTextColor = QColor(207, 91, 92)
    WarnTextColor = QColor(207, 207, 89)
    DefaultTextColor = QColor(160, 160, 160)

    def __init__(self, text_edit: QTextEdit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record: LogRecord) -> None:
        try:
            if self.text_edit:
                if record.levelno >= logging.ERROR:
                    self.text_edit.setTextColor(self.ErrTextColor)
                elif record.levelno >= logging.WARN:
                    self.text_edit.setTextColor(self.WarnTextColor)
                else:
                    self.text_edit.setTextColor(self.DefaultTextColor)
                self.text_edit.append(self.format(record))
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)
