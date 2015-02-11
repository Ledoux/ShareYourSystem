
#ImportModules
import ShareYourSystem as SYS

#Definition a Getter
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
MyGetter.MyStr="hello"
		
#print
'''
print(
	'__getitem__ ["MyInt","MyStr"] returns '+str(
		MyGetter[
			SYS.MapListClass(['MyInt','MyStr'])
		]
	)
)
'''
print(
	map(
		lambda __GetKeyVariable:
		MyGetter.get(__GetKeyVariable).GettedValueVariable,
		['MyInt','MyStr']
		)
)



