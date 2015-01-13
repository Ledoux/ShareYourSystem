#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Functers import Outputer
from ShareYourSystem.Noders import Noder

#Definition a MakerClass
class MakerClass(object):

	def __init__(self):

		#Init attributes
		self.MakingMyFloat=1.
		self.MadeMyInt=1

	@Outputer.OutputerClass()
	def make(self):

		#Print
		print('I make first !')

		#set
		self.MadeMyInt=int(self.MakingMyFloat)

#Definition a BuilderClass
class BuilderClass(Noder.NoderClass):

	def __init__(self,):

		#Init attributes
		self.BuiltMyFloat=0.

		#set the output hierarchy
		self['<Output>MyMaker']=MakerClass()

	@Outputer.OutputerClass()
	def build(self):

		#Print
		print('I build then !')

		#set
		self.BuiltMyFloat=float(2*self['<Output>MyMaker'].MadeMyInt)

#Definition an instance
MyBuilder=BuilderClass().build()

#Definition the AttestedStr
SYS._attest(
	[
		'MyBuilder.BuiltMyFloat is '+str(MyBuilder.BuiltMyFloat)
	]
) 

#Print




