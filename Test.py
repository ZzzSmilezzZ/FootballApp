from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '696')

from kivy.core.window import Window
Window.clearcolor = (.50,.50,.50,1)

class TestApp(App):
    def build(self):
        bl = BoxLayout(orientation = "horizontal")
        instruments_bl = BoxLayout(orientation = "vertical", size_hint = (.4, 1))
        menu_bl = BoxLayout(orientation = "horizontal", size_hint = (1,.1))
        icons_grid = GridLayout()
        icons_background = Image(color = (1,0,0,1), size_hint = (1, .250), size = (.1,.1))
        sc = Scatter()

        # incons
        icon1 = Scatter(pos = (1040, 420), size = (20,33), auto_bring_to_front = True)
        icon1.add_widget(Image(source = r"Footballers_icons\1.png", size = (20,33)))
        icons_grid.add_widget(icon1)

        icon2 = Scatter(pos = (1080, 420), size = (18,36))
        icon2.add_widget(Image(source = r"Footballers_icons\2.png", size = (18,36)))
        icons_grid.add_widget(icon2)

        icon3 = Scatter(pos=(1120, 420), size=(20, 33))
        icon3.add_widget(Image(source= r"Footballers_icons\3.png", size=(20, 33)))
        icons_grid.add_widget(icon3)

        icon4 = Scatter(pos=(1160, 420), size=(20, 33))
        icon4.add_widget(Image(source= r"Footballers_icons\4.png", size=(20, 33)))
        icons_grid.add_widget(icon4)

        icon5 = Scatter(pos=(1200, 420), size=(18, 36))
        icon5.add_widget(Image(source= r"Footballers_icons\5.png", size=(18, 36)))
        icons_grid.add_widget(icon5)

        icon6 = Scatter(pos=(1240, 420), size=(19, 32))
        icon6.add_widget(Image(source= r"Footballers_icons\6.png", size=(19, 32)))
        icons_grid.add_widget(icon6)

        icon7 = Scatter(pos=(1280, 420), size=(20, 32))
        icon7.add_widget(Image(source= r"Footballers_icons\7.png", size=(20, 32)))
        icons_grid.add_widget(icon7)

        icon8 = Scatter(pos=(1320, 420), size=(20, 32))
        icon8.add_widget(Image(source= r"Footballers_icons\8.png", size=(20, 32)))
        icons_grid.add_widget(icon8)

        icon9 = Scatter(pos=(1084, 380), size=(12, 11))
        icon9.add_widget(Image(source= r"Footballers_icons\9.png", size=(12, 11)))
        icons_grid.add_widget(icon9)

        icon10 = Scatter(pos=(1044, 380), size=(11, 28))
        icon10.add_widget(Image(source= r"Footballers_icons\10.png", size=(11, 28)))
        icons_grid.add_widget(icon10)

        icon11 = Scatter(pos=(1124, 380), size=(12, 17))
        icon11.add_widget(Image(source= r"Footballers_icons\11.png", size=(12, 17)))
        icons_grid.add_widget(icon11)

        icon12 = Scatter(pos=(1154, 380), size=(25, 7))
        icon12.add_widget(Image(source= r"Footballers_icons\12.png", size=(25, 7)))
        icons_grid.add_widget(icon12)

        icon13 = Scatter(pos=(1204, 380), size=(10, 16))
        icon13.add_widget(Image(source= r"Footballers_icons\13.png", size=(10, 16)))
        icons_grid.add_widget(icon13)

        icon14 = Scatter(pos=(1244, 380), size=(11, 15))
        icon14.add_widget(Image(source= r"Footballers_icons\14.png", size=(11, 15)))
        icons_grid.add_widget(icon14)

        icon15 = Scatter(pos=(1284, 380), size=(11, 15))
        icon15.add_widget(Image(source= r"Footballers_icons\15.png", size=(11, 15)))
        icons_grid.add_widget(icon15)

        icon16 = Scatter(pos=(1360, 420), size=(14, 36))
        icon16.add_widget(Image(source= r"Footballers_icons\16.png", size=(14, 36)))
        icons_grid.add_widget(icon16)

        icon17 = Scatter(pos=(1390, 420), size=(13, 37))
        icon17.add_widget(Image(source= r"Footballers_icons\17.png", size=(13, 37)))
        icons_grid.add_widget(icon17)

        icon18 = Scatter(pos=(1420, 420), size=(12, 37))
        icon18.add_widget(Image(source= r"Footballers_icons\18.png", size=(12, 37)))
        icons_grid.add_widget(icon18)

        icon19 = Scatter(pos=(1090, 285), size=(38, 85))
        icon19.add_widget(Image(source= r"Footballers_icons\19.png", size=(38, 85)))
        icons_grid.add_widget(icon19)

        icon20 = Scatter(pos=(1040, 285), size=(34, 85))
        icon20.add_widget(Image(source= r"Footballers_icons\20.png", size=(34, 85)))
        icons_grid.add_widget(icon20)


        menu_bl.add_widget(Button(text = "Save"))
        menu_bl.add_widget(Button(text = "Screen"))
        menu_bl.add_widget(Button(text = "Send"))



        instruments_bl.add_widget(menu_bl)
        instruments_bl.add_widget(icons_background)
        instruments_bl.add_widget(icons_grid) #icons
        bl.add_widget(Image(source = r"C:\Users\Cookie\Desktop\FootballApp\Footballers_icons\football_field1.png", allow_stretch = True))
        bl.add_widget(instruments_bl)
        return bl



if __name__ == "__main__":
    TestApp().run()