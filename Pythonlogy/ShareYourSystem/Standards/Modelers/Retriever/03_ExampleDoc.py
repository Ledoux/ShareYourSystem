
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'PymongoingFileKeyStr':"Things",
			'FolderingPathStr':SYS.Retriever.LocalFolderPathStr
		}
	).collect(
	"Retrievers",
	"Things",
	SYS.RetrieverClass().update(
		[
			('Attr_RowingGetStrsList',['MyInt'])	
		]
	)
)

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[2,4,6])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],	
	**{'GatheringVariablesList':['<Retrievers>ThingsRetriever']}		
).update(
			[
				('MyInt',0),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,0])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],	
)


#Retrieve
MyController['<Retrievers>ThingsRetriever'].__setitem__(
	'RetrievingIndexesList',(0,1)
).retrieve()
					
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

#Print
MyController.close()

