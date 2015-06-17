#ImportModules
import ShareYourSystem as SYS

"""
Nicolas tests

rates 5-15 sigmaext 5-5
taums 20-10 thresholds 20-20 resets 10-10 taurps 0-0
delays 1-1 taur 0.5-0.5 taud 5-5

JEE, JEI, JIE, JII=100,100,100,100:
stable, eigenvalue w largest real part = -36,0

100,100,100,0:
unstable,  128, 184 (f=29Hz)

0,100,100,100:
stable, -15, 338

100,0,0,0:
unstable, 135, 0

0,100,100,0:
unstable, 99, 240 (f=38Hz)


"""

#Define
MyHopfer=SYS.HopferClass(
    ).hopf(
        _LateralWeightVariable=[
            [100.,-100.],
            [100.,-100.]
        ],
        _ConstantTimeVariable=[0.01,0.02],
        _DelayTimeVariable=0.001,
        _RiseTimeVariable=0.005,
        _DecayTimeVariable=0.05,
        _DoStabilityBool=True,
        _StabilityScanFrequencyVariable=[10.],
        _InteractionStr="Spike"
    )


#Choose the parameters to print
KeyStrsList=[
            'HopfingConstantTimeVariable', #in ms
            'HopfingDelayTimeVariable',
            'HopfingLateralWeightVariable',
            'HopfedTotalPerturbationComplexesArray', #matrix M
            'HopfedFlatTotalPerturbationComplexesArray', #matrix F
            'HopfedDeterminantFloatsTuple',  #If it has converged, then it has to be closed to (0,0)
            'HopfedInstabilityLambdaFloatsTuple',  # real part should be negative if stable,  (from this particular initial condition)
            'HopfedInstabilityFrequencyFloat'
        ]

#print
SYS._print(SYS.collections.OrderedDict(zip(KeyStrsList,MyHopfer.mapGet(KeyStrsList))))
