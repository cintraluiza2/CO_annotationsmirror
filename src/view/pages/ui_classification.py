from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_push_button import PyPushButtonGUI, PyPushButtonIcon, PyPushButtonGUIIcon
# IMPORTS STYLE
from view.widgets.style_css import text_box_class_style

class UiClassification(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("parent")
        parent.resize(800, 600)
        
        # SET INITIAL PARAMETERS
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #FFFFFF")
# ---------------------------------------------------------------------- ITENS/FRAMES
        # BOX
        self.box = QFrame()
        self.box.setMinimumWidth(500)
        self.box.setMaximumHeight(550)
        self.box.setStyleSheet(text_box_class_style)
        
        # TITLE ARTICLE
        self.title_article = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ")
        self.title_article.setMargin(5)
        self.title_article.setMinimumHeight(25)
        self.title_article.setMaximumHeight(25)
        self.title_article.setMinimumWidth(600)
        self.title_article.setMaximumWidth(900)
        
        # TEXT ARTICLE
        self.text_box_article = QTextBrowser()
        self.text_box_article.setText('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu. Ornare aenean euismod elementum nisi quis eleifend. Adipiscing at in tellus integer feugiat. In nibh mauris cursus mattis molestie a iaculis at erat. Dictum varius duis at consectetur lorem donec massa sapien. Mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum. Tempor orci dapibus ultrices in iaculis nunc sed. Eget magna fermentum iaculis eu non diam. Malesuada fames ac turpis egestas integer eget aliquet. Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Porttitor rhoncus dolor purus non enim praesent elementum. Sit amet mauris commodo quis imperdiet massa. Ultrices in iaculis nunc sed augue lacus. Lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant.
        In vitae turpis massa sed elementum. Sed blandit libero volutpat sed. Consequat ac felis donec et odio. Mauris cursus mattis molestie a iaculis at. Rhoncus urna neque viverra justo. In aliquam sem fringilla ut morbi. Egestas integer eget aliquet nibh praesent. Suspendisse faucibus interdum posuere lorem ipsum dolor sit amet consectetur. Lectus proin nibh nisl condimentum id. Dignissim cras tincidunt lobortis feugiat vivamus at augue eget. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Enim ut sem viverra aliquet. Est pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Justo eget magna fermentum iaculis eu. Laoreet id donec ultrices tincidunt arcu. Dignissim convallis aenean et tortor at risus viverra adipiscing at. Euismod in pellentesque massa placerat duis. Fames ac turpis egestas integer eget aliquet. A diam maecenas sed enim ut. Nisi est sit amet facilisis magna etiam.
        Arcu non sodales neque sodales. Orci nulla pellentesque dignissim enim. Nisi porta lorem mollis aliquam ut porttitor leo. Netus et malesuada fames ac turpis egestas. Gravida quis blandit turpis cursus in hac habitasse. Augue lacus viverra vitae congue eu. Tristique magna sit amet purus gravida quis. Eu turpis egestas pretium aenean pharetra magna ac placerat. Vitae congue mauris rhoncus aenean vel elit scelerisque. Quis varius quam quisque id diam vel quam elementum. Donec massa sapien faucibus et molestie ac. Iaculis at erat pellentesque adipiscing commodo elit at. Tempor id eu nisl nunc mi ipsum faucibus. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus. Quis auctor elit sed vulputate. Magna fermentum iaculis eu non.''')

        # BUTTONS FRAME
        self.frame_buttons = QFrame()
        self.frame_buttons.setMinimumHeight(50)
        self.frame_buttons.setMaximumHeight(50)
        
        # BUTTONS TEXT
        self.button_back = PyPushButtonGUIIcon(width=200, border_radius=20, icon_path="arrow_return.svg", text="Previous", btn_color="#1B4269", btn_hover="#1B5A69", btn_pressed="#3E5369", icon_color="white")
        self.button_finish = PyPushButtonGUI("Finish", width=200, border_radius=20, font_family="Roboto", font_size=13, btn_color="#77966D", btn_hover="#566C4F", btn_pressed="#3B4A36")
        self.button_cancel = PyPushButtonGUI("Cancel", width=200, border_radius=20, font_family="Roboto", font_size=13, btn_color="#941C2F", btn_hover="#8B1A2B", btn_pressed="#470E16")
        self.button_next = PyPushButtonGUIIcon(width=200, minimum_width=320, border_radius=20, icon_path="arrow_next.svg", text="Next", btn_color="#1B4269", btn_hover="#1B5A69", btn_pressed="#3E5369", icon_color="white")
                
# -------------------------------------------------------------------- LAYOUTS
        # CREATE LAYOUT MAIN
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(15, 10, 15, 15)
        self.main_layout.setSpacing(15)
        
        # BOX LAYOUT
        self.box_layout = QVBoxLayout(self.box)
        self.box_layout.setContentsMargins(10, 10, 10, 10)
        self.box_layout.setSpacing(15)
        
        # BUTTONS LAYOUT
        self.buttons_layout = QHBoxLayout(self.frame_buttons)

# -------------------------------------------------------------------- WIDGETS
        # IN MAIN LAYOUT
        self.main_layout.addWidget(self.box)
        self.main_layout.addWidget(self.frame_buttons)
        
        # IN BOX LAYOUT
        self.box_layout.addWidget(self.title_article)
        self.box_layout.addWidget(self.text_box_article) 
        
        # IN BUTTONS LAYOUT
        self.buttons_layout.addWidget(self.button_back)
        self.buttons_layout.addWidget(self.button_finish)
        self.buttons_layout.addWidget(self.button_cancel)
        self.buttons_layout.addWidget(self.button_next)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.addWidget(self.central_frame)
