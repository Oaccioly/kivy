from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.

class Tela(ScreenManager):
    pass


class Inicio(App):
    def build(self):
        return Tela()


if __name__ == '__main__':
    Inicio().run()
