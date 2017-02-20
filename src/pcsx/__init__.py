from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.pcsx = ConfigSubsection()
config.plugins.retrogamestation.pcsx.romlocation = ConfigDirectory(default="/media/")

class Pcsx(EmulationHelper):
	name = _("Pcsx")
	description = _("Playstation One")
	location = config.plugins.retrogamestation.pcsx.romlocation
	pattern = "^.*\.(bin|img|mdf|iso|cue|z|bz|znx|pbp|cbn|exe)"
	cmd = "/usr/bin/pcsx-start"
	icon = "pcsx/pcsx.png"
	packageName = "pcsx"

emulators.append(Pcsx())
