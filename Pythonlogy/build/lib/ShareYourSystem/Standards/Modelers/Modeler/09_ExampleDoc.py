
#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.ClasserClass()
class MakerClass(SYS.ControllerClass):

	def default_init(self,
			_MakingMyIntsList={
							'DefaultValueType':property,
							'PropertyInitVariable':None,
							'PropertyDocStr':'I am doing the thing here',
							'ShapeKeyStrsList':['MakingMyInt']
						},
			_MakingMyInt=3,
			_MadeMyInt=0	
		):
		SYS.ControllerClass.__init__(self)

#Definition 
MyMaker=MakerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr,
			'HdformatingFileKeyStr':'Thing2.hdf'
		}
	).set(
		'/-Models/|Thing',
		[
			('ModelKeyStrsList',['MyStr','MakingMyIntsList'])	
		]
	).get('?v')

#Build a structure with a database
SYS.mapSet(
		MyMaker['/-Models/|Thing'].ModeledHdfTable,
		[
			('row.__setitem__',{'#liarg':('MyStr',"hello")}),
			('row.append',{'#liarg':None}),
			('flush',{'#liarg':None})
		]
)

#print
print('MyMaker is ')
SYS._print(MyMaker)

#view
print('hdf5 file is : \n'+SYS._str(MyMaker.hdfview()))

#close
MyMaker.file(_ModeStr='c')





