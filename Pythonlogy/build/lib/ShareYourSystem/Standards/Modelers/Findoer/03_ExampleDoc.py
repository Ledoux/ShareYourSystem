#ImportModules
import ShareYourSystem as SYS
import tables

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Findoer.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.FindoerClass
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
			],
			'RowingKeyStrsList':[
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
		'/-Models/|Thing',
		'#call:insert'
	)['#map@set'](
		{
			'MyInt':5,
			'MyStr':"bonjour",
			'MyIntsList':[0,0,1]
		}
	).command(
		'/-Models/|Thing',
		[
			'#call:insert',
			(
				'find',
				[
					#FindingWhereVariable
					[
						('MyInt',(SYS.operator.eq,0)),
						('MyIntsList',(SYS.getIsEqualBool,[2,4,1]))
					],
					#FindingRecoverBool
					True
				]
			)
		]
	)


#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')

