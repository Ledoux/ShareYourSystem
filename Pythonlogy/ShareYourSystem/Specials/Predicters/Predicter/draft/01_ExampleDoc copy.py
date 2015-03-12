
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredicter=SYS.PredicterClass(
	).predict(
		#PredictingUnitsInt
		10,
		#PredictingSensorsInt
		1,
		#PredictingDecoderWeightFloat
		10.,
		#PredictingCostFloat
		0.,
		#PredictingNormalisationInt
		0.5,
		#PredictingPerturbativeWeightFloat
		0.1
	)

#print
print('MyPredicter is')
SYS._print(MyPredicter)
