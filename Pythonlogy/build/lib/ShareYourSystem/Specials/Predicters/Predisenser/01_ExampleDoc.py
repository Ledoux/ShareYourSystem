
#ImportModules
import ShareYourSystem as SYS

#Define
MyPredisenser=SYS.PredisenserClass(
	).predict(
		#PredictingUnitsInt
		10,
		#PredictingSensorsInt
		1,
		#PredictingConstantTimeFloat
		0.01,
		#PredictingDecoderWeightFloat
		10.,
		#PredictingCostFloat
		0.,
		#PredictingNormalisationInt
		0.5,
		#PredictingPerturbativeWeightFloat
		0.1
	).predisense(
		#PredisensingRunTimeFloat,
		100.,
		#PredisensingStepTimeFloat
		0.1,
		#PredisensingClampFloat
		0.5
	)

#print
print('MyPredisenser is')
SYS._print(MyPredisenser)
