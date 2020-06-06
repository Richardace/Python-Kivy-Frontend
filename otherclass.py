from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenManagement(ScreenManager):

	def registro(self):
		self.current = 'MyGrid'

class ErrorPage(Screen):

	def chage(self):
		self.current = 'login_page'

class RegisteredPage(Screen):

	def chage(self):
		self.current = 'login_page'

class   RepeatedPage(Screen):
	def chage(self):
		self.current = 'MyGrid'