
#ImportModules
import ShareYourSystem as SYS

#Define
MyApplyier=SYS.ApplyierClass()

#Apply a map with ApplyingMethodVariable understood as a dict of {ApplyingArgVariable:ApplyingArgVariable}
MyApplyier.apply(
	#ApplyingMethodVariable
	{
		'set':['MyFloat',0.2]
	}
)

#Apply just a set with a rigorous ApplyDictClass as a ApplyingArgVariable
MyApplyier.apply(
	#ApplyingMethodVariable
	'__setitem__',
	#ApplyingArgVariable
	SYS.ApplyDictClass(
		{'LiargVariablesList':['MyStr','Hello']}
	)
)

#Apply an apply is possible
MyApplyier.apply(
	'__setitem__',
	SYS.ApplyDictClass(
		{
			'LiargVariablesList':[
				'__setitem__',
				SYS.ApplyDictClass(
					{
						'LiargVariablesList':
						['MyNotLostStr','ben he']
					}
				)
			]
		}
	)
)

#With just one argument
MyApplyier.apply(
	SYS.ApplyDictClass(
		{
			'MethodStr':'__setitem__',
			'LiargVariablesList':['MyInt',5]
		}
	)
)

#print
print('MyApplyier is ')
SYS._print(MyApplyier)

