#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Moduler
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Moduler.ModulerClass.__dict__.items()))

#Print a version of this object
_print(Moduler.ModulerClass())

#Print a version of his __dict__
_print(Moduler.ModulerClass().__dict__)

#Get a module in the instance
print(Moduler.ModulerClass(**{"PackagingModuleVariableStr":"ShareYourSystem.Standards.Classors.Inspecter"}).module())


