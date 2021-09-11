import sys

from pathlib import Path
import os


if __name__ == "__main__":
    """
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    configure_logging()
    window = MainWindow(screen)
    window.show()
    sys.exit(app.exec())
    """

    os.system("unoconv -f pdf " + " Ausflugsziele.odt")
