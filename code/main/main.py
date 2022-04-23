from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder

Window.size = (800, 600)
Window.title = "Справка по языкам программирования"


class PLHelper(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return
