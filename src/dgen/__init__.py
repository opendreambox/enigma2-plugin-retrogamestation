from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.dgen = ConfigSubsection()
config.plugins.dgen.romlocation = ConfigDirectory(default="/media")

class Dgen(object):
	name = _("Dgen")
	description = _("Sega Genesis")
	location = config.plugins.dgen.romlocation
	pattern = "^.*\.(MD|md|ZIP|zip|32x|32X)"
	cmd = "/usr/bin/dgen-start"
	icon = "dgen/dgen.png"

emulators.append(EmulationHelper(Dgen.name, Dgen.description, Dgen.cmd, pattern=Dgen.pattern, romlocation=Dgen.location, icon=Dgen.icon))
