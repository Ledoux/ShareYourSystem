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
		_SymmetryFloat=-0.7,
	).simulate(
		200.
	)

#/###################/#
# View
#

#mapSet
MyHopfer.mapSet(
		{
			'-Populations':{
				'|P':{
					#'PyplotingShiftVariable':[0,5],
					'PyplotingShapeVariable':[5,7],
					'PyplotingLegendDict':{
						'fontsize':10,
						'ncol':2
					}
				}
			}
		}
	).view(
	).pyplot(
	).show(
	)

#/###################/#
# Print
#

#print
print('MyHopfer is ')
SYS._print(MyHopfer) 

