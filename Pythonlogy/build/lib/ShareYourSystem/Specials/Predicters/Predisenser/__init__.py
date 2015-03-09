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
						_PredisensingMonitorDict=None,
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

		#init
		self.PredisensingMonitorDict={
			'Input':[0],
			'Unit':[0],
			'Output':[0]
		}

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

		#/#################/#
		# Build the input-unit traces axes
		#

		#debug
		self.debug(
				[
					('self.',self,['PredisensingMonitorDict'])
				]
			)

		#get
		SensorFigurer=self.set(
			'/-Views/|Run/-Axes/|Sensor',
			{
				'FiguringDrawVariable':
				#Input plot
				map(
						lambda __IndexInt:
						(
							'#plot',
							{
								'#liarg:#map@get':[
									'PredisensedTimeTraceFloatsArray',
									'>>self.PredisensedInputCurrentTraceFloatsArray.__getitem__('+str(__IndexInt)+')'
								],
								'#kwarg':{
									'label':'$\\tau_{D}c(t)$'
								}
							}
						),
						self.PredisensingMonitorDict['Input']
				#Unit plot
					)+map(
						lambda __IndexInt:
						(
							'#plot',
							{
								'#liarg:#map@get':[
									'PredisensedTimeTraceFloatsArray',
									'>>self.PredisensedSensorTraceFloatsArray['+str(__IndexInt)+',:]'
								],
								'#kwarg':{
									'color':'g',
									'label':'$x(t)$',
									'linewidth':3
								}
							}
						),
						self.PredisensingMonitorDict['Unit']
				#Axes set
					)+[
					(
						'#axes',
						{
							'legend':[],
							'set_ylabel':'$\\tau_{D}c(t),\ x(t)$',
							'set_xlim':[0.,self.PredisensingRunTimeFloat],
							'set_ylim':[
											-0.1,
											1.5*self.PredisensingClampFloat*self.PredictingConstantTimeFloat
										]
						}
					)
				],
				'FiguringShapeIntsTuple':(3,10)
			}
		)


	def mimic_show(self):
		
		#call the base method
		BaseClass.show(self)

		

		

#</DefineClass>

#</DefinePrint>
PredisenserClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredisensingRunTimeFloat',
		'PredisensingStepTimeFloat',
		'PredisensingClampFloat',
		'PredisensedTimeTraceFloatsArray',
		'PredisensedInputCurrentTraceFloatsArray',
		'PredisensedCommandTraceFloatsArray',
		'PredisensedInitialSensorFloatsArray',
		'PredisensedSensorTraceFloatsArray',
	]
)
#<DefinePrint>