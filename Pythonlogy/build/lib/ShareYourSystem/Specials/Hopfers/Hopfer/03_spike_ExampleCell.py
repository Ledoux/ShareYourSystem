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
		_UnitsInt=5,
		_MeanWeightFloat=1.,
		_StdWeightFloat=0.,
		_ProbabilityWeigthFloat=0.2,
		#_SymmetryFloat=-0.7,
		_InteractionStr="Spike"
	)
	#.simulate(
	#	500.
	#)

#/###################/#
# View
#

#mapSet
MyHopfer.mapSet(
		{
			'PyplotingFigureVariable':{
				'figsize':(10,8)
			},
			'PyplotingGridIntsTuple':(30,30),
			'-Panels':[
				(
					'|Eigen',
					{
						'PyplotingTextVariable':[-0.6,0.],
						'PyplotingShapeVariable':[10,10],
					}
				),
				(
					'|Run',
					{
						'PyplotingTextVariable':[-0.4,0.],
						'PyplotingShiftVariable':[0,4],
						'PyplotingShapeVariable':[8,9],
						'-Charts':{
							'|P_*U':{
								'PyplotingLegendDict':{
									'fontsize':10,
									'ncol':2
								}
							}
						}
					}
				),
				(
					'|Stat',
					{
						'PyplotingTextVariable':[-0.4,0.],
						'PyplotingShiftVariable':[4,0],
						'PyplotingShapeVariable':[5,9],
					}
				)
			]
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
