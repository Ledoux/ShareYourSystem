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
Executer=BaseModule
from ShareYourSystem.Standards.Itemizers import Getter,Setter
import operator
import types
import copy
#</ImportSpecificModules>

#<DefineLocals>
def getMapList(_LiargVariablesList):
	return _LiargVariablesList[0]
def getLiargVariablesList(_ValueVariable):
	return [_ValueVariable]
ConditionGrabFilterStr="#filter"
ConditionGrabScanStr="#scan"
ConditionGrabIfStr="#if"
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
								'ConditioningFunctionTypesList',
								'ConditioningScanGetVariable',
								'ConditionedIsBool'
							]
	
	def default_init(self,
						_ConditioningTestGetVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestGetVariable=None,
						_ConditioningInstanceVariable=None,
						_ConditioningFunctionTypesList=[
							type(len),
							type,
							types.FunctionType
						],
						_ConditioningScanGetVariable=Executer.ExecutionPrefixStr+'self.__dict__.values()',
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
				('self.',self,[
					'ConditioningTestGetVariable',
					'ConditioningAttestGetVariable'
					]
				)
			]
		)
		'''

		#/###################/#
		# Adapt the TestValueVariable
		#

		#get
		try:

			#get
			ConditionedTestValueVariable=self.ConditioningInstanceVariable[
				self.ConditioningTestGetVariable
			]

		except:

			#set
			self.ConditionedIsBool=False

			#return
			return 
				
		#debug
		'''
		self.debug(
				'ConditionedTestValueVariable is '+SYS._str(ConditionedTestValueVariable)
			)
		'''

		#Check
		if ConditionedTestValueVariable in self.ConditioningFunctionTypesList:
			
			#debug
			self.debug(
					'We test with a function'
				)

			#call
			ConditionedTestValueVariable=ConditionedTestValueVariable(
					self.ConditioningInstanceVariable
				)

		#debug
		'''
		self.debug(
			[
				'We have configured the ConditionedTestValueVariable',
				'ConditionedTestValueVariable is '+str(ConditionedTestValueVariable)
			]
		)
		'''

		#/###################/#
		# Adapt the AttestValueVariable
		#

		#get
		try:

			#get
			ConditionedAttestValueVariable=self.ConditioningInstanceVariable[
				self.ConditioningAttestGetVariable
			]


		except:

			#debug
			'''
			self.debug(
				[
					'The get has not work for the Attest variable',
					'so check what it is',
					('self.',self,['ConditioningInstanceVariable'])
				]
			)
			'''

			#return 
			if hasattr(self.ConditioningInstanceVariable,'items'
				)==False and type(self.ConditioningInstanceVariable) not in [
					list,tuple]:

				#debug
				self.debug(
					[
						'It was not a dict or list so...',
						'there is no reason that it doesnt get except if it false'
					]
				)


				#set
				self.ConditionedIsBool=False

				#return
				return

			else:

				#debug
				'''
				self.debug('It is a dict or list so just put the value')
				'''

				#alias
				ConditionedAttestValueVariable=self.ConditioningAttestGetVariable	
			

		#Check
		if ConditionedAttestValueVariable in self.ConditioningFunctionTypesList:
			
			#call
			ConditionedAttestValueVariable=ConditionedAttestValueVariable(
					self.ConditioningInstanceVariable
				)

		#debug
		'''
		self.debug(
			[
				'We have configured the ConditionedAttestValueVariable',
				'ConditionedAttestValueVariable is '+str(ConditionedAttestValueVariable)
			]
		)
		'''

		#call
		try:

			#call
			self.ConditionedIsBool=self.ConditioningGetBoolFunction(
				ConditionedTestValueVariable,
				ConditionedAttestValueVariable
			)

		except:

			#debug
			'''
			self.debug(
				[
					'The get has not worked for the Attest variable',
					' so check what it is'
				]
			)
			'''

			#return 
			if hasattr(self.ConditioningInstanceVariable,'items'
				)==False and type(self.ConditioningInstanceVariable) not in [
					list,tuple]:

				#debug
				'''
				self.debug(
					[
						'It was not a dict or list so...',
						'There is no reason that it doesnt get except if it false'
					]
				)
				'''

				#set
				self.ConditionedIsBool=False

				#return 
				return 

			else:

				#debug
				'''
				self.debug('It is a dict or list so just put the value')
				'''

				#alias
				ConditionedTestValueVariable=self.ConditioningTestGetVariable	
			

		#debug
		'''
		self.debug(
			('self.',self,[
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
		) and type(self.GettingKeyVariable)!=type:

			#Check
			if ConditionGrabFilterStr in self.GettingKeyVariable:

				#temp
				TempGettingKeyVariable=self.GettingKeyVariable

				#debug
				'''
				self.debug(
							[
								'We map condition here',
								('self.',self,[
									'ConditioningTestGetVariable'
								])
							]
						)
				'''

				#alias
				FilterVariable=self.GettingKeyVariable[ConditionGrabFilterStr]

				#Check
				if ConditionGrabScanStr in TempGettingKeyVariable:

					#get
					ConditionScanValueVariablesList=self[
						TempGettingKeyVariable[ConditionGrabScanStr]
					]

				else:

					#get
					ConditionScanValueVariablesList=self[
						self.ConditioningScanGetVariable
					]

				#debug
				'''
				self.debug(
					'ConditionScanValueVariablesList is '+SYS._str(
						ConditionScanValueVariablesList
					)
				)
				'''

				#Init
				GettedValueVariable=[]

				#Debug
				for __ConditionTestVariable in ConditionScanValueVariablesList:

					#debug
					'''
					self.debug(
							'__ConditionTestVariable is '+SYS._str(__ConditionTestVariable)
						)
					'''

					#set
					self.ConditioningInstanceVariable=__ConditionTestVariable
							
					#loop and break at the first false
					for __ConditionVariable in FilterVariable:

						#Check
						if type(__ConditionVariable)==SYS.GetClass:

							#set
							__ConditionVariable.SelfVariable=__ConditionTestVariable

							#debug
							'''
							self.debug(
								[
									'we call a get function',
									'__ConditionVariable is '+str(__ConditionVariable)
								]
							)
							'''

							#get
							self.ConditionedIsBool=self[__ConditionVariable]

						elif type(__ConditionVariable)==tuple:

							#debug
							'''
							self.debug('we condition here')
							'''

							#condition
							self.condition(*__ConditionVariable)

						else:

							#set
							self.ConditionedIsBool=__ConditionVariable

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
								)['#map@condition'](
								IfVariable
							).ItemizedMapValueVariablesList
						),
						ConditionScanValueVariablesList
					)
				'''

				#/##################/#
				# Copy the TempGettingKeyVariable in order to add a key item and
				# continue then the get process

				#set
				#self.GettedValueVariable=GettedValueVariable
				#self.GettingKeyVariable=
				#self.GettedValueVariable=self[
				#]
				self.GettingKeyVariable=copy.copy(
					TempGettingKeyVariable
				)
				self.GettingKeyVariable[Getter.GetGrabStr]=GettedValueVariable

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
				#return {"HookingIsBool":False}

		#call the base method
		BaseClass.get(self)

	def mimic_set(self):

		"""
		#/###################/#
		# Condition in the Key Variable
		#

		#Check
		if hasattr(self.SettingKeyVariable,'items'
			) and type(self.SettingKeyVariable)!=type:

				#Check
				if ConditionGrabFilterStr in self.SettingKeyVariable:

					#Check
					if self.ConditionedIfBool==False:

						#set
						IfVariable=self.SettingKeyVariable[ConditionGrabFilterStr]

						#debug
						'''
						self.debug(
								[
									'condition in the key',
									'we set if the condition is satisfied',
									'IfVariable is '+str(IfVariable)
								]
							)
						'''
						
						#loop and break at the first false
						for __ConditionVariable in IfVariable:

							#condition
							self.condition(*__ConditionVariable)

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
							self.debug(
									[	
										'Ok we set'
									]
								)

							#set
							self.ConditionedIfBool=True

							#append
							self[
								self.SettingKeyVariable[Setter.SetShortKeyStr]
							]=self.SettingValueVariable

						#stop the setting
						return {'HookingIsBool':False}
		"""

		#/###################/#
		# Condition in the Value Variable
		#

		#Check
		if hasattr(self.SettingValueVariable,'items'
			) and type(self.SettingValueVariable)!=type: 

			#Check
			if ConditionGrabIfStr in self.SettingValueVariable:

				#/###################/#
				# Maybe the condition was not yet check
				#

				#set
				IfVariable=self.SettingValueVariable[ConditionGrabIfStr]
				TempSettingKeyVariable=self.SettingKeyVariable
				TempSettingValueVariable=self.SettingValueVariable

				#debug
				'''
				self.debug(
						[
							'condition in the value',
							'we set if the condition is satisfied',
							'IfVariable is '+str(IfVariable)
						]
					)
				'''

				#reset
				self.ConditioningInstanceVariable=self

				#loop and break at the first false
				for __ConditionVariable in IfVariable:

					#condition
					self.condition(*__ConditionVariable)

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
								'Ok we set',
								'TempSettingKeyVariable is '+str(
									TempSettingKeyVariable),
								'TempSettingValueVariable is '+str(
									TempSettingValueVariable)
							]
						)
					'''

					#/##################/#
					# Copy the TempSettingValueVariable in order to remove the if item and
					# continue then the set process

					self.SettingValueVariable=copy.copy(
						TempSettingValueVariable
					)
					del self.SettingValueVariable[ConditionGrabIfStr]

				else:

					#We append
					'''
					self.debug(
							[	
								'It is false we stop the setting',
								('self.',self,[
									'SettingKeyVariable',
									'SettingValueVariable'
								])
							]
						)
					'''
					
					#stop the setting
					return {'HookingIsBool':False}

		#call the base method
		return BaseClass.set(self)


#</DefineClass>

