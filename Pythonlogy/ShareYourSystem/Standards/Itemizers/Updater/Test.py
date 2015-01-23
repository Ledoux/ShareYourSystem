#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Updater
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Updater.UpdaterClass.__dict__.items()))

#Print a version of this object
_print(Updater.UpdaterClass())

#Print a version of his __dict__
_print(Updater.UpdaterClass().__dict__)

#Test
_print(Updater.attest_update(),**{'RepresentingAlineaIsBool':False})
