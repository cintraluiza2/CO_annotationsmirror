# Imports
import os

from PySide6.QtGui import QPaintEvent

# Import QT Core
from qt_core import *

class PyPushButtonIcon(QPushButton):
    
    def __init__(self, text = "", height = 40, minimum_width = 50, text_padding = 55, text_color = "#FFFFFF", icon_path = "", icon_color = "#FFFFFF", btn_color = "#1B4269", btn_hover = "#2563A0", btn_pressed = "#133557", is_active = False):
        super().__init__()
        
        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        
        # Custom Parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
        # Set Sytle
        self.set_style(text_padding=self.text_padding, text_color=self.text_color, btn_color=self.btn_color, btn_hover=self.btn_hover, btn_pressed=self.btn_pressed, is_active=self.is_active)
        
    # ------------------------------------------------- Methods ----------------------------------------------
    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding, 
            text_color=self.text_color, 
            btn_color=self.btn_color, 
            btn_hover=self.btn_hover, 
            btn_pressed=self.btn_pressed, 
            is_active=is_active_menu
        )
    
    def set_style(self, text_padding = 55, text_color = "#FFFFFF", btn_color = "#1B4269", btn_hover = "#2563A0", btn_pressed = "#133557", is_active = False):
        
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton::hover {{
            background-color: {btn_hover};
        }}
        QPushButton::pressed {{
            background-color: {btn_pressed};
        }}
        """
        active_style = f"""
        QPushButton {{
            background-color: {btn_pressed};
            border-right: 5px solid #941C2F;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
            
    # ------------------------------------------------- Draw Image ----------------------------------------------
    def paintEvent(self, event) -> None:
        # Return Default Style
        QPushButton.paintEvent(self, event)
        
        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        
        # Rectangulo
        rect = QRect(0, 0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        
        qp.end()
        
    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "resources/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))
        
        # Draw Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        
        painter.end()
        
# ------------------------------------------------------------------------------------ BUTTON GUI
class PyPushButtonGUI(QPushButton):
    def __init__(self, text = "", height = 40, width = 50, text_padding = 0, border_radius= 0, text_color = "#FFFFFF", btn_color = "#1B4269", btn_hover = "#2563A0", btn_pressed = "#133557", font_size = 12, font_family = "Arial"):
        super().__init__()
        
        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setMaximumWidth(width)
        self.setMinimumWidth(150)
        self.setCursor(Qt.PointingHandCursor)
        
        # Custom Parameters
        self.text_padding = text_padding
        self.text_color = text_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.font_size = font_size
        self.font_family = font_family
        self.border_radius = border_radius
        
        # Set Sytle
        self._set_style(text_padding=self.text_padding, border_radius=border_radius, text_color=self.text_color, btn_color=self.btn_color, btn_hover=self.btn_hover, btn_pressed=self.btn_pressed, font_size=font_size, font_family=font_family)
        
    def _set_style(self, text_padding, border_radius, text_color, btn_color, btn_hover, btn_pressed, font_size, font_family):
        
        style = f"""
        QPushButton {{
            font-size: {font_size}pt;
            font-family: {font_family};
            color: {text_color};
            background-color: {btn_color};
            padding: {text_padding}px;
            text-align: center;
            border: solid;
            border-radius: {border_radius}px;
        }}
        QPushButton::hover {{
            background-color: {btn_hover};
        }}
        QPushButton::pressed {{
            background-color: {btn_pressed};
        }}
        """

        self.setStyleSheet(style)
        