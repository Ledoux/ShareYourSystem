
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredirater=SYS.PrediraterClass(
	).predict(
		#PredictingUnitsInt
		100,
		#PredictingSensorsInt
		1,
		#PredictingConstantTimeFloat (ms)
		1.,
		#PredictingDecoderWeigtFloat
		3.,
		#PredictingCostFloat
		1.,
		#PredictingNormalisationInt
		0.5,
		#PredictingPerturbativeInputWeightFloat
		0.1,
		#PredictingPerturbativeLateralWeightFloat
		0.1
	).predirate(
		#PrediratingRunTimeFloat (ms)
		100.,
		#PrediratingStepTimeFloat (ms)
		0.1,
		#PrediratingTransferVariable
		#SYS.numpy.tanh,
		lambda _FloatsArray:_FloatsArray,
		#lambda _FloatsArray:SYS.Predirater.getThresholdArray(_FloatsArray,100.),
		#PrediratingClampFloat
		0.5
	)

#print
print('MyPredirater is')
SYS._print(MyPredirater)