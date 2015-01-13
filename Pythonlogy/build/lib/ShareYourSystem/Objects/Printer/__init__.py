# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Printer is an object that can directly print 
Strs in the Representer context.

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Initiator"
DecorationModuleStr="ShareYourSystem.Classors.Representer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Representer=DecorationModule
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class PrinterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'PrintingVariable'
								]
	
	def default_init(self,
						_PrintingVariable=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	#<DefineDoMethod>	
	def do__print(self,**_KwargVariablesDict):

		#debug
		'''
		print('self.PrintingVariable is ',self.PrintingVariable)
		print('')
		'''

		#print
		print(
			Representer.getRepresentedStrWithVariable(
				self.PrintingVariable,
				**_KwargVariablesDict
				)
		)

#</DefineClass>

