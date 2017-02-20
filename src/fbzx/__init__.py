from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.fbzx = ConfigSubsection()
config.plugins.retrogamestation.fbzx.romlocation = ConfigDirectory(default="/media/")

class Fbzx(EmulationHelper):
	name = _("Fbzx")
	description = _("ZX Spectrum")
	location = config.plugins.retrogamestation.fbzx.romlocation
	pattern = "^.*\.(z80|Z80|SNA|sna|TAP|tap|TZX|tzx)"
	cmd = "/usr/bin/fbzx-start"
	icon = "fbzx/fbzx.png"
	packageName = "fbzx"

emulators.append(Fbzx())
