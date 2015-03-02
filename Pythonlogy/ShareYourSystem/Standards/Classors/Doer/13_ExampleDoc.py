#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.DoerClass()
class MakerClass(object):

	def default_init(self,
				_MakingMyFloat=0.,
				):
		object.__init__(self)

	def do_make(self):
		pass

#Define
@SYS.DoerClass()
class BuilderClass(MakerClass):

	def default_init(self,
				_BuildingMyStr=""
				):
		MakerClass.__init__(self)

	def do_build(self):
		pass
	
#define
MyBuilder=BuilderClass(
	).make(
		5.
	)

#print
print('MyBuilder.__dict__ is')
print(SYS.indent(MyBuilder.__dict__))

#reset
MyBuilder.setDoing()

#print
print('MyBuilder.__dict__ is')
print(SYS.indent(MyBuilder.__dict__))



