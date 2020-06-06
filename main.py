
from kivy.app import App
#from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from otherclass import *
from MyGrid import MyGrid
from LoginPage import LoginPage
from MusicPage import MusicPage


kv_file = Builder.load_file('my.kv')
#Builder.load_file('my.kv')

#sm = ScreenManager()
#sm.add_widget(LoginPage(name='LoginPage'))
#sm.add_widget(ErrorPage(name='ErrorPage'))
#sm.add_widget(MyGrid(name='MyGrid'))
#sm.current='LoginPage'


class MyApp(App): # <- Main Class
    def builder(self):
        return kv_file

if __name__ == "__main__":
	MyApp().run()