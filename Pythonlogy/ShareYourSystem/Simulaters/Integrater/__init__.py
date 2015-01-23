# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Integrater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Eulerer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineFunctions>
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class IntegraterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'IntegratingStepsInt',
		'IntegratingInitFloatsArray',
		'IntegratingMoniterVariableIndexIntsArray',
		'IntegratingTimeDelayVariable',
		'IntegratingDelayFloatsVariable',
		'IntegratingRoutineMethodStr',
		'IntegratingMoniterCollectionStr',
		'IntegratedPreFloatsArray',
		'IntegratedPostFloatsArray',
		'IntegratedMonitPreFloatsArray',
		'IntegratedStepInt',
		'IntegratedDelayIntsArray',
		'IntegratedDelayStepIntsArray',
		'IntegratedHookMethodsList'
	]

	def default_init(self,
			_IntegratingStepsInt=1,
			_IntegratingInitFloatsArray=None,
			_IntegratingMoniterVariableIndexIntsArray=None,
			_IntegratingTimeDelayVariable=None,
			_IntegratingDelayFloatsVariable=None,
			_IntegratingRoutineMethodStr="integrate_euler",
			_IntegratingMoniterCollectionStr="StateMoniters",
			_IntegratedPreFloatsArray=None,
			_IntegratedPostFloatsArray=None,
			_IntegratedMonitPreFloatsArray=None,
			_IntegratedStepInt=0,
			_IntegratedDelayIntsArray=None,
			_IntegratedDelayStepIntsArray=None,
			_IntegratedHookMethodsList=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#collect
		self.collect(
			"StateMoniters",
			"Variable",
			SYS.MoniterClass().update(
					{
						'MoniteringSampleTimeIndexIntsArray':np.zeros(1,dtype=int),
						'MoniteringVariableIndexIntsArray':np.array([])
					}
				)
		)

	def integrate_euler(
		self
	):

		#debug
		'''
		self.debug('first we euler')
		'''

		#euler
		self.euler(
			self.IntegratedPreFloatsArray
		)

		#alias
		self.IntegratedPostFloatsArray=self.EuleredPostFloatsArray

		#switch
		self.IntegratedPreFloatsArray=self.IntegratedPostFloatsArray

	def integrate_delay(
			self
	):

		#add in the delay clock
		self.IntegratedDelayIntsArray+=1

		#debug
		'''
		self.debug(
					[
						'before the reset of the delay clocks',
						('self.',self,[
						'IntegratedDelayIntsArray',
						'IntegratedDelayStepIntsArray'
						]),
						'np.where(self.IntegratedDelayIntsArray>self.IntegratedDelayStepIntsArray) is '+str(
							np.where(
							self.IntegratedDelayIntsArray>self.IntegratedDelayStepIntsArray
							)
						)
					]
				)
		'''

		#map a reset
		self.IntegratedDelayIntsArray[
			np.where(
				self.IntegratedDelayIntsArray>=self.IntegratedDelayStepIntsArray
			)
		]=0

		#debug
		'''
		self.debug(
					[
						'After reset of the delay clocks',
						('self.',self,[
						'IntegratedDelayIntsArray',
						])
					]
				)
		'''

		#scale the delay to set
		LocalIntegratedDelayIntsArray=[
			self.IntegratedDelayIntsArray[0] for __Int in xrange(len(self.IntegratingDelayFloatsVariable))
		] if len(
			self.IntegratedDelayIntsArray)<len(self.IntegratingDelayFloatsVariable
		) else self.IntegratedDelayIntsArray

		#debug
		'''
		self.debug(('self.',self,[
							'IntegratedStepInt',
							'IntegratingDelayFloatsVariable',
							'IntegratedDelayIntsArray',
							'IntegratedPostFloatsArray',
							'IntegratedPreFloatsArray'
						]))
		'''

		#put in the delay box
		map(
				lambda __IntegratedDelayFloatsList,__LocalIntegratedDelayInt,__IntegratedPostFloat:
				__IntegratedDelayFloatsList.__setitem__(
					__LocalIntegratedDelayInt,
					__IntegratedPostFloat
				),
				self.IntegratingDelayFloatsVariable,
				LocalIntegratedDelayIntsArray,
				self.IntegratedPostFloatsArray
			)

		
		#debug
		'''
		self.debug(('self.',self,['IntegratedPreFloatsArray']))
		'''

	def do_integrate(
				self
			):	
		
		#populate
		self.populate()

		#set in the monit
		self['<StateMoniters>VariableMoniter'
		].MoniteringVariableIndexIntsArray=self.IntegratingMoniterVariableIndexIntsArray

		#map
		map(
				lambda __PopulatedStateDeriveMoniter:
				__PopulatedStateDeriveMoniter.__setattr__
				(
					'MoniteredTotalVariablesArray',
					np.zeros(
						(
							len(__PopulatedStateDeriveMoniter.MoniteringVariableIndexIntsArray),
							self.IntegratingStepsInt
						)
					)
				),
				self.PopulatedStateDeriveMonitersList
			)

		#Check
		if self.IntegratingTimeDelayVariable==None:

			#alias
			self.IntegratedPreFloatsArray=self.IntegratingInitFloatsArray

		else:

			#debug
			'''
			self.debug('This is an integration with delay')
			'''

			#Check
			if self.IntegratingDelayFloatsVariable==None or len(self.IntegratingDelayFloatsVariable)!=len(self.IntegratingInitFloatsArray):
				
				#Check
				if hasattr(self.IntegratingTimeDelayVariable,'__iter__')==False:

					#debug
					'''
					self.debug('This is the same delay for all')
					'''

					#set an array of dimension 1
					self.IntegratedDelayIntsArray=np.zeros(1,dtype=int)-1

					#set
					self.IntegratedDelayStepIntsArray=np.array([self.IntegratingTimeDelayVariable])

					#define 
					self.IntegratingDelayFloatsVariable=np.zeros(
						(
							len(self.IntegratingInitFloatsArray),
							self.IntegratingTimeDelayVariable
							#self.IntegratingTimeDelayVariable/self.EuleringTimeStep
						),
						dtype=float
					)

				else:

					#debug
					'''
					self.debug('The system has a list of delays')
					'''

					#set just an int here
					self.IntegratedDelayIntsArray=np.zeros(
						len(self.IntegratingTimeDelayVariable)
					)

					#map
					self.IntegratingDelayFloatsVariable=map(
						lambda __IntegratingTimeDelayVariable:
						np.zeros(
							__IntegratingTimeDelayVariable,
							#__IntegratingTimeDelayFloat/self.EuleringTimeStep,
							dtype=float
						)-1,
						self.IntegratingTimeDelayVariable
					)

					#map
					self.IntegratedDelayStepIntsArray=np.array(
						map(
							len,
							self.IntegratingDelayFloatsVariable
							)
					)

				#fill completely the delay box with the value of init
				map(
					lambda __IntegratingDelayFloatsVariable,__IntegratingInitFloat:
					map(
						lambda __Int:
						__IntegratingDelayFloatsVariable.__setitem__(
							__Int,
							__IntegratingInitFloat
						),
						xrange(len(__IntegratingDelayFloatsVariable))
					),
					self.IntegratingDelayFloatsVariable,
					self.IntegratingInitFloatsArray
				)


			#debug
			'''
			self.debug(('self.',self,[
				'IntegratingDelayFloatsVariable',
				'IntegratedDelayStepIntsArray'
			]))
			'''

			#get the 
			self.IntegratedPreFloatsArray=np.array(
				map(
					lambda __IntegratingDelayFloatsVariable:
					__IntegratingDelayFloatsVariable[0],
					self.IntegratingDelayFloatsVariable
				)
			)

			#append
			self.IntegratedHookMethodsList.append(self.integrate_delay)

		#debug
		'''
		self.debug(('self.',self,[
					'IntegratingRoutineMethodStr',
					'IntegratedPreFloatsArray'
				]))
		'''

		#append
		self.IntegratedHookMethodsList.insert(
			0,
			getattr(
				self,
				self.IntegratingRoutineMethodStr
			)
		)

		#adapt the monitoring numpy array
		IntegratedMoniterSampleTimeIndexIntsArray=np.zeros(1,dtype=int)
		IntegratedMoniterRecordTimeIndexIntsArray=np.zeros(1,dtype=int)
		self.IntegratedMonitPreFloatsArray=np.zeros((len(self.IntegratedPreFloatsArray),1),dtype=float)

		#integrativ loop
		for __IntegratingStepInt in xrange(self.IntegratingStepsInt):

			#set and adapt
			self.IntegratedStepInt=__IntegratingStepInt
			IntegratedMoniterRecordTimeIndexIntsArray[0]=__IntegratingStepInt
			self.IntegratedMonitPreFloatsArray[:,0]=self.IntegratedPreFloatsArray

			#debug
			'''
			self.debug(
						[
							'Before monitoring',
							('self.',self,['IntegratedPreFloatsArray'])
						]
					)
			'''

			#moniter
			map(
					lambda __PopulatedStateDeriveMoniter:
					__PopulatedStateDeriveMoniter.monit(
						IntegratedMoniterRecordTimeIndexIntsArray
					),
					self.PopulatedStateDeriveMonitersList
				)

			#debug
			'''
			self.debug(('self.',self,[
								'IntegratedHookMethodsList'
							]))
			'''

			#call the hooks routines
			map(
					lambda __IntegratedHookMethod:
					__IntegratedHookMethod.__call__(),
					self.IntegratedHookMethodsList
				)

#</DefineClass>
