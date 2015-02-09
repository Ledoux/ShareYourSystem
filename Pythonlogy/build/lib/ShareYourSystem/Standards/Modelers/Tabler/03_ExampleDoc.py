
#ImportModules
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'PymongoingDatabaseKeyStr':"Things",
			'FolderingPathStr':SYS.Tabler.LocalFolderPathStr
		}
	).collect(
		"Tablers",
		"Things",
		SYS.TablerClass()
	)

#Tabular in it
MyController['<Tablers>ThingsTabler'].table(
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#close
MyController.close()

