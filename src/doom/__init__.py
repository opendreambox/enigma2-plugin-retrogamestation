from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.doom = ConfigSubsection()
config.plugins.retrogamestation.doom.romlocation = ConfigDirectory(default="/media/")

class CrispyDoom(EmulationHelper):
	name = _("Crispy Doom")
	description = _("DOOM")
	location = config.plugins.retrogamestation.dgen.romlocation
	pattern = "^.*\.(wad|WAD)"
	cmd = "/usr/bin/crispy-doom-start"
	icon = "doom/doom.svg"
	packageName = "crispy-doom"

emulators.append(CrispyDoom())
