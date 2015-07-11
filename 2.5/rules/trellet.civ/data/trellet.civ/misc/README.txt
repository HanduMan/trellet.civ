Trellet.civ ruleset includes a custom nation (Mordor). To display the flaming eye flag in-game the freeciv client installed files in ../data/misc directory must be modified as follows.

flags.spec - add the following line to the end of file:
*include "trellet.civ/misc/flags.spec"

flags-large.spec - add the following line to the end of file:
*include "trellet.civ/misc/flags-large.spec"

shields.spec - add the following line to the end of file:
*include "trellet.civ/misc/shields.spec"

shields-large.spec - add the following line to the end of file:
*include "trellet.civ/misc/shields-large.spec"
