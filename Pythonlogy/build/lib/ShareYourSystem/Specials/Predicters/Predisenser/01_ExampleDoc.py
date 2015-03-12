
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredisenser=SYS.PredisenserClass(
	).predict(
		#PredictingUnitsInt
		10,
		#PredictingSensorsInt
		1,
		#PredictingConstantTimeFloat (ms)
		1.,
		#PredictingInputStatStr
		'norm',
		#PredictingDecoderWeightFloat
		1.,
		#PredictingNormalisationInt
		0.5,			
		#PredictingCostFloat
		0.,
		#PredictingPerturbativeInputWeightFloat
		0.,
		#PredictingPerturbativeLateralWeightFloat
		0.,
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
		0.5,
		#PredisensingMonitorIntsList
		[0]
	).draw(
	).show(
	)

#print
print('MyPredisenser is')
SYS._print(MyPredisenser)
