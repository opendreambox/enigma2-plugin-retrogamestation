from ..Emulator import EmulationHelper
from ..plugin import emulators

class DosBox(object):
	name = _("DosBox")
	description = _("DOS (Disk Operating System)")
	location = None
	pattern = None
	cmd = "/usr/bin/dosbox-start"
	icon = "doxbox/doxbox.png"

emulators.append(EmulationHelper(DosBox.name, DosBox.description, DosBox.cmd, icon=DosBox.icon))
