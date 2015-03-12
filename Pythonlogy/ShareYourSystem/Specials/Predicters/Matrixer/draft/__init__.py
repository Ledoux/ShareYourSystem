# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import types
BaseModuleStr="ShareYourSystem.Standards.Controllers.Systemer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Matrixer','Matrix','Matrixing','Matrixed')
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getNullFloatsArray(_FloatsArray, _RtolFloat=1e-5):
	u, s, v = np.linalg.svd(_FloatsArray)
	RankInt = (s > _RtolFloat*s[0]).sum()
	return v[RankInt:].T.copy()
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class MatrixerClass(BaseClass):
	
	def default_init(self,
						_MatrixingNumpyVariable=None,
						_MatrixingRowsInt=0,
						_MatrixingColsInt=0,
						_MatrixingStatStr='norm',
						_MatrixingMeanFloat=0.,
						_MatrixingStdFloat=1.,
						_MatrixingNormalisationInt=1,		
						_MatrixedNumpyVariable=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_matrix(self):

		

		#Check
		if self.MatrixingNumpyVariable!=None:

			#/#################/#
			# Direct set : 
			#

			#alias
			self.MatrixedNumpyVariable=self.MatrixingNumpyVariable

		else:

			#/#################/#
			# statistic set : 
			#

			#random
			self.MatrixedNumpyVariable=self.MatrixingStdFloat*getattr(
				scipy.stats,
				self.MatrixingStatStr
			).rvs(
				self.MatrixingMeanFloat,
				size=(
					self.MatrixingRowsInt,
					self.MatrixingColsInt
				)
			)/(self.MatrixingRowsInt**self.MatrixingNormalisationInt)

#</DefineClass>

#</DefinePrint>
MatrixerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'MatrixingNumpyVariable',
		'MatrixingRowsInt',
		'MatrixingColsInt',
		'MatrixingStatStr',
		'MatrixingMeanFloat',
		'MatrixingStdFloat',
		'MatrixingNormalisationInt',		
		#'MatrixedNumpyVariable'
	]
)
#<DefinePrint>