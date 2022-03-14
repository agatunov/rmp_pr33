from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        boxLayout = BoxLayout(padding=[200], orientation='vertical');
        boxLayout.add_widget(Button(text="Button1", background_color=[.56,.23,.24,.2], background_normal=""))
        boxLayout.add_widget(Button(text="Button2", background_color=[.26,.75,.15,.75], background_normal=""))
        return boxLayout



if __name__ == "__main__":
    MyApp().run()
