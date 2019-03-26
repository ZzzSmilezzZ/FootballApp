from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import (Line)
from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

class PaintWidget(Widget):
    pass


class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation = "horizontal")
        instruments_bl = BoxLayout(orientation = "vertical", size_hint = (.4, 1))
        menu_bl = BoxLayout(orientation = "horizontal", size_hint = (1,.1))
        iconsGrid = GridLayout(cols = 3)
        iconsScatter = Scatter()

        menu_bl.add_widget(Button(text = "Save"))
        menu_bl.add_widget(Button(text = "Screenshot"))
        menu_bl.add_widget(Button(text = "Send"))

        # here could be icons
        iconsGrid.add_widget(Button(text = "1"))
        iconsGrid.add_widget(Button(text="2"))
        iconsGrid.add_widget(Button(text="3"))
        iconsGrid.add_widget(Button(text="4"))
        iconsGrid.add_widget(Button(text="5"))
        iconsGrid.add_widget(Button(text="6"))
        iconsGrid.add_widget(Button(text="7"))
        iconsGrid.add_widget(Button(text="8"))
        iconsGrid.add_widget(Button(text="9"))
        iconsGrid.add_widget(Button(text="10"))
        iconsGrid.add_widget(Button(text="11"))
        iconsGrid.add_widget(Button(text="12"))


        instruments_bl.add_widget(menu_bl)
        instruments_bl.add_widget(Button(text = "Instruments", size_hint = (1,.250)))
        instruments_bl.add_widget(iconsGrid) #icons
        bl.add_widget(instruments_bl)
        bl.add_widget(Image(source = r"C:\Users\Cookie\Desktop\25582ec5600f53f.jpg", allow_stretch = True))
        return bl

if __name__ == "__main__":
    MyApp().run()