
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Grasper

#Explicit expression
MyGrasper=Grasper.GrasperClass().__setitem__(
	'ChildGrasper',
	Grasper.GrasperClass().__setitem__('MyStr',"hello")
)

#Return
SYS._attest(
	[
		"MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is "+
		str(
			MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable
			),
		"MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable is "+
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
