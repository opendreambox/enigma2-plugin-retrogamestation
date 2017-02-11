from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.stella = ConfigSubsection()
config.plugins.stella.romlocation = ConfigDirectory(default="/media")

class Stella(object):
	name = _("Stella")
	description = _("Atari 2600")
	location = config.plugins.stella.romlocation
	pattern = "^.*\.(bin|BIN)"
	cmd = "/usr/bin/stella-start"
	icon = "stella/stella.png"

emulators.append(EmulationHelper(Stella.name, Stella.description, Stella.cmd, pattern=Stella.pattern, romlocation=Stella.location, icon=Stella.icon))
