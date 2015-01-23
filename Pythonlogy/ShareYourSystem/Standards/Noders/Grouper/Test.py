#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Grouper
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Grouper.GrouperClass.__dict__.items()))

#Print a version of this object
_print(Grouper.GrouperClass())

#Print a version of his __dict__
_print(Grouper.GrouperClass().__dict__)

#Test
_print(Grouper.attest_group(),**{'RepresentingAlineaIsBool':False})