
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.InserterClass
		}
	).set(
		'/&Models/$Things',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
			],
			'RowingGetStrsList':[
					'MyInt',
					'MyStr'
			]	
		}
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"hello",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/&Models/$Things',
		'#call:insert'
	)

#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.close()



"""
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
		),
		'hdf5 file is : '+MyController.hdfview()
	]
) 

#close
MyController.close()
"""
