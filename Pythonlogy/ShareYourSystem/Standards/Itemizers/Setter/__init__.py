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
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class SetterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'SettingKeyVariable',
									'SettingValueVariable',
									'SettingItemBool'
								]

	def default_init(self,
						_SettingKeyVariable=None, 
						_SettingValueVariable=None, 
						_SettingItemBool=True, 			
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

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
				SettedValueMethod(self.SettingValueVariable)

			#debug
			

			#Stop the setting
			return {"HookingIsBool":False}

		#/############################
		# Case of a non method get 
		#

		else:

			#Check
			if type(self.SettingKeyVariable
				)==str and self.SettingKeyVariable.startswith(
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
				self.debug(
					[
						'SettedGetVariablesList is ',
						SYS._str(SettedGetVariablesList),
						('self.',self,['SettingValueVariable'])
					]
				)

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

			else:

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

				#Return
				return {'HookingIsBool':False}

#</DefineClass>
