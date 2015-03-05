
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredispiker=SYS.PredispikerClass(
	).predispike(
		#PredispikingRateUnitsInt
		5,
		#PredispikingSensorUnitsInt
		1,
		#PredispikingPerturbativeMeanWeightFloat
		0.01
	)

#print
print('MyPredispiker is')
SYS._print(MyPredispiker)

