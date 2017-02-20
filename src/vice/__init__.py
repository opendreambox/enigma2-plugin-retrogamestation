from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Language import language

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.vice = ConfigSubsection()
config.plugins.retrogamestation.vice.romlocation = ConfigDirectory(default="/media/")

class Vice(EmulationHelper):
	name = _("Vice")
	description = _("Commodore C64")
	location = config.plugins.retrogamestation.vice.romlocation
	pattern = "^.*\.(d64|D64|t64|T64|crt|CRT|P00|p00|g64|G64|p64|P64|d67|D67|d71|D71|d81|D81|d80|D80|d82|D82|d1m|D1M|d2m|D2M|d4,|D4M|tap|TAP)"
	cmd = "/usr/bin/vice-start"
	icon = "vice/vice.png"
	packageName = "vice"

emulators.append(Vice())
