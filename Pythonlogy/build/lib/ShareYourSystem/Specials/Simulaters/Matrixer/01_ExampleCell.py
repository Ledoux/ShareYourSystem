
#ImportModules
import ShareYourSystem as SYS

#Definition an instance
MyMatrixer=SYS.MatrixerClass().matrix(
	_SizeTuple=(3,2)
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMatrixer is '+SYS._str(
		MyMatrixer,
		**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False,
				'RepresentingKeyStrsList':[
				]
			}
		),
	]
) 

#Print

