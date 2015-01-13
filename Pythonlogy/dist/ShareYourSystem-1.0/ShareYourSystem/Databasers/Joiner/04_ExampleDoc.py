#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Joiner
import operator
import tables
import numpy as np

#Define a Multiplier class
@Classer.ClasserClass()
class MultiplierClass(Structurer.StructurerClass):

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
						"Datome",
						"Parameters",
						Joiner.JoinerClass().update(
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
class ModulizerClass(Structurer.StructurerClass):

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
					"Datome",
					"Parameters",
					Joiner.JoinerClass().update(
						[
							(
								'Attr_ModelingSealTuplesList',
								[
									('ModulizingPowerFloat','ModulizingPowerFloat',tables.Float64Col())
								]
							),
							('Attr_RowingGetStrsList',['ModulizingPowerFloat']),
							('ConnectingAttentionGetStrsList',
								[
									'/NodePointDeriveNoder/<Component>RealMultiplier/<Datome>ParametersJoiner',
									'/NodePointDeriveNoder/<Component>ImageMultiplier/<Datome>ParametersJoiner'
								]
							)
						]
					)
				)


#Definition of a Modulizer instance, structure and network
MyModulizer=ModulizerClass().structure(
	['Component']
).network(
	**{
		'VisitingCollectionStrsList':['Datome','Component'],
		'RecruitingConcludeConditionTuplesList':[
			(
				'__class__.__mro__',
				operator.contains,Joiner.JoinerClass
			)
		]
	}
)

#Update and flush in the results
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
)['<Datome>ParametersJoiner'].flush()

#Update and flush in the results
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
)['<Datome>ParametersJoiner'].flush()


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
		'hdf5 file is : '+MyModulizer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

