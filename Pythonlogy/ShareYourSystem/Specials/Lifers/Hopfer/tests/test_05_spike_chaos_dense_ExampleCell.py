#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#set
StdWeightFloat=15.

#Define
MyHopfer=SYS.HopferClass(
	).mapSet(
		{	
			'BrianingStepTimeFloat':0.1,
			'-Populations':{
				'|Agent':{
					'-Traces':{
						'|U':{
							'RecordingInitMeanVariable':-70.,
							'RecordingInitStdVariable':5.,
						}
					},
					'-Events':{
						'|Default':{
							'BrianingEventSelectVariable':range(0,30)
						}
					}
					#'BrianingDebugVariable':100
					#'LeakingNoiseStdVariable':10.,
					#'LeakingThresholdVariable':'#scalar:U>-50*mV',
				}
			}
		}
	).hopf(
		_UnitsInt=1000,
		_StdWeightFloat=StdWeightFloat,
		_StationaryRateFloat=50.,
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
