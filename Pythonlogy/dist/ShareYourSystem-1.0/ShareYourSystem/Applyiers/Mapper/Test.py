#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Mapper
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Mapper.MapperClass.__dict__.items()))

#Print a version of this object
_print(Mapper.MapperClass())

#Print a version of his __dict__
_print(Mapper.MapperClass().__dict__)

#Test
_print(Mapper.attest_map(),**{'RepresentingAlineaIsBool':False})