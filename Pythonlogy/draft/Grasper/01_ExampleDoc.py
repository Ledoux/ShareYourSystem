
#ImportModules
import ShareYourSystem as SYS

#Define a grasper
MyGrasper=SYS.GrasperClass(
	).set(
		'/ChildGrasper/MyStr',
		"hello"
	)

#Grasp with a path str
print("MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is ")
SYS._print(
	MyGrasper.grasp(
		#GraspingClueVariable
		'/ChildGrasper/MyStr'
	).GraspedAnswerVariable
)

#Grasp direct...
print("MyGrasper.grasp(MySYS.ChildGrasper).GraspedAnswerVariable is ")
SYS._print(
	MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable
)

#Grasp with a grasp dict class
print("MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})).GraspedAnswerVariable is ")
SYS._print(
	MyGrasper.grasp(
		SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})
	).GraspedAnswerVariable
)


