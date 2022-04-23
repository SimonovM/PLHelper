from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from code.screens.main_screen import MainScreen


class PLHelper(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (800, 600)
        self.title = "Справка по языкам программирования"

    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name="MainScreen"))
        return Builder.load_file("../interfaces/main_interface.kv")


if __name__ == "__main__":
    PLHelper().run()
