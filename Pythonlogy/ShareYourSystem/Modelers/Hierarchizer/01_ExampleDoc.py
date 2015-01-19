
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Flusher,Hierarchizer
import tables
import operator

#Define a Sumer class
@Classer.ClasserClass()
class SumerClass(Controller.ControllerClass):

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
						
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Definition of a Storer instance with a noded data
MySumer=SumerClass(
		**{
			'HdformatingFileKeyStr':'Sums_1.hdf5',
			'FolderingPathStr':Hierarchizer.LocalFolderPathStr
		}
	).push(
		[
			(
				"Parameters",
				Hierarchizer.HierarchizerClass().update(
					[
						(
							'Attr_DatabasingSealTuplesList',
							[
								('SumingFirstInt','SumingFirstInt',tables.Int64Col()),
								('SumingSecondInt','SumingSecondInt',tables.Int64Col())
							]
						),
						('Attr_RowingGetStrsList',['SumingFirstInt','SumingSecondInt'])
					]
				)
			),
			(
				"Results",
				Hierarchizer.HierarchizerClass().update(
					[
						(
							'Attr_DatabasingSealTuplesList',
							[
								('SumedTotalInt','SumedTotalInt',tables.Int64Col())
							]
						),
						('ConnectingGraspClueVariablesList',
							[
								'/NodePointDeriveNoder/<Datome>ParametersHierarchizer'
							]
						),
						('TagStr','Networked')
					]
				)
			)
		],
		**{
			'CollectingCollectionStr':'Datome'
		}
	).network(
		**{
			'RecruitingConcludeConditionTuplesList':[
				(
					'__class__.__mro__',
					operator.contains,Hierarchizer.HierarchizerClass
				)
			]
		}
	)

#Update and store
MySumer.update(
		[
			('SumingFirstInt',1),
			('SumingSecondInt',3)
		]
	).sum(
	)['<Datome>ParametersHierarchizer'].flush(
)

#Update and store
MySumer.update(
		[
			('SumingFirstInt',2),
			('SumingSecondInt',4)
		]
	).sum(
	)[
	'<Datome>ParametersHierarchizer'
	].flush()

#Definition the AttestedStr
SYS._attest(
	[
		'MySumer is '+SYS._str(
		MySumer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MySumer.hdfview().hdfclose().HdformatedStr
	]
) 
