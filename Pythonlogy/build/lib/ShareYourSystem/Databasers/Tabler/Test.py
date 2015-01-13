#ImportModules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Tabler

#Print a version of the class
_print(dict(Tabler.TablerClass.__dict__.items()))

#Print a version of this object
_print(Tabler.TablerClass())

#Print a version of his __dict__
_print(Tabler.TablerClass().__dict__)

#Test
print(Tabler.attest_table())