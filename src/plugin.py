# -*- coding: utf-8 -*-
from skin import loadSkin

from Components.ActionMap import NumberActionMap
from Components.MenuList import MenuList
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Tools.Directories import SCOPE_PLUGINS, resolveFilename
from Tools.Log import Log

from Emulator import Emulator
from RomBrowser import RomBrowser

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/skin.xml"))

emulators = []

class RetroGameStation(Screen):
	def __init__(self, session):
		Screen.__init__(self, session, windowTitle=_("Retro GameStation"))
		items = [ ("%s - powered by %s" % (x.description, x.name), x) for x in emulators ]
		self._menuList = MenuList(items, enableWrapAround=True)
		self["list"] = self._menuList
		self["actions"] = NumberActionMap(["OkCancelActions", "MenuActions", "NumberActions"],
		{
			"ok": self._onEmulatorSelected,
			"cancel": self.close,
		})

	def _onEmulatorSelected(self):
		current = self._menuList.getCurrent()
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
