import traceback

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivymd.toast import toast
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.label.label import MDLabel
from kivy.properties import StringProperty


next_screen = 'home'


def change_screen(to='home'):
    global next_screen
    next_screen = to
    Clock.schedule_once(_change_screen, .1)


def _change_screen(_=None):
    if sm.current == next_screen:
        return
    sm.current = next_screen


def keyboard_hook(_, key, *__):
    print(key, sm.current)
    if key == 27:
        if sm.current == 'error_log':
            change_screen("home")
            return True


class MyLabel(MDLabel):
    text_ = StringProperty()

    def __init__(self, txt, **kwargs):
        super().__init__(**kwargs)
        self.text_ = txt


class ErrorLogScreen(Screen):
    error_text = ''

    def on_enter(self, *args):
        # self.ids['container'].clear_widgets()
        # for i in range(len(self.error_text) // 1000 + 1):  # MDLabel text become not readable after 1092 lines
        #     txt = self.error_text[i * 1000:(i+1) * 1000]
        #     self.ids['container'].add_widget(MyLabel(txt))

        self.ids['log_text'].text = self.error_text


class HomeScreen(Screen):
    def run(self):
        self.ids['button'].text = 'Running...'
        text = self.ids['text'].text
        try:
            exec(text)
        except Exception:
            error_log.error_text = traceback.format_exc()
            toast('Failed to execute')
        else:
            toast('Execution complete')
        self.ids['button'].text = 'Run'

    def goto_error_log(self):
        change_screen('error_log')


class MainApp(MDApp):
    def build(self):
        return sm

    def on_start(self):
        Window.bind(on_keyboard=keyboard_hook)


if __name__ == '__main__':
    Builder.load_file('frontend.kv')
    app = MainApp()

    sm = MDScreenManager()

    home = HomeScreen(name='home')
    error_log = ErrorLogScreen(name='error_log')

    sm.add_widget(home)
    sm.add_widget(error_log)

    app.run()
