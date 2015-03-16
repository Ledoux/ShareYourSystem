
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr,
			'HdformatingFileKeyStr':'Thing1.hdf'
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelKeyStrsList':
			[	
				'MyStr',
				'MyIntsList'
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


