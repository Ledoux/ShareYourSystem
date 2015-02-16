
#ImportModules
import ShareYourSystem as SYS

#Definition a Walker instance with a noded tree
MyWalker=SYS.WalkerClass(
	).array(
		[
			["AWalker","BWalker"],
			["1Walker","2Walker"],
			["aWalker","bWalker"]
		]
	)	
)

#Walk inside the Tree in order to parent again because the tree was not yet completely setted when it was done
MyWalker.walk(
		#WalkingSocketDict
		{
			'BeforeUpdateList':
			[

			],
			'GraspVariable':['<Walkers>']
		}
	)


#print
print('MyWalker is ')
SYS._print(MyWalker)


