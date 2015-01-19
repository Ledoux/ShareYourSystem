# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Recuperater instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Joiner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class RecuperaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'RecuperatingRetrieveList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_RecuperatingRetrieveList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_recuperate(self):

		#retrieve
		self.retrieve(self.RecuperatingRetrieveList)

		#debug
		self.debug(('self',self,['RetrievedPickOrderedDict']))
		

#</DefineClass>

