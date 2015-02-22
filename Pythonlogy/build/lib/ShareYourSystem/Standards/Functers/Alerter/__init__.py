# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Alerter is helping during the debug process. 
It is a shortcut decorating manner for saying to a method
to alert the console once the interpreter is about to go and 
leave its frame.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Functer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
AlertingStartStr="\n---- Start of the method : "
AlertingEndStr="\n---- End of the method : "
AlertingJumpStr=" ----\n"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class AlerterClass(BaseClass):
	def __init__(self,
						_AlertingFunction=None,
						_AlertingDebugBool=True,
						_AlertedStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Function):

		#Alert
		self.alert(_Function)

		#Link
		self.FunctedFunction=self.AlertedFunction
		
		#Return the DecoratedFunction
		return BaseClass.__call__(self,_Function)

	def do_alert(self):

		#set
		self.AlertedStr=self.AlertingFunction.__name__+' in '+"/".join(
			self.AlertingFunction.func_globals['__file__'].split('/')[-2:]
		)

		#Definition
		def AlertedFunction(*_LiargVariablesList,**_KwargVariablesDict):

			#Definition the InstanceVariable
			InstanceVariable=_LiargVariablesList[0]

			#Alert start
			if self.AlertingDebugBool:
				#InstanceVariable.__setattr__('DebuggingBacksInt',2)
				InstanceVariable.debug(
											[
												AlertingStartStr+self.AlertedStr+AlertingJumpStr
											],
											#No need of the frames ... because it is a bit redundant
											**{'DebuggingFrameBool':False}
									)
				InstanceVariable.DebuggingFrameBool=True
				#InstanceVariable.__setattr__('DebuggingBacksInt',1)
				
			#Call the DecoratingFunction
			OutputVariable=self.AlertingFunction(*_LiargVariablesList,**_KwargVariablesDict)

			#Alert end
			if self.AlertingDebugBool:

				InstanceVariable.debug(
											[
												AlertingEndStr+self.AlertedStr+AlertingJumpStr
											],
											#No need of the frames ... because it is a bit redundant
											**{'DebuggingFrameBool':False}
									)
				InstanceVariable.DebuggingFrameBool=True
				#InstanceVariable.__setattr__('DebuggingBacksInt',2)
				#InstanceVariable.debug('End of the method '+str(_Function.__name__)+'\n')
				#InstanceVariable.__setattr__('DebuggingBacksInt',1)

			return OutputVariable

		#set
		self.AlertedFunction=AlertedFunction

		#Return self
		return self
#</DefineClass>

