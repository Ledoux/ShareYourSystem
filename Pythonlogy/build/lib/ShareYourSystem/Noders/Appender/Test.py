#ImportModules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Appender

#Print a version of the class
_print(dict(Appender.AppenderClass.__dict__.items()))

#Print a version of this object
_print(Appender.AppenderClass())

#Print a version of his __dict__
_print(Appender.AppenderClass().__dict__)

#Test
_print(Appender.attest_append(),**{'RepresentingAlineaIsBool':False})