
#ImportModules
import ShareYourSystem as SYS

#Init an int
SYS.GrasperClass.ShareCountInt=0

#Set
CommandingSetVariable=[
	(
		'execute',
		';'.join(
			[
				'self.ShareCountInt=self.__class__.ShareCountInt',
				'self.__class__.ShareCountInt+=1'
			]
		)
	) for __Int in xrange(2)
]

#define and command
FirstCommander=SYS.CommanderClass(
	)['map*set'](
			[
				('FirstGrasper',SYS.GrasperClass()),
				('SecondGrasper',SYS.GrasperClass()),
			]
	).command(
		#CommandingGraspVariable,
		[
			'FirstGrasper','SecondGrasper'
		],
		#CommandingSetVariable	
		CommandingSetVariable
	)


#print
print('FirstCommander is ')
SYS._print(FirstCommander)

#Init an int
SYS.GrasperClass.ShareCountInt=0

#define and command
SecondCommander=SYS.CommanderClass(
	)['map*set'](
		[
				('FirstGrasper',SYS.GrasperClass()),
				('SecondGrasper',SYS.GrasperClass()),
		]
	).command(
		#CommandingGraspVariable (map or not),
		[
			'FirstGrasper','SecondGrasper'
		],
		#CommandingUpdateList	
		CommandingSetVariable,
		#CommandingOrderStr
		"EachSetForAllGrasps"	
	)

#print
print('SecondCommander is ')
SYS._print(SecondCommander)	


