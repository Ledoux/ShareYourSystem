#ImportModules
import ShareYourSystem as SYS
import numpy as np
import operator

#Define a Sumer class
@SYS.ClasserClass()
class SumerClass(SYS.OrganizerClass):

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
		SYS.OrganizerClass.__init__(self)
		
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Define a Factorizer class
@SYS.ClasserClass()
class FactorizerClass(SYS.OrganizerClass):

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
		SYS.OrganizerClass.__init__(self)

		#Build the output hierarchy
		self.produce(
				self.OrganizingComponentsCollectionStr,
				['X','Y'],
				SumerClass
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
					self['<Components>']
				)
			),
			self.FactorizingPowerFloat
		)

#Definition of a Factorizer instance, organize structure and network
MyFactorizer=FactorizerClass(
				**{
					'FolderingPathStr':SYS.Organizer.LocalFolderPathStr
				}
			).walk(
				{
					'AfterUpdateList':[
						(
							'organize',
							SYS.ApplyDictClass()
						)
					],
					'GatherVariablesList':['<Components>']
				}
			).structure(
				['Components']
			).network(
				**{
					'VisitingCollectionStrsList':[
						'Models','Components'
					],
					'RecruitingConcludeConditionTuplesList':[
						(
							'MroClassesList',
							operator.contains,
							SYS.HierarchizerClass
						)
					]
				}
			)

#Update transmit the do method and flush in the results
MyFactorizer.__setitem__(
	"Dis_<Components>",
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
		'GatherVariablesList':['<Components>']
	}
)['<Models>ResultsHierarchizer'].flush()

#Update and flush in the results
MyFactorizer.__setitem__(
	"Dis_<Components>",
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
		'GatherVariablesList':['<Components>']
	}
)['<Models>ResultsHierarchizer'].flush()

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

