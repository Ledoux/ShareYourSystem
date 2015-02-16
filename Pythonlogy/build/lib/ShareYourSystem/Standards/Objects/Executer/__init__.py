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
BaseModuleStr="ShareYourSystem.Standards.Objects.Debugger"
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
		'ExecutingCodeStr'
	]

	def default_init(self,
				_ExecutingCodeStr="" ,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_execute(self):

		#debug
		'''
		self.debug(('self.',self,['ExecutingCodeStr']))
		'''
		
		#Execute
		six.exec_(self.ExecutingCodeStr,locals())


#</DefineClass>
