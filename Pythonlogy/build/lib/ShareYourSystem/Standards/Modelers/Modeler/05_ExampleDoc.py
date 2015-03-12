
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.ModelerClass
		}
	)['#map@set'](
		[
			('UnitsInt',3),
			('/-Models/|Stuff',
			{
				'ModelingDescriptionTuplesList':
				[
					#GetStr #ColumnStr #Col
					('MyInt','MyInt',tables.Int64Col()),
					('MyFloatsList','MyFloatsList',(tables.Float64Col,['UnitsInt']))
				]
			})
		]
	)

#Build a structure with a database
SYS.mapSet(
		MyController['/-Models/|Stuff'].ModeledHdfTable,
		[
			('row.__setitem__',{'#liarg':('MyFloatsList',[0.,1.,2.])}),
			('row.append',{'#liarg':None}),
			('flush',{'#liarg':None})
		]
)


#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.ModelerClass
		}
	)['#map@set'](
		[
			('UnitsInt',2),
			('/-Models/|Stuff',
			{
				'ModelingDescriptionTuplesList':
				[
					#GetStr #ColumnStr #Col
					('MyInt','MyInt',tables.Int64Col()),
					('MyFloatsList','MyFloatsList',(tables.Float64Col,['UnitsInt']))
				]
			})
		]
	)

#Build a structure with a database
SYS.mapSet(
		MyController['/-Models/|Stuff'].ModeledHdfTable,
		[
			('row.__setitem__',{'#liarg':('MyFloatsList',[0,0])}),
			('row.append',{'#liarg':None}),
			('flush',{'#liarg':None})
		]
)


#print
print('MyController is ')
SYS._print(MyController)

#view
print('hdf5 file is : \n'+SYS._str(MyController.hdfview()))

#close
MyController.file(_ModeStr='c')


