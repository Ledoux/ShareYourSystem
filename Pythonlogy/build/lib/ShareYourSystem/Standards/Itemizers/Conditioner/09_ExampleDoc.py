
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
MyConditioner.MyInt=1
		
#set but condition not satisfied
MyConditioner.set(
		{
			'SetKeyVariable':"FirstStr",
			'#if':
			[
				('MyInt',SYS.operator.eq,2),
			]
		},
		"hello"
	)

#set with condition satisfied
MyConditioner.set(
		{
			'#set':"SecondStr",
			'#if':
			[
				('MyInt',SYS.operator.eq,1),
			]
		},
		"bonjour"
	)

#the same but the condition is on the value
MyConditioner.set(
		"ThirdStr",
		{
			'#set':"allo !",
			'#if':
			[
				('MyInt',SYS.operator.eq,1),
			]
		}
	)

#print
print('MyConditioner is')
SYS._print(MyConditioner)

