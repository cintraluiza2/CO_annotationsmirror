from qt_core import *

def calculate_color(model, row):
    value = model.index(row, 3).data()
    if (value == 'Dúvida') or (value == None):
        color = QColor("#D4AA7B")
        return QBrush(color)
    elif value == 'Relevante':
        color = QColor("#96ADC8")
        return QBrush(color)
    elif value == 'Irrelevante':
        color = QColor("#C2707A")
        return QBrush(color)
    else:
        return QBrush(Qt.white)


class PyColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.column():
            model = index.model()
            r = index.row()
            color = calculate_color(model, r)
            if color != index.data(Qt.BackgroundRole):
                for i in range(model.columnCount()):
                    model.setData(model.index(r, i), color, Qt.BackgroundRole)
        super(PyColorDelegate, self).paint(painter, option, index)
