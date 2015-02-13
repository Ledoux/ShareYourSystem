
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyGrasper=SYS.GrasperClass(
	).set(
		'/ChildGrasper/MyStr',
		"hello"
	)

#Return
SYS._attest(
	[
		"MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is "+
		str(
			MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable
			),
		"MyGrasper.grasp(MySYS.ChildGrasper).GraspedAnswerVariable is "+
		str(
			MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable
			),
		"MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})).GraspedAnswerVariable is "+
		str(
			MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})
			).GraspedAnswerVariable),
	]
)

#Print
