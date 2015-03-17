
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Findoer.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.FindoerClass
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelKeyStrsList':
			[
				'MyInt',
				'MyStr',
				'MyIntsList'
			],
			'RowingKeyStrsList':[
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
			'MyInt':5,
			'MyStr':"bonjour",
			'MyIntsList':[0,0,1]
		}
	).command(
		'/-Models/|Thing',
		[
			'#call:insert',
			(
				'find',
				[
					#FindingWhereVariable
					{
						'MyInt':{'$gt':1},
						'MyIntsList':[0,0,1]
					}
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


