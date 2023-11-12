from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen


class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return sm


if __name__ == '__main__':
    Builder.load_file('frontend.kv')
    app = MainApp()

    sm = MDScreenManager()

    home = HomeScreen(name='home')

    sm.add_widget(home)

    app.run()
