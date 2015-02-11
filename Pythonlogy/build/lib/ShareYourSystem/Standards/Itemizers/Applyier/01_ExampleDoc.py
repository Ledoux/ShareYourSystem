
#ImportModules
import ShareYourSystem as SYS

#Definition an applyier instance
MyApplyier=SYS.ApplyierClass()

#Apply just a set... (even if we can do shorter !)
MyApplyier.apply(
	'__setitem__',
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

#With set
MyApplyier['__setitem__']=SYS.ApplyDictClass(
	{
		'LiargVariablesList':
		['MyFloat',0.2]
	}
)

#print
print('MyApplyier is ')
SYS._print(MyApplyier)

