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
	).mapSet(
		{
			'BrianingStepTimeFloat':0.1,
			'-Populations':{
				'|Agent':{
					'LeakingTotalBool':True,
					'-Traces':{
						'|*U':{
							'RecordingInitStdVariable':0.5
						}
					},
					#'BrianingDebugVariable':100
				}
			}
		}
	).hopf(
		_UnitsInt=100,
		_StdWeightFloat=1.2,
		_SymmetryFloat=-0.7,
		#_GlobalBool=True,
		#_TotalBool=False
	).simulate(
		500.
	)

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
						'-Charts':{
							'|Perturbation':{
									'PyplotingShiftVariable':[4,0],
								}
							}
					}
				),
				(
					'|Run',
					{
						'PyplotingTextVariable':[-0.4,0.],
						'PyplotingShiftVariable':[0,4],
						'PyplotingShapeVariable':[8,9],
						'-Charts':{
							'|Agent_*U':{
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

print(MyHopfer['/-Panels/|Run/-Charts'])

#/###################/#
# Print
#

#print
print('MyHopfer is ')
SYS._print(MyHopfer) 
