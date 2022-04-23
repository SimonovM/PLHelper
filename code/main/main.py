from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from code.screens.lang_type_screen import LangTypeScreen
from code.screens.main_screen import MainScreen

Builder.load_file("../interfaces/main_screen.kv")
Builder.load_file("../interfaces/lang_type_screen.kv")


class PLHelper(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (800, 600)
        self.title = "Справка по языкам программирования"

    def build(self):
        manager = ScreenManager(transition=FadeTransition())
        manager.add_widget(MainScreen(name="main"))
        manager.add_widget(LangTypeScreen(name="lang_type"))
        return manager


if __name__ == "__main__":
    PLHelper().run()
