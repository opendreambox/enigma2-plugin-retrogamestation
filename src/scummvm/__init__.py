from ..Emulator import EmulationHelper
from ..plugin import emulators

class ScummVM(EmulationHelper):
	name = _("ScummVM")
	description = _("ScummVM")
	location = None
	pattern = None
	cmd = "/usr/bin/scummvm-start;"
	icon = "scummvm/scummvm.png"
	packageName = "scummvm"

emulators.append(ScummVM())
