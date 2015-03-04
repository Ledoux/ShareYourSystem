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

	#Debug
	'''
	print('Setter l 31')
	print('_LiargVariablesList is ')
	print(_LiargVariablesList)
	print('')
	'''

	#Check
	if len(_LiargVariablesList)==1:

		#Check
		if hasattr(_LiargVariablesList[0],'items'):
			return _LiargVariablesList[0].items()
		else:
			return _LiargVariablesList[0]

	else:

		#return the total
		return _LiargVariablesList
		
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
SetModifyGrabStr='#set'
SetUndirectPrefixStr=Getter.GetUndirectPrefixStr
SetLiargGrabStr='#liarg'
SetLiargGrabPrefixStr=SetLiargGrabStr+':'
SetLiargGetGrabStr=SetLiargGrabPrefixStr+Getter.GetUndirectStr
SetMapLiargGetGrabStr=SetLiargGrabPrefixStr+Getter.GetMapStr
SetKwargGrabStr='#kwarg'
SetKwargGrabPrefixStr=SetKwargGrabStr+':'
SetKwargGetGrabStr=SetKwargGrabPrefixStr+Getter.GetUndirectStr
SetKwargGetGrabPrefixStr=SetKwargGetGrabStr+':'
SetMapKwargGetGrabPrefixStr=SetKwargGrabPrefixStr+Getter.GetMapStr+':'
SetMapKwargGetKeyGrabStr=SetMapKwargGetGrabPrefixStr+'#key'
SetMapKwargGetValueGrabStr=SetMapKwargGetGrabPrefixStr+'#value'
SetMapKwargGetKeyValueGrabStr=SetMapKwargGetGrabPrefixStr+'#key:value'
SetListTypesSet=set(['list','ndarray'])
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class SetterClass(BaseClass):

	def default_init(self,
						_SetTagStr="",
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
		#self.SetTagStr=""
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
			'''
			self.debug(
					[
						'SettedValueMethod is '+SYS._str(SettedValueMethod),
						'Before calling the itemized method, we adapt the liarg',
						('self.',self,['SettingValueVariable'])
					]
				)
			'''

			#Temp
			SettedTempLiargSettingValueVariable=self.SettingValueVariable
			SettedLiargSettingValueVariable=SettedTempLiargSettingValueVariable
			SettedKwargSettingValueVariable=None

			#Check
			if hasattr(
					SettedTempLiargSettingValueVariable,'items'
				):

				#debug
				'''
				self.debug(
						[
							'Check for a set value dict',
						]
					)
				'''

				#/###################/#
				# Check for #liarg
				#

				if SetLiargGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we itemize with a value with a SetValueGrabStr inside',
							'SettedTempLiargSettingValueVariable is '+SYS._str(SettedTempLiargSettingValueVariable)
						]
					)
					'''

					#set
					SettedLiargSettingValueVariable=SettedTempLiargSettingValueVariable[
						SetLiargGrabStr
					]

				elif SetMapLiargGetGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we set a value with a map SetMapValueGetGrabStr inside',
						]
					)
					'''

					#set
					SettedLiargSettingValueVariable=self[
						SYS.deprefix(
							SetMapLiargGetGrabStr,
							SetLiargGrabPrefixStr
						)
					](
						*SettedTempLiargSettingValueVariable[SetMapLiargGetGrabStr]
					).ItemizedMapValueVariablesList
					
				#Check
				elif SetLiargGetGrabStr in SettedTempLiargSettingValueVariable:

					#Get 
					SettedLiargSettingValueVariable=self[
						SettedTempLiargSettingValueVariable[SetLiargGetGrabStr]
					]

					#debug
					'''
					self.debug(
						[
							'we set a value with a SetLiargGetGrabStr inside',
						]
					)
					'''

				#/###################/#
				# Check for #kwarg
				#

				#Check
				if SetKwargGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					self.debug(
							[
								'There is a #kwarg here'
							]
						)

					#get
					SettedKwargSettingValueVariable=SettedTempLiargSettingValueVariable[
						SetKwargGrabStr
					]

				elif SetMapKwargGetKeyGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we set a value with a map SetMapKwargGetKeyGrabStr inside',
						]
					)
					'''

					#get get the keys
					SettedKeyVariablesList=self[
						Getter.GetMapStr
					](
						*SettedTempLiargSettingValueVariable[SetMapKwargGetKeyGrabStr].keys()
					).ItemizedMapValueVariablesList

					#get the values
					SettedValueVariablesList=SettedTempLiargSettingValueVariable[
						SetMapKwargGetKeyGrabStr
					].values()

					#set
					SettedKwargSettingValueVariable=dict(
						zip(
							SettedKeyVariablesList,
							SettedValueVariablesList
						)
					)
					
				elif SetMapKwargGetValueGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we set a value with a map SetMapKwargGetValueGrabStr inside',
						]
					)
					'''

					#get get the keys
					SettedKeyVariablesList=SettedTempLiargSettingValueVariable[
						SetMapKwargGetValueGrabStr
					].keys()

					#get the values
					SettedValueVariablesList=self[
						Getter.GetMapStr
					](
						*SettedTempLiargSettingValueVariable[
						SetMapKwargGetValueGrabStr
					].values()
					).ItemizedMapValueVariablesList

					#set
					SettedKwargSettingValueVariable=dict(
						zip(
							SettedKeyVariablesList,
							SettedValueVariablesList
						)
					)

				elif SetMapKwargGetKeyValueGrabStr in SettedTempLiargSettingValueVariable:

					#debug
					'''
					self.debug(
						[
							'we set a value with a map SetMapKwargGetKeyValueGrabStr inside',
						]
					)
					'''

					#get get the keys
					SettedKeyVariablesList=self[
						Getter.GetMapStr
					](
						*SettedTempLiargSettingValueVariable[
							SetMapKwargGetKeyValueGrabStr
						].keys()
					).ItemizedMapValueVariablesList

					#get the values
					SettedValueVariablesList=self[
						Getter.GetMapStr
					](
						*SettedTempLiargSettingValueVariable[
							SetMapKwargGetKeyValueGrabStr
						].values()
					).ItemizedMapValueVariablesList

					#set
					SettedKwargSettingValueVariable=dict(
						zip(
							SettedKeyVariablesList,
							SettedValueVariablesList
						)
					)


			#get the 
			#SettedLiargVariable=self[self.SettingValueVariable]
			SettedLiargVariable=SettedLiargSettingValueVariable
			SettedKwargVariable=SettedKwargSettingValueVariable
			
			#debug
			'''
			self.debug(
				[
					'SettedValueMethod is '+SYS._str(SettedValueMethod),
					'SettedLiargVariable is '+SYS._str(SettedLiargVariable),
					'SettedKwargVariable is '+SYS._str(SettedKwargVariable)
				]
			)
			'''

			#define
			try:

				#get
				SettedLiargVariablesList=SettedValueMethod.im_func.BaseDoClass.Module.getLiargVariablesList(
					SettedLiargVariable
				)

				#debug
				'''
				self.debug(
						'SettedLiargVariablesList is '+str(SettedLiargVariablesList)
					)
				'''
				
				if SettedKwargVariable!=None:

					#get the method and put the value as arguments
					SettedValueMethod(*SettedLiargVariablesList,**SettedKwargVariable)

				else:

					#get the method and put the value as arguments
					SettedValueMethod(*SettedLiargVariablesList)

				#Stop the setting
				return {"HookingIsBool":False}

			except:

				#debug
				'''
				self.debug(
					[
						'call the SettedValueMethod with self.SettingValueVariable directly',
						'SettedLiargVariable is '+SYS._str(SettedLiargVariable)
					]
				)
				'''
				
				#Check
				if hasattr(SettedLiargVariable,'items'):
					SettedLiargVariable=SettedLiargVariable.items()
				elif type(SettedLiargVariable)!=list:
					SettedLiargVariable=[SettedLiargVariable]

				#Check
				if SettedKwargVariable!=None:

					#direct
					#SettedValueMethod(*self.SettingValueVariable)
					SettedValueMethod(*SettedLiargVariable,**SettedKwargVariable)

				else:

					#direct
					#SettedValueMethod(*self.SettingValueVariable)
					SettedValueMethod(*SettedLiargVariable)
			
				#Stop the setting
				return {"HookingIsBool":False}

		#/####################/#
		# Case of a non method  with set with a set key str 
		#

		elif type(
			self.SettingKeyVariable
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
				SettedTempLiargSettingValueVariable=self.SettingValueVariable

				#get
				SettedEachGetVariable=self[
					SYS.deprefix(
						self.SettingKeyVariable,
						SetEachPrefixStr
					)
				]

				#debug
				'''
				self.debug(
					[
						'We each here',
						('self.',self,['SettingKeyVariable']),
						'SettedEachGetVariable is '+str(SettedEachGetVariable)
					]
				)
				'''
				
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
						'SettedTempLiargSettingValueVariable is ',
						SYS._str(SettedTempLiargSettingValueVariable)
					]
				)
				'''
				
				#map
				map(
						lambda __SettedGetVariable,__SettedValueVariable:
						__SettedGetVariable[SetMapStr](
							SYS.SetList(__SettedValueVariable)
						),
						SettedEachGetVariablesList,
						SettedTempLiargSettingValueVariable
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
				# Case of a set with a #get in the value
				#

				if type(
					self.SettingValueVariable
				)==str and self.SettingValueVariable.startswith(SetUndirectPrefixStr):

					#deprefix
					SettedKeyStr=SYS.deprefix(
							self.SettingValueVariable,
							SetUndirectPrefixStr
						)

					#debug
					'''
					self.debug(
						[
							'This is a undirect of a str variable',
							'SettedKeyStr is '+SettedKeyStr
						]
					)
					'''

					#Check
					if SetUndirectPrefixStr in SettedKeyStr:

						#split
						SettedKeyStrsList=SettedKeyStr.split(SetUndirectPrefixStr)

						#define
						SettedRecursiveKeyStr=''.join(
							SettedKeyStrsList[:-1])+self[SettedKeyStrsList[-1]]

						#debug
						'''
						self.debug(
								[
									'This is a recursive undirect set',
									'SettedRecursiveKeyStr is '+SettedRecursiveKeyStr
								]
							)
						'''

						#set
						self[
							self.SettingKeyVariable
						]=SetUndirectPrefixStr+SettedRecursiveKeyStr

					else:

						#debug
						'''
						self.debug(
								'This is one level undirect set'
							)
						'''

						#set
						self[
							self.SettingKeyVariable
						]=self[SettedKeyStr]

					#Stop the getting
					return {"HookingIsBool":False}

				#/####################/#
				# Case of a set with a set dict
				#

				#Check
				elif hasattr(
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

					#type
					SettedSettingValueVariableType=type(self.SettingValueVariable)

					#Check
					if SettedValueType!=SettedSettingValueVariableType:

						#debug
						'''
						self.debug(
								[
									'Check that the type is not a lst and a numpy array'
								]
							)
						'''
						
						#Check
						if set([
							SettedValueType.__name__,
							SettedSettingValueVariableType.__name__
						])!=SetListTypesSet:

							#debug
							'''
							self.debug(
								[
									'SettedValueType is '+str(SettedValueType),
									('self.',self,['SettingKeyVariable'])
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
								'''
								self.debug(
									'Ok we have instanced'
								)
								'''

								#Return
								return {'HookingIsBool':False}

				#/####################/#
				# Check that it is not a property
				#

				#Check
				if hasattr(self.__class__,self.SettingKeyVariable):

					#get
					SettedPropertyValueVariable=getattr(self.__class__,self.SettingKeyVariable)
					
					#Check
					if type(SettedPropertyValueVariable)==property:

						#debug
						'''
						self.debug('It is a property set')
						'''

						#set the property
						setattr(
								self,
								self.SettingKeyVariable,
								self.SettingValueVariable
							)

						#Return
						return {'HookingIsBool':False}


				#/####################/#
				# Set in the __dict__ ... finally 
				# 

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

				#/####################/#
				# GIve maybe some things to the setted value 
				# 

				#add in the SettingValue
				try:
					self.SettingValueVariable.SetTagStr=self.SettingKeyVariable
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
			'''
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
			'''
			
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
				'''
				self.debug(
						[
							'This is a get dict ',
							'self.TempSetVariable is '+SYS._str(self.TempSetVariable),
							('self.',self,['SettingValueVariable'])
						]
					)
				'''

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
			'''
			self.debug(
				[
					'we call here',
					('self.',self,['SettingKeyVariable']),
					'SettedLiargVariablesList is '+SYS._str(SettedLiargVariablesList)
				]
			)
			'''

			#call
			self.SettingKeyVariable(
					*SettedLiargVariablesList	
				)

			#debug
			'''
			self.debug(
					'self.SettingKeyVariable.__self__ is '+SYS._str(
						self.SettingKeyVariable.__self__
					)
				)
			'''

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

#</DefinePrint>
SetterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'SetTagStr',
		'SetDeriveSetter',
		'SettingKeyVariable',
		'SettingValueVariable',
		'SettingItemBool',
		'SettingNewBool',
		'SettedValueVariable'
	]
)
#<DefinePrint>
