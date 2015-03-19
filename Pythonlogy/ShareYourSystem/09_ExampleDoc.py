
#ImportModules
import ShareYourSystem as SYS

#print
print('The translate gives')
print(
	SYS.translate(
		"#BonjourStr Erwan #EndStr",
		{
			'#BonjourStr':'Salut',
			'#EndStr':'!'
		}
	)
)


#print
print('\nThe replace gives')
print(
	SYS.replace(
		{
			'MyStr':"#BonjourStr Erwan #EndStr",
			'MyInt':'#MyInt',
			'MyTotalInt':'#get:>>#MyInt+2',
			'MyDict':{
				'MyStr':'#BonjourStr'
			}
		},
		{
			'#BonjourStr':'Salut',
			'#EndStr':'!',
			'#MyInt':1
		},
		SYS.PointerClass()
	)
)


#print
print('\nThe mapReplace gives')
SYS._print(
	SYS.mapReplace(
			{
				'MyStr':"#BonjourStr Erwan #EndStr",
				'MyInt':'#MyInt',
				'MyTotalInt':'#get:>>#MyInt+2',
				'MyDict':{
					'MyStr':'#BonjourStr'
					}
			},
			[
				['#BonjourStr','#EndStr','#MyInt'],
				[
					['Salut','!',1],
					['Hello','?',5]
				]
			],
			SYS.PointerClass()
		)
	)



