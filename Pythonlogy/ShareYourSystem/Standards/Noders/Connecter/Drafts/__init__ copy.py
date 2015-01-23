# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Connecters...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Settler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConnecterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ConnectingGetStrsTuple',
									'ConnectedPrePointedVariable',
									'ConnectedPostPointedVariable'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_ConnectingGetStrsTuple=None,
						_ConnectedPrePointedVariable=None,
						_ConnectedPostPointedVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	def do_connect(self):	

		#debug
		'''
		self.debug(('self.',self,['ConnectingGetStrsTuple']))
		'''
		
		#link
		self.link(
					[
						[self.ConnectingGetStrsTuple[0],'ConnectedPre'],
						[self.ConnectingGetStrsTuple[1],'ConnectedPost']
					]
				)
		
		#Return self
		#return self

#</DefineClass>
