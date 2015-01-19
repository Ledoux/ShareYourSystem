#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Guiders import Documenter

#Definition a Documenter instance
MyDocumenter=Documenter.DocumenterClass().document(
	map(
			lambda __BaseClass:
			__BaseClass.__module__.replace('.','/'),
			SYS.reverse(SYS.FilerClass.__mro__)[1:]
		)
	#_AllBool=True	
)