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
        border: solid;
        border-radius: 8px;
        font-family: 'Roboto';
        margin-right: 7px;
    }
    
    QHeaderView::section:hover {
        background-color: #FFF8F0;
    }
    
    QHeaderView::section:pressed {
        background-color: #FFC786;
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
    
    QTableWidget::item {
        border-bottom: 1px solid white;
        font-family: 'Roboto';
    }
    
"""

text_box_class_style = """
    QFrame {
        background-color: #EBEAEA;
    }
    
    QLabel {
        border: solid;
        border-radius: 10px;
        background-color: white;
        margin-right: 7px;
    }
    
    QTextBrowser {
        background-color: #FFFFFF; 
        border: none;
        border-radius: 4px;
        font-family: 'Roboto';
        font-size: 20px; 
        text-align: justify; 
        word-spacing: 5px;
    }
    
    QScrollBar::handle:vertical {
        background: #D6D6D6;
        min-height: 7px;
        border-radius: 7;
    }
    
    QScrollBar:vertical {
        border:none;
        background: transparent;
        width: 14px;
    }
    
    QScrollBar::sub-line:vertical,
    QScrollBar::add-line:vertical {
        subcontrol-origin: none;
        background: transparent;
    }
"""
