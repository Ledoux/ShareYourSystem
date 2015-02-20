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
def getMapList(_LiargVariablesList):

	#Check
	if hasattr(_LiargVariablesList[0],'items'):
		return _LiargVariablesList[0].items()
	else:
		return _LiargVariablesList[0]
		
def getLiargVariablesList(_ValueVariable):
	return _ValueVariable
#</ImportSpecificModules>

#<DefineLocals>
SetEachPrefixStr="each*"
SetAllPrefixStr="all*"
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
			'''
			self.debug('SettedValueMethod is '+str(SettedValueMethod))
			'''

			#define
			try:

				#get
				SettedLiargVariablesList=SettedValueMethod.im_func.BaseDoClass.Module.getLiargVariablesList(
					self.SettingValueVariable
				)

				'''
				self.debug(
						'SettedLiargVariablesList is '+str(SettedLiargVariablesList)
					)
				'''
				
				#get the method and put the value as arguments
				SettedValueMethod(*SettedLiargVariablesList)

			except:

				#debug
				'''
				self.debug('call the SettedValueMethod with self.SettingValueVariable directly')
				'''

				#direct
				#SettedValueMethod(*self.SettingValueVariable)
				SettedValueMethod(self.SettingValueVariable)

			#debug
			

			#Stop the setting
			return {"HookingIsBool":False}

		#/####################/#
		# Case of a non method  with set with a set key str 
		#

		elif type(self.SettingKeyVariable
				)==str:

			#/####################/#
			# Case of each* set
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
						__SettedGetVariable['map*set'](
							__SettedValueVariable
						),
						SettedGetVariablesList,
						self.SettingValueVariable
					)

				#Return stop the setting
				return {'HookingIsBool':False}

			#/####################/#
			# Case of all* set
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
							__SettedGetVariable['map*set'](
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
							self.debug(
								[
									'we wrap the setting value',
									('self.',self,['SettingValueVariable'])
								]
							)

							#alias
							'''
							try:
							'''

							#map set
							self.SettingValueVariable=SettedValueType(
								)['map*set'](
								self.SettingValueVariable
							)

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
					[
						'we just set in the __dict__',
						('self.',self,[
								'SettingKeyVariable',
								'SettingValueVariable'
							])
					]
				)
				'''

				#map
				'''
				if type(self.SettingKeyVariable)==SYS.MapListClass:

					#map
					map(
							lambda __MappedVariable:
							self.__setitem__(
								*__MappedVariable
							),
							self.SettingKeyVariable
						)

					#Return an output dict
					return {"HookingIsBool":False}
				else:
				'''

				#__setitem__ in the __dict__, this is an utility set
				self.__dict__[
					self.SettingKeyVariable
				]=self.SettingValueVariable

				#add in the SettingValue
				try:
					self.SettingValueVariable.DictKeyStr=self.SettingKeyVariable
					#self.SettingValueVariable.DictDeriveSetter=self
				except:
					pass

				#Return
				return {'HookingIsBool':False}

		#/####################/#
		# Case of a non method  with set with a set dict
		#

		elif hasattr(self.SettingKeyVariable,'items'):

			#debug
			self.debug(
					[
						'SettingKeyVariable has items...',
						('self.',self,['SettingKeyVariable'])
					]
				)

			try:

				#debug
				self.debug(
						'We set with a GetKeyVariable'
					)

				#set
				self.set(
					self.SettingKeyVariable['GetKeyVariable'],
					self.SettingValueVariable
				)

				#delete
				del self.SettingKeyVariable['GetKeyVariable']

			except:

				#debug
				self.debug(
						'We set with a SetKeyVariable'
					)

				#set
				self.set(
					self.SettingKeyVariable['SetKeyVariable'],
					SYS.update(
						self.SettingKeyVariable,
						self.SettingValueVariable
					)
				)

				#delete
				del self.SettingKeyVariable['SetKeyVariable']

			#Return
			return {'HookingIsBool':False}



#</DefineClass>
