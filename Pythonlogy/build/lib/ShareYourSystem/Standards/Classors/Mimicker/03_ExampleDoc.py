#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass with decorated make by a Switcher
@SYS.SwitcherClass(**{
	'SwitchingIsBool':True,
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

#Definition
@SYS.MimickerClass(**{
	'MimickingDoMethodStr':"make"
})
class BuilderClass(MakerClass):

	#Definition
	RepresentingKeyStrsList=[
							]

	def default_init(self,
					**_KwarVariablesDict
				):
		MakerClass.__init__(self,**_KwarVariablesDict)

	def mimic_make(self):
		
		#print
		print('I am in the mimic_make of the Builder')

		#call the parent method
		MakerClass.make(self)

		#cast
		self.MadeMyInt+=10

	def do_build(self):
		pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt']
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	]
})

#make again
print('Now we switch')
MyBuilder.setSwitch('Maker',['Make'])

#Print
print('After the switch MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt'
	]
})

#make again
MyBuilder.make(7.)

#Print
print('After the third make, MyBuilder is ')
SYS._print(MyBuilder,**{
	'RepresentingKeyStrsList':[
	'MakingMyFloat',
	'MadeMyInt',
	'WatchBeforeMakeWithMakerBool']
})

#Definition the AttestedStr
SYS._attest(
	[
		'BuilderClass.WatchBeforeMakeWithMakerBool is '+str(BuilderClass.WatchBeforeMakeWithMakerBool),
		'BuilderClass.make is '+str(BuilderClass.make),
		'MyBuilder is '+SYS._str(
			MyBuilder,**{
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':[
			'MakingMyFloat',
			'MadeMyInt'
			]
		}
		),
	]
) 

#Print
