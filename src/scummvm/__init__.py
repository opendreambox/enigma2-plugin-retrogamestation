from ..Emulator import EmulationHelper
from ..plugin import emulators

class ScummVM(object):
	name = _("ScummVM")
	description = _("ScummVM")
	location = None
	pattern = None
	cmd = "/usr/bin/scummvm-start;"
	icon = "summvm/scummvm.png"

emulators.append(EmulationHelper(ScummVM.name, ScummVM.description, ScummVM.cmd))
