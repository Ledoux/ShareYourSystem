
#ImportModules
import ShareYourSystem as SYS
import tables,operator

#Definition
MyController=SYS.ControllerClass(
		**{
			'PymongoingFileKeyStr':"Things",
			'FolderingPathStr':SYS.Findoer.LocalFolderPathStr
		}
	).collect(
	"Findoers",
	"Things",
	SYS.FindoerClass().update(
		[
			('Attr_RowingGetStrsList',['MyInt','MyStr','MyIntsList'])	
		]
	)
)

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,1])
			]
)['<Findoers>ThingsFindoer'].insert()

MyController.update(
			[
				('MyInt',2),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,1])
			]
)['<Findoers>ThingsFindoer'].insert()

MyController.update(
			[
				('MyInt',0),
				('MyStr',"bonjour"),
				('MyIntsList',[0,5,0])
			]
)['<Findoers>ThingsFindoer'].insert()

#Retrieve
MyController['<Findoers>ThingsFindoer'].find(
	{
		"MyInt":{"$in":[0,1]},
		'MyIntsList':[0,5,0]
	}
)
		
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
	]
) 

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#Print
MyController.close()


