#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS
import scipy.stats

#/###################/#
# Build the model
#

def checkPeak(self):
	print(self.TransferedPeakVariable);
	return len(self.TransferedPeakVariable[0])>0 and self.TransferedPeakVariable[0][0][0]>120. and self.TransferedPeakVariable[0][0][0]<200.

#Define
MyTransferer=SYS.TransfererClass(
	).stationarize(
		_ConstantTimeVariable=[0.02,0.01],
		_RateVariable = [10.,30.],
		_InteractionStr = "Spike"
	).stabilize(
		_ComputeBool=False,
		_DelayTimeVariable=[
			[0.001,0.0005],
			[0.001,0.0005]
		],
		_DecayTimeVariable=[
			[0.002,0.006],
			[0.002,0.006]
		],
		_RiseTimeVariable=[
			[0.001,0.0005],
			[0.001,0.0005]
		]
	).explore(
		_MethodStr = 'transfer',
		_RangeVariable={
			'StationarizingMeanWeightVariable':lambda self:np.array([
				[100.*scipy.stats.uniform.rvs(),-100.*scipy.stats.uniform.rvs()],
				[100.*scipy.stats.uniform.rvs(),-100.*scipy.stats.uniform.rvs()]
			])
		},
		_ConditionVariable=[
			(
				'checkPeak',
				checkPeak
			)
		]
	).execute(
		"self.mapSet(self.ExploredStoreTuplesListsList[0])"
	).view(
		_ColorStrsList = ["red","blue"],
		_LabelStrsList = ["E","I"]
	).pyplot(
	).show(
	)

#print
print('MyTransferer is ')
SYS._print(MyTransferer) 

