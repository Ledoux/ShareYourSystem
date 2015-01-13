#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Sharer
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Sharer.SharerClass.__dict__.items()))

#Print a version of this object
_print(Sharer.SharerClass())

#Print a version of his __dict__
_print(Sharer.SharerClass().__dict__)

#Test
print(Sharer.attest_share())


