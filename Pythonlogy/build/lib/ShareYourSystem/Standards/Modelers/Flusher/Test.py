#ImportModules
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Flusher

#Print a version of the class
_print(dict(Flusher.FlusherClass.__dict__.items()))

#Print a version of this object
_print(Flusher.FlusherClass())

#Print a version of his __dict__
_print(Flusher.FlusherClass().__dict__)

#Test
_print(Flusher.attest_flush())
