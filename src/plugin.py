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
from Screens.MessageBox import MessageBox

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/skin.xml"))

emulators = []

def RetroGameStationEntryComponent(emulator):
	return emulator.toList()

class RetroGameStation(Screen):
	def __init__(self, session):
		Screen.__init__(self, session, windowTitle=_("Retro GameStation"))
		self._list = List([], enableWrapAround = True, item_height = 50 )
		self["list"] = self._list
		self["red"] = Label()
		self["green"] = Label()
		self["actions"] = NumberActionMap(["OkCancelActions", "MenuActions", "NumberActions"],
		{
			"ok": self._onEmulatorSelected,
			"cancel": self.close,
		})
		self.reload()

	def reload(self):
		EmulationHelper.updatePackages()
		emus = sorted(emulators, key=lambda emulator: emulator.description)
		installed = []
		missing = []
		for emu in emus:
			entry = RetroGameStationEntryComponent(emu)
			if emu.check():
				installed.append(entry)
			else:
				missing.append(entry)
		installed.extend(missing)
		self._list.list = installed

	def _onEmulatorSelected(self):
		current = self._list.getCurrent()
		Log.w(current)
		if current:
			self._currentHelper = current[0]
			if not self._currentHelper.check():
				self.session.openWithCallback(self._onEmulatorInstalled, MessageBox, _("Do you want to install %s (%s)?") %(self._currentHelper.name, self._currentHelper.description), windowTitle=_("Emulator not installed!"))
				return
			if self._currentHelper.location != None:
				self.session.openWithCallback(self._onRomSelected, RomBrowser, self._currentHelper.name, self._currentHelper.pattern, self._currentHelper.location, filemode=self._currentHelper.fileMode)
			else:
				self.session.open(Emulator, self._currentHelper)

	def _onRomSelected(self, rom):
		if rom:
			self.session.open(Emulator, self._currentHelper, rom)

	def _onEmulatorInstalled(self, answer):
		if answer:
			self._currentHelper.install(self.session, self.reload)

def main(session, **kwargs):
	session.open(RetroGameStation)

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Retro GameStation"), description=_("Retro Gamging Emulators for dreambox"), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main),
		PluginDescriptor(name=_("Retro GameStation"), description=_("Retro Gamging Emulators for dreambox"), where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)
		]
