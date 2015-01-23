#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Gatherer
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Gatherer.GathererClass.__dict__.items()))

#Print a version of this object
_print(Gatherer.GathererClass())

#Print a version of his __dict__
_print(Gatherer.GathererClass().__dict__)

#Test
print(Gatherer.attest_gather())