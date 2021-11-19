from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kv import screen_helper


Window.size = (310, 580)


class SNTI(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(screen_helper)
        return screen

    class HomeScreen(Screen):
        pass

    class SignScreen(Screen):
        pass

    class MainScreen(Screen):
        pass

    class CoursesScreen(Screen):
        pass

    class AdmissionprocedureScreen(Screen):
        pass

    class AdministrationScreen(Screen):
        pass

    class FeeScreen(Screen):
        pass

    class AboutScreen(Screen):
        pass


SNTI().run()
