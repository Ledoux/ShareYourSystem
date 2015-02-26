#ImportModules
import operator
import tables
import numpy as np
import ShareYourSystem as SYS,Classer
from ShareYourSystem.Hdformaters import Storer
from ShareYourSystem.Standards.Modelers import Hierarchizer

#Define a Multiplier class
@Classer.ClasserClass()
class MultiplierClass(Storer.StorerClass):

	#Definition
	RepresentingKeyStrsList=[
									'MultiplyingFirstInt',
									'MultiplyingSecondInt'
								]
								
	def default_init(self,
						_MultiplyingFirstInt=0,
						_MultiplyingSecondInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

		#Set a parameters database
		self.collect(
						"Data",
						"Parameters",
						Hierarchizer.HierarchizerClass().update(
							[
								(
									'Attr_ModelingSealTuplesList',
									[
										('MultiplyingFirstInt','MultiplyingFirstInt',tables.Int64Col()),
										('MultiplyingSecondInt','MultiplyingSecondInt',tables.Int64Col())
									]
								),
								('Attr_RowingGetStrsList',['MultiplyingFirstInt','MultiplyingSecondInt'])
							]
						)
				)
		
#Define a Modulizer class
@Classer.ClasserClass()
class ModulizerClass(Storer.StorerClass):

	#Definition
	RepresentingKeyStrsList=[
									'ModulizingPowerFloat',
									'ModulizedTotalFloat'
								]
								
	def default_init(self,
						_ModulizingPowerFloat=1.,
						_ModulizedTotalFloat=0.,
						**_KwargVariablesDict
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

		#Build the output hierarchy
		self.update(
						[
							('<Component>RealMultiplier',MultiplierClass()),
							('<Component>ImageMultiplier',MultiplierClass())
						]
					)

		#Set a parameters database
		self.collect(
					"Data",
					"Parameters",
					Hierarchizer.HierarchizerClass().update(
						[
							(
								'Attr_ModelingSealTuplesList',
								[
									('ModulizingPowerFloat','ModulizingPowerFloat',tables.Float64Col())
								]
							),
							('Attr_RowingGetStrsList',['ModulizingPowerFloat'])
						]
					)
				)

#Definition of a Modulizer instance
MyModulizer=ModulizerClass()

#Update and store

MyModulizer.__setitem__(
	"Dis_<Component>",
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
)['<Data>ParametersHierarchizer'].insert()

MyModulizer.__setitem__(
	"Dis_<Component>",
	[
		[
			('MultiplyingFirstInt',2)
		],
		[
			('MultiplyingSecondInt',4)
		]
	]
)['<Data>ParametersHierarchizer'].insert()


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

