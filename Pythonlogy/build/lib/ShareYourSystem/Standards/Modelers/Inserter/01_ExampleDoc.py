
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.InserterClass
		}
	).set(
		'/-Models/|Things',
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
		'/-Models/|Things',
		'#call:insert'
	)['#map@set'](
		{
			'MyInt':5,
			'MyStr':"bonjour",
			'MyIntsList':[0,0,1]
		}
	).command(
		'/-Models/|Things',
		'#call:insert'
	)
	
#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#print
print('MyController is ')
SYS._print(MyController)

#Print
MyController.process(_ActionStr='kill')



