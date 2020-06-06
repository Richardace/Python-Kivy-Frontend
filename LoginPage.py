#import kivy
#from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests
from MusicPage import MusicPage

class LoginPage(Screen):


	def login(self):

	
		sampleData = { 
			"name" : self.user.text
			}

		Headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		jsonData = json.dumps(sampleData)
		print(jsonData)

		url='http://127.0.0.1:5000/login'
		response = requests.post(url,json=jsonData,headers=Headers)

		print("Status code: ", response.status_code)
		resp_content = response.content


		try:
			resp_content = response.json()
			print('json')
			print(resp_content)
			if(resp_content['status']=='logged'):
				print(str(self.manager.screens[0].ids.user.text))
				#print(str(self.manager.get_screen('LoginPage').ids.user.text))
				
				#add_widget(MusicPage(name='MusicPage'))

				#self.manager.clear_widgets(screens=[self.manager.get_screen('MusicPage')])
				#self.manager.clear_widgets(screens=[self.manager.screens[1]])
				self.manager.add_widget(MusicPage(self.user.text,name="MusicPage"))
				self.manager.current = 'MusicPage'
			elif (resp_content['status']=='unknow'):
				self.manager.current = 'ErrorPage'


		except ValueError:
			resp_content = response.content
			print('njson')
			print(resp_content)
			self.manager.current = 'ErrorPage'


	def btn(self):
		print('algo')
