
#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass
@SYS.ClasserClass()
class MakerClass(SYS.AttributerClass):

	#Definition
	RepresentingKeyStrsList=[
							'MakingIntsList',
							'MadeSumInt'
						]

	def default_init(self,
			_MakingIntsList={
							'DefaultingSetType':property,
							'PropertizingInitVariable':[],
							'PropertizingDocStr':'I am doing the thing here'
							},
			_MadeSumInt=0	
		):
		pass

	#Definition a binding function
	def setMakingIntsList(self,_SettingValueVariable):

		#set the value of the "hidden" property variable
		self._MakingIntsList=_SettingValueVariable

		#Bind with MadeInt setting
		self.MadeSumInt=sum(self._MakingIntsList)

#define and set
MyMaker=MakerClass(
	).__setitem__(
		'Attr_MakingIntsList',
		[3,4]
	)

#print
print('MyMaker is ')
SYS._print(MyMaker)

