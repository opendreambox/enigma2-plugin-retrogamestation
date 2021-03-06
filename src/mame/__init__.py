from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.mame = ConfigSubsection()
config.plugins.retrogamestation.mame.romlocation = ConfigDirectory(default="/media/")

config.plugins.retrogamestation.mess = ConfigSubsection()
config.plugins.retrogamestation.mess.romlocation = ConfigDirectory(default="/media/")

class Mame(EmulationHelper):
	name = _("AdvanceMAME")
	description = _("Mame")
	location = config.plugins.retrogamestation.mame.romlocation
	pattern = "^.*\.(zip|ZIP)"
	cmd = "/usr/bin/advmame-start"
	icon = "mame/mame.svg"
	packageName = "advancemame"

emulators.append(Mame())

class MessEmulationHelperCart(EmulationHelper):
	def getRunCmd(self, rom=None):
		if rom:
			return "%s %s '%s';" % (self.cmd, self.system, rom)
		return ""

class MessNES(MessEmulationHelperCart):
	name = _("AdvanceMESS")
	description = _("Nintendo Entertainment System / Famicom")
	location = config.plugins.retrogamestation.mess.romlocation
	pattern = "^.*\.(zip|ZIP|nes)"
	cmd = "/usr/bin/advmess-start-cart"
	icon = "mame/nes.svg"
	system = "nes"
	packageName = Mame.packageName

emulators.append(MessNES())

""" MAME INIT """
from os import path as os_path
from os import mkdir as os_mkdir
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile

if not os_path.exists("/root/.advance"):
	os_mkdir("/root/.advance")
if not os_path.exists("/root/.advance/advmame.rc"):
	print "[advmame]: config  /root/.advance/advmame.rc not found creating it..."
	copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/mame/advmame.rc.default"), "/root/.advance/advmame.rc")
if not os_path.exists("/root/.advance/advmess.rc"):
	print "[advmame]: config  /root/.advance/advmess.rc not found creating it..."
	copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/mame/advmess.rc.default"), "/root/.advance/advmess.rc")
