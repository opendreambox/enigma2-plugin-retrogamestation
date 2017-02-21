# -*- coding: utf-8 -*-
from skin import loadSkin

from Components.ActionMap import NumberActionMap
from Components.Sources.List import List
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Tools.Directories import SCOPE_PLUGINS, resolveFilename
from Tools.Log import Log

from Emulator import Emulator, EmulationHelper
from RomBrowser import RomBrowser
from Components.Label import Label

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/skin.xml"))

emulators = []

def RetroGameStationEntryComponent(emulator):
	return emulator.toList()

class RetroGameStation(Screen):
	def __init__(self, session):
		Screen.__init__(self, session, windowTitle=_("Retro GameStation"))
		EmulationHelper.updatePackages()
		emus = sorted(emulators, key=lambda emulator: emulator.description)
		items = [ RetroGameStationEntryComponent(emulator) for emulator in emus if emulator.check()]
		self._list = List(items, enableWrapAround = True, item_height = 50 )
		self["list"] = self._list
		self["red"] = Label()
		self["green"] = Label()
		self["actions"] = NumberActionMap(["OkCancelActions", "MenuActions", "NumberActions"],
		{
			"ok": self._onEmulatorSelected,
			"cancel": self.close,
		})

	def _onEmulatorSelected(self):
		current = self._list.getCurrent()
		Log.w(current)
		if current:
			self._currentHelper = current[1]
			if current[1].location != None:
				self.session.openWithCallback(self._onRomSelected, RomBrowser, self._currentHelper.name, self._currentHelper.pattern, self._currentHelper.location)
			else:
				self.session.open(Emulator, self._currentHelper)

	def _onRomSelected(self, rom):
		if rom:
			self.session.open(Emulator, self._currentHelper, rom)

def main(session, **kwargs):
	session.open(RetroGameStation)

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Retro GameStation"), description=_("Retro Gamging Emulators for dreambox"), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main),
		PluginDescriptor(name=_("Retro GameStation"), description=_("Retro Gamging Emulators for dreambox"), where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)
		]
