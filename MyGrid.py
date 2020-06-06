#import kivy

from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests


class MyGrid(Screen):

	#def __init__(self, **kwargs):
	#	super(MyGrid, self).__init__(**kwargs)

	#name = ObjectProperty(None)
	#email = ObjectProperty(None)
	#password = ObjectProperty(None)

	def btn(self):
		
		sampleData = { 
			'name' : self.nameuser.text
			}

		Headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		jsonData = json.dumps(sampleData)
		print(jsonData)

		url='http://127.0.0.1:5000/registro'

		response = requests.post(url,json=jsonData,headers=Headers)

		print("Status code: ", response.status_code)
		resp_content = response.content

		

		try:
			resp_content = response.json()
			print('json')
			print(resp_content)
			if(resp_content['status']=='registered'):
				self.manager.current = 'RegisteredPage'
			elif(resp_content['status']=='fail'):
				self.manager.current = 'ErrorPage'
			elif(resp_content['status']=='existe'):
				self.manager.current = 'RepeatedPage'

		except ValueError:
			resp_content = response.content
			print('njson')
			print(resp_content)
			self.manager.current = 'ErrorPage'

	def regret(self):
		print("regreso")