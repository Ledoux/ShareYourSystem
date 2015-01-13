#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Hierarchizer
import operator
import tables
import numpy as np

#Define a Sumer class
@Classer.ClasserClass()
class SumerClass(Structurer.StructurerClass):

	#Definition
	RepresentingKeyStrsList=[
									'SumingFirstInt',
									'SumingSecondInt',
									'SumedTotalInt'
								]
								
	def default_init(self,
						_SumingFirstInt=0,
						_SumingSecondInt=0,
						_SumedTotalInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

		#Set a parameters database
		self.collect(
				"Datome",
				"Parameters",
				Hierarchizer.HierarchizerClass().update(
					[
						(
							'Attr_ModelingSealTuplesList',
							[
								('SumingFirstInt','SumingFirstInt',tables.Int64Col()),
								('SumingSecondInt','SumingSecondInt',tables.Int64Col())
							]
						),
						('Attr_RowingGetStrsList',['SumingFirstInt','SumingSecondInt'])
					]
				)
			)

		#Set a results database
		self.collect(
			"Datome",
			"Results",
			Hierarchizer.HierarchizerClass().update(
				[
					(
						'Attr_ModelingSealTuplesList',
						[
							('SumedTotalInt','SumedTotalInt',tables.Int64Col())
						]
					),
					('ConnectingAttentionGetStrsList',
						[
							'/NodePointDeriveNoder/<Datome>ParametersHierarchizer'
						]
					),
					('TagStr','Networked')
				]
			)
		)
		
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Define a Factorizer class
@Classer.ClasserClass()
class FactorizerClass(Structurer.StructurerClass):

	#Definition
	RepresentingKeyStrsList=[
								'FactorizingPowerFloat',
								'FactorizedTotalFloat'
							]
								
	def default_init(self,
						_FactorizingPowerFloat=1.,
						_FactorizedTotalFloat=0.,
						**_KwargVariablesDict
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

		#Build the output hierarchy
		self.update(
						[
							('<Component>XSumer',SumerClass()),
							('<Component>YSumer',SumerClass())
						]
					)

		#Set a parameters database
		self.collect(
					"Datome",
					"Parameters",
					Hierarchizer.HierarchizerClass().update(
						[
							(
								'Attr_ModelingSealTuplesList',
								[
									('FactorizingPowerFloat','FactorizingPowerFloat',tables.Float64Col())
								]
							),
							('Attr_RowingGetStrsList',['FactorizingPowerFloat']),
							('ConnectingAttentionGetStrsList',
								[
									'/NodePointDeriveNoder/<Component>XSumer/<Datome>ParametersHierarchizer',
									'/NodePointDeriveNoder/<Component>YSumer/<Datome>ParametersHierarchizer'
								]
							)
						]
					)
				)

		#Set a results database
		self.collect(
			"Datome",
			"Results",
			Hierarchizer.HierarchizerClass().update(
				[
					(
						'Attr_ModelingSealTuplesList',
						[
							('FactorizedTotalFloat','FactorizedTotalFloat',tables.Float64Col())
						]
					),
					('ConnectingAttentionGetStrsList',
						[
							'/NodePointDeriveNoder/<Datome>ParametersHierarchizer'
						]
					),
					('TagStr','Networked')
				]
			)
		)

	def do_factorize(self):

		#debug
		self.debug('We factorize here')

		#set the FactorizedTotalFloat
		self.FactorizedTotalFloat=np.power(
			sum(
				map(
					lambda __DeriveSumer:
					__DeriveSumer.SumedTotalInt,
					self['<Component>']
				)
			),
			self.FactorizingPowerFloat
		)

#Definition of a Factorizer instance, structure and network
MyFactorizer=FactorizerClass().structure(
	['Component']
).network(
	**{
		'VisitingCollectionStrsList':['Datome','Component'],
		'RecruitingConcludeConditionTuplesList':[
			(
				'__class__.__mro__',
				operator.contains,Hierarchizer.HierarchizerClass
			)
		]
	}
)

#Update transmit the do method and flush in the results
MyFactorizer.__setitem__(
	"Dis_<Component>",
	[
		[
			('SumingFirstInt',1),
			('SumingSecondInt',2)
		],
		[
			('SumingFirstInt',1),
			('SumingSecondInt',3)
		]
	]
).walk(
	{
		'AfterUpdateList':[
			('callDo',{'LiargVariablesList':[]})
		],
		'GatherVariablesList':['<Component>']
	}
)['<Datome>ResultsHierarchizer'].flush()

#Update and flush in the results
MyFactorizer.__setitem__(
	"Dis_<Component>",
	[
		[
			('SumingFirstInt',2)
		],
		[
			('SumingSecondInt',4)
		]
	]
).walk(
	{
		'AfterUpdateList':[
			('callDo',{'LiargVariablesList':[]})
		],
		'GatherVariablesList':['<Component>']
	}
)['<Datome>ResultsHierarchizer'].flush()

#Definition the AttestedStr
SYS._attest(
	[
		'MyFactorizer is '+SYS._str(
		MyFactorizer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyFactorizer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

