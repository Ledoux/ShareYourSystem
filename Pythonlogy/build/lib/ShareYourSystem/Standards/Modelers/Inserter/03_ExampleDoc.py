
#ImportModules
import ShareYourSystem as SYS

#Define config
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr,
			'HdformatingFileKeyStr':'ThingAndStuff.hdf5'
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyStr','MyStr',SYS.tables.StringCol(10)),
				('MyIntsList','MyIntsList',SYS.tables.Int64Col(shape=3))
			],
			'RowingKeyStrsList':[
					'MyStr',
					'MyIntsList'
			]	
		}
	).get('?v')

#insert
MyController['#map@set'](
		{
			'MyStr':"hello",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/-Models/|Thing',
		'#call:insert'
	)['#map@set'](
		{
			'MyStr':"bonjour",
			'MyIntsList':[0,0,1]
		}
	).command(
		'/-Models/|Thing',
		'#call:insert'
	)

#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')



