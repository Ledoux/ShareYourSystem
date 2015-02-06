
#ImportModules
import ShareYourSystem as SYS
import tables
import operator

#Define a Sumer class
@SYS.ClasserClass()
class SumerClass(SYS.ControllerClass):

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
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)
						
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
			'FolderingPathStr':SYS.Hierarchizer.LocalFolderPathStr
		}
	).collect(
		"Hierarchizers",
		"Parameters",
		SYS.HierarchizerClass().update(
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
	).collect(
		"Hierarchizers",
		"Results",
		SYS.HierarchizerClass().update(
			[
				(
					'Attr_DatabasingSealTuplesList',
					[
						('SumedTotalInt','SumedTotalInt',tables.Int64Col())
					]
				),
				('ConnectingGraspClueVariablesList',
					[
						'/NodePointDeriveNoder/<Hierarchizers>ParametersHierarchizer'
					]
				),
				('TagStr','Networked')
			]
		)
	).network(
		**{
			'RecruitingConcludeConditionTuplesList':[
				(
					'MroClassesList',
					operator.contains,SYS.HierarchizerClass
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
	)['<Hierarchizers>ParametersHierarchizer'].flush(
)

#Update and store
MySumer.update(
		[
			('SumingFirstInt',2),
			('SumingSecondInt',4)
		]
	).sum(
	)[
	'<Hierarchizers>ParametersHierarchizer'
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
		'hdf5 file is : '+MySumer.hdfview().hdfclose().HdformatedConsoleStr
	]
) 
