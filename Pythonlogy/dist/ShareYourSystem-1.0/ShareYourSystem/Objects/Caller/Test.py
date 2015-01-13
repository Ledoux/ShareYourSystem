#<ImportSpecificModules>
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Caller
#</ImportSpecificModules>

#Print a version of the class
_print(dict(Caller.CallerClass.__dict__.items()))

#Print a version of this object
_print(Caller.CallerClass())

#Print a version of his __dict__
_print(Caller.CallerClass().__dict__)

_print(Caller.CallerClass(**{
								'PackagingModuleVariableStr':"ShareYourSystem.Classors.Representer",
								'CallingFunctionStr':"_print"
							}).call())


_print(Caller.CallerClass(**{
								'PackagingModuleVariableStr':"ShareYourSystem.Classors.Inspecter",
								'CallingMethodStr':"inspect"
							}).call())


_print(Caller.CallerClass(**{
								'CallingVariable':Caller.CallerClass.call
							}).call())
