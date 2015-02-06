
#ImportModules
import ShareYourSystem as SYS

#Definition a "graph" structure
MyStructurer=SYS.StructurerClass().update(
	[
		(
			'<Graph>FirstChildStructurer',
			SYS.StructurerClass().update(
			[
				('<Graph>GrandChildStructurer',
				SYS.StructurerClass())
			])
		),
		(
			'<Graph>SecondChildStructurer',
			SYS.StructurerClass().update(
			[
				('<Tree>OtherGrandChildStructurer',
				SYS.StructurerClass())
			])
		)
	]	
).structure(
	['Graph','Tree'],
	**{
		'FolderingPathStr':SYS.Structurer.LocalFolderPathStr
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
		'MyStructurer.hdfview().HdformatedConsoleStr is '+MyStructurer.hdfview(
			).HdformatedConsoleStr
	]
) 

#Print

