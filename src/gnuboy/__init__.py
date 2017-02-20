from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.gnuboy = ConfigSubsection()
config.plugins.retrogamestation.gnuboy.romlocation = ConfigDirectory(default="/media/")

class Gnuboy(EmulationHelper):
	name = _("Gnuboy")
	description = _("GameBoy")
	location = config.plugins.retrogamestation.gnuboy.romlocation
	pattern = "^.*\.(gb|GB)"
	cmd = "/usr/bin/gnuboy-start"
	icon = "gnuboy/gnuboy.png"
	packageName = "gnuboy"

emulators.append(Gnuboy())
