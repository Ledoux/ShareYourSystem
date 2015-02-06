
#ImportModules
import numpy as np

import ShareYourSystem as SYS,Classer
from ShareYourSystem.Functers import Triggerer,Outputer
from ShareYourSystem.Standards.Objects import Storer

#Define a Multiplier class
@Classer.ClasserClass()
class MultiplierClass(Storer.StorerClass):

	#Definition
	RepresentingKeyStrsList=[
									'MultiplyingFirstInt',
									'MultiplyingSecondInt',
									'MultipliedTotalInt'
								]
								
	def default_init(self,
						_MultiplyingFirstInt=0,
						_MultiplyingSecondInt=0,
						_MultipliedTotalInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		Storer.StorerClass.__init__(self,**_KwargVariablesDict)

		#analyze
		self.analyze(
			['MultiplyingFirstInt','MultiplyingSecondInt'],  	#Parameters
			['MultipliedTotalInt'] 					   			#Results
		)
			
	@Outputer.OutputerClass()
	def do_multiply(self):
		
		#debug
		'''
		self.debug(('self.',self,['MultiplyingFirstInt','MultiplyingSecondInt']))
		'''

		#set the MultipliedTotalInt
		self.MultipliedTotalInt=self.MultiplyingFirstInt*self.MultiplyingSecondInt

#Define a Modulizer class
@Classer.ClasserClass()
class ModulizerClass(Storer.StorerClass):

	#Definition
	RepresentingKeyStrsList=[
									'ModulizingPowerFloat',
									'ModulizedTotalFloat'
								]
								
	def default_init(self,
						_ModulizingPowerFloat=0.5,
						_ModulizedTotalFloat=0.,
						**_KwargVariablesDict
					):

		#Call the parent init method
		Storer.StorerClass.__init__(self,**_KwargVariablesDict)

		#Build the output hierarchy
		self.update(
						[
							('<Output>RealMultiplier',MultiplierClass()),
							('<Output>ImageMultiplier',MultiplierClass()),
						]
					)

		#analyze
		self.analyze(
			['ModulizingPowerFloat'],  	#Parameters
			['ModulizedTotalFloat'] 	#Results
		)

		#Set the outputing node
		self['<Database>ParametersHierarchizer'].HierarchizingNodeStr="Output"
						
	@Outputer.OutputerClass()
	def do_modulize(self):
		
		#debug
		'''
		self.debug(('self.',self,['<Group>']))
		'''

		#set the ModulizedTotalFloat
		self.ModulizedTotalFloat=np.power(
			sum(
				map(
					lambda __OutputedDeriveMultiplier:
					__OutputedDeriveMultiplier.MultipliedTotalInt,
					self['<Output>']
				)
			),
			self.ModulizingPowerFloat
		)

#Definition a hierarching Modulizer and analyze
MyModulizer=ModulizerClass()

#Update and store
MyModulizer.__setitem__(
	"Dis_<Output>",
	[
		[
			('MultiplyingFirstInt',1),
			('MultiplyingSecondInt',2)
		],
		[
			('MultiplyingFirstInt',1),
			('MultiplyingSecondInt',3)
		]
	]
).collect()

#Do a store which is a scan 
MyModulizer.update(
[
	(
		"Dis_<Output>",
		[
			[
				('/<Database>ParametersFeaturer/ScanningRangeTuplesList',
					[
						('MultiplyingFirstInt',[0,1]),
						('MultiplyingSecondInt',[2])
					]
				)
			],
			[
				('/<Database>ParametersFeaturer/ScanningRangeTuplesList',
					[
						('MultiplyingFirstInt',[1,2]),
						('MultiplyingSecondInt',[3])
					]
				)
			]
		]
	),
	(
		'/<Database>ParametersFeaturer/ScanningRangeTuplesList',
		[
			('ModulizingPowerFloat',[1.])
		]
	)
]
).collect()

#Definition the AttestedStr
SYS._attest(
	[
		'MyModulizer is '+SYS._str(
		MyModulizer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyModulizer.hdfview().hdfclose().HdformatedConsoleStr
	]
) 

#Print

