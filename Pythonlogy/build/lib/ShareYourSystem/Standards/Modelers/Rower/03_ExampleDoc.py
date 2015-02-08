
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass().collect(
	"Rowers",
	"Things",
	SYS.RowerClass().update(
		[
			('Attr_RowingGetStrsList',['MyInt'])	
		]
	)
)

#Tabular in it
MyController.update(								
[
	('MyInt',0),
	('MyStr',"hello"),
	('MyIntsList',[2,4,1])
])['<Rowers>ThingsRower'].row()
	


#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#print
print('mongo db is : \n'+MyController.pymongoview().PymongoneViewStr)

#Print
MyController.close()

#Print

