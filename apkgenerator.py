from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from cartoon import cartoonize

KV = '''
MDScreen:
    orientation: 'vertical'
    MDTopAppBar:
        title: "Cartoonize Your Image"
        
    Image:
        allow_stretch: True
        keep_ratio: True
        id: convert_state
        size_hint_y : 0.7
        size_hint_x : 0.7
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        source: "assets/image.png"

    MDRaisedButton:
        background_color: 0.1, 0.5, 0.6, 1
        id:'convert'
        text: " Click for your image. "
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_release: app.app_same()
    
    MDRaisedButton:
        background_color: 0.1, 0.9, 0.0, 1
        text: " Click for cartoon."
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_release: app.convert_to_cartoon()
        
    MDRaisedButton:
        background_color: 1, 0.0, 0.7, 0.3
        text: " Click for edges."
        pos_hint: {'center_x': 0.8, 'center_y': 0.2}
        on_release: app.convert_to_edges()


'''

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)
        
    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen
    
    def convert_to_cartoon(self):
        self.kvs.ids.convert_state.source = cartoonize("cartoon_app/image.png",8)[1]
    def convert_to_edges(self):
            self.kvs.ids.convert_state.source = cartoonize("cartoon_app/image.png",8)[2]
    def app_same(self):
            self.kvs.ids.convert_state.source = cartoonize("cartoon_app/image.png",8)[0]
    
    
ma = MainApp()
ma.run()