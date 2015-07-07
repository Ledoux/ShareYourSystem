#/###################/#
# Import modules
#


#ImportModules
import ShareYourSystem as SYS

#set
StdWeightFloat=15.

#/###################/#
# Build the model
#

#Define
MyHopfer=SYS.HopferClass(
	).mapSet(
		{	
			'-Populations':{
				'|Agent':{
					'-Traces':{
						'|U':{
							'RecordingInitMeanVariable':-70.,
							'RecordingInitStdVariable':5.,
						}
					},
					'-Events':{
						'|Default_Events':{
							'BrianingEventSelectVariable':range(0,30)
						}
					},
					#'-Rates':{
					#	'|Default_Rates':{
					#	}
					#}
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
		_ExternalNoiseFloat = 5.,
		_SymmetryFloat=-0.7,
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
			'PyplotingGridVariable':(45,45),
			'-Panels':[
				(
					'|Eigen',
					{
						'PyplotingTextVariable':[-0.6,0.],
						'PyplotingShapeVariable':[10,10],
						'-Charts':{
							'|Perturbation':{
								'PyplotingShiftVariable':[6,0],
							}
						}
					}
				),
				(
					'|Transfer',
					{
						'PyplotingTextVariable':[-0.5,-1.],
						'PyplotingShapeVariable':[10,10],
						'-Charts':{
							'|Isolate':{
								'PyplotingShiftVariable':[6,0],
							}
						}
					}
				),
				(
					'|Run',
					{
						'PyplotingTextVariable':[0.,0.1],
						'PyplotingShiftVariable':[["top",1],6],
						'PyplotingShapeVariable':[8,18],
						'-Charts':{
								'|Agent_U':{
									'PyplotingLegendDict':{
										'fontsize':10,
										'ncol':1
									}
								}
							}
					}
				),
				(
					'|Stat',
					{
						'PyplotingTextVariable':[0.,0.],
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
