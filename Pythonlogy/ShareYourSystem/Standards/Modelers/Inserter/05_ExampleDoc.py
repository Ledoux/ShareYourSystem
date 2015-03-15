
#ImportModules
import ShareYourSystem as SYS

#Define config
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr,
		}
	).set(
		'/-Models/|Stuff',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',SYS.tables.Int64Col()),
				('MyFloatsList','MyFloatsList',(SYS.tables.Float64Col,['UnitsInt']))
			],
			'RowingGetStrsList':[
					'MyInt',
					'MyFloatsList'
			]
		}
	).get('?v')


MyController['#map@set'](
		{
			'MyInt':1,
			'MyFloatsList':[0.,1.,2.]
		}
	).command(
		'/-Models/|Stuff',
		'#call:insert'
	)['#map@set'](
		{
			'MyInt':5,
			'MyFloatsList':[0.,0.]
		}
	).command(
		'/-Models/|Stuff',
		'#call:insert'
	)


#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')


