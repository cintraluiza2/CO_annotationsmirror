table_style = """
    QTableWidget {
        font-size: 12pt; 
        color: black;
        background-color: #E5E5E5;
        border:none;
    }
    
    QHeaderView::section {
        background-color: white;
        color: black;
        border-style: none;
        font-family: 'Roboto';
        margin-right: 7px;
    }
    
    QScrollBar::handle:vertical {
        background: #D6D6D6;
        min-height: 20px;
        border-radius: 7;
    }
    
    QScrollBar:vertical {
        border:none;
        background: transparent;
        width: 15px;
    }
    
    QScrollBar::sub-line:vertical,
    QScrollBar::add-line:vertical {
        subcontrol-origin: none;
        background: transparent;
    }
    
    QScrollBar::handle:horizontal {
        background: #D6D6D6;
        min-height: 20px;
        border-radius: 7;
    }
    
    ScrollBar::sub-line:horizontal,
    QScrollBar::add-line:horizontal {
        subcontrol-origin: none;
        background: transparent;
    }

    QScrollArea{
        border:none;
    }
    
    QTableWidget::item {
        border-bottom: 1px solid white;
        font-family: 'Roboto';
    }
    
"""