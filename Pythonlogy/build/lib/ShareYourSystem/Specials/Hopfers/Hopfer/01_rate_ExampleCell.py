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
	).hopf(
		_UnitsInt=100,
		_SymmetryFloat=-0.5,
	)
	#.simulate(
	#	SimulationTimeFloat
	#)

#/###################/#
# View
#

MyHopfer.view(
	).pyplot(
	)
SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyHopfer is ')
SYS._print(MyHopfer) 





