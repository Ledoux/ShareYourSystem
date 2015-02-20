# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Conditioner

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Executer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
Executer=BaseModule
from ShareYourSystem.Standards.Itemizers import Setter
#</ImportSpecificModules>

#<DefineLocals>
def getMapList(_LiargVariablesList):
	return _LiargVariablesList[0]
def getLiargVariablesList(_ValueVariable):
	return [_ValueVariable]
ConditionShortKeyStr="#if"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ConditionerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ConditioningTestVariable',
								'ConditioningGetBoolFunction',
								'ConditioningAttestVariable',
								'ConditioningInstanceVariable',
								'ConditioningTypesList',
								'ConditioningGetVariable',
								'ConditionedTestVariable',
								'ConditionedIsBool',
							]
	
	def default_init(self,
						_ConditioningTestVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestVariable=None,
						_ConditioningInstanceVariable=None,
						_ConditioningTypesList=[type(len),type(type)],
						_ConditioningGetVariable=Executer.ExecutionPrefixStr+'self.__dict__.values()',
						_ConditionedTestVariable=None,
						_ConditionedIsBool=True,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
		#Set to itself as a default
		self.ConditioningInstanceVariable=self

	def getMapValueVariable(self):

		#return
		return self.ConditionedIsBool

	def do_condition(self):

		#debug
		'''
		self.debug(
			[
				'We configure the ConditioningTestVariable',
				('self.',self,[
					'ConditioningInstanceVariable',
					'ConditioningTestVariable',
					'ConditioningAttestVariable'
					]
				)
			]
		)
		'''
		
		#Check
		if self.ConditioningInstanceVariable!=None:

			#debug
			'''
			self.debug(
				[
					'self.ConditioningInstanceVariable!=None',
					('self.',self,['ConditioningTestVariable'])
				]
			)	
			'''

			#Check
			if self.ConditioningTestVariable in self.ConditioningTypesList:

				#debug
				'''
				self.debug('This is a call condition')
				'''

				#call
				self.ConditionedTestVariable=self.ConditioningTestVariable(
						self.ConditioningInstanceVariable
					)

			else:
				
				#debug
				'''
				self.debug('Maybe it is get condition')
				'''

				#try
				if type(
					self.ConditioningTestVariable
				)==str or (
				hasattr(
					self.ConditioningTestVariable,'items'
				) and ('GetKeyVariable' in self.ConditioningTestVariable or 'ConditionTuplesList' in self.ConditioningTestVariable)
				):

					#Check
					if hasattr(self.ConditioningInstanceVariable,'__getitem__'):

						#debug
						'''
						self.debug(
							[
								'This is a condition get',
								('self.',self,['ConditioningInstanceVariable'])
							]
						)
						'''

						#try
						try:
					
							#get
							self.ConditionedTestVariable=self.ConditioningInstanceVariable[
								self.ConditioningTestVariable
							]

						except:

							#set
							self.ConditionedTestVariable=None

					else:

						#debug
						'''
						self.debug('The instance variable is something that cannot get')
						'''

						#set
						self.ConditionedTestVariable=None

						#set to false
						self.ConditionedIsBool=False

						#return 
						return

				else:

					#set
					self.ConditionedTestVariable=self.ConditioningTestVariable

		#/####################/#
		# Case where the InstanceVariable is None but... there is ConditioningTestVariable...
		# it is necessary false if ConditioningTestVariable asks for a get or a call

		#Check
		elif self.ConditioningTestVariable in self.ConditioningTypesList or (
			type(
					self.ConditioningTestVariable
				)==str or (
				hasattr(
					self.ConditioningTestVariable,'items'
					) and (
					'GetKeyVariable' in self.ConditioningTestVariable or 'ConditionTuplesList' in self.ConditioningTestVariable)
				)
			):

			#set
			self.ConditionedTestVariable=None

			#set to false
			self.ConditionedIsBool=False

			#return 
			return


		#debug
		'''
		self.debug(
			[
				'We have configured the ConditioningTestVariable',
				('self.',self,[
									'ConditioningTestVariable',
									'ConditioningAttestVariable'
								]
				)
			]
		)
		'''

		#call
		try:

			#call
			self.ConditionedIsBool=self.ConditioningGetBoolFunction(
				self.ConditionedTestVariable,
				self.ConditioningAttestVariable
			)
		except:

			#set
			self.ConditionedIsBool=False

		#debug
		'''
		self.debug(
			('self.',self,[
							#'ConditioningInstanceVariable',
							#'ConditioningTestVariable',
							'ConditionedTestVariable',
							'ConditionedIsBool',
						])
		)
		'''

	def mimic_get(self):

		#debug
		'''
		self.debug(
				('self.',self,['GettingKeyVariable'])
			)
		'''

		#Check
		if hasattr(
			self.GettingKeyVariable,'items'
		) and(
		 'ConditionTuplesList' in self.GettingKeyVariable or ConditionShortKeyStr in self.GettingKeyVariable):

			#debug
			'''
			self.debug(
						[
							'We map condition here',
							('self.',self,[
								#'ConditioningInstanceVariable',
								#'ConditioningTestVariable',
								'ConditioningGetVariable'
							])
						]
					)
			'''

			#alias
			try:
				ConditionTuplesList=self.GettingKeyVariable['ConditionTuplesList']
			except:
				ConditionTuplesList=self.GettingKeyVariable[ConditionShortKeyStr]

			#get
			ConditionTestVariablesList=self[
				self.ConditioningGetVariable
			]

			#debug
			'''
			self.debug(
				'ConditionTestVariablesList is '+SYS._str(
					ConditionTestVariablesList
				)
			)
			'''

			#Init
			GettedValueVariable=[]

			#Debug
			for __ConditionTestVariable in ConditionTestVariablesList:

				#debug
				'''
				self.debug(
						'__ConditionTestVariable is '+SYS._str(__ConditionTestVariable)
					)
				'''

				#set
				self.ConditioningInstanceVariable=__ConditionTestVariable
						
				#loop and break at the first false
				for __ConditionTuple in ConditionTuplesList:

					#condition
					self.condition(*__ConditionTuple)

					#Check
					if self.ConditionedIsBool==False:

						#debug
						'''
						self.debug('we break')
						'''

						#break
						break

				#append
				if self.ConditionedIsBool:

					#We append
					'''
					self.debug(
							[	
								'This __ConditionTestVariable is keeped',
								SYS._str(__ConditionTestVariable)
							]
						)
					'''

					#append
					GettedValueVariable.append(__ConditionTestVariable)

			'''
			#map condition
			self.GettedValueVariable=SYS._filter(
					lambda __ConditionTestVariable:
					all(
							self.set(
								'ConditioningInstanceVariable',
								__ConditionTestVariable
							)['map*condition'](
							ConditionTuplesList
						).ItemizedMapValueVariablesList
					),
					ConditionTestVariablesList
				)
			'''

			#set
			self.GettedValueVariable=GettedValueVariable

			#debug
			'''
			self.debug(
					[
						'We have filtered',
						('self.',self,['GettedValueVariable'])
					]
				)
			'''

			#stop the getting
			return {"HookingIsBool":False}

		else:

			#call the base method
			BaseClass.get(self)

	def mimic_set(self):

		#Check
		if hasattr(self.SettingKeyVariable,'items'
			) and (
			'ConditionTuplesList' in self.SettingKeyVariable or ConditionShortKeyStr in self.SettingKeyVariable):

			#set
			try:
				ConditionTuplesList=self.SettingKeyVariable['ConditionTuplesList']
			except:
				ConditionTuplesList=self.SettingKeyVariable[ConditionShortKeyStr]

			#debug
			'''
			self.debug(
					[
						'condition in the key',
						'we set if the condition is satisfied',
						'ConditionTuplesList is '+str(ConditionTuplesList)
					]
				)
			'''
			
			#loop and break at the first false
			for __ConditionTuple in ConditionTuplesList:

				#condition
				self.condition(*__ConditionTuple)

				#Check
				if self.ConditionedIsBool==False:

					#debug
					'''
					self.debug('we break')
					'''

					#break
					break

			#append
			if self.ConditionedIsBool:

				#We append
				'''
				self.debug(
						[	
							'Ok we set'
						]
					)
				'''

				#append
				try:
					self[
						self.SettingKeyVariable['SetKeyVariable']
					]=self.SettingValueVariable
				except:
					self[
						self.SettingKeyVariable[Setter.SetShortKeyStr]
					]=self.SettingValueVariable

			#stop the setting
			return {'HookingIsBool':False}

		#Check
		elif hasattr(self.SettingValueVariable,'items'
			) and (
			'ConditionTuplesList' in self.SettingValueVariable or ConditionShortKeyStr in self.SettingValueVariable
			):

			#set
			try:
				ConditionTuplesList=self.SettingValueVariable['ConditionTuplesList']
			except:
				ConditionTuplesList=self.SettingValueVariable[ConditionShortKeyStr]

			#debug
			'''
			self.debug(
					[
						'condition in the value',
						'we set if the condition is satisfied',
						'ConditionTuplesList is '+str(ConditionTuplesList)
					]
				)
			'''
			
			#loop and break at the first false
			for __ConditionTuple in ConditionTuplesList:

				#condition
				self.condition(*__ConditionTuple)

				#Check
				if self.ConditionedIsBool==False:

					#debug
					'''
					self.debug('we break')
					'''

					#break
					break

			#append
			if self.ConditionedIsBool:

				#We append
				'''
				self.debug(
						[	
							'Ok we set'
						]
					)
				'''

				#append
				try:
					self[
						self.SettingKeyVariable
					]=self.SettingValueVariable['SetValueVariable']
				except:
					self[
						self.SettingKeyVariable
					]=self.SettingValueVariable[Setter.SetShortKeyStr]

			#stop the setting
			return {'HookingIsBool':False}


		#call the base method
		return BaseClass.set(self)


#</DefineClass>

