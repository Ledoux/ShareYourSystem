#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Walker
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Walker.WalkerClass.__dict__.items()))

#Print a version of this object
_print(Walker.WalkerClass())

#Print a version of his __dict__
_print(Walker.WalkerClass().__dict__)

#Test
_print(Walker.attest_walk(),**{'RepresentingAlineaIsBool':False})