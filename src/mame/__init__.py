from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.mame = ConfigSubsection()
config.plugins.retrogamestation.mame.romlocation = ConfigDirectory(default="/media/")

config.plugins.retrogamestation.mess = ConfigSubsection()
config.plugins.retrogamestation.mess.romlocation = ConfigDirectory(default="/media/")

class Mame(object):
	name = _("AdvanceMAME")
	description = _("Mame")
	location = config.plugins.retrogamestation.mame.romlocation
	pattern = "^.*\.(zip|ZIP)"
	cmd = "/usr/bin/advmame-start"
	icon = "mame/mame.png"

emulators.append(EmulationHelper(Mame.name, Mame.description, Mame.cmd, pattern=Mame.pattern, romlocation=Mame.location, icon=Mame.icon))

class MessEmulationHelperCart(EmulationHelper):
	def __init__(self, system, name, description, cmd, pattern=None, romlocation=None, icon=None):
		EmulationHelper.__init__(self, name, description, cmd, pattern=pattern, romlocation=romlocation, icon=icon)
		self._system = system

	def getRunCmd(self, rom=None):
		if rom:
			return "%s %s '%s';" % (self._cmd, self._system, rom)
		return ""

class MessNES(object):
	name = _("AdvanceMESS")
	description = _("Nintendo Entertainment System / Famicom")
	location = config.plugins.retrogamestation.mess.romlocation
	pattern = "^.*\.(zip|ZIP|nes)"
	cmd = "/usr/bin/advmess-start-cart"
	icon = "mame/mame.png"
	system = "nes"

emulators.append(MessEmulationHelperCart(MessNES.system, MessNES.name, MessNES.description, MessNES.cmd, pattern=MessNES.pattern, romlocation=MessNES.location, icon=MessNES.icon))

""" MAME INIT """
from os import path as os_path
from os import mkdir as os_mkdir
from os import system as os_system
if not os_path.exists("/root/.advance/advmame.rc"):
	print "[advmame]: config  /root/.advance/advmame.rc not found creating it..."
	os_system("/usr/bin/advmame --default")

