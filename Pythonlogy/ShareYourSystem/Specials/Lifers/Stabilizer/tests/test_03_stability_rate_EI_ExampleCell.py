
#ImportModules
import ShareYourSystem as SYS

#Define
MyHopfer=SYS.HopferClass(
	).hopf(
		_LateralWeightVariable=[
			[0.5,-500.],
			[500.,-10.]
		],
		_DelayTimeVariable=0.001,
		_DoStabilityBool=True,
		_StabilityScanFrequencyVariable=[10.]
	)


#Choose the parameters to print
KeyStrsList=[
			'HopfingConstantTimeVariable', #in ms
			'HopfingDelayTimeVariable',
			'HopfingLateralWeigthVariable',
			'HopfedTotalPerturbationComplexesArray', #matrix M
			'HopfedFlatTotalPerturbationComplexesArray', #matrix F
			'HopfedDeterminantFloatsTuple',  #If it has converged, then it has to be closed to (0,0)
			'HopfedInstabilityLambdaFloatsTuple',  # real part should be negative if stable,  (from this particular initial condition)
			'HopfedInstabilityFrequencyFloat'
		]

#print
SYS._print(SYS.collections.OrderedDict(zip(KeyStrsList,MyHopfer.mapGet(KeyStrsList))))
