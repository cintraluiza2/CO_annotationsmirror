from qt_core import *

def calculate_color(model, row):
    """
    Função para calcular a cor de fundo de uma célula em uma 
    tabela com base no valor da célula em uma determinada coluna.

    Parâmetros:
    ----------
    model : QAbstractItemModel
        O modelo que contém os dados da tabela.
    row : int
        O índice da linha da célula a ser avaliada.

    Retorna:
    --------
    Um objeto QBrush contendo a cor de fundo correspondente ao valor da célula na coluna 3:
    """
    value = model.index(row, 3).data()
    if (value == 'Dúvida'):
        color = QColor("#D4AA7B")
        return QBrush(color)
    elif value == 'Relevante':
        color = QColor("#96ADC8")
        return QBrush(color)
    elif value == 'Irrelevante':
        color = QColor("#C2707A")
        return QBrush(color)
    else:
        color = QColor("#E5E5E5")
        return QBrush(color)


class PyColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        """
        Método sobrescrito de QStyledItemDelegate para pintar as células da 
        tabela com base em uma lógica de cores.

        Parâmetros:
        ----------
        painter : QPainter
            O objeto QPainter usado para renderizar o conteúdo da célula.
        option : QStyleOptionViewItem
            O objeto que contém as opções de estilo para desenhar a célula.
        index : QModelIndex
            O índice que identifica a célula a ser desenhada.

        Descrição:
        -----------
        Este método altera a cor de fundo das células de uma linha inteira, 
        com base no valor da célula em uma coluna específica.
        """
        if index.column():
            model = index.model()
            r = index.row()
            color = calculate_color(model, r)
            if color != index.data(Qt.BackgroundRole):
                for i in range(model.columnCount()):
                    model.setData(model.index(r, i), color, Qt.BackgroundRole)
        super(PyColorDelegate, self).paint(painter, option, index)
