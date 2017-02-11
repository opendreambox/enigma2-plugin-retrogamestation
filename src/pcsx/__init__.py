from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.pcsx = ConfigSubsection()
config.plugins.pcsx.romlocation = ConfigDirectory(default="/media")

class Pcsx(object):
	name = _("Pcsx")
	description = _("Playstation One")
	location = config.plugins.pcsx.romlocation
	pattern = "^.*\.(bin|img|mdf|iso|cue|z|bz|znx|pbp|cbn|exe)"
	cmd = "/usr/bin/pcsx-start"
	icon = "pcsx/pcsx.png"

emulators.append(EmulationHelper(Pcsx.name, Pcsx.description, Pcsx.cmd, pattern=Pcsx.pattern, romlocation=Pcsx.location, icon=Pcsx.icon))
