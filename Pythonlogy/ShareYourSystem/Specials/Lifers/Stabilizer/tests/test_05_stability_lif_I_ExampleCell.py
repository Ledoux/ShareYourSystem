#ImportModules
import ShareYourSystem as SYS

#ImportModules
import ShareYourSystem as SYS

LateralWeightVariablesList=[
    [[-100.]]
]

#Check
for __LateralWeightVariable in LateralWeightVariablesList:

    #Define
    MyStabilizer=SYS.StabilizerClass(
        ).stationarize(
            _LateralWeightVariable=__LateralWeightVariable,
            _ConstantTimeVariable=[0.01],
            _RateVariable=[15.],
            _InteractionStr="Spike"
        ).stabilize(
            _DelayTimeVariable=0.001,
            #_DecayTimeVariable=0.005,
            #_RiseTimeVariable=0.0005,
            #_ScanFrequencyVariable=[10.]
        )

    #Choose the parameters to print
    KeyStrsList=[
        'StationarizingLateralWeightVariable',
        'StabilizingConstantTimeVariable', #in ms
        'StabilizingDelayTimeVariable',
        'StabilizedTotalPerturbationComplexesArray', #matrix M
        'StabilizedFlatTotalPerturbationComplexesArray', #matrix F
        'StabilizedDeterminantFloatsTuple',  #If it has converged, then it has to be closed to (0,0)
        'StabilizedBiggestLambdaFloatsTuple',
        'StabilizedInstabilityLambdaFloatsTuple',  # real part should be negative if stable,  (from this particular initial condition)
        'StabilizedInstabilityFrequencyFloat'
    ]

    #print
    SYS._print(SYS.collections.OrderedDict(zip(KeyStrsList,MyStabilizer.mapGet(KeyStrsList))))

