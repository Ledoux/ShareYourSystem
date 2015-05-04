#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
MyHopfer=SYS.HopferClass(
	).numscipy(
		_SizeTuple=(100,100),
		_SymmetryFloat=0.,
		_EigenvalueBool=True
	).hopf(
	)
	#.simulate(
	#	SimulationTimeFloat
	#)

#/###################/#
# View
#

MyHopfer.pyplot(
	)
SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyHopfer is ')
SYS._print(MyHopfer) 





