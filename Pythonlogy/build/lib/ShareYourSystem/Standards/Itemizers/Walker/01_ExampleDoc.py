
#ImportModules
import ShareYourSystem as SYS

#Definition a Walker instance with a noded tree
MyWalker=SYS.WalkerClass(
	).array(
		[
			["ATextWalker","BTextWalker"],
			["1TextWalker","2TextWalker"],
			["aTextWalker","bTextWalker"]
		]
	)	

#Walk inside the Tree in order to parent again because the tree was not yet completely setted when it was done
MyWalker.walk(
		#WalkingSocketDict
		{
			'BeforeCommandVariable':
			(
				'/',
				{
					'MyInt':0
				}
			),
			'RouteGetVariable':{
				'ConditionTuplesList':[
					('DictKeyStr',SYS.operator.contains,'Text')
				]
			}
		}
	)


#print
print('MyWalker is ')
SYS._print(MyWalker)

