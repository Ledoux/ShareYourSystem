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
		'/-Models/|Things',
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
		'/-Models/|Things',
		'#call:insert'
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"bonjour",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/-Models/|Things',
		[
			'#call:insert',
			(
				'find',
				[
					[
						('MyInt',(SYS.operator.eq,1)),
						('MyIntsList',(SYS.getIsEqualBool,[0,0,1]))
					]
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

