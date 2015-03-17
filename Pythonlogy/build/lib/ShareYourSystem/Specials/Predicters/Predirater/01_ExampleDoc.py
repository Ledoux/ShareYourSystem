

#ImportModules
import ShareYourSystem as SYS

#Define
MyPredirater=SYS.PrediraterClass(
	).predict(
		#PredictingUnitsInt
		100,
		#PredictingSensorsInt
		1,
		#PredictingDynamicStr
		'leak',
		#PredictingConstantTimeFloat (ms)
		1.,
		#PredictingInputStatStr
		'norm',
		#PredictingDecoderMeanWeightFloat
		0.,
		#PredictingDecoderStdWeightFloat
		40.,
		#PredictingNormalisationInt
		1.,			
		#PredictingCostFloat
		0.,
		#PredictingPerturbativeInputWeightFloat
		0.5,
		#PredictingPerturbativeLateralWeightFloat
		1.,
		#PredictingInputRandomStatStr
		'norm',
		#PredictingLateralRandomStatStr
		'norm'
	).predisense(
		#PredisensingRunTimeFloat (ms)
		100.,
		#PredisensingStepTimeFloat (ms)
		0.1,
		#PredisensingClampFloat
		2.,
		#PredisensingMonitorList
		[0]
	).predirate(
		#PrediratingConstantTimeFloat
		1.,
		#PrediratingTransferVariable
		lambda _FloatsArray:0.2*SYS.numpy.tanh(5.*_FloatsArray),
		#lambda _FloatsArray:_FloatsArray,
		#lambda _FloatsArray:SYS.Predirater.getThresholdArray(_FloatsArray,100.),
		#PrediratingMonitorIntsList
		[0,1,3,4,5,6,7],
		#PrediratingInititalFloat
		0.1
	).draw(
	).show(
	)

#print
print('MyPredirater is')
SYS._print(MyPredirater)
