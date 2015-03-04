
#ImportModules
import ShareYourSystem as SYS
import tables

SYS._print(SYS.ShaperClass.SwitchedMethodDict)

"""
#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Shaper.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.ShaperClass
		}
	).set(
		'/-Models/|Things',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',(tables.Int64Col,['UnitsInt']))
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
	)
"""

"""
	['#map@set'](
		{
			'MyInt':1,
			'MyStr':"ola",
			'MyIntsList':[0,1]
		}
	).command(
		'/-Models/|Things',
		'#call:insert'
	)
"""

"""
#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')

"""
