
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Retriever.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.RetrieverClass
		}
	).set(
		'/-Models/|Things',
		{
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
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"bonjour",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/-Models/|Things',
		[
			'#call:insert',
			(
				'retrieve',
				[
					#RetrievingIndexesList
					(0,1)
				]
			)
		]
	)
				
#Definition the AttestedStr
print('MyController is ')
SYS._print(MyController) 

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#Print
MyController.close()

