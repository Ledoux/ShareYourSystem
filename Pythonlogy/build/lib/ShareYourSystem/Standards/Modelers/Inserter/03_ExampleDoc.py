
#ImportModules
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr
		}
	).collect(
		"Inserters",
		"Things",
		SYS.InserterClass().update(
		[
			('Attr_RowingGetStrsList',[
					'MyInt',
					'MyStr'
			])		
		]
	)
)

#Definition a structure with a db
MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[2,4,6])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],
	**{'GatheringVariablesList':['<Inserters>ThingsInserter']}		
).update(
			[
				('MyInt',0),
				('MyStr',"hello"),
				('MyIntsList',[0,0,0])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],		
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
		)
	]
) 

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))


