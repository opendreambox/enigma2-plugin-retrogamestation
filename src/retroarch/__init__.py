from enigma import eEnv
from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.dgen = ConfigSubsection()
config.plugins.retrogamestation.dgen.romlocation = ConfigDirectory(default="/media/")

class RetroArch(EmulationHelper):
	name = _("RetroArch - Multi-System Emulation Frontend")
	description = _("RetroArch (www.retroarch.com)")
	location = None
	pattern = None
	cmd = eEnv.resolve("${bindir}/retroarch-start")
	icon = "retroarch/retroarch.svg"
	packageName = "retroarch"

emulators.append(RetroArch())
