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
	cmd = "/usr/bin/mame-start"
	icon = "mame/mame.png"

emulators.append(EmulationHelper(Mame.name, Mame.description, Mame.cmd, pattern=Mame.pattern, romlocation=Mame.location, icon=Mame.icon))

class Mess(object):
	name = _("AdvanceMESS")
	description = _("Multiple System Emulator")
	location = config.plugins.retrogamestation.mess.romlocation
	pattern = "^.*\.(zip|ZIP)"
	cmd = "/usr/bin/mess-start"
	icon = "mame/mame.png"

emulators.append(EmulationHelper(Mess.name, Mess.description, Mess.cmd, pattern=Mess.pattern, romlocation=Mess.location, icon=Mess.icon))

""" MAME INIT """
from os import path as os_path
from os import mkdir as os_mkdir
from os import system as os_system
if not os_path.exists("/root/.advance/advmame.rc"):
	print "[advmame]: config  /root/.advance/advmame.rc not found creating it..."
	os_system("/usr/bin/advmame --default")

