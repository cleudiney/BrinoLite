from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class Frame(Widget):
#	log=ObjectProperty(None)
#	code=ObjectProperty(None)
#	def setLogText(self,txt):
#		self.log.text=txt
#	def setCodeText(self,txt):
#		self.code.text=txt
#	def getLogText(self):
#		return self.log.text
#	def getCodeText(self):
#		return self.code.text
	pass

class Code(ScrollView):
	pass

class Log(ScrollView):
	pass

class MainApp(App):
	def build(self):
		frame = Frame()
		return frame

if __name__ == '__main__':
	Window.clearcolor = (1, 1, 1, 1)
	MainApp().run()
