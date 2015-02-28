#ImportModules
import ShareYourSystem as SYS

#Definition 
@SYS.ClasserClass(**
{
	'ClassingSwitchMethodStrsList':['make']
})
class MakerClass(SYS.RebooterClass):

	def default_init(self,
					_MakingMyFloat=0.,
					_MadeMyInt=0,
					**_KwargVariablesDict
				):
		SYS.RebooterClass.__init__(self,**_KwargVariablesDict)

	def do_make(self):
		
		#print
		print('I am in the do_make of the Maker')

		#cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Define
MyMaker=SYS.MakerClass()

#print
print('MyMaker before make is ')
print(SYS.indent(MyMaker.__dict__))

#
MyMaker.make(5.)

#print
print('MyMaker after make is ')
print(SYS.indent(MyMaker.__dict__))

#
MyMaker.reboot()
