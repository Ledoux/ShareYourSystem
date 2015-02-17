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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Setter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import six
#</ImportSpecificModules>

#<DefineLocals>
ExecutionPrefixStr=">>"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ExecuterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'ExecutingCodeStr',
		'ExecutedLocalsDict'
	]

	def default_init(self,
				_ExecutingCodeStr="" ,
				_ExecutedLocalsDict=None,
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

		#alias
		self.ExecutedLocalsDict=locals()

	def mimic_get(self):

		#Check
		if type(self.GettingKeyVariable
			)==str and self.GettingKeyVariable.startswith(ExecutionPrefixStr):

			#deprefix
			ExecutedStr="ExecutedVariable="+SYS.deprefix(
						self.GettingKeyVariable,
						ExecutionPrefixStr
					)

			#debug
			'''
			self.debug('ExecutedStr is '+ExecutedStr)
			'''

			#execute
			self.execute(
					ExecutedStr
				)

			#alias
			self.GettedValueVariable=self.ExecutedLocalsDict['ExecutedVariable']

			#stop the getting
			return {'HookingIsBool':False}

		#Check
		else:

			#call the base method
			BaseClass.get(self)


#</DefineClass>
