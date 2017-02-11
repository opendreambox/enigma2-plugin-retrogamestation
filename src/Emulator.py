from enigma import eConsoleAppContainer, eDBoxLCD, eRCInput, fbClass

from Components.Language import language
from Components.Sources.StaticText import StaticText
from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Log import Log

from os import path as os_path

class EmulatorSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent=parent)
		self.skinName = ["EmulatorSummary"]

class EmulationHelper(object):
	def __init__(self, name, description, cmd, pattern=None, romlocation=None, icon=None):
		self.name = name
		self.description = description
		self._cmd = cmd
		self.pattern = pattern
		self.location = romlocation
		self.icon = icon

	def getRunCmd(self, rom=None):
		if rom:
			return "%s '%s';" % (self._cmd, rom)
		else:
			return self._cmd

class Emulator(Screen, ServiceStopScreen):
	def __init__(self, session, emulationHelper, rom=None):
		Screen.__init__(self, session, emulationHelper.name)
		ServiceStopScreen.__init__(self)
		self._emulationHelper = emulationHelper
		self.__rom = rom
		if rom:
			self["lcdinfo"] = StaticText(os_path.basename(self.__rom))
		else:
			self["lcdinfo"] = StaticText(emulationHelper.name)
		self.__container = eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu(self.__rom)

	def __runEmu(self, rom=None):
		Log.i(rom)
		eDBoxLCD.getInstance().lock()
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		cmd = "export LANG=" + language.getLanguage() + ".UTF-8;%s" % (self._emulationHelper.getRunCmd(rom),)
		Log.w(cmd)
		self.__container.execute(cmd)

	def __runFinished(self, retval=1):
		Log.i(retval)
		eDBoxLCD.getInstance().unlock()
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()

	def createSummary(self):
		return EmulatorSummary
