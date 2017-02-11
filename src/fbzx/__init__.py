from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.fbzx = ConfigSubsection()
config.plugins.fbzx.romlocation = ConfigDirectory(default="/media")

class Fbzx(object):
	name = _("Fbzx")
	description = _("ZX Spectrum")
	location = config.plugins.fbzx.romlocation
	pattern = "^.*\.(z80|Z80|SNA|sna|TAP|tap|TZX|tzx)"
	cmd = "/usr/bin/fbzx-start"
	icon = "fbzx/fbzx.png"

emulators.append(EmulationHelper(Fbzx.name, Fbzx.description, Fbzx.cmd, pattern=Fbzx.pattern, romlocation=Fbzx.location, icon=Fbzx.icon))
