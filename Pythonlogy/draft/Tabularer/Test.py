#ImportModules
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Tabularer

#Print a version of the class
_print(dict(Tabularer.TabularerClass.__dict__.items()))

#Print a version of this object
_print(Tabularer.TabularerClass())

#Print a version of his __dict__
_print(Tabularer.TabularerClass().__dict__)

#Test
print(Tabularer.attest_tabular())