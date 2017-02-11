# # -*- coding: utf-8 -*-
# code by emanuel@ihad.tv / reichi@opendreambox.org

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.FileList import FileList
from Components.Label import Label
from Components.Sources.StaticText import StaticText

class RomBrowserSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent=parent)
		self.skinName = ["RomBrowserSummary"]

class RomBrowser(Screen):
	def __init__(self, session, title, pattern, location, filemode=True):
		Screen.__init__(self, session)
		self._title = title
		self._pattern = pattern
		self._location = location
		self._filemode = filemode
		self["title"] = StaticText("Rom Browser")
		self["lcdinfo"] = StaticText()
		if self._filemode:
			self.filelist = FileList(self._location.value, matchingPattern=self._pattern, showDirectories=True)
		else:
			self.filelist = FileList(self._location.value, showDirectories=True, showFiles=False)

		self["filelist"] = self.filelist
		self["buttonred"] = Label(_("Cancel"))
		self["buttongreen"] = Label(_("Select"))
		self["info"] = Label("")
		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "ShortcutActions", "DirectionActions"],
		{
			"ok": self._ok,
			"cancel": self._cancel,
			"green": self._green,
			"red" : self._red,
			"up": self._up,
			"upRepeated": self._up,
			"downRepeated": self._down,
			"down": self._down,
			"left": self._left,
			"right": self._right
		}, -1)

		self.onShown.append(self.__setInfo)
		self.onShown.append(self.__setTitle)

	def __setTitle(self):
		if self._filemode:
			self.setTitle(_("Select a rom for %s" % (self._title,)))
		else:
			self.setTitle(_("Select a rom directory for %s" % (self._title,)))

	def __setInfo(self):
		self["info"].setText(self["filelist"].getCurrentDirectory())
		self["lcdinfo"].setText(self["filelist"].getCurrent()[1][7])

	def createSummary(self):
		return RomBrowserSummary

	def _up(self):
		self["filelist"].up()
		self.__setInfo()

	def _down(self):
		self["filelist"].down()
		self.__setInfo()

	def _right(self):
		self["filelist"].pageDown()
		self.__setInfo()

	def _left(self):
		self["filelist"].pageUp()
		self.__setInfo()

	def _green(self):
		if self._filemode:
			self._ok()
		elif self["filelist"].getSelection()[0] <> "/autofs/" and self["filelist"].canDescent(): # isDir
			self._location.value = self["filelist"].getCurrentDirectory()
			self._location.save()
			if self["filelist"].getCurrentDirectory().endswith("/"):
				dir = self["filelist"].getCurrentDirectory()
			else:
				dir = self["filelist"].getCurrentDirectory() + "/"
			self.close(dir)

	def _ok(self):
		if self["filelist"].getSelection()[0] <> "/autofs/":
			if self["filelist"].canDescent(): # isDir
				self["filelist"].descent()
				self.__setInfo()

			elif self._filemode and self["filelist"].getFilename():
				self._location.value = self["filelist"].getCurrentDirectory()
				self._location.save()
				if self["filelist"].getCurrentDirectory().endswith("/"):
					file = self["filelist"].getCurrentDirectory() + self["filelist"].getFilename()
				else:
					file = self["filelist"].getCurrentDirectory() + "/" + self["filelist"].getFilename()
				self.close(file)

	def _red(self):
		self._cancel()

	def _cancel(self):
		self.close(None)
