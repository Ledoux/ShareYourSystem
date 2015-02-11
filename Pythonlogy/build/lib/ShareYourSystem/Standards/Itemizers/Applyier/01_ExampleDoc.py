
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

#With just one argument
MyApplyier.apply(
	['set','set'],
	[
		['MyFirstBool',True],
		['MySecondBool',False],
	]
)

#Special map option (like an update)
MyApplyier.apply(
	'map*set',
	[
		['MyFirstObject',SYS.ObjectClass()],
		['MySecondObject',SYS.ObjectClass()]
	]
)

#Special set apply because of the ApplyDictClass
MyApplyier['set']=SYS.ApplyDictClass(
	['MyFirstDirectInt',3]
)

#Special set apply because of the ApplySetPrefixStr in the SettingKeyVariable
MyApplyier['apply*set']=['MySecondDirectInt',10]


#print
print('MyApplyier is ')
SYS._print(MyApplyier)

