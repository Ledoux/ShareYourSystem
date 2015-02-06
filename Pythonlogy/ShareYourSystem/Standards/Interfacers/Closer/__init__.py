# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Closer
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Filer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Closer","Close","Closing","Closed"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class CloserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								]

	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_close(self):

		#close
		self.FiledFileVariable.close()

		#Close the HdformatedFileVariable
		if hasattr(self,'hdfclose'):
			self.hdfclose()

		#Close the HdformatedFileVariable
		if hasattr(self,'mongoclose'):
			self.mongoclose()
	
#</DefineClass>

