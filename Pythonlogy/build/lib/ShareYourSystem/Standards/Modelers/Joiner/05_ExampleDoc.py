#ImportModules
import ShareYourSystem as SYS
import operator
import tables
import numpy as np

#Define a Multiplier class
@SYS.ClasserClass()
class MultiplierClass(SYS.ControllerClass):

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
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)

		#Set a parameters database
		self.collect(
						"Joiners",
						"Parameters",
						SYS.JoinerClass().update(
							[
								(
									'Attr_DatabasingSealTuplesList',
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
@SYS.ClasserClass()
class ModulizerClass(SYS.ControllerClass):

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
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)

		#Build the output hierarchy
		self.update(
						[
							('<Components>RealMultiplier',MultiplierClass()),
							('<Components>ImageMultiplier',MultiplierClass())
						]
					)

		#Set a parameters database
		self.collect(
					"Joiners",
					"Parameters",
					SYS.JoinerClass().update(
						[
							(
								'Attr_DatabasingSealTuplesList',
								[
									('ModulizingPowerFloat','ModulizingPowerFloat',tables.Float64Col())
								]
							),
							('Attr_RowingGetStrsList',['ModulizingPowerFloat']),
							('ConnectingGraspClueVariablesList',
								[
									'/NodePointDeriveNoder/<Components>RealMultiplier/<Joiners>ParametersJoiner',
									'/NodePointDeriveNoder/<Components>ImageMultiplier/<Joiners>ParametersJoiner'
								]
							)
						]
					)
				)


#Definition of a Modulizer instance, structure and network
MyModulizer=ModulizerClass(
		**{
			'FolderingPathStr':SYS.Joiner.LocalFolderPathStr
		}
	).structure(
		['Components']
	).network(
		**{
			'VisitingCollectionStrsList':['Joiners','Components'],
			'RecruitingConcludeConditionTuplesList':[
				(
					'MroClassesList',
					operator.contains,SYS.JoinerClass
				)
			]
		}
	)

#Update and flush in the results
MyModulizer.__setitem__(
	"Dis_<Components>",
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
)['<Joiners>ParametersJoiner'].flush()

#Update and flush in the results
MyModulizer.__setitem__(
	"Dis_<Components>",
	[
		[
			('MultiplyingFirstInt',2)
		],
		[
			('MultiplyingSecondInt',4)
		]
	]
)['<Joiners>ParametersJoiner'].flush()


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
