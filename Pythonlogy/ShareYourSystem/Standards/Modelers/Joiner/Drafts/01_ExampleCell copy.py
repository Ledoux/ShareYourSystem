
#ImportModules
import tables
import operator
import ShareYourSystem as SYS
from ShareYourSystem.Tutorials import Sumer
from ShareYourSystem.Standards.Modelers import Featurer,Joiner

#Definition a Sumer and set inside a db
MySumer=Sumer.SumerClass().analyze(
			['ModulizingPowerFloat'], 	#Parameters
			['ModulizedTotalFloat']  	#Results
		)

#
MySumer.update(
	[
		('SumingFirstInt',1),
		('SumingSecondInt',3)
	]
).collect()

'''
MySumer=Sumer.SumerClass().update(
[
	('HdformatingFileKeyStr','Sums.hdf5'),
	(
		'<Database>ParametersFeaturer',
		Featurer.FeaturerClass().update(
			[
				('Attr_DatabasingSealTuplesList',
					[
						#GetStr #ColumnStr #Col
						('SumingFirstInt','SumingFirstInt',tables.Int64Col()),
						('SumingSecondInt','SumingSecondInt',tables.Int64Col())
					]
				),
				('FeaturingAllBool',True)
			]
		)
	),
	(
		'<Database>ResultsJoiner',
		Joiner.JoinerClass().update(
			[
				('Attr_DatabasingSealTuplesList',
					[
						#GetStr #ColumnStr #Col
						('SumedTotalInt','SumedTotalInt',tables.Int64Col()),
					]
				),
				('JoiningDownGetKeyStrsList',["ParametersFeaturer"])
			]
		)
	)
]
)
'''


"""

print("\n\n\nHHHHAAAAHH\n\n\n")

MySumer.command(
	[
		('insert',{'LiargVariablesList':[]})
	],
	**{'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]}		
).update(
	[
		('SumingFirstInt',2),
		('SumingSecondInt',3)
	]
).command(
	[
		('insert',{'LiargVariablesList':[]}),
	],
	**{
		'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]
	}		
)


print('\n\n\n\nFSFFFFFFF\n\n\n\n\n\n')
"""
MySumer.command(
	[
		('retrieve',{'LiargVariablesList':[[0,0]]})
	],
	**{
		'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]
	}		
)
"""

MySumer.command(
	[
		('find',{'LiargVariablesList':[[('SumedTotalInt',(operator.eq,4))]]})
	],
	**{
		'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]
	}		
)

MySumer.command(
	[
		('recover',{'LiargVariablesList':[]})
	],
	**{
		'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]
	}		
)

"""
MySumer.command(
	[
		('recover',{'LiargVariablesList':[[('SumedTotalInt',(operator.eq,4))]]})
	],
	**{
		'GatherVariablesList':[
									#'<Database>ParametersFeaturer'
									'<Database>ResultsJoiner'
								]
	}		
)
"""

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

#Print

