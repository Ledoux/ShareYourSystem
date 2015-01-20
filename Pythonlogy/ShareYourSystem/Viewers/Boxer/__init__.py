# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Boxer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Viewers.Viewer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class BoxerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'BoxingInitWidthInt',
								'BoxingInitHeigthInt',
								'BoxedWidthInt',
								'BoxedHeigthInt',
							]

	def default_init(self, 
						_BoxingInitWidthInt=400,
						_BoxingInitHeigthInt=100,
						_BoxingStepWidthInt=10,
						_BoxingStepHeightInt=10,
						_BoxedWidthInt=0,
						_BoxedHeigthInt=0,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_box(self):
		
		#parent first
		self.parent(['MeteoredConcurrentDDPClientVariable'])

		#debug
		self.debug(('self.',self,['ParentedGrandParentVariablesList']))

		#insert  box
		self.MeteoredConcurrentDDPClientVariable.call(
				'control',
				'boxes',
				'insert',
				{
					'x':self.BoxingInitWidthInt,
					'y':self.BoxingInitHeigthInt
				}
			)

#</DefineClass>