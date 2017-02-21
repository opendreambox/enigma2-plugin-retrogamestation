from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.quake = ConfigSubsection()
config.plugins.retrogamestation.quake.romlocation = ConfigDirectory(default="/media/")

class Quake(EmulationHelper):
	fileMode = False
	name = _("sdlquake")
	description = _("Quake")
	location = config.plugins.retrogamestation.quake.romlocation
	pattern = "^.*\.(wad|WAD)"
	cmd = "/usr/bin/quake-start"
	icon = "quake/quake.svg"
	packageName = "sdlquake"

emulators.append(Quake())

