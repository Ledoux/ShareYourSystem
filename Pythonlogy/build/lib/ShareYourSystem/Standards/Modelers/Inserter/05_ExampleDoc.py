
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
		'/-Models/|Stuff',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyFloatsList','MyFloatsList',(tables.Float64Col,['UnitsInt']))
			],
			'RowingGetStrsList':[
					'MyInt',
					'MyFloatsList'
			]
		}
	)['#map@set'](
		{
			'MyInt':1,
			'MyFloatsList':[0.,1.,2.]
		}
	).command(
		'/-Models/|Stuff',
		'#call:insert'
	)


"""
	['#map@set'](
		{
			'MyInt':1,
			'MyStr':"ola",
			'MyFloatsList':[0,1]
		}
	).command(
		'/-Models/|Things',
		'#call:insert'
	)
"""

#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')


