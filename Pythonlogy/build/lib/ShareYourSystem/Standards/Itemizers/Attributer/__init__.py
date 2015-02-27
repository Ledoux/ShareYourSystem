# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

An Attributer instance has a __setitem__ method for setting things in the <InstanceVariable>.__dict__
This is helpful for setting Propertized mutable variables in the instance different 
from the propertized value setted at the level of the class

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Arrayer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
AttributionInstancePrefixStr='<Instance>'
AttributionClassPrefixStr='<Class>'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class AttributerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'AttributingKeyStr',
								'AttributingValueVariable',
								'AttributingInstanceBool',
								'AttributingClassBool'
							]

	def default_init(self,  
						_AttributingKeyStr="",
						_AttributingValueVariable=None,
						_AttributingInstanceBool=True,
						_AttributingClassBool=False,			
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)


	def do_attribute(self):

		#debug
		self.debug(
				('self.',self,['AttributingKeyStr','AttributingValueVariable'])
			)

		#Check
		if self.AttributingInstanceBool:

			#debug
			self.debug(
					'We set attribute in the instance here'
				)

			#Call the set
			self[self.AttributingKeyStr]=self.AttributingValueVariable

		elif self.AttributingClassBool:

			#debug
			self.debug(
					'We set attribute in the class here'
				)

			#set
			setattr(
				self.__class__,
				self.AttributingKeyStr,
				self.AttributingValueVariable
			)

	def mimic_get(self):

		#get
		if type(self.GettingKeyVariable
			)==str:

			#Check
			if self.GettingKeyVariable.startswith(AttributionInstancePrefixStr):

				#debug
				'''
				self.debug('We are going to get into the instance')
				'''

				#get
				self.GettedValueVariable=self.__dict__[
					SYS.deprefix(
						self.GettingKeyVariable,
						AttributionInstancePrefixStr
					)
				]

				#Stop the setting
				return {'HookingIsBool':False}

			elif self.GettingKeyVariable.startswith(AttributionClassPrefixStr):

				#debug
				'''
				self.debug('We are going to get from the class')
				'''

				#Path
				self.GettedValueVariable=self.__class__.__dict__[
					SYS.deprefix(
						self.GettingKeyVariable,
						AttributionClassPrefixStr
					)
				]

				#Stop the setting
				return {'HookingIsBool':False}

		#return 
		return BaseClass.get(self)

	def mimic_set(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
		'''

		#Check
		if type(self.SettingKeyVariable
			)==str:

			#Check
			if self.SettingKeyVariable.startswith(AttributionInstancePrefixStr):

				#debug
				'''
				self.debug('We are going to attribute to the instance')
				'''

				#Path
				self.attribute(
					SYS.deprefix(
						self.SettingKeyVariable,
						AttributionInstancePrefixStr
					),
					self.SettingValueVariable,
					_InstanceBool=True,
					_ClassBool=False
				)

				#Stop the setting
				return {'HookingIsBool':False}

			elif self.SettingKeyVariable.startswith(AttributionClassPrefixStr):

				#debug
				'''
				self.debug('We are going to attribute to the class')
				'''

				#Path
				self.attribute(
					SYS.deprefix(
						self.SettingKeyVariable,
						AttributionClassPrefixStr
					),
					self.SettingValueVariable,
					_InstanceBool=False,
					_ClassBool=True,
				)

				#Stop the setting
				return {'HookingIsBool':False}

			
		#Set and return 
		return BaseClass.set(self)
			


#</DefineClass>
