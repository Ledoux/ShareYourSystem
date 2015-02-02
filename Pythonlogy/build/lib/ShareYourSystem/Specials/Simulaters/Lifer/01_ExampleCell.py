#ImportModules
import ShareYourSystem as SYS
import scipy.stats

#Definition an instance
MyLifer=SYS.LiferClass(
		**{
			'PopulatingUnitsInt':10
		}
	).collect(
		'SpikeMoniters',
		'MySpikes',
		SYS.MoniterClass()
	).lif(
		#LifingRestVariable
		-60.,
		#-60.+2.*scipy.stats.uniform.rvs(0,size=10),
		#LifingConstantTimeVariable
		20.,
		#20.+2.*scipy.stats.uniform.rvs(0,size=10),
		#LifingThresholdVariable
		#-50.,
		-50.+scipy.stats.uniform.rvs(0,size=10),
		#LifingResetVariable
		#-70.
		-70.+scipy.stats.uniform.rvs(0,size=10),
	).neurongroup(
	)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyLifer is '+SYS._str(
		MyLifer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
from brian2 import Network,ms,mV
MyNetwork=Network()
map(
	MyNetwork.add,
	SYS.flat(
		[
			MyLifer.NeurongroupedBrianVariable,
			MyLifer.NeurongroupedSpikeMonitorsList,
			MyLifer.NeurongroupedStateMonitorsList
		]
	)
)

#plot
MyLifer.NeurongroupedBrianVariable.v=-55.*mV
MyNetwork.run(100.*ms)
M=MyLifer.NeurongroupedSpikeMonitorsList[0]
from matplotlib import pyplot
pyplot.plot(M.t/ms, M.i, '.')
pyplot.show()
