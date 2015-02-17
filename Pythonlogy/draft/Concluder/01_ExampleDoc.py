
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance Concluder and make it print hello
MyConcluder=SYS.ConcluderClass(
	).conclude(
		#ConcludingTestVariable
		{'MyColorStr':'Black','MySuperInt':6},
		#ConcludingConditionTuplesList
		[
			(type,SYS.operator.eq,dict),
			('MyColorStr',SYS.operator.eq,"Black"),
			('MySuperInt',SYS.operator.gt,3),
			(1,SYS.operator.eq,1)
		]
	)
		
#Definition the AttestedStr
print('MyConcluder is ')
SYS._print(MyConcluder)


	

