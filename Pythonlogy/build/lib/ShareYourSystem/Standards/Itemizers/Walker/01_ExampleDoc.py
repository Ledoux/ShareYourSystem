
#ImportModules
import ShareYourSystem as SYS

#Definition a Walker instance with a noded tree
MyWalker=SYS.WalkerClass(
	).array(
		[
			["ATextWalker"],
			["1TextWalker","2TextWalker"],
			["aTextWalker"]
		]
	)	

#Walk inside the Tree in order to parent again because the tree was not yet completely setted when it was done
MyWalker.walk(
		#WalkingSocketDict
		{
			'BeforeCommandLiargVariablesList':
			(
				'/',
				{
					'MyInt':0
				}
			),
			'RouteGetVariable':{
				'ConditionVariable':[
					('SetTagStr',SYS.operator.contains,'Text')
				]
			}
		}
	)

#print
print('MyWalker is ')
SYS._print(MyWalker)

