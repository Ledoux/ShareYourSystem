#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Adder
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Adder.AdderClass.__dict__.items()))

#Print a version of this object
_print(Adder.AdderClass())

#Print a version of his __dict__
_print(Adder.AdderClass().__dict__)

#Test
_print(Adder.attest_add(),**{'RepresentingAlineaIsBool':False})