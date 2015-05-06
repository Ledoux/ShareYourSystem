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
			_HopfingPerturbationEnvelopBool=True,
			_HopfingStabilityBool=True,
			_HopfedLateralWeigthFloatsArray = None,
			_HopfedRealLateralEigenFloatsArray = None,
			_HopfedImagLateralEigenFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedLateralHalfWidthFloat=0., 
			_HopfedLateralContourComplexesArray=None,
			_HopfedEigenComplex=None,
			_HopfedRealPerturbationEigenFloatsArray = None,
			_HopfedImagPerturbationEigenFloatsArray = None,
			_HopfedInstabilityComplex=None,
			_HopfedStableBool=True,
			_HopfedInstabilityStr="",
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

		#/###############/#
		# Build the eigen values real and imag
		#

		#real and imag
		self.HopfedRealLateralEigenFloatsArray=np.real(self.NumscipiedEigenvalueComplexesArray)
		self.HopfedImagLateralEigenFloatsArray=np.imag(self.NumscipiedEigenvalueComplexesArray)

		#debug
		'''
		self.debug(
			[
				'We have built the real and imag',
				('self.',self,[
						'HopfedRealLateralEigenFloatsArray',
						'HopfedImagLateralEigenFloatsArray'
					])
			]
		)
		'''

		#/###############/#
		# Build the contour of the eigen values real and ima
		#

		self.HopfedLateralContourComplexesArray=[
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
		self.HopfedLateralContourComplexesArray+=list(
			np.array(
			self.HopfedLateralContourComplexesArray
			).conjugate()[::-1]  
		)
		self.HopfedLateralContourComplexesArray=np.array(
			self.HopfedLateralContourComplexesArray
		)
          	      
		#/###############/#
		# Compute for each eigen of the contour a possible solution
		#

		#Check
		if self.HopfingPerturbationEnvelopBool:

			#map
			HopfedSolutionFloatsTuplesList=map(
				lambda __HopfedContourComplex:
				self.setAttr(
					'HopfedEigenComplex',
					__HopfedContourComplex
				).getSolutionFloatsTuple(),
				self.HopfedLateralContourComplexesArray
			)

			#unpack
			[
				RealFloatsTuple,
				ImagFloatsTuple
			]=SYS.unzip(
				HopfedSolutionFloatsTuplesList,
				[0,1]
			)
			self.HopfedRealPerturbationEigenFloatsArray=np.array(RealFloatsTuple)
			self.HopfedImagPerturbationEigenFloatsArray=np.array(ImagFloatsTuple)
			

			#Check
			if self.HopfingStabilityBool:

				#get
				self.HopfedInstabilityIndexInt = np.argmax(self.HopfedRealPerturbationEigenFloatsArray)
			
			#get	
			self.HopfedInstabilityComplex=self.HopfedLateralContourComplexesArray[self.HopfedInstabilityIndexInt]

			#set
			self.HopfedStableBool=self.HopfedRealPerturbationEigenFloatsArray[self.HopfedInstabilityIndexInt]<0.

			#Check
			if self.HopfedStableBool==False:

				#set
				self.HopfedInstabilityStr='Rate' if self.HopfedImagPerturbationEigenFloatsArray[self.HopfedInstabilityIndexInt]==0. else 'Hopf'

			#debug
			self.debug(
				[
					('self.',self,[
							'HopfedInstabilityIndexInt',
							'HopfedInstabilityComplex',
							'HopfedStableBool',
							'HopfedInstabilityStr'
						])
				]
			)



		else:

			#Check
			if self.HopfingStabilityBool:

				#for
				for __HopfedContourComplex in self.HopfedLateralContourComplexesArray:

					#set
					self.setAttr(
						'HopfedEigenComplex',
						__HopfedContourComplex
					).getSolutionFloatsTuple(
					)




		#debug
		'''
		self.debug(
			[
				('self.',self,[
					'HopfedRealPerturbationEigenFloatsArray',
					'HopfedImagPerturbationEigenFloatsArray'

				])
			]
		)
		'''

		#/###############/#
		# Build the simulation structure
		#

		#map
		self.mapSet(
			{
				'-Populations':{
					'|P':{
						'LeakingUnitsInt':100,
						'LeakingMonitorIndexIntsList':[0,1,2],
						'LeakingTransferVariable':'mV*tanh((#CurrentStr)/mV)',
						'-Interactions':{
							'|/':{
								'LeakingWeigthVariable':self.HopfedLateralWeigthFloatsArray,
								'LeakingDelayVariable':self.HopfingDelayTimeFloat
							}
						},
						'LeakingGlobalBool':True,
						'LeakingTimeVariable':self.HopfingConstantTimeFloat
					}
				}
			}
		).leak(
		)

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
						 	width=2.*(1.+self.NumscipiedSommersFloat),
						 	height=2.*(1.-self.NumscipiedSommersFloat),
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
				'plot',
				{
					'#liarg':[
						[1.,1.],
						[-2.,2.]
					],
					'#kwarg':dict(
						{
							'linestyle':"-",
							'linewidth':2,
							'color':'black',
							'alpha':0.5
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
						np.real(self.HopfedLateralContourComplexesArray),
						np.imag(self.HopfedLateralContourComplexesArray)
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
						self.HopfedRealLateralEigenFloatsArray,
						self.HopfedImagLateralEigenFloatsArray
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
		# View chart
		#

		#set
		ViewedConnectivityChartDerivePyploter.PyplotingShapeVariable=(10,8)

		#concatenate
		ViewedVariablesArray=np.concatenate(
			[
				self.HopfedRealLateralEigenFloatsArray,
				self.HopfedImagLateralEigenFloatsArray
			]
		)
		ViewedMinFloat=ViewedVariablesArray.min()
		ViewedMaxFloat=max(ViewedVariablesArray.max(),1.)
		ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

		#view
		ViewedConnectivityChartDerivePyploter.view(
			_XLabelStr="$Re(\lambda_{J})$",
			_YLabelStr="$Im(\lambda_{J})$",
			_XVariable=ViewedLimFloatsArray,
			_YVariable=ViewedLimFloatsArray
		)

		#/################/#
		# Build an Eigen Perturb Chart
		#

		#get
		ViewedPerturbationChartDerivePyploter=ViewedChartsDerivePyploter.getManager(
			'Perturbation'
		)

		#get
		ViewedPerturbationDrawDerivePyploter=ViewedPerturbationChartDerivePyploter.getTeamer(
			'Draws'
		).getManager(
			'Default'
		)

		#/##################/#
		# draw
		#

		#list
		ViewedPerturbationDrawDerivePyploter.PyplotingDrawVariable=[
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
				'plot',
				{
					'#liarg':[
						self.HopfedRealPerturbationEigenFloatsArray,
						self.HopfedImagPerturbationEigenFloatsArray
					],
					'#kwarg':dict(
						{
							'linestyle':"-",
							'linewidth':3,
							'color':'red'
						}
					)
				}
			)
		]

		#/##################/#
		# view chart
		#

		#set
		ViewedPerturbationChartDerivePyploter.PyplotingShapeVariable=(10,8)

		#concatenate
		ViewedVariablesArray=np.concatenate(
			[
				self.HopfedRealPerturbationEigenFloatsArray,
				self.HopfedImagPerturbationEigenFloatsArray
			]
		)
		ViewedMinFloat=ViewedVariablesArray.min()
		ViewedMaxFloat=ViewedVariablesArray.max()
		ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

		#view
		ViewedPerturbationChartDerivePyploter.view(
			_XLabelStr="$Re(\lambda_{P})$",
			_YLabelStr="$Im(\lambda_{P})$",
			_XVariable=ViewedLimFloatsArray,
			_YVariable=ViewedLimFloatsArray
		)
		
		#/###############/#
		# Call the base method
		#

		#view
		BaseClass.view(self)

#</DefineClass>

#</DefinePrint>
HopferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'HopfingUnitsInt',
		'HopfingDelayTimeFloat',
		'HopfingConstantTimeFloat',
		'HopfingMeanWeightFloat',
		'HopfingStdWeightFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfingPerturbationEnvelopBool',
		'HopfingStabilityBool',
		'HopfedLateralWeigthFloatsArray',
		'HopfedHalfHeightFloat',
		'HopfedLateralHalfWidthFloat',
		'HopfedRealLateralEigenFloatsArray',
		'HopfedImagLateralEigenFloatsArray',
		'HopfedLateralContourComplexesArray',
		'HopfedEigenComplex',
		'HopfedRealPerturbationEigenFloatsArray',
		'HopfedImagPerturbationEigenFloatsArray',
		'HopfedInstabilityComplex',
		'HopfedStableBool',
		'HopfedInstabilityStr'
	]
)
#<DefinePrint>