#ImportModules
import ShareYourSystem as SYS

#Define and condition
MyConditioner=SYS.ConditionerClass(
			).condition(
				#ConditioningTestVariable
				3,
				#ConditioningGetBoolFunction
				lambda _TestVariable,_AttestVariable:_TestVariable==_AttestVariable,
				#ConditioningAttestVariable
				2
			)

#print
print('MyConditioner is ')
SYS._print(MyConditioner)

#print
print('MyConditioner.condition(2).ConditionedIsBool is ')
SYS._print(MyConditioner.condition(2).ConditionedIsBool)
