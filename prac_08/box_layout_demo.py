from kivy.app import App
from kivy.lang import Builder
import random


class BoxLayoutDemo(App):
    def build(self):
        """build the kivy app from the kivy file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
def handle_greet(self):
    if random.randint(1,10) <=5:
        self.root.ids.my_label.txt = "ouch!"
    else:
        self.root.ids.my_label.txt = "oh no!"

BoxLayoutDemo().run()
