#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Databasers import Hierarchizer
from ShareYourSystem.Noders import Organizer
import numpy as np
import operator

#Define a Sumer class
@Classer.ClasserClass()
class SumerClass(Organizer.OrganizerClass):

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
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self)
		
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Define a Factorizer class
@Classer.ClasserClass()
class FactorizerClass(Organizer.OrganizerClass):

	#Definition
	RepresentingKeyStrsList=[
								'FactorizingPowerFloat',
								'FactorizedTotalFloat'
							]
								
	def default_init(self,
						_FactorizingPowerFloat=1.,
						_FactorizedTotalFloat=0.
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self)

		#Build the output hierarchy
		self.produce(
				['X','Y'],
				SumerClass,
				**{'CollectingCollectionStr':self.OrganizingComponentCollectionStr}
			)

	def do_factorize(self):

		#debug
		'''
		self.debug('We factorize here')
		'''

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

#Definition of a Factorizer instance, organize structure and network
MyFactorizer=FactorizerClass().walk(
				{
					'AfterUpdateList':[
						('organize',{'LiargVariablesList':[]})
					],
					'GatherVariablesList':['<Component>']
				}
			).structure(
				['Component']
			).network(
				**{
					'VisitingCollectionStrsList':[
						'Data','Component'
					],
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
)['<Data>ResultsHierarchizer'].flush()

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
)['<Data>ResultsHierarchizer'].flush()

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

