# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Setter has a __setitem__ method for setting things in the <InstanceVariable>.__dict__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Getter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Getter=BaseModule
from ShareYourSystem.Standards.Itemizers import Itemizer
#</ImportSpecificModules>

#<DefineLocals>
def getMapList(_LiargVariablesList):

	#Check
	if hasattr(_LiargVariablesList[0],'items'):
		return _LiargVariablesList[0].items()
	else:
		return _LiargVariablesList[0]
		
def getLiargVariablesList(_ValueVariable):
	return _ValueVariable
SetEachPrefixStr="#each:"
SetAllPrefixStr="#all:"
SetShortKeyStr="#set"
SetBoundPrefixStr="#bound:"
SetSetterStr="<"
SetMapGetShortKeyStr=Itemizer.ItemMapPrefixStr+'get'
SetMapSetShortKeyStr=Itemizer.ItemMapPrefixStr+'set'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class SetterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'SettingKeyVariable',
									'SettingValueVariable',
									'SettingItemBool',
									'SettingNewBool',
									'SettedValueVariable'
								]

	def default_init(self,
						_SettingKeyVariable=None, 
						_SettingValueVariable=None, 
						_SettingItemBool=True, 	
						_SettingNewBool=True,	
						_SettedValueVariable=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def getMapValueVariable(self):

		#return None
		return None

	def __setitem__(self,_KeyVariable,_ValueVariable):
		""" """

		#debug
		'''
		self.debug(
					[
						('locals()[\'',locals(),[
										'_KeyVariable',
										'_ValueVariable']
										,'\']'),
						('self.',self,[
									'SettingKeyVariable',
									#'SettingValueVariable'
									])
					])
		'''
		
		#set (and set before argument to facilitate switch triggers (see later...)
		self.SettingKeyVariable=_KeyVariable
		self.SettingValueVariable=_ValueVariable
		self.set()		

		#set
		return self

	def do_set(self):
		""" """

		#debug
		'''
		self.debug(
			("self.",self,[
				'SettingKeyVariable',
				'SettingValueVariable'
			])
		)	
		'''

		#itemize first
		if self.SettingItemBool:

			#debug
			'''
			self.debug('first we itemize')
			'''

			#itemize
			self.itemize(
					self.SettingKeyVariable
				)

		else:

			#set
			self.ItemizedValueMethod=None

		#/############################
		# Case of a method get 
		#

		#debug
		'''
		self.debug(
				('self.',self,['ItemizedValueMethod'])
			)
		'''

		#Check 
		if self.ItemizedValueMethod!=None:

			#debug
			'''
			self.debug('we are going to call the method but first get it')
			'''

			#get
			SettedValueMethod=self[self.SettingKeyVariable]

			#debug
			self.debug(
					('self.',self,['SettingValueVariable'])
				)

			#get the 
			SettedLiargVariable=self[self.SettingValueVariable]

			#debug
			'''
			self.debug(
				[
					'SettedValueMethod is '+SYS._str(SettedValueMethod),
					'SettedLiargVariable is '+SYS._str(SettedLiargVariable)
				]
			)
			'''

			#define
			try:

				#get
				SettedLiargVariablesList=SettedValueMethod.im_func.BaseDoClass.Module.getLiargVariablesList(
					SettedLiargVariable
				)

				'''
				self.debug(
						'SettedLiargVariablesList is '+str(SettedLiargVariablesList)
					)
				'''
				
				#get the method and put the value as arguments
				SettedValueMethod(*SettedLiargVariablesList)

				#Stop the setting
				return {"HookingIsBool":False}

			except:

				#debug
				'''
				self.debug('call the SettedValueMethod with self.SettingValueVariable directly')
				'''

				#direct
				#SettedValueMethod(*self.SettingValueVariable)
				SettedValueMethod(SettedLiargVariable)
			
				#Stop the setting
				return {"HookingIsBool":False}

		#/####################/#
		# Case of a non method  with set with a set key str 
		#

		elif type(self.SettingKeyVariable
				)==str:

			#/####################/#
			# Case of #bound: set
			#

			#Check
			if self.SettingKeyVariable.startswith(
				SetBoundPrefixStr
			):

				#deprefix
				SettedMethodStr=SYS.deprefix(
						self.SettingKeyVariable,
						SetBoundPrefixStr
					)

				#debug
				'''
				self.debug(
					[
						'We bound here',
						'SettedMethodStr is '+SettedMethodStr
					]
				)
				'''

				#bound
				setattr(
					self.__class__,
					SettedMethodStr,
					self.SettingValueVariable
				)

				#call
				self.SettingValueVariable(self)

				#stop the setting
				return {'HookingIsBool':False}


			#/####################/#
			# Case of #each: set
			#

			#Check
			if self.SettingKeyVariable.startswith(
				SetEachPrefixStr
			):

				#get
				SettedGetVariable=self[
					SYS.deprefix(
						self.SettingKeyVariable,
						SetEachPrefixStr
					)
				]

				#Check
				if hasattr(SettedGetVariable,'values'):
					SettedGetVariablesList=SettedGetVariable.values()
				else:
					SettedGetVariablesList=SettedGetVariable

				#debug
				'''
				self.debug(
					[
						'SettedGetVariablesList is ',
						SYS._str(SettedGetVariablesList),
						('self.',self,['SettingValueVariable'])
					]
				)
				'''

				#map
				map(
						lambda __SettedGetVariable,__SettedValueVariable:
						__SettedGetVariable.set(
							*__SettedValueVariable
						)
						if type(__SettedValueVariable) in [
							list,tuple
						] and len(__SettedValueVariable)==2
						else
						__SettedGetVariable[SetMapSetShortKeyStr](
							__SettedValueVariable
						),
						SettedGetVariablesList,
						self.SettingValueVariable
					)

				#Return stop the setting
				return {'HookingIsBool':False}

			#/####################/#
			# Case of #all: set
			#

			#Check
			elif self.SettingKeyVariable.startswith(
				SetAllPrefixStr
			):

				#get
				SettedGetVariable=self[
					SYS.deprefix(
						self.SettingKeyVariable,
						SetAllPrefixStr
					)
				]

				#Check
				if hasattr(SettedGetVariable,'values'):
					SettedGetVariablesList=SettedGetVariable.values()
				else:
					SettedGetVariablesList=SettedGetVariable

				#debug
				'''
				self.debug(
					[
						'SettedGetVariablesList is ',
						SYS._str(SettedGetVariablesList),
						('self.',self,['SettingValueVariable'])
					]
				)
				'''

				#Check
				if type(self.SettingValueVariable) in [
							list,tuple
						] and len(self.SettingValueVariable)==2:

					#map
					map(
							lambda __SettedGetVariable:
							__SettedGetVariable.set(
								*self.SettingValueVariable
							),
							SettedGetVariablesList
						)

				else:

						
					#map
					map(
							lambda __SettedGetVariable:
							__SettedGetVariable[SetMapSetShortKeyStr](
								self.SettingValueVariable
							),
							SettedGetVariablesList
						)

				#Return stop the setting
				return {'HookingIsBool':False}

			#/####################/#
			# Case of a set in the __dict__
			#

			else:

				#/####################/#
				# Case of a set with a set dict
				#

				#Check
				if hasattr(
						self.SettingValueVariable,'items'
					):

					#debug
					self.debug(
							[
								'Check for a set value dict',
								('self.',self,['SettingValueVariable'])
							]
						)

					if Getter.GetShortKeyStr in self.SettingValueVariable:

						#debug
						self.debug(
							[
								'we set a value with a GetShortKeyStr inside',
								('self.',self,['SettingValueVariable'])
							]
						)

						#set
						self[self.SettingKeyVariable]=self[
							self.SettingValueVariable[Getter.GetShortKeyStr]
						]

						#Return
						return {'HookingIsBool':False}

					elif SetMapGetShortKeyStr in self.SettingValueVariable:

						#debug
						self.debug(
							[
								'we set a value with a map GetShortKeyStr inside',
								('self.',self,['SettingValueVariable'])
							]
						)

						#set
						self[self.SettingKeyVariable]=self[
							SetMapGetShortKeyStr
						](
							*self.SettingValueVariable[SetMapGetShortKeyStr]
						).ItemizedMapValueVariablesList
						

						#Return
						return {'HookingIsBool':False}

					#Check
					elif SetShortKeyStr in self.SettingValueVariable:

						#debug
						self.debug(
							[
								'we set a value with a SetShortKeyStr inside',
								('self.',self,['SettingValueVariable'])
							]
						)

						#set
						self[
							self.SettingKeyVariable
						]=self.SettingValueVariable[SetShortKeyStr]

						#Return
						return {'HookingIsBool':False}


				#/####################/#
				# Case of an instancing set
				#

				#Check
				if self.SettingNewBool:

					#debug
					'''
					self.debug(
							[
								'we check if we have to set a default value here',
								('self.',self,[
									'SettingKeyVariable',
									'SettingValueVariable'
								])
							]
						)
					'''

					#get
					SettedValueType=SYS.getTypeClassWithTypeStr(
						SYS.getTypeStrWithKeyStr(
							self.SettingKeyVariable)
					)

					#Check
					if SettedValueType!=type(self.SettingValueVariable): 

						#debug
						'''
						self.debug(
							[
								'SettedValueType is '+str(SettedValueType)
							]
						)	
						'''

						#Check
						if SettedValueType!=None.__class__:

							#debug
							'''
							self.debug(
								[
									'we wrap the setting value',
									('self.',self,['SettingValueVariable'])
								]
							)
							'''
							
							#alias
							'''
							try:
							'''

							#map set
							self[self.SettingKeyVariable]=SettedValueType(
								)[SetMapSetShortKeyStr](
								self.SettingValueVariable
							)
							#self.SettingValueVariable=SettedValueType(
							#	)[SetMapSetShortKeyStr](
							#	self.SettingValueVariable
							#)

							'''
							except:

								#debug
								self.debug(
										[
											'set failed because the suffix str indicates a different type from the value',
											'SettedValueType is '+str(SettedValueType),
											'type(self.SettingValueVariable) is '+str(
												type(self.SettingValueVariable))
										]
									)
							'''

							#Return
							return {'HookingIsBool':False}

				#/####################/#
				# Set in the __dict__ ... finally 
				# But first check the special case of a dict set that is not a #set dict

				#debug
				'''
				self.debug(
					[
						'we just maybe set in the __dict__',
						('self.',self,[
								'SettingKeyVariable',
								'SettingValueVariable'
							])
					]
				)
				'''
				
				#__setitem__ in the __dict__, this is an utility set
				self.__dict__[
					self.SettingKeyVariable
				]=self.SettingValueVariable

				#add in the SettingValue
				try:
					self.SettingValueVariable.DictKeyStr=self.SettingKeyVariable
					self.SettingValueVariable.DictDeriveSetter=self
				except:
					pass

				#Return
				return {'HookingIsBool':False}

		#/####################/#
		# Case of a non method set with a set dict in the Key Variable
		#

		elif hasattr(self.SettingKeyVariable,'items'):

			#debug
			'''
			self.debug(
					[
						'SettingKeyVariable has items...',
						('self.',self,['SettingKeyVariable'])
					]
				)
			'''

			#set
			self.set(
				self.SettingKeyVariable[SetShortKeyStr],
				self.SettingValueVariable
			)

			#Return
			return {'HookingIsBool':False}


		#/####################/#
		# Case of a function set
		#

		elif callable(self.SettingKeyVariable):

			#/####################/#
			# Case of a non method with a set dict in the Value Variable
			#

			#debug
			self.debug(
					[
						'The key is callable',
						('self.',self,[
							'SettingValueVariable',
							'PathDerivePather'
						]),
						'map get the values to have the liargvariables list'
					]
				)

			#Check
			if type(self.SettingValueVariable)in [tuple,list]:

				#/###################/
				# map get with the PathDerivePather
				#

				#get
				self.GettingNewBool=False
				SettedLiargVariablesList=self[SetMapGetShortKeyStr](
					*self.SettingValueVariable
				).ItemizedMapValueVariablesList
				self.GettingNewBool=True

			elif hasattr(self.SettingValueVariable,'items'):

				#/###################/
				# dict get with the PathDerivePather
				#

				#get
				SettedLiargVariablesList=self[self.SettingValueVariable]

			else:

				#/###################/
				# list and get
				#

				#get
				SettedLiargVariablesList=[self[self.SettingValueVariable]]

			#debug
			self.debug(
				[
					'we call here',
					('self.',self,['SettingKeyVariable']),
					'SettedLiargVariablesList is '+SYS._str(SettedLiargVariablesList)
				]
			)

			#call
			self.SettingKeyVariable(
					*SettedLiargVariablesList	
				)

			#debug
			self.debug(
					'self.SettingKeyVariable.__self__ is '+SYS._str(
						self.SettingKeyVariable.__self__
					)
				)

			#Return
			return {'HookingIsBool':False}

	def mimic_get(self):

		#Check
		if self.GettingKeyVariable==SetSetterStr:

			#get
			self.GettedValueVariable=self.DictDeriveSetter

			#return 
			return {'HookingIsBool':False}
		
		#call the base method
		return BaseClass.get(self)


#</DefineClass>
