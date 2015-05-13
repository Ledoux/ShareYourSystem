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
			_HopfingSparseWeigthFloat=0.,
			_HopfingSwitchWeigthFloat=0.5,
			_HopfingNormalisationInt= 0.5,
			_HopfingSymmetryFloat = 0.0,
			_HopfingPerturbationEnvelopBool=True,
			_HopfingStabilityBool=True,
			_HopfingContourSamplesInt=50,
			_HopfingInteractionStr="Rate",
			_HopfedLateralWeigthFloatsArray=None,
			_HopfedMeanfieldWeigthFloat=0.,
			_HopfedRealLateralEigenFloatsArray = None,
			_HopfedImagLateralEigenFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedLateralHalfWidthFloat=0., 
			_HopfedLateralContourComplexesArray=None,
			_HopfedEigenComplex=None,
			_HopfedPerturbationContourRealFloatsArray = None,
			_HopfedPerturbationContourImagFloatsArray = None,
			_HopfedInstabilityIndexInt=-1,
			_HopfedInstabilityContourIndexInt=-1,
			_HopfedInstabilityContourComplex=None,
			_HopfedStableBool=True,
			_HopfedInstabilityStr="",
			_HopfedStdSparseFloat=0.,
			_HopfedParentSingularStr="",
			_HopfedAgentDeriveHopferVariable=None,
			_HopfedNetworkDeriveHopferVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_hopf(self):

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We leak here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(
			self.ParentedTotalSingularListDict
		)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.HopfedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['HopfedParentSingularStr'])
			]
		)
		'''

		#Check
		if (self.ParentDeriveTeamerVariable==None or "Populations" in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			"Interactions",
			'Inputs'
		]) and self.HopfedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the hopf',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.HopfedNetworkDeriveHopferVariable=self

			#/########################/#
			# hopfNetwork
			# 

			#hopf
			self.hopfNetwork()

			#/########################/#
			# structure hopf 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the hopfing children...'
				]
			)	
			'''

			#structure
			self.structure(
				[
					"Populations",
					'Inputs',
					'Interactomes',
					"Interactions",
				],
				'#all',
				_ManagerCommandSetList=[
						'hopf'
					]
			)

			#/########################/#
			# leak
			#

			#leak
			self.leak()
			

		else:

			#/########################/#
			# Inside structure
			#

			#debug
			'''
			self.debug(
				[
					'Ok we check if this parentsingular has a special method ',
					('self.',self,[
						'HopfedParentSingularStr'
					])
				]
			)
			'''

			#set
			HopfedMethodKeyStr='hopf'+self.HopfedParentSingularStr

			#Check
			if hasattr(self,HopfedMethodKeyStr):

				#/########################/#
				# call the special hopf<HopfedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.HopfedParentSingularStr+' level',
						'We hopf<HopfedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					HopfedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted hopf'+self.HopfedParentSingularStr
					]
				)
				'''	
	
	def hopfNetwork(self):

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

		#Check
		#if self.HopfingInteractionStr=="Spike":
		self.NumscipyingSparseFloat=self.HopfingSparseWeigthFloat
		self.NumscipyingSwitchFloat=self.HopfingSwitchWeigthFloat

		#numscipy
		self.numscipy(
			)

		#alias
		self.HopfedLateralWeigthFloatsArray=self.NumscipiedValueFloatsArray

		#debug
		self.debug(
			[
				'We have setted the laterals',
				('self.',self,[
					'HopfedLateralWeigthFloatsArray'
				])
			]
		)

		#set
		self.HopfedMeanfieldWeigthFloat=self.HopfingStdWeightFloat if self.HopfingStdWeightFloat>0. else self.HopfingMeanWeightFloat

		#Check
		if self.HopfedMeanfieldWeigthFloat==0.:

			#return
			self.HopfedStableBool=True

			#return 
			return self

		#/###############/#
		# Determine the contour properties
		#

		#debug
		'''
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
		'''

		#/###############/#
		# Build the eigen values real and imag
		#

		#real and imag
		self.HopfedRealLateralEigenFloatsArray=np.real(
			self.NumscipiedEigenvalueComplexesArray
		)
		self.HopfedImagLateralEigenFloatsArray=np.imag(
			self.NumscipiedEigenvalueComplexesArray
		)

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
		# Compute for each eigenvalues a possible solution
		#

		#Check
		if self.HopfingPerturbationEnvelopBool:

			#map
			HopfedPerturbationFloatsTuplesList=map(
				lambda __NumscipiedEigenvalueComplex:
				self.setAttr(
					'HopfedEigenComplex',
					__NumscipiedEigenvalueComplex
				).getSolutionFloatsTuple(),
				self.NumscipiedEigenvalueComplexesArray
			)
		
		else:

			#Check
			if self.HopfingStabilityBool:

				#for
				for __NumscipiedEigenvalueComplex in self.NumscipiedEigenvalueComplexesArray:

					#set
					self.HopfedInstabilityPerturbationComplex=self.setAttr(
						'HopfedEigenComplex',
						__NumscipiedEigenvalueComplex
					).getSolutionFloatsTuple(
					)


		#unpack
		[
			HopfedPerturbationRealFloatsTuple,
			HopfedPerturbationImagFloatsTuple
		]=SYS.unzip(
			HopfedPerturbationFloatsTuplesList,
			[0,1]
		)
		self.HopfedPerturbationRealFloatsArray=np.array(HopfedPerturbationRealFloatsTuple)
		self.HopfedPerturbationImagFloatsArray=np.array(HopfedPerturbationImagFloatsTuple)
		
		#/###############/#
		# Build the contour of the eigen values real and ima
		#

		#list
		self.HopfedLateralContourComplexesArray=[
			__Float + (
				1.-self.NumscipiedSommersFloat
			)*np.sqrt(
				1-(__Float/(1+self.NumscipiedSommersFloat))**2
			)*1j for __Float in np.linspace(
				-1.-self.NumscipiedSommersFloat,
				1.+self.NumscipiedSommersFloat,
				self.HopfingContourSamplesInt
			)
		]

		#list
		self.HopfedLateralContourComplexesArray+=list(
			np.array(
			self.HopfedLateralContourComplexesArray
			).conjugate()[::-1]  
		)

		#array
		self.HopfedLateralContourComplexesArray=np.array(
			self.HopfedLateralContourComplexesArray
		)

		#Check
		if self.HopfingStdWeightFloat>0.:

			#set
			self.HopfedLateralContourComplexesArray*=self.HopfingStdWeightFloat

		else:

			#sqrt
			self.HopfedStdSparseFloat=np.sqrt(self.NumscipyingSparseFloat*(1.-self.NumscipyingSparseFloat))
			
			#set
			self.HopfedLateralContourComplexesArray*=self.HopfedStdSparseFloat
          	      
		#/###############/#
		# Compute for each eigen of the contour a possible solution
		#

		#Check
		if self.HopfingPerturbationEnvelopBool:

			#map
			HopfedPerturbationContourFloatsTuplesList=map(
				lambda __HopfedContourComplex:
				self.setAttr(
					'HopfedEigenComplex',
					__HopfedContourComplex
				).getSolutionFloatsTuple(),
				self.HopfedLateralContourComplexesArray
			)

			#unpack
			[
				HopfedPerturbationContourRealFloatsTuple,
				HopfedPerturbationContourImagFloatsTuple
			]=SYS.unzip(
				HopfedPerturbationContourFloatsTuplesList,
				[0,1]
			)
			self.HopfedPerturbationContourRealFloatsArray=np.array(HopfedPerturbationContourRealFloatsTuple)
			self.HopfedPerturbationContourImagFloatsArray=np.array(HopfedPerturbationContourImagFloatsTuple)
			

			#Check
			if self.HopfingStabilityBool:

				#get
				self.HopfedInstabilityContourIndexInt = np.argmax(
					self.HopfedPerturbationContourRealFloatsArray
				)
			
			#get	
			self.HopfedInstabilityContourComplex=self.HopfedLateralContourComplexesArray[
				self.HopfedInstabilityContourIndexInt
			]

			#set
			self.HopfedStableBool=self.HopfedPerturbationContourRealFloatsArray[
				self.HopfedInstabilityContourIndexInt
			]<0.

			#Check
			if self.HopfedStableBool==False:

				#set
				self.HopfedInstabilityStr='Rate' if self.HopfedPerturbationContourImagFloatsArray[
					self.HopfedInstabilityContourIndexInt
				]==0. else 'Hopf'

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'HopfedInstabilityContourIndexInt',
							'HopfedInstabilityContourComplex',
							'HopfedStableBool',
							'HopfedInstabilityStr'
						])
				]
			)
			'''

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
					'HopfedPerturbationContourRealFloatsArray',
					'HopfedPerturbationContourImagFloatsArray'

				])
			]
		)
		'''

		#/###################/#
		# Check for Populations
		# 

		#get
		HopfedPopulationsDeriveManager=self.getTeamer(
			"Populations"
		)

		#debug
		'''
		self.debug(
			[
				'We predict network here',
				'Check for a sensor population'
			]
		)
		'''

		#/###################/#
		# Check for Agent
		# 

		#get
		LeakedAgentDeriveHopfer=HopfedPopulationsDeriveManager.getManager(
			"Agent"
		)

	def hopfPopulation(self):

		#Check
		if self.ManagementTagStr=='Agent':

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedNetworkDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Set properties
			#

			#set
			self.LeakingUnitsInt=self.HopfedNetworkDeriveHopferVariable.HopfingUnitsInt

			#set
			self.LeakingGlobalBool=True

			#Check
			if self.RecordingLabelVariable==None:
				self.RecordingLabelVariable=[0,1,2]

			#set
			self.LeakingTimeVariable=self.HopfedNetworkDeriveHopferVariable.HopfingConstantTimeFloat
			
			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'LeakingInteractionStr'
						])
				]
			)
			'''

			#/####################/#
			# Rate case
			#

			#Check
			if self.LeakingInteractionStr=="Rate":

				#Check
				if self.LeakingTransferVariable==None:
					
					#set
					self.LeakingTransferVariable='mV*tanh((#CurrentStr)/mV)'

			#/####################/#
			# Spike case
			#

			else:

				#/####################/#
				# Check for Inputs
				#

				#get
				HopfedInputsDeriveHopfer=self.getTeamer(
					"Inputs"
				)

				#get
				HopfedInputsDeriveHopfer.getManager(
					"Rest"
				)	

			#/####################/#
			# Check for Interactions
			#

			#get
			HopfedInteractionsDeriveHopfer=self.getTeamer(
				"Interactions"
			)

			#get
			HopfedInteractionsDeriveHopfer.getManager(
				"/"
			)

	def hopfInteraction(self):

		#Check
		if self.ManagementTagStr=='/':

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedAgentDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.HopfedNetworkDeriveHopferVariable=self.HopfedAgentDeriveHopferVariable.HopfedNetworkDeriveHopferVariable

			#/####################/#
			# Set properties
			#

			#alias
			self.LeakingWeigthVariable=self.HopfedNetworkDeriveHopferVariable.HopfedLateralWeigthFloatsArray

			#Check
			if self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeFloat!=0.:
				self.LeakingDelayVariable=self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeFloat

			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

	def hopfInput(self):

		#debug
		self.debug(
			[
				'We hopfInput here'
			]
		)

		#Check
		if self.ManagementTagStr=="Rest":

			#debug
			self.debug(
				[
					'We hopf Input Rest here'
				]
			)

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedAgentDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.HopfedNetworkDeriveHopferVariable=self.HopfedAgentDeriveHopferVariable.HopfedNetworkDeriveHopferVariable

			#/####################/#
			# Set properties
			#

			#Check
			if self.LeakingWeigthVariable==None:

				#get
				self.LeakingWeigthVariable='#scalar:-60*mV'
	
	def getRootFloatsTuple(self,_PerturbationComplex):
			
		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationComplex

		#compute
		PrefixComplex=(1./self.HopfedMeanfieldWeigthFloat)*np.exp(
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

	#/######################/#
	# Augment view
	#

	def viewSample(self):

		#debug
		'''
		self.debug(
			[
				'We predict view sample here',
				('self.',self,[
						'StructureTagStr'
					])
			]
		)
		'''

		#Check
		self.ViewingXScaleFloat=1000.
		self.ViewingYScaleFloat=1000.

		#base
		BaseClass.viewSample(self)

		
	def mimic_view(self):

		#Check
		if self.HopfedNetworkDeriveHopferVariable==self:

			#get the Panels
			ViewedPanelsDerivePyploter=self.getTeamer(
				'Panels'
			)

			#debug
			'''
			self.debug(
				[
					'ViewedPanelsDerivePyploter is '+str(ViewedPanelsDerivePyploter)
				]
			)
			'''

			#Check
			if self.HopfedMeanfieldWeigthFloat==0.:

				#del
				del ViewedPanelsDerivePyploter.ManagementDict['Eigen']

				#view
				BaseClass.view(self)

				#return
				return

			#/################/#
			# Build an Eigen Panel with Charts
			#

			#get
			ViewedChartsDerivePyploter=ViewedPanelsDerivePyploter.getManager(
				'Eigen'
			).getTeamer(
				'Charts'
			)

			#/################/#
			# Build an Eigen J Chart
			#

			#get
			ViewedConnectivityChartDerivePyploter=ViewedChartsDerivePyploter.getManager(
				'Connectivity',
				_IndexInt=0
			)

			#get
			ViewedConnectivityDrawDerivePyploter=ViewedConnectivityChartDerivePyploter.getTeamer(
				'Draws'
			).getManager(
				'Default'
			)

			#debug
			'''
			self.debug(
				[
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)
			'''

			#/##################/#
			# Build the theoritical ellipse
			#

			#import
			import matplotlib.patches

			#Add the matrix contour Ellipse
			PyplotedBifurcationEllipse=matplotlib.patches.Ellipse(
								xy=(self.NumscipiedCenterFloat,0.), 
							 	width=self.NumscipiedWidthFloat,
							 	height=self.NumscipiedHeightFloat,
							 	color='r',
						)
			PyplotedBifurcationEllipse.set_alpha(0.2)

			#Add the Wiener Circle
			PyplotedBifurcationCircle=matplotlib.patches.Ellipse(
								xy=(self.NumscipiedCenterFloat,0.), 
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
							self.HopfedPerturbationContourRealFloatsArray,
							self.HopfedPerturbationContourImagFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"-",
								'linewidth':3,
								'color':'red'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							self.HopfedPerturbationRealFloatsArray,
							self.HopfedPerturbationImagFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"",
								'marker':"o",
								'color':'black'
							}
						)
					}
				)
			]

			#/##################/#
			# view chart
			#

			#concatenate
			ViewedVariablesArray=np.concatenate(
				[
					self.HopfedPerturbationContourRealFloatsArray,
					self.HopfedPerturbationContourImagFloatsArray
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
			
			#/################/#
			# Prepare a Run Panel
			#

			#Check
			if 'Populations' in self.TeamDict:

				#debug
				'''
				self.debug(
					[
						'We put the Run on the right'
					]
				)
				'''

				#get
				ViewedRunDerivePyploter=ViewedPanelsDerivePyploter.getManager(
						'Run'
					)
				#ViewedRunDerivePyploter.PyplotingShiftVariable=[0,3]

		#/###############/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys()),
				'BaseClass.view is ',
				str(BaseClass.view)
			]
		)
		'''

		#view
		BaseClass.view(self)

		#debug
		'''
		self.debug(
			[
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys())
			]
		)
		'''

#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=HopferClass
#<DefineLocals>

#</DefinePrint>
HopferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'HopfingUnitsInt',
		'HopfingDelayTimeFloat',
		'HopfingConstantTimeFloat',
		'HopfingMeanWeightFloat',
		'HopfingStdWeightFloat',
		'HopfingSparseWeigthFloat',
		'HopfingSwitchWeigthFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfingPerturbationEnvelopBool',
		'HopfingStabilityBool',
		'HopfingContourSamplesInt',
		'HopfingInteractionStr',
		'HopfedLateralWeigthFloatsArray',
		'HopfedHalfHeightFloat',
		'HopfedLateralHalfWidthFloat',
		'HopfedMeanfieldWeigthFloat',
		'HopfedRealLateralEigenFloatsArray',
		'HopfedImagLateralEigenFloatsArray',
		'HopfedLateralContourComplexesArray',
		'HopfedEigenComplex',
		'HopfedPerturbationComplex',
		'HopfedPerturbationRealFloatsArray',
		'HopfedPerturbationImagFloatsArray',
		'HopfedPerturbationContourRealFloatsArray',
		'HopfedPerturbationContourImagFloatsArray',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityContourIndexInt',
		'HopfedInstabilityContourComplex',
		'HopfedStableBool',
		'HopfedInstabilityStr',
		'HopfedStdSparseFloat',
		'HopfedParentSingularStr',
		'HopfedAgentDeriveHopferVariable',
		'HopfedNetworkDeriveHopferVariable'
	]
)
#<DefinePrint>