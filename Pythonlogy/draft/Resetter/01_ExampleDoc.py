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
		self.__class__.__bases__[0].__init__(self)

	def do_make(self):

		#print
		print('self.MakingMyFloat is '+str(self.MakingMyFloat))
		print('self.MadeMyInt is '+str(self.MadeMyInt))
		print('')

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition an instance
MyMaker=MakerClass()

#Print
print('Before make, MyMaker is ')
SYS._print(MyMaker)

#make once
MyMaker.make(3.)

#Print
print('After the first make, MyMaker is ')
SYS._print(MyMaker)

#Reset
print('Now we reset')
MyMaker.WatchMakeWithMakerBool=False

#Print
print('After the reset, MyMaker is ')
SYS._print(MyMaker)

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.WatchMakeBoolWithMaker is '+str(MakerClass.WatchMakeWithMakerBool),
		'MakerClass.setResetBoolWithMaker_ is '+str(MakerClass.setResetBoolWithMaker_),
		'MakerClass.make is '+str(MakerClass.make),
		'MyMaker is '+SYS._str(
			MyMaker,**{'RepresentingAlineaIsBool':False}
		),
	]
) 

#Print

