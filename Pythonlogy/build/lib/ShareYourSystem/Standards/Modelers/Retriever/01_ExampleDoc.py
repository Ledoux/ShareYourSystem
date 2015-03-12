
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Retriever.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.RetrieverClass
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelKeyStrsList':[
				'MyInt',
				'MyStr',
				'MyIntsList'
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
		'/-Models/|Thing',
		'#call:insert'
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"bonjour",
			'MyIntsList':[0,0,0]
		}
	).command(
		'/-Models/|Thing',
		[
			'#call:insert',
			(
				'retrieve',
				[
					#RetrievingIndexesList
					(0,0)
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
MyController.file(_ModeStr='c')
