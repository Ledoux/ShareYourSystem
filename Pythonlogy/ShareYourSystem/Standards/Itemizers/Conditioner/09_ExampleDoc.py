
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
MyConditioner.MyInt=1
		
#the same but the condition is on the value
MyConditioner.set(
		"FirstStr",
		{
			'#value':"allo !",
			'#if':
			[
				('MyInt',SYS.operator.eq,1),
			]
		}
	)

#print
print('MyConditioner is')
SYS._print(MyConditioner)

