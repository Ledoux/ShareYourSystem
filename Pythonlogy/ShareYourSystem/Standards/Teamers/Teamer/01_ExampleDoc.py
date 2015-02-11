
#ImportModules
import ShareYourSystem as SYS

#Definition of a Familiarizer instance
MyFamiliarizer=SYS.FamiliarizerClass(
	).familiarize(
		'Children'
	).command(
		'Children',
		[
			(
				'parent',
				SYS.ApplyDictClass(
					{
						'LiargVariablesList':
						[
							'FirstChild',
							SYS.FamiliarizerClass()
						]
					}
				)
			)
		]
	)

MyFamiliarizer['*Things/$Stuff']=SYS.FamiliarizerClass()

#print
print('MyFamiliarizer is ')
SYS._print(MyFamiliarizer)

