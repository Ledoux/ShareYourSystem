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
			_HopfingWeightStdFloat = 1.0,
			_HopfingWeightMeanFloat = 0.0,
			_HopfingNormalisationInt= 0.5,
			_HopfingSymmetryFloat = 0.5,
			_HopfedLateralWeigthFloatsArray = None,
			_HopfedRealEigenvalueFloatsArray = None,
			_HopfedImagEigenvalueFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedHalfWidthFloat=0.,  
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
		self.debug(
			[
				'Ok we build the laterals'
			]
		)

		#numscipy
		'''
		self.NumscipyingRowsInt=self.HopfingUnitsInt
		self.NumscipyingColsInt=self.HopfingUnitsInt
		self.NumscipyingStdFloat=self.HopfingWeightStdFloat
		self.NumscipyingMeanFloat=self.HopfingWeightStdFloat
		self.numscipy(
			)
		'''

		#alias
		self.HopfedLateralWeigthFloatsArray=self.NumscipiedRandomFloatsArray

		#add mean
		self.HopfedLateralWeigthFloatsArray -= self.HopfingWeightMeanFloat/float(self.HopfingUnitsInt)

		#debug
		self.debug(
			[
				'We have setted the laterals',
				('self.',self,[
					'HopfedLateralWeigthFloatsArray'
				])
			]
		)

		#/###############/#
		# Determine the contour properties
		#

		#set
		self.HopfedHalfWidthFloat=self.NumscipiedDeviationFloat*(
			1.+self.NumscipiedCovarianceFloat
		)
		self.HopfedHalfHeightFloat=self.NumscipiedDeviationFloat*(
			1.-self.NumscipiedCovarianceFloat
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

		self.HopfedRealEigenvalueFloatsArray=np.real(self.NumscipiedEigenvalueComplexesArray)
		self.HopfedImagEigenvalueFloatsArray=np.imag(self.NumscipiedEigenvalueComplexesArray)

	def pyplotDraw(self):

		#get
		#ViewedChartDerivePyploter=self.getTeamer(
		#	'Panels'
		#).getManager(
		#	'Eigen'
		#).getTeamer(
		#	'Charts'
		#)

		#debug
		'''
		self.debug(
			[
				'We build a view of the eigenvalues',
				('self.',self,[
						'HopfedRealEigenvalueFloatsArray',
						'HopfedImagEigenvalueFloatsArray'
					])
			]
		)
		'''

		#/##################/#
		# Build the theoritical ellipse
		#

		#import
		import matplotlib.patches

		#Add the Wiener Ellipse
		PyplotedBifurcationEllipse=matplotlib.patches.Ellipse(
							xy=(self.HopfingWeightMeanFloat,0.), 
						 	width=2.*self.HopfedHalfWidthFloat,
						 	height=2.*self.HopfedHalfHeightFloat,
						 	color='r',
					)
		PyplotedBifurcationEllipse.set_alpha(0.2)


		#/##################/#
		# Build the PyplotingDrawVariable
		#

		#list
		self.PyplotingDrawVariable=[
			(
				'add_artist',
				PyplotedBifurcationEllipse
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
		
		#pyplotChart
		#self.pyplotChart()

		#view
		self.view(
			_XLabelStr="$Im(\lambda)$",
			_YLabelStr="$Re(\lambda)$",
			_XVariable=[-2.,2.],
			_YVariable=[-2.,2.]
		)

		#debug
		self.debug(
			[
				('self.',self,[
					'PyplotingChartVariable'
					]
				)
			]
		)

		#return
		return BaseClass.pyplotDraw(self)

	"""
	def pyplotChart(self):

		#view
		self.view(
			_XLabelStr="$Im(\lambda)$",
			_YLabelStr="$Re(\lambda)$",
			_XVariable=[-2.,2.],
			_YVariable=[-2.,2.]
		)

		#return
		return BaseClass.pyplotChart(self)
	"""

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
		'HopfedImagEigenvalueFloatsArray' 
	]
)
#<DefinePrint>