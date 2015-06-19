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
					'LeakingGlobalBool':True,
					'LeakingMaxBool':True,
					'-Traces':{
						'|U':{
							'RecordingInitStdVariable':0.1
						}
					},
					#'BrianingDebugVariable':100
				}
			}
		}
	).hopf(
		_UnitsInt=100,
		_StdWeightFloat=1.3,
		_SymmetryFloat=-0.7
	)

CountInt=0
while MyHopfer.HopfedInstablesInt!=2 and CountInt<10:
	MyHopfer.hopf(
		_StdWeightFloat=1.+0.5*SYS.scipy.stats.uniform.rvs(size=1)
	)
	CountInt+=1

#Check
if MyHopfer.HopfedInstablesInt==2:

	#/###################/#
	# Leak and simulate
	#

	#leak
	MyHopfer.leak(
		).simulate(
			400.
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
							'PyplotingShiftVariable':[0,6],
							'PyplotingShapeVariable':[8,12],
							'-Charts':[
								(
									'|Agent_J_AutapseU',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':1
										}
									}
								),
								(
									'|Agent_U',
									{
										'PyplotingShiftVariable':[5,0],
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':1
										}
									}
								)
							]
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
