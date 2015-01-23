
#ImportModules
import ShareYourSystem as SYS

#Definition a structure of Grouper
MyGrouper=SYS.GrouperClass().hdformat(
	_FileKeyStr='Groupers.hdf5',
	**{
		'FolderingPathStr':SYS.Grouper.LocalFolderPathStr
	}
		).update(
			[
				(
					'<Tree>FirstChildGrouper',
					SYS.GrouperClass().update(
						[
							('<Tree>GrandChildGrouper',
							SYS.GrouperClass())
						]
					)
				),
				(
					'<Tree>SecondChildGrouper',
					SYS.GrouperClass()
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

