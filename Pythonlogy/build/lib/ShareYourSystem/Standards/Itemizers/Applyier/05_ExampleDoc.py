
#ImportModules
import ShareYourSystem as SYS

#Define
MyApplyier=SYS.ApplyierClass()

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

