#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Applyier
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Applyier.ApplyierClass.__dict__.items()))

#Print a version of this object
_print(Applyier.ApplyierClass())

#Print a version of his __dict__
_print(Applyier.ApplyierClass().__dict__)

#Test
_print(Applyier.attest_apply(),**{'RepresentingAlineaIsBool':False})