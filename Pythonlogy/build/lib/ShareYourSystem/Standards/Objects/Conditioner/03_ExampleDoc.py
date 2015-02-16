#ImportModules
import ShareYourSystem as SYS

#Define and condition
MyConditioner=SYS.ConditionerClass(
			).condition(
				#ConditioningTestVariable
				'MyInt',
				#ConditioningGetBoolFunction
				lambda _TestVariable,_AttestVariable:_TestVariable==_AttestVariable,
				#ConditioningAttestVariable
				2,
				#ConditioningInstanceVariable
				{'MyInt':3}
			)

#print
print('MyConditioner is ')
SYS._print(MyConditioner)

#print
print('MyConditioner.condition(type,_AttestVariable=dict) is ')
SYS._print(MyConditioner.condition(type,_AttestVariable=dict))