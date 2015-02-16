
#ImportModules
import ShareYourSystem as SYS

#Define a grasper
MyGrasper=SYS.GrasperClass(
	)['map*set'](
		{
			'/ChildGrasper/MyStr':"hello",
			'MyInt':0
		}
	)

#print
print('MyGrasper is ')
SYS._print(MyGrasper)

#grasp
MyGrasper['map*grasp'](
		[
			'/ChildGrasper/MyStr',
			SYS.GraspDictClass({'HintVariable':'MyInt'})
		]
	)

#Grasp with a path str
print('MyGrasper.ItemizedMapValueVariablesList is ')
SYS._print(MyGrasper.ItemizedMapValueVariablesList)



