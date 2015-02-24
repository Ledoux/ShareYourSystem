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
SetSetterShortStr="<"
SetEachPrefixStr="#each:"
SetAllPrefixStr="#all:"
SetBoundPrefixStr="#bound:"
SetKeyGrabStr=Getter.GetGrabStr
SetValueGrabStr="#value"
SetValueGrabPrefixStr=SetValueGrabStr+':'
SetValueGetGrabStr=SetValueGrabPrefixStr+Getter.GetUndirectStr
SetMapStr=Itemizer.ItemMapPrefixStr+'set'
SetMapValueGetGrabStr=SetValueGrabPrefixStr+Getter.GetMapStr
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class SetterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'SetKeyStr',
								#'SetDeriveSetter',
								'SettingKeyVariable',
								'SettingValueVariable',
								#'SettingItemBool',
								#'SettingNewBool',
								'SettedValueVariable'
							]

	def default_init(self,
						_SetKeyStr="",
						_SetDeriveSetter=None,
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

		#Init
		#self.SetKeyStr=""
		#self.SetDeriveSetter=None

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

			#/####################/#
			# Check for the value in order to adapt the liarg
			#

			#debug
			self.debug(
					[
						'SettedValueMethod is '+SYS._str(SettedValueMethod),
						'Before calling the itemized method, we adapt the liarg',
						('self.',self,['SettingValueVariable'])
					]
				)

			#Temp
			SettedTempSettingValueVariable=self.SettingValueVariable

			#Check
			if hasattr(
					SettedTempSettingValueVariable,'items'
				):

				#debug
				'''
				self.debug(
						[
							'Check for a set value dict',
						]
					)
				'''

				if SetValueGrabStr in SettedTempSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we itemize with a value with a SetValueGrabStr inside',
							'SettedTempSettingValueVariable is '+SYS._str(SettedTempSettingValueVariable)
						]
					)
					'''

					#set
					SettedTempSettingValueVariable=SettedTempSettingValueVariable[SetValueGrabStr]

				elif SetMapValueGetGrabStr in SettedTempSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we set a value with a map SetMapValueGetGrabStr inside',
						]
					)
					'''

					#set
					SettedTempSettingValueVariable=self[
						SYS.deprefix(
							SetMapValueGetGrabStr,
							SetValueGrabPrefixStr
						)
					](
						*SettedTempSettingValueVariable[SetMapValueGetGrabStr]
					).ItemizedMapValueVariablesList
					
				#Check
				elif SetValueGetGrabStr in SettedTempSettingValueVariable:

					#Get 
					SettedTempSettingValueVariable=self[
						SettedTempSettingValueVariable[SetValueGetGrabStr]
					]

					#debug
					'''
					self.debug(
						[
							'we set a value with a SetValueGetGrabStr inside',
						]
					)
					'''

			#get the 
			#SettedLiargVariable=self[self.SettingValueVariable]
			SettedLiargVariable=SettedTempSettingValueVariable

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

				#temp
				SettedTempSettingValueVariable=self.SettingValueVariable

				#get
				SettedEachGetVariable=self[
					SYS.deprefix(
						self.SettingKeyVariable,
						SetEachPrefixStr
					)
				]

				#debug
				self.debug(
					[
						'We each here',
						('self.',self,['SettingKeyVariable']),
						'SettedEachGetVariable is '+str(SettedEachGetVariable)
					]
				)

				#Check
				if hasattr(SettedEachGetVariable,'values'):
					SettedEachGetVariablesList=SettedEachGetVariable.values()
				else:
					SettedEachGetVariablesList=SettedEachGetVariable

				#debug
				'''
				self.debug(
					[
						'SettedEachGetVariablesList is ',
						SYS._str(SettedEachGetVariablesList),
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
						__SettedGetVariable[SetMapStr](
							__SettedValueVariable
						),
						SettedEachGetVariablesList,
						SettedTempSettingValueVariable
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
							__SettedGetVariable[SetMapStr](
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
					'''
					self.debug(
							[
								'Check for a set value dict',
								('self.',self,['SettingValueVariable'])
							]
						)
					'''

					if SetValueGrabStr in self.SettingValueVariable:

						#debug
						'''
						self.debug(
							[
								'we set a value with a SetValueGrabStr inside',
								('self.',self,['SettingValueVariable'])
							]
						)
						'''

						#set
						self[self.SettingKeyVariable]=self.SettingValueVariable[SetValueGrabStr]

						#Return
						return {'HookingIsBool':False}

					elif SetMapValueGetGrabStr in self.SettingValueVariable:

						#debug
						'''
						self.debug(
							[
								'we set a value with a map SetMapValueGetGrabStr inside',
								('self.',self,['SettingValueVariable'])
							]
						)
						'''

						#set
						self[self.SettingKeyVariable]=self[
							SYS.deprefix(
								SetMapValueGetGrabStr,
								SetValueGrabPrefixStr
							)
						](
							*self.SettingValueVariable[SetMapValueGetGrabStr]
						).ItemizedMapValueVariablesList
						

						#Return
						return {'HookingIsBool':False}

					#Check
					elif SetValueGetGrabStr in self.SettingValueVariable:

						#Get 
						SettedGrabValueVariable=self[
							self.SettingValueVariable[SetValueGetGrabStr]
						]

						#debug
						'''
						self.debug(
							[
								'we set a value with a SetValueGetGrabStr inside',
								('self.',self,['SettingValueVariable']),
								'SettedGrabValueVariable is '+SYS._str(
									SettedGrabValueVariable)
							]
						)
						'''

						#set
						self[
							self.SettingKeyVariable
						]=SettedGrabValueVariable

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
						self.debug(
							[
								'SettedValueType is '+str(SettedValueType),
								('self.',self,['SettingKeyVariable'])
							]
						)	


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
								)[SetMapStr](
								self.SettingValueVariable
							)
							#self.SettingValueVariable=SettedValueType(
							#	)[SetMapValueGetGrabStr](
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

							#debug
							self.debug('Ok we have instanced')

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
					self.SettingValueVariable.SetKeyStr=self.SettingKeyVariable
					self.SettingValueVariable.SetDeriveSetter=self
				except:
					pass

				#Return
				return {'HookingIsBool':False}

		#/####################/#
		# Case of a non method set with a set dict in the Key Variable
		#

		elif hasattr(self.SettingKeyVariable,'items'):

			#get
			SettedGetKeyVariable=self[self.SettingKeyVariable]

			#debug
			'''
			self.debug(
					[
						'SettingKeyVariable has items...',
						('self.',self,['SettingKeyVariable']),
						'SettedGetKeyVariable is '+SYS._str(SettedGetKeyVariable)
					]
				)
			'''

			#set
			self.set(
				SettedGetKeyVariable,
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
			if type(self.SettingValueVariable) in [tuple,list]:

				#/###################/
				# map get with the PathDerivePather
				#

				#get
				#self.GettingNewBool=False
				#SettedLiargVariablesList=self[SetMapGetGrabStr](
				#	*self.SettingValueVariable
				#).ItemizedMapValueVariablesList
				#self.GettingNewBool=True
				SettedLiargVariablesList=self.SettingValueVariable

			elif hasattr(self.SettingValueVariable,'items'):

				#/###################/
				# dict get with the PathDerivePather
				#

				#Temp
				SettedSettingKeyVariable=self.SettingKeyVariable

				#call a set to active the #value get
				self.set(
						'TempSetVariable',
						self.SettingValueVariable
					)

				#debug
				self.debug(
						[
							'This is a get dict ',
							'self.TempSetVariable is '+SYS._str(self.TempSetVariable),
							('self.',self,['SettingValueVariable'])
						]
					)

				#get
				SettedLiargVariablesList=self.TempSetVariable if type(
					self.TempSetVariable)==list else [self.TempSetVariable]

				#reupdate
				self.SettingKeyVariable=SettedSettingKeyVariable

			else:

				#/###################/
				# list and get
				#

				#get
				#SettedLiargVariablesList=[self[self.SettingValueVariable]]
				SettedLiargVariablesList=[self.SettingValueVariable]

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
		if self.GettingKeyVariable==SetSetterShortStr:

			#get
			self.GettedValueVariable=self.SetDeriveSetter

			#return 
			return {'HookingIsBool':False}
		
		#call the base method
		return BaseClass.get(self)


#</DefineClass>
