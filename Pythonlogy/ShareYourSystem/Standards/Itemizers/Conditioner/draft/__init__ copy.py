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
								'ConditioningTestGetVariable',
								'ConditioningGetBoolFunction',
								'ConditioningAttestGetVariable',
								'ConditioningInstanceVariable',
								'ConditioningTypesList',
								'ConditioningGetVariable',
								'ConditionedTestVariable',
								'ConditionedIsBool',
							]
	
	def default_init(self,
						_ConditioningTestGetVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestGetVariable=None,
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
				'We configure the ConditioningTestGetVariable',
				('self.',self,[
					'ConditioningInstanceVariable',
					'ConditioningTestGetVariable',
					'ConditioningAttestGetVariable'
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
					('self.',self,['ConditioningTestGetVariable'])
				]
			)	
			'''

			#Check
			if self.ConditioningTestGetVariable in self.ConditioningTypesList:

				#debug
				'''
				self.debug('This is a call condition')
				'''

				#call
				self.ConditionedTestVariable=self.ConditioningTestGetVariable(
						self.ConditioningInstanceVariable
					)

			else:
				
				#debug
				'''
				self.debug('Maybe it is get condition')
				'''

				#try
				if type(
					self.ConditioningTestGetVariable
				)==str or (
				hasattr(
					self.ConditioningTestGetVariable,'items'
				) and ('GetVariable' in self.ConditioningTestGetVariable or 'ConditionVariable' in self.ConditioningTestGetVariable)
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
								self.ConditioningTestGetVariable
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
					self.ConditionedTestVariable=self.ConditioningTestGetVariable

		#/####################/#
		# Case where the InstanceVariable is None but... there is ConditioningTestGetVariable...
		# it is necessary false if ConditioningTestGetVariable asks for a get or a call

		#Check
		elif self.ConditioningTestGetVariable in self.ConditioningTypesList or (
			type(
					self.ConditioningTestGetVariable
				)==str or (
				hasattr(
					self.ConditioningTestGetVariable,'items'
					) and (
					'GetVariable' in self.ConditioningTestGetVariable or 'ConditionVariable' in self.ConditioningTestGetVariable)
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
				'We have configured the ConditioningTestGetVariable',
				('self.',self,[
									'ConditioningTestGetVariable',
									'ConditioningAttestGetVariable'
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
				self.ConditioningAttestGetVariable
			)
		except:

			#set
			self.ConditionedIsBool=False

		#debug
		'''
		self.debug(
			('self.',self,[
							#'ConditioningInstanceVariable',
							#'ConditioningTestGetVariable',
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
		 'ConditionVariable' in self.GettingKeyVariable or ConditionShortKeyStr in self.GettingKeyVariable):

			#debug
			'''
			self.debug(
						[
							'We map condition here',
							('self.',self,[
								#'ConditioningInstanceVariable',
								#'ConditioningTestGetVariable',
								'ConditioningGetVariable'
							])
						]
					)
			'''

			#alias
			try:
				ConditionVariable=self.GettingKeyVariable['ConditionVariable']
			except:
				ConditionVariable=self.GettingKeyVariable[ConditionShortKeyStr]

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
				for __ConditionTuple in ConditionVariable:

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
							)['#map:condition'](
							ConditionVariable
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
			'ConditionVariable' in self.SettingKeyVariable or ConditionShortKeyStr in self.SettingKeyVariable):

			#set
			try:
				ConditionVariable=self.SettingKeyVariable['ConditionVariable']
			except:
				ConditionVariable=self.SettingKeyVariable[ConditionShortKeyStr]

			#debug
			'''
			self.debug(
					[
						'condition in the key',
						'we set if the condition is satisfied',
						'ConditionVariable is '+str(ConditionVariable)
					]
				)
			'''
			
			#loop and break at the first false
			for __ConditionTuple in ConditionVariable:

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
			'ConditionVariable' in self.SettingValueVariable or ConditionShortKeyStr in self.SettingValueVariable
			):

			#set
			try:
				ConditionVariable=self.SettingValueVariable['ConditionVariable']
			except:
				ConditionVariable=self.SettingValueVariable[ConditionShortKeyStr]

			#debug
			'''
			self.debug(
					[
						'condition in the value',
						'we set if the condition is satisfied',
						'ConditionVariable is '+str(ConditionVariable)
					]
				)
			'''
			
			#loop and break at the first false
			for __ConditionTuple in ConditionVariable:

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

