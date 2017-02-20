from ..Emulator import EmulationHelper
from ..plugin import emulators

class DosBox(EmulationHelper):
	name = _("DosBox")
	description = _("DOS (Disk Operating System)")
	location = None
	pattern = None
	cmd = "/usr/bin/dosbox-start"
	icon = "doxbox/doxbox.png"
	packageName = "dosbox"

emulators.append(DosBox())
