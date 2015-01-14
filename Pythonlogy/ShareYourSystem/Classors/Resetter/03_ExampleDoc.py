#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Resetter,Attester
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Switcher
@Resetter.ResetterClass()
class MakerClass(Initiator.InitiatorClass):

	#Definition
	RepresentingKeyStrsList=[
								'MakingMyFloat',
								'MadeMyInt'
							]

	def default_init(self,
				_MakingMyFloat=0.,
				_MadeMyInt=0
				):
		Initiator.InitiatorClass.__init__(self)

	def do_make(self):

		#print
		print('self.MakingMyFloat is '+str(self.MakingMyFloat))
		print('self.MadeMyInt is '+str(self.MadeMyInt))
		print('')

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition a MakerClass with decorated make by a Switcher
@Resetter.ResetterClass()
class BuilderClass(MakerClass):

	#Definition
	RepresentingKeyStrsList=[
								'BuildingMyStr',
								'BuiltMyStr'
							]

	def default_init(self,
				_BuildingMyStr="",
				_BuiltMyStr=""
				):
		MakerClass.__init__(self)

	def do_build(self):
		#set
		pass

#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
print('Now we reset')
MyBuilder.WatchMakeWithMakerBool=False

#Print
print('After the reset MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
MyBuilder.make(7.)

#Print
print('After the third make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#Definition the AttestedStr
SYS._attest(
	[
		'BuilderClass.WatchMakeWithMakerBool is '+str(BuilderClass.WatchMakeWithMakerBool),
		'BuilderClass.setResetBoolWithMaker_ is '+str(BuilderClass.setResetBoolWithMaker_),
		'BuilderClass.make is '+str(BuilderClass.make),
		'MyBuilder is '+SYS._str(
			MyBuilder,**{
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':[
				'MakingMyFloat','MadeMyInt'
			]
			}
		),
	]
) 

#Print

