
#ImportModules
import ShareYourSystem as SYS

#Define
MyApplyier=SYS.ApplyierClass()

#Apply a set with an ApplyingArgVariable understood as a LiargVariablesList
MyApplyier.apply(
	'set',
	['MyFloat',0.2]
)

#Apply a get with an ApplyingArgVariable understood as a LiargVariablesList
MyApplyier.apply(
		#ApplyingMethodVariable
		'get',
		#ApplyingArgVariable
		["MyFloat"]
	)

#print
print('MyApplyier.GettedValueVariable is ')
SYS._print(MyApplyier.GettedValueVariable)

#Note that for certain special method like get, ApplyingArgVariable can be direct the just one arg 
MyApplyier.apply(
		#ApplyingMethodVariable
		'get',
		#ApplyingArgVariable
		"MyFloat"
	)

#print
print('Once again MyApplyier.GettedValueVariable is ')
SYS._print(MyApplyier.GettedValueVariable)
