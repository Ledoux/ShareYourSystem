
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredirater=SYS.PrediraterClass(
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
		#PredisensingMonitorList
		[0]
	).predirate(
		#PrediratingTransferVariable
		#SYS.numpy.tanh,
		lambda _FloatsArray:_FloatsArray,
		#lambda _FloatsArray:SYS.Predirater.getThresholdArray(_FloatsArray,100.),
		#PrediratingMonitorList
		[0,1]
	).draw(
	).show(
	)

#print
print('MyPredirater is')
SYS._print(MyPredirater)