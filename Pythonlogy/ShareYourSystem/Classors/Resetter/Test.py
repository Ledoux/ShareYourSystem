#Import modules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Functers import Argumenter,Switcher
from ShareYourSystem.Objects import Setter

#Print a version of the class
_print(dict(Switcher.SwitcherClass.__dict__.items()))

#Print a version of this object
_print(Switcher.SwitcherClass())

#Print a version of his __dict__
_print(Switcher.SwitcherClass().__dict__)

#Test
class MakerClass(Setter.SetterClass):

	def default_init(self):

		#Call the based method
		Setter.SetterClass.__init__(self)

		#Call the init
		self.init()

	def init(self):

		#Definition a default Int
		self.MakingInt=1
		self.MadeInt=0

	'''
	@Switcher.SwitcherClass()
	def make(self):
		self.MadeInt+=2*self.MakingInt
	'''

	#Be carefule Argumenter must be before Switcher... for setting goodly the argumenting inputs
	@Switcher.SwitcherClass()
	@Argumenter.ArgumenterClass()
	def make(self,_Int=None):
		self.MadeInt+=2*self.MakingInt

#Get an instance
MyMaker=MakerClass()

#Show the default value of the instance
print('At the beginning the object is...')
print(MyMaker)
print('')

#Change the int
print('make with the object...')
MyMaker.make(2)
print(MyMaker)
print('')

#Change the int
print('make again with the object, but it is switched off now')
MyMaker.make()
print(MyMaker)
print('')

#Now set InititatedIsBool to False to bind with a reinit of the object
print('Now swith on the object...')
MyMaker['SwitchingMakeBool']=False
print(MyMaker)
print('')

#Test
from ShareYourSystem.Functers import Hooker

class BuilderClass(MakerClass):

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':MakerClass.init}]})
	def init(self):

		#Definition a default Int
		self.BuildingFloat=1.
		self.BuiltInt=0

	#Be carefule Argumenter must be before Switcher... for setting goodly the argumenting inputs
	@Switcher.SwitcherClass()
	@Argumenter.ArgumenterClass()
	def build(self,_Float=None):
		self.BuiltInt+=2*self.MakingInt+int(self.BuildingFloat)

#Get an instance
MyBuilder=BuilderClass()

#Show the default value of the instance
print('At the beginning the object is...')
print(MyBuilder)
print('')

#Change the int
print('build with the object...')
MyBuilder.make(2)
print(MyBuilder)
print('')

#Change the int
print('build again with the object, but it is switched off now')
MyBuilder.build()
print(MyBuilder)
print('')

#Now set InititatedIsBool to False to bind with a reinit of the object
print('Now swith on the object for the make process...')
MyBuilder['SwitchingMakeBool']=False
print(MyBuilder)
print('')