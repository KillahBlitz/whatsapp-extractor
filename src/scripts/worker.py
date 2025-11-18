from PySide6.QtCore import QObject, Signal, Slot
from typing import List, Tuple
import traceback
from . import scrappy, errors

class ScraperWorker(QObject):
    started = Signal()
    progress = Signal(int, str)        # porcentaje y mensaje
    finished = Signal(list)            # lista de tuplas (nombre, telefono)
    error = Signal(str)                # mensaje de error

    def __init__(self, profile_path: str, group_name: str, parent=None):
        super().__init__(parent)
        self.profile_path = profile_path
        self.group_name = group_name
        self._cancel = False

    @Slot()
    def run(self):
        self.started.emit()
        try:
            self.progress.emit(5, "initializing browser...")
            rows = scrappy.scrape_group(self.profile_path, self.group_name)
            self.progress.emit(100, f"extraction completed: {len(rows)} participants")
            self.finished.emit(rows)

        except Exception as e:
            tb = traceback.format_exc()
            errors.handle_exception(e, context="ScraperWorker")
            self.error.emit(str(e) + "\n" + tb)
