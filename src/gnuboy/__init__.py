from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.gnuboy = ConfigSubsection()
config.plugins.retrogamestation.gnuboy.romlocation = ConfigDirectory(default="/media/")

class Gnuboy(object):
	name = _("Gnuboy")
	description = _("GameBoy")
	location = config.plugins.retrogamestation.gnuboy.romlocation
	pattern = "^.*\.(gb|GB)"
	cmd = "/usr/bin/gnuboy-start"
	icon = "gnuboy/gnuboy.png"

emulators.append(EmulationHelper(Gnuboy.name, Gnuboy.description, Gnuboy.cmd, pattern=Gnuboy.pattern, romlocation=Gnuboy.location, icon=Gnuboy.icon))
