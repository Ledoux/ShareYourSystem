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
								'ConditioningFunctionTypesList',
								'ConditioningScanGetVariable',
								'ConditionedIsBool',
							]
	
	def default_init(self,
						_ConditioningTestGetVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestGetVariable=None,
						_ConditioningFunctionTypesList=[type(len),type(type)],
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
			ConditionedTestValueVariable=self.ConditioningInstanceVariable[
				self.ConditioningTestGetVariable
			]
		except:

			#set
			self.ConditionedIsBool=False

			#return
			return 
			
		#Check
		if ConditionedTestValueVariable in self.ConditioningFunctionTypesList:
			
			#call
			ConditionedTestValueVariable=ConditionedTestValueVariable(
					self
				)

		#debug
		self.debug(
			[
				'We have configured the ConditionedTestValueVariable',
				'ConditionedTestValueVariable is '+str(ConditionedTestValueVariable)
			]
		)

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

			#set
			self.ConditionedIsBool=False

			#return 
			return

		#Check
		if ConditionedAttestValueVariable in self.ConditioningFunctionTypesList:
			
			#call
			ConditionedAttestValueVariable=ConditionedAttestValueVariable(
					self
				)

		#debug
		self.debug(
			[
				'We have configured the ConditionedAttestValueVariable',
				'ConditionedAttestValueVariable is '+str(ConditionedAttestValueVariable)
			]
		)
		
		#call
		try:

			#call
			self.ConditionedIsBool=self.ConditioningGetBoolFunction(
				ConditionedTestValueVariable,
				ConditionedAttestValueVariable
			)

		except:

			#set
			self.ConditionedIsBool=False

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
			if ConditionShortKeyStr in self.GettingKeyVariable:

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
				IfVariable=self.GettingKeyVariable[ConditionShortKeyStr]

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
					for __ConditionVariable in IfVariable:

						#Check
						if type(__ConditionVariable)==SYS.GetClass:

							#set
							__ConditionVariable.SelfVariable=__ConditionTestVariable

							#debug
							self.debug(
								[
									'we call a get function',
									'__ConditionVariable is '+str(__ConditionVariable)
								]
							)

							#get
							self.ConditionedIsBool=self[__ConditionVariable]

						else:

							#debug
							'''
							self.debug('we condition here')
							'''

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
								IfVariable
							).ItemizedMapValueVariablesList
						),
						ConditionScanValueVariablesList
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

		#call the base method
		BaseClass.get(self)

	def mimic_set(self):

		#Check
		if hasattr(self.SettingKeyVariable,'items'
			) and type(self.SettingKeyVariable)!=type:

				#Check
				if 'IfVariable' in self.SettingKeyVariable:

					#set
					IfVariable=self.SettingKeyVariable[ConditionShortKeyStr]

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
						'''
						self.debug(
								[	
									'Ok we set'
								]
							)
						'''

						#append
						self[
							self.SettingKeyVariable[Setter.SetShortKeyStr]
						]=self.SettingValueVariable

					#stop the setting
					return {'HookingIsBool':False}

		#Check
		elif hasattr(self.SettingValueVariable,'items'
			) and type(self.SettingValueVariable)!=type: 

			#Check
			if ConditionShortKeyStr in self.SettingValueVariable:

				#set
				IfVariable=self.SettingValueVariable[ConditionShortKeyStr]

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
								'Ok we set'
							]
						)
					'''
					
					#append
					self[
						self.SettingKeyVariable
					]=self.SettingValueVariable[Setter.SetShortKeyStr]

				#stop the setting
				return {'HookingIsBool':False}

		#call the base method
		return BaseClass.set(self)


#</DefineClass>
