
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
		10.,
		#PredictingDecoderWeightFloat
		10.,
		#PredictingCostFloat
		0.,
		#PredictingNormalisationInt
		0.5,
		#PredictingPerturbativeWeightFloat
		0.1
	).predisense(
		#PredisensingRunTimeFloat (ms)
		100.,
		#PredisensingStepTimeFloat (ms)
		0.1,
		#PredisensingClampFloat
		0.5,
		#PredisensingMonitorDict
		{
			'Input':[0],
			'Unit':[0,1],
			'Output':[0]
		}
	).show(
	)

#print
print('MyPredisenser is')
SYS._print(MyPredisenser)
