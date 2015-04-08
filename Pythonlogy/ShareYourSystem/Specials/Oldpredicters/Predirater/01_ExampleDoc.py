

#ImportModules
import ShareYourSystem as SYS

#Define
MyPredirater=SYS.PrediraterClass(
	).oldpredict(
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
		5.,
		#PredictingInputRandomStatStr
		'norm',
		#PredictingLateralRandomStatStr
		'norm',
		#PredictingPerturbativeNullBool
		False
	).predisense(
		#PredisensingRunTimeFloat (ms)
		100.,
		#PredisensingStepTimeFloat (ms)
		0.1,
		#PredisensingMonitorList
		[0],
		#PredisensingKrenelClampFloat
		1.,
		#PredisensingFourierClampFloat
		0.,
	).predirate(
		#PrediratingConstantTimeFloat
		1.,
		#PrediratingTransferVariable
		#lambda _FloatsArray:0.5*SYS.numpy.tanh(2.*_FloatsArray),
		#lambda _FloatsArray:0.2*SYS.numpy.tanh(5.*_FloatsArray),
		#lambda _FloatsArray:0.1*SYS.numpy.tanh(10.*_FloatsArray),
		lambda _FloatsArray:0.05*SYS.numpy.tanh(20.*_FloatsArray),
		#lambda _FloatsArray:_FloatsArray,
		#lambda _FloatsArray:SYS.Predirater.getThresholdArray(_FloatsArray,100.),
		#PrediratingMonitorIntsList
		[0,1,3,4,5,6,7],
		#PrediratingInititalFloat
		0.1,
		#PrediratingCommandNoiseFloat
		0.,
		#PrediratingRateNoiseFloat
		0.
	).view(
	).pyplot(
	)
SYS.matplotlib.pyplot.show()

#print
print('MyPredirater is')
SYS._print(MyPredirater)
