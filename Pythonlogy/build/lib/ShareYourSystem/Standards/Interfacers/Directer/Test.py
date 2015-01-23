#ImportModules
import ShareYourSystem
from ShareYourSystem.Standards.Classors.Representer import _print
from ShareYourSystem.Standards.Objects import Directer

Directer.DirecterClass().direct(
			lambda _LiargVariablesList,_FolderPathStr,_FileKeyStrsList:
			_print(_LiargVariablesList[0]+_FolderPathStr),
			["_FolderPathStr is "],
			**{'FolderingPathStr':'/'.join(ShareYourSystem.__file__.split('/')[:-1])}
		)
