# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Killer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Statuser"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Killer","Kill","Killing","Killed"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class KillerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_kill(self):

		#first status
		self.status()

		#debug
		'''
		self.debug(('self.',self,['StatusedIdStrsList']))
		'''
		
		#map kill the other previous process
		if self.StatusingProcessStr=='Python' and len(self.StatusedIdStrsList)>1:
			map(
				lambda __IdStr:
				os.popen("kill "+__IdStr),
				sorted(self.StatusedIdStrsList)[:-1]
			)

		#Return self
		#return self

#</DefineClass>
