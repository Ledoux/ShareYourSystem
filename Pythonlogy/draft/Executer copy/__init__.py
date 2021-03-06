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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Grasper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import six
#</ImportSpecificModules>

#<DefineLocals>
ExecutionPrefixStr="Exec_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ExecuterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ExecutionPrefixStr'
								]

	def default_init(self,
				_ExecutionPrefixStr="" ,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_get(self):

		#Check
		if self.GettingKeyVariable.startswith(ExecutionPrefixStr):

			#Definition the ExecStr
			self.ExecutionPrefixStr=ExecutionPrefixStr.join(
				self.GettingKeyVariable.split(ExecutionPrefixStr)[1:])

			#debug
			'''
			self.debug(('self.',self,['ExecutionPrefixStr']))
			'''

			#Put the output in a local Local Variable
			self.execute()

		#debug
		'''
		self.debug('BaseClass.get is '+str(BaseClass.get))
		'''

		#Call the parent get method
		return BaseClass.get(self).GettedValueVariable

	def mimic_set(self):

		#Check
		if type(self.SettingValueVariable
			) in SYS.StrTypesList and self.SettingValueVariable.startswith(
			ExecutionPrefixStr):

			#Definition the ExecStr
			self.ExecutionPrefixStr=ExecutionPrefixStr.join(
				self.SettingValueVariable.split(ExecutionPrefixStr)[1:])

			#debug
			'''
			self.debug(('self.',self,['ExecutionPrefixStr',"SettingValueVariable"]))
			'''

			#Put the output in a local Local Variable
			self.execute()

			#debug
			'''
			self.debug(('self.',self,['ExecutionPrefixStr',"SettingValueVariable"]))
			'''

		#Call the parent get method
		BaseClass.set(self)

	def do_execute(self):

		#debug
		'''
		self.debug(('self.',self,['ExecutionPrefixStr']))
		'''
		
		#Execute
		six.exec_(self.ExecutionPrefixStr,locals())


#</DefineClass>
