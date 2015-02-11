
#ImportModules
import ShareYourSystem as SYS

#Init an int
SYS.GrasperClass.ShareCountInt=0

#Set
CommandingUpdateList=[
	(
		'apply*execute',
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
	).apply(
			'map*set',
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
		CommandingUpdateList
	)


#print
print('FirstCommander is ')
SYS._print(FirstCommander)

"""
#Init an int
SYS.GrasperClass.ShareCountInt=0

#define and command
SecondCommander=SYS.CommanderClass(
	).set(
		SYS.MapListClass(
			[
				('FirstGrasper',SYS.GrasperClass()),
				('SecondGrasper',SYS.GrasperClass()),
			]
		)
	).command(
		#CommandingGraspVariable (map or not),
		[
			'FirstGrasper','SecondGrasper'
		],
		#CommandingUpdateList	
		CommandingUpdateList,
		#CommandingOrderStr
		"EachSetForAll"	
	)

#print
print('SecondCommander is ')
SYS._print(SecondCommander)	

"""
