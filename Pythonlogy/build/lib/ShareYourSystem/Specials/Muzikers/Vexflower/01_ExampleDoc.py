
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Structurer

#Definition a "graph" structure
MyStructurer=Structurer.StructurerClass().update(
	[
		(
			'<Graph>ChildStructurer1',
			Structurer.StructurerClass().update(
			[
				('<Graph>GrandChildStructurer1',
				Structurer.StructurerClass())
			])
		),
		(
			'<Graph>ChildStructurer2',
			Structurer.StructurerClass()
		)
	]	
).structure(**{
					'HdformatingFileKeyStr':'MyStructurer.hdf5',
					'ParentingNodeStr':'Graph'
			}).hdfclose()
		
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

