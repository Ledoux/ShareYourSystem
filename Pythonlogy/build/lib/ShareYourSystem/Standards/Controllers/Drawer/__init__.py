# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Displayer
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Controllers.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Drawer','Draw','Drawing','Drawn')
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DrawerClass(BaseClass):

	def default_init(self,
						_DrawingSetVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_draw(self):

		#team
		self.team('Views')

		#map set
		self.TeamDict['Views']['#map@set'](
			self.DrawingSetVariable
		)

#</DefineClass>

#</DefinePrint>
DrawerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'DrawingSetVariable'
	]
)
#<DefinePrint>
