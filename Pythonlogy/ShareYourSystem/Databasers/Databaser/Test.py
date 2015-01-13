#ImportModules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Databaser

#Print a version of the class
_print(dict(Databaser.DatabaserClass.__dict__.items()))

#Print a version of this object
_print(Databaser.DatabaserClass())

#Print a version of his __dict__
_print(Databaser.DatabaserClass().__dict__)

#Test
_print(Databaser.attest_database())


