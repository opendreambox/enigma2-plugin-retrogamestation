from Components.config import config, ConfigSubsection, ConfigDirectory

from ..Emulator import EmulationHelper
from ..plugin import emulators

config.plugins.retrogamestation.gngeo = ConfigSubsection()
config.plugins.retrogamestation.gngeo.romlocation = ConfigDirectory(default="/media/")

class GnGeo(EmulationHelper):
	name = _("GnGeo")
	description = _("NeoGeo")
	location = config.plugins.retrogamestation.gngeo.romlocation
	pattern = "^.*\.(zip|ZIP)"
	cmd = "/usr/bin/gngeo-start"
	icon = "gngeo/gngeo.png"
	packageName = "gngeo"

emulators.append(GnGeo())

""" INIT """
from os import path as os_path, mkdir as os_mkdir
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile
if not os_path.exists("/root/.gngeo/gngeorc"):
	print "[gngeo]: config  /root/.gngeo/gngeorc not found creating defaults..."
	if not os_path.exists("/root/.gngeo"):
		os_mkdir("/root/.gngeo")
	if not os_path.exists("/root/.gngeo/roms"):
		os_mkdir("/root/.gngeo/roms")
	if not os_path.exists("/root/.gngeo/bios"):
		os_mkdir("/root/.gngeo/bios")
	copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/RetroGameStation/gngeo/gngeorc.default"), "/root/.gngeo/gngeorc")