
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Grouper

#Definition a structure of Grouper
MyGrouper=Grouper.GrouperClass().hdformat(
	_FileKeyStr='Groupers.hdf5',
	**{
		'FolderingPathStr':Grouper.LocalFolderPathStr
	}
		).update(
			[
				(
					'<Tree>FirstChildGrouper',
					Grouper.GrouperClass().update(
						[
							('<Tree>GrandChildGrouper',
							Grouper.GrouperClass())
						]
					)
				),
				(
					'<Tree>SecondChildGrouper',
					Grouper.GrouperClass()
				)
			]	
		)

#Walk to set the same structure in the hdf5
MyGrouper.walk(
		{
				'BeforeUpdateList':
				[
					('parent',{'LiargVariablesList':[['HdformatedFileVariable']]}),
					('group',{'LiargVariablesList':[]})
				],
				'GatherVariablesList':['<Tree>']
		}
).hdfclose()

#Definition the AttestedStr
SYS._attest(
	[
		'MyGrouper is '+SYS._str(
		MyGrouper,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		),
		'MyGrouper.hdfview().HdformatedStr is '+MyGrouper.hdfview().HdformatedStr
	]
) 

#Print

