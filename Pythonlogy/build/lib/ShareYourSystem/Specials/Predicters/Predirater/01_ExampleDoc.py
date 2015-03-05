
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredirater=SYS.PrediraterClass(
	).predict(
		#PredictingUnitsInt
		10,
		#PredictingSensorsInt
		1,
		#PredictingDecoderWeigtFloat
		10.,
		#PredictingCostFloat
		0.,
		#PredictingNormalisationInt
		1,
		#PredictingPerturbativeWeightFloat
		0.1
	).predirate(
		#PrediratingRunTimeFloat
		100.,
		#PrediratingStepTimeFloat
		0.1,
		#PrediratingTransferVariable
		SYS.numpy.tanh,
		#lambda _Float:_Float
		#PrediratingClampFloat
		0.1
	)

#print
print('MyPredirater is')
SYS._print(MyPredirater)
