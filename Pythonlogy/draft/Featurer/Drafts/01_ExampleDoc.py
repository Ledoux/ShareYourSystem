
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Structurer
from ShareYourSystem.Modelers import Featurer

#Definition a structure with a db
ThingsStructurer=Structurer.StructurerClass(
).update(								
			[
				('MyInt',0),
				('MyStr',"hello"),
				('MyIntsList',[2,4,1]),
				('HdformatingFileKeyStr',"Things.hdf5"),
				(
					'<Database>ThingsFeaturer',
					Featurer.FeaturerClass().update(
						[
							('Attr_DatabasingSealTuplesList',
								[
									('MyInt','MyInt',tables.Int64Col()),
									('MyStr','MyStr',tables.StrCol(10)),
									('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
								]
							),
							('FeaturingAllBool',True)
						]
					)
				)
			]
).command(
	_UpdateList=[('insert',{'LiargVariablesList':[]})],
	**{'GatheringVariablesList':['<Database>ThingsFeaturer']}		
).update(
			[
				('MyInt',0),
				('MyStr',"hello"),
				('MyIntsList',[2,4,6])
			]
).command(
	_UpdateList=[('insert',{'LiargVariablesList':[]})],	
)
																	
#Definition the AttestedStr
SYS._attest(
	[
		'ThingsStructurer is '+SYS._str(
		ThingsStructurer,
		**{
			'RepresentingAlineaIsBool':False,
			'RepresentingBaseKeyStrsListBool':False
		}
		),
		'hdf5 file is : '+ThingsStructurer.hdfview().hdfclose().HdformatedConsoleStr
	]
)

#Print

