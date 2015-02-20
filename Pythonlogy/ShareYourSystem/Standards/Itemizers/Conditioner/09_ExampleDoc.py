
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
MyConditioner.MyInt=1
		
#set but condition not satisfied
MyConditioner.set(
		{
			'SetKeyVariable':"FirstStr",
			'ConditionTuplesList':
			[
				('MyInt',SYS.operator.eq,2),
			]
		},
		"hello"
	)

#set with condition satisfied
MyConditioner.set(
		{
			'SetKeyVariable':"SecondStr",
			'ConditionTuplesList':
			[
				('MyInt',SYS.operator.eq,1),
			]
		},
		"bonjour"
	)

#print
print('MyConditioner is')
SYS._print(MyConditioner)

