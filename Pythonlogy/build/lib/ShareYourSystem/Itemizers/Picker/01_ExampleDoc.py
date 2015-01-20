
#ImportModules
import ShareYourSystem as SYS

#Definition an Picker
MyPicker=SYS.PickerClass()

#set some items
map(
		lambda __ItemTuple:
		MyPicker.__setitem__(__ItemTuple[0],__ItemTuple[1]),
		[
			('MyInt',0),
			('MyPicker',SYS.PickerClass().__setitem__('MyStr',"hello")),
		]
	)

#Map some gets
PickedVariablesList=MyPicker.pick(
	[
		#Get directly in the __dict__
		'MyInt',
		'MyPicker',
		#Get with a DeepShortStr
		'/MyPicker/MyStr'
	]
)
	
#Definition the AttestedStr
SYS._attest(
	[
		'PickedVariablesList is '+SYS._str(
			PickedVariablesList
			,**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

