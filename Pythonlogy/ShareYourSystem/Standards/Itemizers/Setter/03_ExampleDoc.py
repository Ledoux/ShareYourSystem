#ImportModules
import ShareYourSystem as SYS

#Define and set
MySetter=SYS.SetterClass()

'''
MySetter.set(
		SYS.MapListClass(
			[
				('MyInt',0),
				('MyStr',"hello")
			]
		)
	)
'''

#
map(
		lambda __SetTuple:
		MySetter.set(*__SetTuple),
		[
			('MyInt',0),
			('MyStr',"hello")
		]
	)

#print
print('MySetter is ')
SYS._print(MySetter)
