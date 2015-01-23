# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Eulerer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class EulererClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'EuleringPreFloatsArray',
		'EuleringJacMethodStr',
		'EuleringStepTimeFloat',
		'EuleredPostFloatsArray',
	]

	def default_init(self,
						_EuleringPreFloatsArray=None,
						_EuleringJacMethodStr="euler_null",
						_EuleringStepTimeFloat=0.1,
						_EuleredPostFloatsArray=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)


	def euler_null(self):

		#return
		return np.zeros(
			len(self.EuleringPreFloatsArray)
		)

	def do_euler(
				self,
				**_KwargVariablesDict
			):	

		#debug
		'''
		self.debug(('self.',self,[
								'EuleringJacMethodStr'
							]))
		'''
		
		#Do euler
		self.EuleredPostFloatsArray=self.EuleringPreFloatsArray+getattr(
			self,self.EuleringJacMethodStr)()*self.EuleringStepTimeFloat

#</DefineClass>
