import os.path as path
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests

from kivy.core.audio import SoundLoader ,Sound
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

class Song(Sound):

	on_pause= False
	position=0

	def __init__(self , song):
		self.sound = SoundLoader.load(song)
		self.position=self.sound.get_pos()


	def play_pause(self):
	
		if(self.on_pause):
			self.sound.play()
			self.sound.seek(self.position)
			self.on_pause= False
		elif (self.sound.state == 'stop'):
			self.sound.play()
			self.position=0
		else:
			self.on_pause= True
			self.position= self.sound.get_pos()
			self.sound.stop()

	def set_stop(self):
		self.on_pause= False
		self.sound.stop()


class MusicPage(Screen):

	sound=None
	position=0
	play_pause_image=ObjectProperty()
	songlist=[]
	user=''
	actual_song = StringProperty()

	def __init__(self,user, **kwargs):
		self.user=user
		self.actual_song=''
		super(MusicPage, self).__init__(**kwargs)
	
	def play(self):
		if(self.sound!=None):
			if self.sound.on_pause:
				self.ids.play_pause_image.source='icons/01.png'
			else:
				self.ids.play_pause_image.source='icons/02.png'
			self.sound.play_pause()

	def stop(self):
		if(self.sound!=None):
			self.sound.set_stop()

	def volme(self):
		if(self.sound!=None):
			self.sound.volume -=0.1

	def volma(self):
		if(self.sound!=None):
			self.sound.volume += 0.1
			
	def findfile(self,name):

		for x in self.songlist:
			if x['name']== name:
				return x['file']

	def regreso(self):
		self.stop()
		self.manager.clear_widgets(screens=[self.manager.get_screen('MusicPage')])
		self.current = 'login_page'

	# For Spinner defining spinner clicked function 
	def spinner_clicked(self, value):
		file = self.findfile(value)

		if file!=None and path.exists(file):
			self.stop()
			self.sound=Song(file)
			self.play()
			#self.ids.label_cancion.text=value


	def defval(self):

		arr= []
		for x in range(5):
			arr.append("asd"+str(x))
		print("arra: "+str(arr))

		return arr


	def prarr(self):

		#username= self.manager.screens[0].ids.user.text

		sampleData = { 
			"name" : self.user
			}

		Headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		jsonData = json.dumps(sampleData)
		print(jsonData)

		url='http://127.0.0.1:5000/list'
		response = None
		try:
			response = requests.post(url,json=jsonData,headers=Headers)
		except ConnectionError:
			return self.defval()


		print("Status code: ", response.status_code)
	

		try:
			resp_content = response.json()
			print('json')
			print(resp_content)

		except ValueError:
			resp_content = response.content
			print('njson')
			print(resp_content)
			return self.defval()


		self.songlist=resp_content

		arr= []

		for x in self.songlist:
			asd= x#['song']
			arr.append(asd['name'])

		print("songs "+str(arr))

		return arr
