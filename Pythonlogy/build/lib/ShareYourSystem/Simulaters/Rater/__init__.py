# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Rater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Dynamizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineFunctions>
def RateJacUnboundFunction(
				_InstanceVariable,
				_FloatsArray,
				**_KwargVariablesDict
			):

	return (_FloatsArray+_InstanceVariable.RatingExternalFloatsArray
		)/_InstanceVariable.RatingTimeConstantVariable

#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class RaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'RatingMatrixStr',
								'RatedPreStr'
							]

	def default_init(self,
						_RatingTimeConstantVariable=1.,
						_RatedPostFloatsArray"",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.EuleringJacUnboundFunction=RateJacUnboundFunction

	def do_rate(
				self,
			):	

		pass
		


		

#</DefineClass>
