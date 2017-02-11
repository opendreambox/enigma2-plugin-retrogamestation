AC_INIT([enigma2-plugin-extensions-retrogamestation], [0.1.0], [reichi@opendreambox.org])
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])

# Silent rules are available since 1.11, but older versions
# are still in use. So don't use them unconditionally.
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE

m4_ifdef([LT_INIT], [LT_INIT], [AC_PROG_LIBTOOL])
AC_CONFIG_MACRO_DIR([m4])

AM_PATH_PYTHON

AC_CONFIG_FILES([
Makefile
script/Makefile
src/Makefile
src/dgen/Makefile
src/dosbox/Makefile
src/fbzx/Makefile
src/gngeo/Makefile
src/gnuboy/Makefile
src/mame/Makefile
src/pcsx/Makefile
src/scummvm/Makefile
src/snes/Makefile
src/stella/Makefile
src/vice/Makefile
])
AC_OUTPUT

