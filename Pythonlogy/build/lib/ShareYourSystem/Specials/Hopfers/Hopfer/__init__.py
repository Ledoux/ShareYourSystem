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
BaseModuleStr="ShareYourSystem.Standards.Recorders.Leaker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Hopfer','Hopf','Hopfing','Hopfed')
#</DefineAugmentation>

#<ImportSpecificModules>
Leaker=BaseModule
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class HopferClass(BaseClass):
	
	def default_init(self,
			_HopfingUnitsInt = 1,
			_HopfingDelayTimeFloat = 2.0,
			_HopfingConstantTimeFloat = 10.0,
			_HopfingMeanWeightFloat = 0.0,
			_HopfingStdWeightFloat = 1.0,
			_HopfingNormalisationInt= 0.5,
			_HopfingSymmetryFloat = 0.5,
			_HopfedLateralWeigthFloatsArray = None,
			_HopfedRealEigenvalueFloatsArray = None,
			_HopfedImagEigenvalueFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedHalfWidthFloat=0., 
			_HopfedContourComplexesArray=None, 
			_HopfedEigenComplex=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_hopf(self):

		#/###############/#
		# Build the laterals
		#

		#debug
		'''
		self.debug(
			[
				'Ok we build the laterals'
			]
		)
		'''

		#numscipy
		self.NumscipyingRowsInt=self.HopfingUnitsInt
		self.NumscipyingColsInt=self.HopfingUnitsInt
		self.NumscipyingStdFloat=self.HopfingStdWeightFloat
		self.NumscipyingMeanFloat=self.HopfingMeanWeightFloat
		self.NumscipyingSymmetryFloat=self.HopfingSymmetryFloat
		self.NumscipyingEigenvalueBool=True
		self.NumscipyingNormalisationFunction=lambda __ColsInt:__ColsInt**0.5
		self.numscipy(
			)

		#alias
		self.HopfedLateralWeigthFloatsArray=self.NumscipiedRandomFloatsArray

		#debug
		'''
		self.debug(
			[
				'We have setted the laterals',
				('self.',self,[
					'HopfedLateralWeigthFloatsArray'
				])
			]
		)
		'''

		#/###############/#
		# Determine the contour properties
		#

		#debug
		self.debug(
			[
				'We set the contour of the ellipse',
				('self.',self,[
						'NumscipiedVarianceFloat',
						'NumscipiedStdFloat',
						'NumscipiedCovarianceFloat',
						'NumscipiedSommersFloat'
					])
			]
		)

		#set
		self.HopfedHalfWidthFloat=self.HopfingUnitsInt*(
			#1.+self.NumscipiedCovarianceFloat
			1.+self.NumscipiedSommersFloat

		)
		self.HopfedHalfHeightFloat=self.HopfingUnitsInt*(
			#1.-self.NumscipiedCovarianceFloat
			1.-self.NumscipiedSommersFloat
		)

		#debug
		self.debug(
			[
				'We have the size of the ellipse',
				('self.',self,[
						'HopfedHalfWidthFloat',
						'HopfedHalfHeightFloat'
					])
			]
		)

		#/###############/#
		# Build the eigen values real and imag
		#

		#real and imag
		self.HopfedRealEigenvalueFloatsArray=np.real(self.NumscipiedEigenvalueComplexesArray)
		self.HopfedImagEigenvalueFloatsArray=np.imag(self.NumscipiedEigenvalueComplexesArray)

		#debug
		'''
		self.debug(
			[
				'We have built the real and imag',
				('self.',self,[
						'HopfedRealEigenvalueFloatsArray',
						'HopfedImagEigenvalueFloatsArray'
					])
			]
		)
		'''

		#/###############/#
		# Build the contour of the eigen values real and ima
		#

		self.HopfedContourComplexesArray=[
			__Float + (
				1.-self.NumscipiedSommersFloat
			)*np.sqrt(
				1-(__Float/(1+self.NumscipiedSommersFloat))**2
			)*1j for __Float in np.arange(
				-1.-self.NumscipiedSommersFloat,
				1.+self.NumscipiedSommersFloat,
				0.005
			)
		]
		self.HopfedContourComplexesArray+=list(
			np.array(
			self.HopfedContourComplexesArray
			).conjugate()[::-1]  
		)
		self.HopfedContourComplexesArray=np.array(
			self.HopfedContourComplexesArray
		)
          	      
		#/###############/#
		# Compute for each eigen of the contour a possible solution
		#

		#map
		HopfedSolutionFloatsTuplesList=map(
			lambda __HopfedContourComplex:
			self.setAttr(
				'HopfedEigenComplex',
				__HopfedContourComplex
			).getSolutionFloatsTuple(),
			self.HopfedContourComplexesArray
		)

		#debug
		self.debug(
			[
				'HopfedSolutionFloatsTuplesList is ',
				str(HopfedSolutionFloatsTuplesList)
			]
		)

		"""
			FinalContourEvals[i] = Sol[0] + Sol[1]*1j
			ContourList = ContourEvals
			TransformedContourList = list(FinalContourEvals)
			LEV = np.array(TransformedContourList)[np.argmax(np.array(TransformedContourList).real)]
			if LEV.real > 0:
			if np.abs(LEV.imag) == 0:
			    TheoreticalStability += [0]
			else:     
			    TheoreticalStability += [1]
			else:
			TheoreticalStability += [2]
			print(WeightFloat, TauSommersFloat)
		"""

	def getRootFloatsTuple(self,_PerturbationComplex):
			
		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationComplex

		#compute
		PrefixComplex=(1./self.HopfingStdWeightFloat)*np.exp(
				PerturbationRealFloat*self.HopfingDelayTimeFloat
			)

		#compute
		CosFloat=np.cos(PerturbationImagFloat*self.HopfingDelayTimeFloat)
		SinFloat=np.sin(PerturbationImagFloat*self.HopfingDelayTimeFloat)

		#compute
		NeuralFloat=(1.+self.HopfingConstantTimeFloat*PerturbationRealFloat)

		#compute
		FirstRootFloat = PrefixComplex*(
			NeuralFloat*CosFloat-self.HopfingConstantTimeFloat*PerturbationImagFloat*SinFloat
		)-self.HopfedEigenComplex.real

		#compute
		SecondRootFloat = PrefixComplex*(
			self.HopfingConstantTimeFloat*PerturbationImagFloat*CosFloat+NeuralFloat*SinFloat
		)-self.HopfedEigenComplex.imag
		
		#return
		return (FirstRootFloat,SecondRootFloat)

	def getSolutionFloatsTuple(self):

		#import
		import scipy.optimize

		#return
		return scipy.optimize.fsolve(self.getRootFloatsTuple, (0,0))


	def mimic_view(self):

		#/################/#
		# Build an Eigen Panel with Charts
		#

		#get
		ViewedChartsDerivePyploter=self.getTeamer(
			'Panels'
		).getManager(
			'Eigen'
		).getTeamer(
			'Charts'
		)

		#/################/#
		# Build an Eigen J Chart
		#

		#get
		ViewedConnectivityChartDerivePyploter=ViewedChartsDerivePyploter.getManager(
			'Connectivity'
		)

		#get
		ViewedConnectivityDrawDerivePyploter=ViewedConnectivityChartDerivePyploter.getTeamer(
			'Draws'
		).getManager(
			'Default'
		)

		#/##################/#
		# Build the theoritical ellipse
		#

		#import
		import matplotlib.patches

		#Add the matrix contour Ellipse
		PyplotedBifurcationEllipse=matplotlib.patches.Ellipse(
							xy=(self.HopfingMeanWeightFloat,0.), 
						 	width=2.*self.HopfedHalfWidthFloat,
						 	height=2.*self.HopfedHalfHeightFloat,
						 	color='r',
					)
		PyplotedBifurcationEllipse.set_alpha(0.2)

		#Add the Wiener Circle
		PyplotedBifurcationCircle=matplotlib.patches.Ellipse(
							xy=(self.HopfingMeanWeightFloat,0.), 
						 	width=2.,
						 	height=2.,
						 	linewidth=2,
						 	color='black',
						 	fill=False
					)
		PyplotedBifurcationCircle.set_alpha(0.4)


		#/##################/#
		# draw
		#

		#list
		ViewedConnectivityDrawDerivePyploter.PyplotingDrawVariable=[
			(
				'plot',
				{
					'#liarg':[
						[-2.,2.],
						[0.,0.]
					],
					'#kwarg':dict(
						{
							'linestyle':"--",
							'linewidth':1,
							'color':'black'
						}
					)
				}
			),
			(
				'plot',
				{
					'#liarg':[
						[-0.,0.],
						[-2.,2.]
					],
					'#kwarg':dict(
						{
							'linestyle':"--",
							'linewidth':1,
							'color':'black'
						}
					)
				}
			),
			(
				'add_artist',
				PyplotedBifurcationEllipse
			),
			(
				'add_artist',
				PyplotedBifurcationCircle
			),
			(
				'plot',
				{
					'#liarg':[
						np.real(self.HopfedContourComplexesArray),
						np.imag(self.HopfedContourComplexesArray)
					],
					'#kwarg':dict(
						{
							'linestyle':"-",
							'color':'red',
							'linewidth':5
						}
					)
				}
			),
			(
				'plot',
				{
					'#liarg':[
						self.HopfedRealEigenvalueFloatsArray,
						self.HopfedImagEigenvalueFloatsArray
					],
					'#kwarg':dict(
						{
							'linestyle':"",
							'marker':'o',
							'color':'black'
						}
					)
				}
			)
		]
		
		#/##################/#
		# view chart
		#

		#set
		ViewedConnectivityChartDerivePyploter.PyplotingShapeVariable=(10,8)

		#concatenate
		ViewedVariablesArray=np.concatenate(
			[
				self.HopfedRealEigenvalueFloatsArray,
				self.HopfedImagEigenvalueFloatsArray
			]
		)
		ViewedMinFloat=ViewedVariablesArray.min()
		ViewedMaxFloat=ViewedVariablesArray.max()
		ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

		#view
		ViewedConnectivityChartDerivePyploter.view(
			_XLabelStr="$Im(\lambda)$",
			_YLabelStr="$Re(\lambda)$",
			_XVariable=ViewedLimFloatsArray,
			_YVariable=ViewedLimFloatsArray
		)


#</DefineClass>

#</DefinePrint>
HopferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'HopfingUnitsInt',
		'HopfingDelayTimeFloat',
		'HopfingConstantTimeFloat',
		'HopfingWeightStdFloat',
		'HopfingWeightMeanFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfedLateralWeigthFloatsArray',
		'HopfedHalfHeightFloat',
		'HopfedHalfWidthFloat',
		'HopfedRealEigenvalueFloatsArray',
		'HopfedImagEigenvalueFloatsArray',
		'HopfedContourComplexesArray',
		'HopfedEigenComplex'
	]
)
#<DefinePrint>