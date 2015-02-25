#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.PropertiserClass()
class MakerClass(SYS.ObjectClass):

	def default_init(self,
			_MakingMyFloat={
							'DefaultingSetType':property,
							'PropertizingInitVariable':3.,
							'PropertizingDocStr':'I am doing the thing here'
							},
			_MakingMyList={
							'DefaultingSetType':property,
							'PropertizingInitVariable':[],
							'PropertizingDocStr':'I am doing the thing here'
							},
			_MakingMyInt={'DefaultingSetType':int},
			_MadeMyInt=0	
		):
		SYS.ObjectClass.__init__(self)

	#Definition a binding function
	def setMakingMyFloat(self,_SettingValueVariable):

		#Print
		#print('I am going to make the job directly !')

		#set the value of the "hidden" property variable
		self._MakingMyFloat=_SettingValueVariable

		#Bind with MadeInt setting
		self.MadeMyInt=int(self._MakingMyFloat)

	#Definition a binding function
	def setMakingMyList(self,_SettingValueVariable):

		#set the value of the "hidden" property variable
		self._MakingMyList=_SettingValueVariable+['Hellllllo']


#Definition a default instance 
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyFloat=5,_MakingMyList=[4])

#Definition the AttestedStr
print('\n'.join(
	[
		'MakerClass.PropertizedDefaultTuplesList is '+SYS._str(
			MakerClass.PropertizedDefaultTuplesList),
		'What are you saying DefaultMaker ?',
		'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
		'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
		'DefaultMaker.MakingMyList is '+str(DefaultMaker.MakingMyList),
		'DefaultMaker.MadeMyInt is '+str(DefaultMaker.MadeMyInt),
		'What are you saying SpecialMaker ?',
		'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
		'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
		'SpecialMaker.MakingMyList is '+str(SpecialMaker.MakingMyList),
		'SpecialMaker.MadeMyInt is '+str(SpecialMaker.MadeMyInt),
	]
	)
) 

#Print
