
#ImportModules
import ShareYourSystem as SYS

#Define
MyShower=SYS.ShowerClass(
	).array(
		[
			['-Views'],
			[
				{
					'#key':'|Foo',
					'#map@set':[
					]
				},
				{
					'#key':'|Fee',
					'#map@set':[
					]
				}
			]
		]
	).show()

#print
print('MyShower is ')
SYS._print(MyShower)

