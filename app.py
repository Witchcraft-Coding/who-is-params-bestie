import sys
from PySide6 import QtWidgets

from ui import WhoIsParamsBestie

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = WhoIsParamsBestie()
    widget.show()
    sys.exit(app.exec())