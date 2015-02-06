
#ImportModules
import tables
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass().collect(
	"Databasers",
	"Things",
	SYS.DatabaserClass()
)

#Definition a Databaser instance
MyController['<Databasers>ThingsDatabaser'].database([
		#GetStr #ColumnStr #Col
		('MyInt','MyInt',tables.Int64Col()),
		('MyStr','MyStr',tables.StringCol(10)),
		('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
])
							
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyController["<Databasers>ThingsDatabaser"].DatabasedModelClass.__dict__ is '+SYS._str(
		dict(MyController['<Databasers>ThingsDatabaser'].DatabasedModelClass.__dict__.items()
			) if MyController['<Databasers>ThingsDatabaser'
		].DatabasedModelClass!=None else {},**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

