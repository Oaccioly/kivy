from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))


class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class Main_scroll2(App):
    def build(self):
        return Tarefas(['Comprar Hd',
                        'Comprar ssd',
                        'Comprar teclado',
                        'Comprar  Monitor'])


if __name__ == '__main__':
    Main_scroll2().run()
