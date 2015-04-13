# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Numscipyer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Processer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Numscipyer','Numscipy','Numscipying','Numscipied')
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class NumscipyerClass(BaseClass):
	
	def default_init(self,
			_NumscipyingRowsInt=0,
			_NumscipyingColsInt=0,
			_NumscipyingSizeTuple=None,
			_NumscipyingMeanFloat=0.,
			_NumscipyingStdFloat=1.,
			_NumscipyingNormalisationFunction=None,
			_NumscipyingDivideVariable=None,
			_NumscipyingStatStr="norm",
			_NumscipyingDiagFloatsArray=None,
			_NumscipyingSpecificTagVariablesArray=None,
			_NumscipyingRowTagVariablesArray=None,
			_NumscipyingColTagVariablesArray=None,
			_NumscipiedStatFunction=None,
			_NumscipiedRandomFloatsArray=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_numscipy(
				self,
			):	

		#/#################/#
		# Build the possible random numscipy
		#

		#debug
		'''
		self.debug(
				[
					'We numscipy here'
				]
			)
		'''
		
		#Check
		if self.NumscipyingStatStr!="":

			#import
			import scipy.stats

			#get
			self.NumscipiedStatFunction=getattr(
				scipy.stats,
				self.NumscipyingStatStr
			).rvs

		#set
		if self.NumscipyingSizeTuple==None or len(self.NumscipyingSizeTuple)==0 :
			self.NumscipyingSizeTuple=(self.NumscipyingRowsInt,self.NumscipyingColsInt)

		#debug
		'''
		self.debug(('self.',self,['NumscipyingSizeTuple']))
		'''

		#Check
		if self.NumscipyingStatStr=='norm':

			#debug
			'''
			self.debug(
				[
					'This is a random norm distribution',
					('self.',self,[
							'NumscipyingMeanFloat',
							'NumscipyingStdFloat'
						])
				]
			)
			'''
			
			#set
			self.NumscipiedRandomFloatsArray=self.NumscipyingStdFloat*self.NumscipiedStatFunction(
				self.NumscipyingMeanFloat,
				size=self.NumscipyingSizeTuple
			)

		#Check
		if self.NumscipyingDivideVariable!=None:
			self.NumscipiedRandomFloatsArray=(
				self.NumscipiedRandomFloatsArray.T/self.NumscipyingDivideVariable
			).T
		
		#Check
		if self.NumscipyingNormalisationFunction!=None and len(
			self.NumscipyingSizeTuple) and self.NumscipyingSizeTuple[0]==self.NumscipyingSizeTuple[1]:

				#normalize
				self.NumscipiedRandomFloatsArray/=self.NumscipyingNormalisationFunction(
					self.NumscipyingSizeTuple[0]
				)

		#Check
		if type(self.NumscipyingDiagFloatsArray)!=None.__class__ and len(
			self.NumscipyingDiagFloatsArray)==np.shape(
				self.NumscipiedRandomFloatsArray
			)[0]:

			#debug
			'''
			self.debug(('self.',self,['NumscipyingDiagFloatsArray']))
			'''
			
			#map
			map(
					lambda __RowInt,__NumscipyingDiagFloat:
					self.NumscipiedRandomFloatsArray.__setitem__(
						(__RowInt,__RowInt),
						__NumscipyingDiagFloat
					),
					xrange(len(self.NumscipiedRandomFloatsArray)),
					self.NumscipyingDiagFloatsArray
				)
	

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Remove the num scipy array if None
			#

			#Check
			if type(self.NumscipiedRandomFloatsArray)!=None.__class__:

				#get the shape
				ShapeList=np.shape(self.PrintingCopyVariable.NumscipiedRandomFloatsArray)

				#get a str repr
				self.PrintingCopyVariable.NumscipiedRandomFloatsArray='< numscipy array of shape '+str(ShapeList)+' >'

				#forcePrint
				self.forcePrint(
					['NumscipiedRandomFloatsArray'],
					'NumscipierClass'
				)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>


#</DefinePrint>
NumscipyerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NumscipyingRowsInt',
		'NumscipyingColsInt',
		'NumscipyingSizeTuple',
		'NumscipyingMeanFloat',
		'NumscipyingStdFloat',
		'NumscipyingNormalisationFunction',
		'NumscipyingDivideVariable',
		'NumscipyingStatStr',
		'NumscipyingDiagFloatsArray',
		'NumscipyingSpecificTagVariablesArray',
		'NumscipyingRowTagVariablesArray',
		'NumscipyingColTagVariablesArray',
		'NumscipiedStatFunction',
		'NumscipiedRandomFloatsArray'
	]
)
#<DefinePrint>
