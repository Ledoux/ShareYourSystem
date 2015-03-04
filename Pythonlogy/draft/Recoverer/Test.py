#ImportModules
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Recoverer

#Print a version of the class
_print(dict(Recoverer.RecovererClass.__dict__.items()))

#Print a version of this object
_print(Recoverer.RecovererClass())

#Print a version of his __dict__
_print(Recoverer.RecovererClass().__dict__)

#Test
print(Recoverer.attest_find())
