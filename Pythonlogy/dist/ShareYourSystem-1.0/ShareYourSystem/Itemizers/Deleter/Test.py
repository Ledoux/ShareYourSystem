#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Deleter
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Deleter.DeleterClass.__dict__.items()))

#Print a version of this object
_print(Deleter.DeleterClass())

#Print a version of his __dict__
_print(Deleter.DeleterClass().__dict__)

#Test
print(Deleter.attest_delete())