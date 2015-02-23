#ImportModules
import ShareYourSystem as SYS

#Define and map set with a dict
MySetter=SYS.SetterClass(
	)['#map:set'](
		{
			'MyInt':0,
			'MyStr':"hello"
		}
	)

#Define and map set with a tuples list
MySetter['#map:set'](
		[
			('MyFloat',2.),
			('MyBool',False)
		]
	)

#Define and map set 
MySetter['#map:set']={
			'FirstObject':SYS.ObjectClass(),
			'SecondObject':SYS.ObjectClass()
		}

#Set a map set
MySetter.set(
		'#map:set',
		{
			'FirstInt':1,
			'SecondInt':2
		}
	)

#mapset a mapset
MySetter['#map:set'](
	[
		(
			'#map:set',
			{
				'FirstFloat':4.,
				'SecondFloat':5.
			}
		)
	]
)

#print
print('MySetter is ')
SYS._print(MySetter)
