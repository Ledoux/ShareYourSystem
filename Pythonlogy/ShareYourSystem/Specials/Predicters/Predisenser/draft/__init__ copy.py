# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import types
BaseModuleStr="ShareYourSystem.Specials.Predicters.Predicter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Predisenser','Predisense','Predisensing','Predisensed')
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getKrenelFloatsArray(
		_LevelFloatsTuple=None,
		_TimeFloatsTuple=None,
		_RunTimeFloat=100.,
		_StepTimeFloat=0.1,
	):

	#get the bins
	BinsInt=_RunTimeFloat/_StepTimeFloat

	#init
	KrenelFloatsArray=_LevelFloatsTuple[0]*np.ones(
		BinsInt,
		dtype=type(_LevelFloatsTuple[0])
	)

	#Debug
	'''
	print('getKrenelFloatsArray')
	print('_TimeFloatsTuple[0]/_StepTimeFloat:_TimeFloatsTuple[1]/_StepTimeFloat')
	print(_TimeFloatsTuple[0]/_StepTimeFloat,_TimeFloatsTuple[1]/_StepTimeFloat)
	print('_LevelFloatsTuple[1] is '+str(_LevelFloatsTuple[1]))
	print('')
	'''

	#put the second level
	KrenelFloatsArray[
		int(_TimeFloatsTuple[0]/_StepTimeFloat):int(_TimeFloatsTuple[1]/_StepTimeFloat)
	]=_LevelFloatsTuple[1]

	#return
	return KrenelFloatsArray
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PredisenserClass(BaseClass):
	
	def default_init(self,
						_PredisensingRunTimeFloat=100.,
						_PredisensingStepTimeFloat=0.1,
						_PredisensingClampFloat=0.1,
						_PredisensingMonitorList=None,
						_PredisensedTimeTraceFloatsArray=None,
						_PredisensedCommandTraceFloatsArray=None,
						_PredisensedInputCurrentTraceFloatsArray=None,
						_PredisensedInitialSensorFloatsArray=None,
						_PredisensedSensorTraceFloatsArray=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predisense(self):

		#/#################/#
		# External care : Prepare time and the command
		#

		#arange
		self.PredisensedTimeTraceFloatsArray=np.arange(
			0.,
			self.PredisensingRunTimeFloat,
			self.PredisensingStepTimeFloat
		)

		#array
		self.PredisensedCommandTraceFloatsArray=np.array(
			map(
				lambda __IndexInt:
				getKrenelFloatsArray(
					[
						0.,
						self.PredisensingClampFloat
					],
					[
						self.PredisensingRunTimeFloat/4.,
						self.PredisensingRunTimeFloat/2.
					],
					self.PredisensingRunTimeFloat,
					self.PredisensingStepTimeFloat
				),
				xrange(self.PredictingSensorsInt)
			)
		)

		#set
		self.PredisensedInputCurrentTraceFloatsArray=self.PredisensedCommandTraceFloatsArray*self.PredictingConstantTimeFloat

		#/#################/#
		# Prepare the initial conditions
		#

		#random sensors
		PredisensedInitialSensorFloatsArray=0.1*self.PredisensingClampFloat*scipy.stats.uniform.rvs(
			size=self.PredictingSensorsInt
		)
		
		#/#################/#
		# Shape the size of the sensors run
		#

		#init sensors
		self.PredisensedSensorTraceFloatsArray=np.zeros(
				(
					self.PredictingSensorsInt,
					len(self.PredisensedTimeTraceFloatsArray)
				)
			)
		self.PredisensedSensorTraceFloatsArray[:,0]=PredisensedInitialSensorFloatsArray

		#/#################/#
		# integrativ Loop
		#

		#for loop
		for __IndexInt in xrange(1,len(self.PredisensedTimeTraceFloatsArray)):

			#/#################/#
			# Sensor part
			#

			#debug
			'''
			self.debug(
					[
						'shape(self.PredisensedCommandTraceFloatsArray) is '+str(
							np.shape(self.PredisensedCommandTraceFloatsArray)
						),
						'shape(self.PredisensedSensorTraceFloatsArray) is '+str(
							np.shape(self.PredisensedSensorTraceFloatsArray)
						),
						('self.',self,[
							'PredictedSensorJacobianFloatsArray'
						])
					]
				)
			'''
			
			#Current
			PredisensedSensorCurrentFloatsArray=np.dot(
				self.PredictedSensorJacobianFloatsArray,
				self.PredisensedSensorTraceFloatsArray[:,__IndexInt-1]
			)+self.PredisensedCommandTraceFloatsArray[:,__IndexInt-1]

			#/#################/#
			# Euler part
			#

			#sensor
			self.PredisensedSensorTraceFloatsArray[
				:,
				__IndexInt
			]=self.PredisensedSensorTraceFloatsArray[
				:,
				__IndexInt-1
			]+PredisensedSensorCurrentFloatsArray*self.PredisensingStepTimeFloat

			#set
			LocalDict=locals()

	def mimic_draw(self):
		
		#/#################/#
		# Build the input-unit traces axes
		#

		#debug
		self.debug(
				[
					('self.',self,['PredisensingMonitorList'])
				]
			)

		#init
		if self.DrawingSetVariable==None:
			self.DrawingSetVariable={
				'/|A/-Axes/|Sensor':
				{
					'-Plots':{
						'#map@set':map(
							lambda __IndexInt:
							(
								'|'+str(__IndexInt),
								{
									'FiguringDrawVariable':
									[
										('#plot',
											{
												'#liarg:#map@get':[
													'PredisensedTimeTraceFloatsArray',
													'>>self.PredisensedInputCurrentTraceFloatsArray.__getitem__('+str(__IndexInt)+')'
												],
												'#kwarg':{
													'label':'$\\tau_{D}c_{'+str(__IndexInt)+'}(t)$',
													'linestyle':'-'
												}
											}
										),
										('#plot',
											{
												'#liarg:#map@get':[
													'PredisensedTimeTraceFloatsArray',
													'>>self.PredisensedSensorTraceFloatsArray['+str(__IndexInt)+',:]'
												],
												'#kwarg':{
													'color':'g',
													'label':'$x_{'+str(__IndexInt)+'}(t)$',
													'linewidth':3,
													'linestyle':'-'
												}
											}
										)
									]
								}
							),
							self.PredisensingMonitorList
						)	
					},
					'FiguringDrawVariable':
					[
						(
							'#axes',
							[
								('set_xticks',{
									'#liarg:#map@get':[
										">>SYS.set(SYS,'TimeTicksArray',SYS.numpy.arange(0.,self.PredisensingRunTimeFloat+1.,self.PredisensingRunTimeFloat/4.)).TimeTicksArray"
										#">>SYS.numpy.arange(0.,self.PredisensingRunTimeFloat+1.,self.PredisensingRunTimeFloat/4.)"
									]
								}),
								('set_xticklabels',{
									'#liarg:#map@get':[
										#">>map(lambda __Float:'$%.0f$'%__Float,SYS.numpy.arange(0.,self.PredisensingRunTimeFloat+1.,self.PredisensingRunTimeFloat/4.))"
										">>map(lambda __Float:'$%.0f$'%__Float,SYS.TimeTicksArray)"
									]
								}),
								('set_xlim',{
									'#liarg:#map@get':[0.,'>>self.PredisensingRunTimeFloat']
								}),
								('set_ylabel','$\\tau_{D}c(t),\ x(t)$'),
								('set_yticks',{
									'#liarg:#map@get':[
										#">>SYS.set(map(int,SYS.numpy.arange(0.,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat/3.))"
										">>SYS.set(SYS,'RateTicksArray',map(int,SYS.numpy.arange(0.,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat/3.))).RateTicksArray"
									]
								}),
								('set_yticklabels',{
									'#liarg:#map@get':[
										#'>>map(lambda __Float:"$%.0f$"%__Float,SYS.numpy.arange(-0.1,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat/3.))'
										">>map(lambda __Float:'$%.0f$'%__Float,SYS.RateTicksArray)"
									]
								}),
								('set_ylim',{
									'#liarg:#map@get':[
										'>>[-0.1,1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat]'
									]
								}),
								('tick_params',{
									'#kwarg':{
										'length':10,
										'width':5,
										'which':'major'
									}
								}),
								('tick_params',{
									'#kwarg':{
										'length':5,
										'width':2,
										'which':'minor'
									}
								}),
								('xaxis.set_ticks_position',
									{
										'#liarg':['bottom']
									}
								),
								('yaxis.set_ticks_position',
									{
										'#liarg':['left']
									}
								),
								('legend',{
									'#liarg':[],
									'#kwarg':{
										'fontsize':10,
										'shadow':True,
										'fancybox':True,
										'ncol':1
									}
								})
							]
						)
					],
					'FiguringShapeIntsTuple':(5,15)
				}
			}

		#call the base method
		BaseClass.draw(self)

#</DefineClass>

#</DefinePrint>
PredisenserClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredisensingRunTimeFloat',
		'PredisensingStepTimeFloat',
		'PredisensingClampFloat',
		'PredisensingMonitorList',
		'PredisensedTimeTraceFloatsArray',
		'PredisensedInputCurrentTraceFloatsArray',
		'PredisensedCommandTraceFloatsArray',
		'PredisensedInitialSensorFloatsArray',
		'PredisensedSensorTraceFloatsArray',
	]
)
#<DefinePrint>