from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from code.screens.c_sharp_lang_screen import CSharpLangScreen
from code.screens.erlang_lang_screen import ErlangLangScreen
from code.screens.f_sharp_lang_screen import FSharpLangScreen
from code.screens.func_langs_choose_screen import FuncLangsChooseScreen
from code.screens.haskell_lang_screen import HaskellLangScreen
from code.screens.java_lang_screen import JavaLangScreen
from code.screens.lang_type_screen import LangTypeScreen
from code.screens.lisp_lang_screen import LispLangScreen
from code.screens.main_screen import MainScreen
from code.screens.imperative_langs_choose_screen import ImperativeLangsChooseScreen
from code.screens.python_lang_screen import PythonLangScreen
from code.screens.cplus_lang_screen import CPlusLangScreen
from code.screens.go_lang_screen import GoLangScreen
from code.screens.scala_lang_screen import ScalaLangScreen

Builder.load_file("../interfaces/ui/rounded_button.kv")
Builder.load_file("../interfaces/main_screen.kv")
Builder.load_file("../interfaces/lang_type_screen.kv")
Builder.load_file("../interfaces/imperative_langs/imperative_langs_choose_screen.kv")
Builder.load_file("../interfaces/func_langs/func_langs_choose_screen.kv")
Builder.load_file("../interfaces/imperative_langs/C#.kv")
Builder.load_file("../interfaces/imperative_langs/Java.kv")
Builder.load_file("../interfaces/imperative_langs/Python.kv")
Builder.load_file("../interfaces/func_langs/F#.kv")
Builder.load_file("../interfaces/func_langs/Haskell.kv")
Builder.load_file("../interfaces/func_langs/Lisp.kv")
Builder.load_file("../interfaces/imperative_langs/C++.kv")
Builder.load_file("../interfaces/imperative_langs/Go.kv")
Builder.load_file("../interfaces/func_langs/Erlang.kv")
Builder.load_file("../interfaces/func_langs/Scala.kv")

class PLHelper(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (800, 600)
        self.title = "Справка по языкам программирования"

    def build(self):
        manager = ScreenManager(transition=FadeTransition())
        manager.add_widget(MainScreen(name="main"))
        manager.add_widget(LangTypeScreen(name="lang_type"))
        manager.add_widget(ImperativeLangsChooseScreen(name="imperative"))
        manager.add_widget(FuncLangsChooseScreen(name="func"))
        manager.add_widget(CSharpLangScreen(name="c#"))
        manager.add_widget(JavaLangScreen(name="java"))
        manager.add_widget(PythonLangScreen(name="python"))
        manager.add_widget(FSharpLangScreen(name="f#"))
        manager.add_widget(HaskellLangScreen(name="haskell"))
        manager.add_widget(LispLangScreen(name="lisp"))
        manager.add_widget(CPlusLangScreen(name="cplus"))
        manager.add_widget(GoLangScreen(name="go"))
        manager.add_widget(ErlangLangScreen(name="erlang"))
        manager.add_widget(ScalaLangScreen(name="scala"))
        return manager


if __name__ == "__main__":
    PLHelper().run()
