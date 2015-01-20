# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Executer can exec commands with the six.exec_ function
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Grasper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import six
#</ImportSpecificModules>

#<DefineLocals>
ExecutingPrefixStr="Exec_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ExecuterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ExecutingPrefixStr'
								]

	def default_init(self,
				_ExecutingPrefixStr="" ,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_get(self):

		#Check
		if self.GettingKeyVariable.startswith(ExecutingPrefixStr):

			#Definition the ExecStr
			self.ExecutingPrefixStr=ExecutingPrefixStr.join(
				self.GettingKeyVariable.split(ExecutingPrefixStr)[1:])

			#debug
			'''
			self.debug(('self.',self,['ExecutingPrefixStr']))
			'''

			#Put the output in a local Local Variable
			self.execute()

		#debug
		'''
		self.debug('BaseClass.get is '+str(BaseClass.get))
		'''

		#Call the parent get method
		return BaseClass.get(self)

	def mimic_set(self):

		#Check
		if type(self.SettingValueVariable
			) in SYS.StrTypesList and self.SettingValueVariable.startswith(
			ExecutingPrefixStr):

			#Definition the ExecStr
			self.ExecutingPrefixStr=ExecutingPrefixStr.join(
				self.SettingValueVariable.split(ExecutingPrefixStr)[1:])

			#debug
			'''
			self.debug(('self.',self,['ExecutingPrefixStr',"SettingValueVariable"]))
			'''

			#Put the output in a local Local Variable
			self.execute()

			#debug
			'''
			self.debug(('self.',self,['ExecutingPrefixStr',"SettingValueVariable"]))
			'''

		#Call the parent get method
		BaseClass.set(self)

	def do_execute(self):

		#debug
		'''
		self.debug(('self.',self,['ExecutingPrefixStr']))
		'''
		
		#Execute
		six.exec_(self.ExecutingPrefixStr,locals())


#</DefineClass>
