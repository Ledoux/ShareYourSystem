#ImportModules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Shaper

#Print a version of the class
_print(dict(Shaper.ShaperClass.__dict__.items()))

#Print a version of this object
_print(Shaper.ShaperClass())

#Print a version of his __dict__
_print(Shaper.ShaperClass().__dict__)

#Test
print(Shaper.attest_flushWithShaping())

