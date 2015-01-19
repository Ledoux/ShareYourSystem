
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer

#Definition a "graph" structure
MyStructurer=Structurer.StructurerClass().update(
	[
		(
			'<Graph>FirstChildStructurer',
			Structurer.StructurerClass().update(
			[
				('<Graph>GrandChildStructurer',
				Structurer.StructurerClass())
			])
		),
		(
			'<Graph>SecondChildStructurer',
			Structurer.StructurerClass().update(
			[
				('<Tree>OtherGrandChildStructurer',
				Structurer.StructurerClass())
			])
		)
	]	
).structure(
	['Graph','Tree'],
	**{
		'FolderingPathStr':Structurer.LocalFolderPathStr
	}
	).hdfclose()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyStructurer is '+SYS._str(
		MyStructurer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyStructurer.hdfview().HdformatedStr is '+MyStructurer.hdfview().HdformatedStr
	]
) 

#Print

