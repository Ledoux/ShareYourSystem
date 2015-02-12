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

			#get
			SettedValueMethod=self[self.SettingKeyVariable]

			#debug
			self.debug('SettedValueMethod is '+str(SettedValueMethod))

			#define
			try:

				#get
				SettedLiargVariablesList=SettedValueMethod.im_func.DoClass.Module.getLiargVariablesList(
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

				#direct
				SettedValueMethod(self.SettingValueVariable)

			#debug
			

			#Stop the setting
			return {"HookingIsBool":False}

		#/############################
		# Case of a non method get 
		#

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
