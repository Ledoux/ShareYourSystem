#ImportModules
import ShareYourSystem as SYS
import collections

#Define and set child setters in a child dict
MySetter=SYS.SetterClass(
	)['array*set'](
		[['A','B'],['1','2'],['a','b']],
		[
			#for the A, B all set
			SYS.SetterClass(),
			#for 1 and 2 each set
			[
				{
					'MyInt':0
				},
				{
					'MyStr':"hello"
				}
			],
			#default SetterClass all set
			None
		]
	)


#print
print('MySetter is ')
SYS._print(MySetter)
