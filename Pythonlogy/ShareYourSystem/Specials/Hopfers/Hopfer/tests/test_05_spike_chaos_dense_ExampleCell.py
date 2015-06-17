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
			'-Populations':{
				'|Agent':{
					#'BrianingDebugVariable':100
					#'LeakingNoiseStdVariable':10.,
					#'LeakingThresholdVariable':'#scalar:U>-50*mV',
				}
			}
		}
	).hopf(
		_UnitsInt=100,
		_DelayTimeVariable=0.002,
		_StdWeightFloat=1.2,
		_InteractionStr="Spike"
	).leak(
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
			'PyplotingGridVariable':(30,30),
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
							'|Agent_I_Stimulation':{

							},
							'|Agent_U':{
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
