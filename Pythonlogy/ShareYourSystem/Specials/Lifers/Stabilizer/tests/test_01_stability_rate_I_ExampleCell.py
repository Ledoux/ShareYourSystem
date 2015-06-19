
#ImportModules
import ShareYourSystem as SYS

#Define
MyStabilizer=SYS.StabilizerClass(
	).stationarize(
		_LateralWeightVariable=[[-1700.]]
	).stabilize(
		_DelayTimeVariable=0.001,
		_ScanFrequencyVariable=[10.]
	)

#Choose the parameters to print
KeyStrsList=[
			'StabilizingConstantTimeVariable', #in ms
			'StabilizingDelayTimeVariable',
			'StabilizingLateralWeigthVariable',
			'StabilizedTotalPerturbationComplexesArray', #matrix M
			'StabilizedFlatTotalPerturbationComplexesArray', #matrix F
			'StabilizedDeterminantFloatsTuple',  #If it has converged, then it has to be closed to (0,0)
			'StabilizedInstabilityLambdaFloatsTuple',  # real part should be negative if stable,  (from this particular initial condition)
			'StabilizedInstabilityFrequencyFloat'
		]

#print
SYS._print(SYS.collections.OrderedDict(zip(KeyStrsList,MyStabilizer.mapGet(KeyStrsList))))
