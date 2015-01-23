# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Matrixer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Controllers.Systemer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MatrixerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'MatrixingNumpyVariable',
								'MatrixingRowsInt',
								'MatrixingColsInt',
								'MatrixingSizeTuple',
								'MatrixingMeanFloat',
								'MatrixingStdFloat',
								'MatrixingNormalisationFunction',
								'MatrixingStatStr',
								'MatrixedStatFunction',
								'MatrixedNumpyVariable'
							]

	def default_init(self,
						_MatrixingNumpyVariable=None,
						_MatrixingRowsInt=0,
						_MatrixingColsInt=0,
						_MatrixingSizeTuple=None,
						_MatrixingMeanFloat=0.,
						_MatrixingStdFloat=1.,
						_MatrixingNormalisationFunction=None,
						_MatrixingStatStr="norm",
						_MatrixedStatFunction=None,
						_MatrixedNumpyVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_matrix(
				self,
			):	

		#set
		if self.MatrixingStatStr!="":

			#import
			import scipy.stats

			#get
			self.MatrixedStatFunction=getattr(
				scipy.stats,
				self.MatrixingStatStr
			).rvs

		#set
		if self.MatrixingSizeTuple==None:
			self.MatrixingSizeTuple=(self.MatrixingRowsInt,self.MatrixingColsInt)

		#Check
		if self.MatrixingStatStr=='norm':

			#set
			self.MatrixedNumpyVariable=self.MatrixingStdFloat+self.MatrixedStatFunction(
				self.MatrixingMeanFloat,size=self.MatrixingSizeTuple
			)

		#Check
		if self.MatrixingNormalisationFunction!=None and len(
			self.MatrixingSizeTuple) and self.MatrixingSizeTuple[0]==self.MatrixingSizeTuple[1]:

				#normalize
				self.MatrixedNumpyVariable/=self.MatrixingNormalisationFunction(
					self.MatrixingSizeTuple[0]
				)

	
#</DefineClass>
