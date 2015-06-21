#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Simulation time
BrianingDebugVariable=25.

#Define
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'BrianingStepTimeFloat':0.05, #(ms)
			'-Populations':[
				('|Sensor',{
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Inputs':{
						'|Command':{
							'RecordingLabelVariable':[0,1]
						}
					},
					'-Interactions':{
						'|Encod':{
							#'BrianingDebugVariable':BrianingDebugVariable
						}
					},
					'RecordingLabelVariable':[0,1]
				}),
				('|Agent',{
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Fast':{
							#'BrianingDebugVariable':BrianingDebugVariable
						}
					},
					'RecordingLabelVariable':[0,1]
				}),
				('|Decoder',{
					#'BrianingDebugVariable':BrianingDebugVariable,
					'RecordingLabelVariable':[0,1]
				})
			]
		}
	).predict(
		_DynamicBool=False,
		_AgentUnitsInt=2,
		_JacobianVariable={
			'ModeStr':"Track",
			'ConstantTimeFloat':10. #(ms)
		},
		_CommandVariable=(
			'#custom:#clock:25*ms',
			[
				"1.*mV*int(t>=25*ms)*int(t<75*ms)",
				"-0.5*mV*int(t==25*ms)"
				#"1.*mV",
				#"-0.5*mV"
			]
		),
		#_DecoderVariable="#array",
		#_DecoderMeanFloat=2.,
		#_DecoderStdFloat=0.,
		#_DecoderVariable=[[5.,2.],[2.,5.]],
		#_DecoderVariable=[[0.,5.],[5.,0.]],
		#_DecoderVariable=[[0.,5.],[5.,0.]],
		_DecoderVariable=[[7.,1.],[1.2,7.1]],
		_AgentTimeFloat=10., #(ms)
		_StationaryBool=True,
		_InteractionStr="Rate"
	).simulate(
		100
	)

#/###################/#
# View
#

MyPredicter.view(
	).mapSet(
		{
			'PyplotingFigureVariable':{
				'figsize':(10,8)
			},
			'PyplotingGridVariable':(30,30),
			'-Panels':[
				(
					'|Run',
					[
						(
							'-Charts',
							[
								(
									'|Sensor_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':2
										}
									}
								),
								(
									'|Agent_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':2
										}
									}
								),
								(
									'|Decoder_U',
									{
										'PyplotingLegendDict':{
											'fontsize':10,
											'ncol':2
										}
									}
								)
							]
						)
					]
				)
			]
		}
	).pyplot(
	).show(
	)

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyPredicter is ')
SYS._print(MyPredicter) 





