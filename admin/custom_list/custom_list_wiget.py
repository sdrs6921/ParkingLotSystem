from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UserModel(QAbstractListModel):
    def __init__(self, data=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, role=None):
        item = self._data[QModelIndex.row()]

        if role == Qt.DisplayRole:
            return "%s" % (item['car_number'])
        elif role == Qt.DecorationRole:
            return QColor(item['enter_time'])
        elif role == Qt.BackgroundRole:
            return QBrush(Qt.Dense7Pattern)
        elif role == Qt.ToolTipRole:
            return "Tool Tip: %s" % (item['name'])
        return QVariant()
