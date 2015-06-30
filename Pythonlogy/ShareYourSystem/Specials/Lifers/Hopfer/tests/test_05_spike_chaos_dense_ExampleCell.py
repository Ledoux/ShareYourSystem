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
		_UnitsInt = 1000,
		_StdWeightFloat = StdWeightFloat,
		_StationaryRateFloat = 50.,
		_ExternalNoiseFloat = 5.,
		_InteractionStr = "Spike"
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

"""
from matplotlib import pyplot
pyplot.figure()
axes=pyplot.axes()
for _List in SYS.TempList[:100]:

	axes.plot(
		_List[0].imag/(2.*SYS.numpy.pi),
		abs(_List[1]),
		'.',
		color="r"
	)
	axes.plot(
		_List[0].imag/(2.*SYS.numpy.pi),
		abs(_List[2]),
		'.',
		color="b"
	)
axes.set_xscale('log')
pyplot.show()
"""

"""
#print
print("DEBUG CHECK THE TRANSFER FUNCTION")

#map
PerturbationFrequencyFloatsArray=SYS.numpy.array(
    [
        0.
     ]+list(
        SYS.numpy.logspace(0,3,100)
       #[130.]
    )
);




MyLifer=MyHopfer.HopfedAgentDeriveHopferVariable

#set
MyLifer.LifingPerturbationMethodStr="Brunel"
MyLifer.LifingPerturbationLambdaVariable=None

#map
LifedPerturbationMeanComplexesArray=SYS.numpy.array(
	map(
		lambda __PerturbationFrequencyFloat:
		MyLifer.lif(   
			_PerturbationFrequencyFloat=__PerturbationFrequencyFloat
		).LifedPerturbationMeanComplexVariable,
		PerturbationFrequencyFloatsArray
	)
)

#plot
SYS.plot(
	PerturbationFrequencyFloatsArray,
	abs(LifedPerturbationMeanComplexesArray),
	'-',
	linewidth=10,
	color="blue"
);
    
#init figure
SYS.plot(
    [1.,100.],
    [MyLifer.LifedPerturbationMeanNullFloat]*2,
    '--',linewidth=3,markersize=25,color="black"
);
SYS.Axes.set_xscale('log')
SYS.Axes.legend()

SYS.show()
"""