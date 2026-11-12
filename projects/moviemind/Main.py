import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from PySide6.QtWidgets import QApplication, QMainWindow

from BackEnd.Initial_System import initial
from UI.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, system):
        super().__init__()
        self.setupUi(self, system)


def main():
    app = QApplication(sys.argv)
    with TemporaryDirectory(prefix="moviemind-") as directory:
        system = initial(Path(directory) / "MovieMind.db")
        window = MainWindow(system)
        window.show()
        return app.exec()


if __name__ == "__main__":
    sys.exit(main())
