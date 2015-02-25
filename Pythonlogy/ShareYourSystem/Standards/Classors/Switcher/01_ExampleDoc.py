#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass with decorated make by a Switcher
@SYS.SwitcherClass(**{
	'SwitchingIsBool':True,
	#'ObservingWrapMethodStr':'do_make'
	#'ObservingWrapMethodStr':'superDo_make'
	'SwitchingWrapMethodStr':'make'
})
class MakerClass(SYS.ObjectClass):

	#Definition
	RepresentingKeyStrsList=[
								'MakingMyFloat',
								'MadeMyInt'
							]

	def default_init(self,
				_MakingMyFloat=1.,
				_MadeMyInt=0
				):
		SYS.ObjectClass.__init__(self)

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

#make again
MyMaker.make(5.)

#Print
print('After the second make, MyMaker is ')
SYS._print(MyMaker)

#make again
print('Now we switch')
MyMaker.setSwitch()

#Print
print('After the switch MyMaker is ')
SYS._print(MyMaker)

#make again
MyMaker.make(7.)

#Print
print('After the third make, MyMaker is ')
SYS._print(MyMaker)

#Define
print('\n'.join(
	[
		'MakerClass.make is '+str(MakerClass.make),
		'MyMaker is '+SYS._str(
			MyMaker,**{'RepresentingAlineaIsBool':False}
		),
	]
))



