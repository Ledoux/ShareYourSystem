#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass with decorated make by a Switcher
@SYS.SwitcherClass(**{
	'SwitchingIsBool':True,
	'SwitchingWrapMethodStr':'make'
})
class MakerClass(object):

	def default_init(self,
				_MakingMyFloat=1.,
				_MadeMyInt=0
				):
		object.__init__(self)

	def do_make(self):

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition a MakerClass with decorated make by a Switcher
@SYS.SwitcherClass(**{
	'SwitchingIsBool':True,
	'SwitchingWrapMethodStr':'make'
})
class BuilderClass(MakerClass):

	def default_init(self,
				):
		MakerClass.__init__(self)

	def mimic_make(self):

		#first make
		MakerClass.make()

		#Cast
		self.MadeMyInt+=10

#print 
print('BuilderClass.SwitchMethodDict is ')
print(SYS.indent(BuilderClass.SwitchMethodDict))

#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder.__dict__ is ')
SYS._print(MyBuilder.__dict__)

#make once
MyBuilder.make(3.)

#Print
print('After the build, MyBuilder.__dict__ is ')
SYS._print(MyBuilder.__dict__)

#Switch by default it is just the last Name and the the last do in the mro
print('Now we switch')
MyBuilder.setSwitch('make')

#Print
print('After the switch MyBuilder.__dict__ is ')
SYS._print(MyBuilder.__dict__)


