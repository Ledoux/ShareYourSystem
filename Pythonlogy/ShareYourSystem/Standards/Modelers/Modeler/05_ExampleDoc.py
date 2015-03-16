
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr,
			'HdformatingFileKeyStr':'Thing2.hdf'
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelingDescriptionTuplesList':
			[
				#GetStr #ColumnStr #Col
				('MyStr','MyStr',SYS.tables.StringCol(10)),
				('MyIntsList','MyIntsList',SYS.tables.Int64Col(shape=3))
			]	
		}
	).get('?v')

#Build a structure with a database
SYS.mapSet(
		MyController['/-Models/|Thing'].ModeledHdfTable,
		[
			('row.__setitem__',{'#liarg':('MyStr',"hello")}),
			('row.append',{'#liarg':None}),
			('flush',{'#liarg':None})
		]
)

#Definition the AttestedStr
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')


