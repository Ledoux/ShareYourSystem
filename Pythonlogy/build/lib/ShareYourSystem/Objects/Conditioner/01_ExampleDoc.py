#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Conditioner

#Definition of an instance Conditioner and make it print hello
MyConditioner=Conditioner.ConditionerClass(**{
		'ConditioningGetBoolFunction':lambda _TestVariable,_AttestVariable:_TestVariable==_AttestVariable,
		'ConditioningAttestVariable':2
	})
MyConditioner.condition(3).ConditionedIsBool
		
#Definition the AttestedStr
SYS._attest(
					[
						'MyConditioner.condition(3).ConditionedIsBool is '+str(
							MyConditioner.condition(3).ConditionedIsBool),
						'MyConditioner.condition(2).ConditionedIsBool is '+str(
							MyConditioner.condition(2).ConditionedIsBool)
					]
				) 

#Print

