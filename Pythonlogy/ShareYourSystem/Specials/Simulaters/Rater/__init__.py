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
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Pydelayer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineFunctions>
from ShareYourSystem.Specials.Simulaters import Rater
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class RaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'RatingTimeConstantVariable',
								'RatedPostFloatsArray'
							]

	def default_init(self,
						_RatingUnitsInt=0,
						_RatingTimeConstantVariable=1.,
						_RatingDelayTimeFloat=0.,
						_RatingWeigthFloat=0.,
						_RatingSymmetryFloat=0.,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#collect
		self.collect(
			'Equationers',
			'RateEquationer',
			SYS.EquationerClass(
			).collect(
				'JacobianMatrixers',
				'Leak',
				SYS.MatrixerClass(
					).matrix(
						_SizeTuple=(2,2),
						_StdFloat=0.,
						_DiagFloatsArray=np.array([-1.,-1.])
					)
			).collect(
				'JacobianMatrixers',
				'Delay',
				SYS.MatrixerClass(
					).matrix(
						_SizeTuple=(2,2),
						_TagVariablesArray=np.array(
							[
								[{},{'DelayFloat':5.}],
								[{'DelayFloat':5.},{}]
							]
						)
					)
			).equation(
			)
	)


	def do_rate(
				self,
			):	

		pass
		


		

#</DefineClass>
